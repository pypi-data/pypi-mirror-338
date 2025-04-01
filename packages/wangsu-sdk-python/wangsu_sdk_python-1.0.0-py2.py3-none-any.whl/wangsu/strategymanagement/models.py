# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class UpdatePropagationPoliciesOwnerReference(TeaModel):
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


class UpdatePropagationPoliciesFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdatePropagationPoliciesManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: UpdatePropagationPoliciesFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this UpdatePropagationPoliciesManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'UpdatePropagationPoliciesFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“UpdatePropagationPoliciesFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"UpdatePropagationPoliciesFieldsV1 holds the first JSON version format as described in the 'UpdatePropagationPoliciesFieldsV1' type", "zh_CN":"UpdatePropagationPoliciesFieldsV1 包含类型 “UpdatePropagationPoliciesFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = UpdatePropagationPoliciesFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class UpdatePropagationPoliciesObjectMeta(TeaModel):
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
        owner_references: List[UpdatePropagationPoliciesOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[UpdatePropagationPoliciesManagedFieldsEntry] = None,
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
                temp_model = UpdatePropagationPoliciesOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = UpdatePropagationPoliciesManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class UpdatePropagationPoliciesLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdatePropagationPoliciesMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[UpdatePropagationPoliciesLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = UpdatePropagationPoliciesLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class UpdatePropagationPoliciesResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        label_selector: UpdatePropagationPoliciesMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

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
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = UpdatePropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class UpdatePropagationPoliciesCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdatePropagationPoliciesFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[UpdatePropagationPoliciesCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = UpdatePropagationPoliciesCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class UpdatePropagationPoliciesClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: UpdatePropagationPoliciesMetaV1LabelSelector = None,
        field_selector: UpdatePropagationPoliciesFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = UpdatePropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = UpdatePropagationPoliciesFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class UpdatePropagationPoliciesToleration(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
        effect: str = None,
        toleration_seconds: int = None,
    ):
        # {"en":"The taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.", "zh_CN":"容忍度所适用的污点的键名。此字段为空意味着匹配所有的污点键。 如果 key 为空，则 operator 必须为 Exists；这种组合意味着匹配所有值和所有键。"}
        self.key = key
        # {"en":"Represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.", "zh_CN":"表示 key 与 value 之间的关系。有效的 operator 取值是 Exists 和 Equal。默认为 Equal。 Exists 相当于 value 为某种通配符，因此 Pod 可以容忍特定类别的所有污点。"}
        self.operator = operator
        # {"en":"The taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.", "zh_CN":"容忍度所匹配的污点值。如果 operator 为 Exists，则此 value 值应该为空， 否则 value 值应该是一个正常的字符串。"}
        self.value = value
        # {"en":"Indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.", "zh_CN":"指示要匹配的污点效果。空值意味著匹配所有污点效果。如果要设置此字段，允许的值为 NoSchedule、PreferNoSchedule 和 NoExecute 之一。"}
        self.effect = effect
        # {"en":"Represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.", "zh_CN":" 表示容忍度（effect 必须是 NoExecute，否则此字段被忽略）容忍污点的时间长度。 默认情况下，此字段未被设置，这意味着会一直能够容忍对应污点（不会发生驱逐操作）。 零值和负值会被系统当做 0 值处理（立即触发驱逐）。"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        if self.effect is not None:
            result['effect'] = self.effect
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class UpdatePropagationPoliciesSpreadConstraint(TeaModel):
    def __init__(
        self,
        spread_by_field: str = None,
        spread_by_label: str = None,
        max_groups: int = None,
        min_groups: int = None,
    ):
        # {"en":"The member clusters in the cluster federation are divided into multiple groups based on an attribute of the member cluster (currently, only cluster is supported, and the region, zone, and provider attributes may be supported in the future)", "zh_CN":"根据成员集群的某个属性（当前仅支持cluster、后续可能增加对成员集群region、zone、provider等属性支持）将集群联邦中的成员集群分为多个小组"}
        self.spread_by_field = spread_by_field
        # {"en":"The member cluster is divided into groups based on labels", "zh_CN":"根据label将成员集群分为多个小组"}
        self.spread_by_label = spread_by_label
        # {"en":"Maximum number of groups", "zh_CN":"最大分组数"}
        self.max_groups = max_groups
        # {"en":"Minimum number of groups", "zh_CN":"最小分组数"}
        self.min_groups = min_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spread_by_field is not None:
            result['spreadByField'] = self.spread_by_field
        if self.spread_by_label is not None:
            result['spreadByLabel'] = self.spread_by_label
        if self.max_groups is not None:
            result['maxGroups'] = self.max_groups
        if self.min_groups is not None:
            result['minGroups'] = self.min_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spreadByField') is not None:
            self.spread_by_field = m.get('spreadByField')
        if m.get('spreadByLabel') is not None:
            self.spread_by_label = m.get('spreadByLabel')
        if m.get('maxGroups') is not None:
            self.max_groups = m.get('maxGroups')
        if m.get('minGroups') is not None:
            self.min_groups = m.get('minGroups')
        return self


class UpdatePropagationPoliciesStaticClusterWeight(TeaModel):
    def __init__(
        self,
        target_cluster: UpdatePropagationPoliciesClusterAffinity = None,
        weight: int = None,
    ):
        # {"en":"affected clusters by the weight", "zh_CN":"比重生效的目标集群"}
        self.target_cluster = target_cluster
        # {"en":"proportion of replicas in total", "zh_CN":"集群实例数占比"}
        self.weight = weight

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetCluster') is not None:
            temp_model = UpdatePropagationPoliciesClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class UpdatePropagationPoliciesClusterPreferences(TeaModel):
    def __init__(
        self,
        static_weight_list: List[UpdatePropagationPoliciesStaticClusterWeight] = None,
        dynamic_weight: str = None,
    ):
        # {"en":"static proportion of cluster replicas in total", "zh_CN":"集群副本数占比"}
        self.static_weight_list = static_weight_list
        # {"en":"dynamic proportion of replicas in total", "zh_CN":"动态比重"}
        self.dynamic_weight = dynamic_weight

    def validate(self):
        if self.static_weight_list:
            for k in self.static_weight_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.static_weight_list is not None:
            result['staticWeightList'] = []
            for k in self.static_weight_list:
                result['staticWeightList'].append(k.to_map() if k else None)
        if self.dynamic_weight is not None:
            result['dynamicWeight'] = self.dynamic_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('staticWeightList') is not None:
            self.static_weight_list = []
            for k in m.get('staticWeightList'):
                temp_model = UpdatePropagationPoliciesStaticClusterWeight()
                self.static_weight_list.append(temp_model.from_map(k))
        if m.get('dynamicWeight') is not None:
            self.dynamic_weight = m.get('dynamicWeight')
        return self


class UpdatePropagationPoliciesReplicaSchedulingStrategy(TeaModel):
    def __init__(
        self,
        replica_scheduling_type: str = None,
        replica_division_preference: str = None,
        weight_preference: UpdatePropagationPoliciesClusterPreferences = None,
    ):
        # {"en":"scheduling type of replicas", "zh_CN":"副本调度类型"}
        self.replica_scheduling_type = replica_scheduling_type
        # {"en":"division preference of replicas", "zh_CN":"副本数切分方式"}
        self.replica_division_preference = replica_division_preference
        # {"en":"weight preference", "zh_CN":"权重配置"}
        self.weight_preference = weight_preference

    def validate(self):
        if self.weight_preference:
            self.weight_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.replica_scheduling_type is not None:
            result['replicaSchedulingType'] = self.replica_scheduling_type
        if self.replica_division_preference is not None:
            result['replicaDivisionPreference'] = self.replica_division_preference
        if self.weight_preference is not None:
            result['weightPreference'] = self.weight_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('replicaSchedulingType') is not None:
            self.replica_scheduling_type = m.get('replicaSchedulingType')
        if m.get('replicaDivisionPreference') is not None:
            self.replica_division_preference = m.get('replicaDivisionPreference')
        if m.get('weightPreference') is not None:
            temp_model = UpdatePropagationPoliciesClusterPreferences()
            self.weight_preference = temp_model.from_map(m['weightPreference'])
        return self


class UpdatePropagationPoliciesPlacement(TeaModel):
    def __init__(
        self,
        cluster_affinity: UpdatePropagationPoliciesClusterAffinity = None,
        cluster_tolerations: UpdatePropagationPoliciesToleration = None,
        spread_constraints: List[UpdatePropagationPoliciesSpreadConstraint] = None,
        replica_scheduling: UpdatePropagationPoliciesReplicaSchedulingStrategy = None,
    ):
        # {"en":"the policy that only applies to resources propagated to the matching clusters", "zh_CN":"策略应用到成员集群的目标选择"}
        self.cluster_affinity = cluster_affinity
        # {"en":"toleration of cluster", "zh_CN":"集群容忍度"}
        self.cluster_tolerations = cluster_tolerations
        # {"en":"Cluster grouping constraint", "zh_CN":"根据约束对集群进行分组，把资源分散到多个小组"}
        self.spread_constraints = spread_constraints
        # {"en":"scheduling strategy of replicas", "zh_CN":"副本调度策略"}
        self.replica_scheduling = replica_scheduling

    def validate(self):
        if self.cluster_affinity:
            self.cluster_affinity.validate()
        if self.cluster_tolerations:
            self.cluster_tolerations.validate()
        if self.spread_constraints:
            for k in self.spread_constraints:
                if k:
                    k.validate()
        if self.replica_scheduling:
            self.replica_scheduling.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_affinity is not None:
            result['clusterAffinity'] = self.cluster_affinity.to_map()
        if self.cluster_tolerations is not None:
            result['clusterTolerations'] = self.cluster_tolerations.to_map()
        if self.spread_constraints is not None:
            result['spreadConstraints'] = []
            for k in self.spread_constraints:
                result['spreadConstraints'].append(k.to_map() if k else None)
        if self.replica_scheduling is not None:
            result['replicaScheduling'] = self.replica_scheduling.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterAffinity') is not None:
            temp_model = UpdatePropagationPoliciesClusterAffinity()
            self.cluster_affinity = temp_model.from_map(m['clusterAffinity'])
        if m.get('clusterTolerations') is not None:
            temp_model = UpdatePropagationPoliciesToleration()
            self.cluster_tolerations = temp_model.from_map(m['clusterTolerations'])
        if m.get('spreadConstraints') is not None:
            self.spread_constraints = []
            for k in m.get('spreadConstraints'):
                temp_model = UpdatePropagationPoliciesSpreadConstraint()
                self.spread_constraints.append(temp_model.from_map(k))
        if m.get('replicaScheduling') is not None:
            temp_model = UpdatePropagationPoliciesReplicaSchedulingStrategy()
            self.replica_scheduling = temp_model.from_map(m['replicaScheduling'])
        return self


class UpdatePropagationPoliciesDecisionConditions(TeaModel):
    def __init__(
        self,
        toleration_seconds: int = None,
    ):
        # {"en":"represents the period of time Karmada should wait", "zh_CN":"应用经过多长时间后算失败"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class UpdatePropagationPoliciesApplicationFailoverBehavior(TeaModel):
    def __init__(
        self,
        decision_conditions: UpdatePropagationPoliciesDecisionConditions = None,
        purge_mode: str = None,
        grace_period_seconds: int = None,
    ):
        # {"en":"indicates the decision conditions of performing the failover process.", "zh_CN":"程序经过多长时间的失败,才属于不健康"}
        self.decision_conditions = decision_conditions
        # {"en":"represents how to deal with the legacy applications on the cluster from which the application is migrated. there are three options: Immediately,Graciously and Never. Graciously by defautl", "zh_CN":"应用在失败后的驱逐方式,有3个可填值: Immediately,Graciously and Never 默认:Graciously "}
        self.purge_mode = purge_mode
        # {"en":"the maximum waiting duration in seconds before application on the migrated cluster should be deleted.", "zh_CN":"平滑删除时间"}
        self.grace_period_seconds = grace_period_seconds

    def validate(self):
        if self.decision_conditions:
            self.decision_conditions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decision_conditions is not None:
            result['decisionConditions'] = self.decision_conditions.to_map()
        if self.purge_mode is not None:
            result['purgeMode'] = self.purge_mode
        if self.grace_period_seconds is not None:
            result['gracePeriodSeconds'] = self.grace_period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('decisionConditions') is not None:
            temp_model = UpdatePropagationPoliciesDecisionConditions()
            self.decision_conditions = temp_model.from_map(m['decisionConditions'])
        if m.get('purgeMode') is not None:
            self.purge_mode = m.get('purgeMode')
        if m.get('gracePeriodSeconds') is not None:
            self.grace_period_seconds = m.get('gracePeriodSeconds')
        return self


class UpdatePropagationPoliciesFailoverBehavior(TeaModel):
    def __init__(
        self,
        application: UpdatePropagationPoliciesApplicationFailoverBehavior = None,
    ):
        # {"en":"indicates failover behaviors in case of application failure", "zh_CN":"failover 重调度策略"}
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('application') is not None:
            temp_model = UpdatePropagationPoliciesApplicationFailoverBehavior()
            self.application = temp_model.from_map(m['application'])
        return self


class UpdatePropagationPoliciesPropagationSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[UpdatePropagationPoliciesResourceSelector] = None,
        association: bool = None,
        placement: UpdatePropagationPoliciesPlacement = None,
        dependent_overrides: List[str] = None,
        scheduler_name: str = None,
        failover: UpdatePropagationPoliciesFailoverBehavior = None,
    ):
        # {"en":"resource that this propagation policy applies to", "zh_CN":"策略应用的资源"}
        self.resource_selectors = resource_selectors
        # {"en":"association", "zh_CN":"association"}
        self.association = association
        # {"en":"scheduling strategy", "zh_CN":"调度策略"}
        self.placement = placement
        # {"en":"dependent overrides", "zh_CN":"依赖的覆盖策略"}
        self.dependent_overrides = dependent_overrides
        # {"en":"name of scheduler", "zh_CN":"调度器名称"}
        self.scheduler_name = scheduler_name
        # {"en":"indicates how Karmada migrates applications in case of failures", "zh_CN":"failover 重调度策略"}
        self.failover = failover

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.placement:
            self.placement.validate()
        if self.failover:
            self.failover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.association is not None:
            result['association'] = self.association
        if self.placement is not None:
            result['placement'] = self.placement.to_map()
        if self.dependent_overrides is not None:
            result['dependentOverrides'] = self.dependent_overrides
        if self.scheduler_name is not None:
            result['schedulerName'] = self.scheduler_name
        if self.failover is not None:
            result['failover'] = self.failover.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = UpdatePropagationPoliciesResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('association') is not None:
            self.association = m.get('association')
        if m.get('placement') is not None:
            temp_model = UpdatePropagationPoliciesPlacement()
            self.placement = temp_model.from_map(m['placement'])
        if m.get('dependentOverrides') is not None:
            self.dependent_overrides = m.get('dependentOverrides')
        if m.get('schedulerName') is not None:
            self.scheduler_name = m.get('schedulerName')
        if m.get('failover') is not None:
            temp_model = UpdatePropagationPoliciesFailoverBehavior()
            self.failover = temp_model.from_map(m['failover'])
        return self


class UpdatePropagationPoliciesRequest(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: UpdatePropagationPoliciesObjectMeta = None,
        spec: UpdatePropagationPoliciesPropagationSpec = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a UpdatePropagationPoliciesPropagationPolicy", "zh_CN":"spec 定义 UpdatePropagationPoliciesPropagationPolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

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
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = UpdatePropagationPoliciesObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdatePropagationPoliciesPropagationSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class UpdatePropagationPoliciesPropagationPolicy(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: UpdatePropagationPoliciesObjectMeta = None,
        spec: UpdatePropagationPoliciesPropagationSpec = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a UpdatePropagationPoliciesPropagationPolicy", "zh_CN":"spec 定义 UpdatePropagationPoliciesPropagationPolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

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
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = UpdatePropagationPoliciesObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdatePropagationPoliciesPropagationSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class UpdatePropagationPoliciesResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdatePropagationPoliciesPropagationPolicy = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"UpdatePropagationPoliciesPropagationPolicy object", "zh_CN":"PropagationPolicy对象"}
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
            temp_model = UpdatePropagationPoliciesPropagationPolicy()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdatePropagationPoliciesPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"The name of propagationPolicy", "zh_CN":"propagationPolicy 名称"}
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


class UpdatePropagationPoliciesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdatePropagationPoliciesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdatePropagationPoliciesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PatchHorizontalPodAutoscalerOwnerReference(TeaModel):
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


class PatchHorizontalPodAutoscalerFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PatchHorizontalPodAutoscalerManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: PatchHorizontalPodAutoscalerFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this PatchHorizontalPodAutoscalerManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'PatchHorizontalPodAutoscalerFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“PatchHorizontalPodAutoscalerFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"PatchHorizontalPodAutoscalerFieldsV1 holds the first JSON version format as described in the 'PatchHorizontalPodAutoscalerFieldsV1' type", "zh_CN":"PatchHorizontalPodAutoscalerFieldsV1 包含类型 “PatchHorizontalPodAutoscalerFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = PatchHorizontalPodAutoscalerFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class PatchHorizontalPodAutoscalerObjectMeta(TeaModel):
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
        owner_references: List[PatchHorizontalPodAutoscalerOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[PatchHorizontalPodAutoscalerManagedFieldsEntry] = None,
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
                temp_model = PatchHorizontalPodAutoscalerOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = PatchHorizontalPodAutoscalerManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class PatchHorizontalPodAutoscalerCrossVersionObjectReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the API version of the referent", "zh_CN":"被引用对象的 API 版本"}
        self.api_version = api_version
        # {"en":"the kind of the referent", "zh_CN":"被引用对象的类别"}
        self.kind = kind
        # {"en":"the name of the referent", "zh_CN":"被引用对象的名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.name, 'name')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class PatchHorizontalPodAutoscalerMetricTarget(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        average_value: str = None,
        average_utilization: int = None,
    ):
        # {"en":"type represents whether the metric type is Utilization, Value, or AverageValue", "zh_CN":"type 表示指标类别是 Utilization、Value 或 AverageValue"}
        self.type = type
        # {"en":"the target value of the metric (as a quantity)", "zh_CN":"value 是指标的目标值（以数量形式给出）"}
        self.value = value
        # {"en":"the target value of the average of the metric across all relevant pods (as a quantity)", "zh_CN":"averageValue 是跨所有 Pod 得出的指标均值的目标值（以数量形式给出）"}
        self.average_value = average_value
        # {"en":"the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type", "zh_CN":"averageUtilization 是跨所有相关 Pod 得出的资源指标均值的目标值， 表示为 Pod 资源请求值的百分比。目前仅对 “Resource” 指标源类别有效"}
        self.average_utilization = average_utilization

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.average_value is not None:
            result['averageValue'] = self.average_value
        if self.average_utilization is not None:
            result['averageUtilization'] = self.average_utilization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('averageValue') is not None:
            self.average_value = m.get('averageValue')
        if m.get('averageUtilization') is not None:
            self.average_utilization = m.get('averageUtilization')
        return self


class PatchHorizontalPodAutoscalerLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"the label key that the selector applies to", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist", "zh_CN":"表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class PatchHorizontalPodAutoscalerLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[PatchHorizontalPodAutoscalerLabelSelectorRequirement] = None,
    ):
        # {"en":"a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is 'key', the operator is 'In', and the values array contains only 'value'. The requirements are ANDed", "zh_CN":"matchLabels 是 {key,value} 键值对的映射。matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。所表达的需求最终要按逻辑与的关系组合"}
        self.match_labels = match_labels
        # {"en":"a list of label selector requirements. The requirements are ANDed", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = PatchHorizontalPodAutoscalerLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class PatchHorizontalPodAutoscalerMetricIdentifier(TeaModel):
    def __init__(
        self,
        name: str = None,
        selector: PatchHorizontalPodAutoscalerLabelSelector = None,
    ):
        # {"en":"the name of the given metric", "zh_CN":"给定指标的名称"}
        self.name = name
        # {"en":"the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics", "zh_CN":"给定指标的标准 Kubernetes 标签选择算符的字符串编码形式。 设置后，它作为附加参数传递给指标服务器，以获取更具体的指标范围。 未设置时，仅 metricName 参数将用于收集指标"}
        self.selector = selector

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.selector:
            self.selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('selector') is not None:
            temp_model = PatchHorizontalPodAutoscalerLabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        return self


class PatchHorizontalPodAutoscalerObjectMetricSource(TeaModel):
    def __init__(
        self,
        described_object: PatchHorizontalPodAutoscalerCrossVersionObjectReference = None,
        target: PatchHorizontalPodAutoscalerMetricTarget = None,
        metric: PatchHorizontalPodAutoscalerMetricIdentifier = None,
    ):
        # {"en":"describedObject specifies the descriptions of a object,such as kind,name apiVersion", "zh_CN":"describeObject 表示对象的描述，如对象的 kind、name、apiVersion"}
        self.described_object = described_object
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric

    def validate(self):
        self.validate_required(self.described_object, 'described_object')
        if self.described_object:
            self.described_object.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.described_object is not None:
            result['describedObject'] = self.described_object.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('describedObject') is not None:
            temp_model = PatchHorizontalPodAutoscalerCrossVersionObjectReference()
            self.described_object = temp_model.from_map(m['describedObject'])
        if m.get('target') is not None:
            temp_model = PatchHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('metric') is not None:
            temp_model = PatchHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        return self


class PatchHorizontalPodAutoscalerPodsMetricSource(TeaModel):
    def __init__(
        self,
        metric: PatchHorizontalPodAutoscalerMetricIdentifier = None,
        target: PatchHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = PatchHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = PatchHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class PatchHorizontalPodAutoscalerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: PatchHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = PatchHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class PatchHorizontalPodAutoscalerContainerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: PatchHorizontalPodAutoscalerMetricTarget = None,
        container: str = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target
        # {"en":"the name of the container in the pods of the scaling target", "zh_CN":"扩缩目标的 Pod 中容器的名称"}
        self.container = container

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.container, 'container')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.container is not None:
            result['container'] = self.container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = PatchHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('container') is not None:
            self.container = m.get('container')
        return self


class PatchHorizontalPodAutoscalerExternalMetricSource(TeaModel):
    def __init__(
        self,
        metric: PatchHorizontalPodAutoscalerMetricIdentifier = None,
        target: PatchHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = PatchHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = PatchHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class PatchHorizontalPodAutoscalerMetricSpec(TeaModel):
    def __init__(
        self,
        type: str = None,
        object: PatchHorizontalPodAutoscalerObjectMetricSource = None,
        pods: PatchHorizontalPodAutoscalerPodsMetricSource = None,
        resource: PatchHorizontalPodAutoscalerResourceMetricSource = None,
        container_resource: PatchHorizontalPodAutoscalerContainerResourceMetricSource = None,
        external: PatchHorizontalPodAutoscalerExternalMetricSource = None,
    ):
        # {"en":"the type of metric source. It should be one of 'ContainerResource', 'External', 'Object', 'Pods' or 'Resource', each mapping to a matching field in the object. Note: 'ContainerResource' type is available on when the feature-gate HPAContainerMetrics is enabled", "zh_CN":"type 是指标源的类别。它取值是 “ContainerResource”、“External”、“Object”、“Pods” 或 “Resource” 之一， 每个类别映射到对象中的一个对应的字段。注意：“ContainerResource” 类别在特性门控 HPAContainerMetrics 启用时可用"}
        self.type = type
        # {"en":"refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object)", "zh_CN":"指描述单个 Kubernetes 对象的指标"}
        self.object = object
        # {"en":"refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value", "zh_CN":"指描述当前扩缩目标中每个 Pod 的指标（例如，transactions-processed-per-second）。 在与目标值进行比较之前，这些指标值将被平均"}
        self.pods = pods
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 此结构描述当前扩缩目标中的每个 Pod（例如 CPU 或内存）。此类指标内置于 Kubernetes 中， 并且在使用 “Pods” 源的、按 Pod 统计的普通指标之外支持一些特殊的扩缩选项"}
        self.resource = resource
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 描述当前扩缩目标中每个 Pod 中的单个容器（例如 CPU 或内存）。 此类指标内置于 Kubernetes 中，在使用 “pods” 源的、按 Pod 计算的普通指标之外，还具有一些特殊的扩缩选项。 这是一个 Alpha 特性，可以通过 HPAContainerMetrics 特性标志启用"}
        self.container_resource = container_resource
        # {"en":"refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)", "zh_CN":"指的是不与任何 Kubernetes 对象关联的全局指标。 这一字段允许基于来自集群外部运行的组件（例如云消息服务中的队列长度，或来自运行在集群外部的负载均衡器的 QPS）的信息进行自动扩缩容"}
        self.external = external

    def validate(self):
        self.validate_required(self.type, 'type')
        if self.object:
            self.object.validate()
        if self.pods:
            self.pods.validate()
        if self.resource:
            self.resource.validate()
        if self.container_resource:
            self.container_resource.validate()
        if self.external:
            self.external.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.object is not None:
            result['object'] = self.object.to_map()
        if self.pods is not None:
            result['pods'] = self.pods.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.container_resource is not None:
            result['containerResource'] = self.container_resource.to_map()
        if self.external is not None:
            result['external'] = self.external.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('object') is not None:
            temp_model = PatchHorizontalPodAutoscalerObjectMetricSource()
            self.object = temp_model.from_map(m['object'])
        if m.get('pods') is not None:
            temp_model = PatchHorizontalPodAutoscalerPodsMetricSource()
            self.pods = temp_model.from_map(m['pods'])
        if m.get('resource') is not None:
            temp_model = PatchHorizontalPodAutoscalerResourceMetricSource()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('containerResource') is not None:
            temp_model = PatchHorizontalPodAutoscalerContainerResourceMetricSource()
            self.container_resource = temp_model.from_map(m['containerResource'])
        if m.get('external') is not None:
            temp_model = PatchHorizontalPodAutoscalerExternalMetricSource()
            self.external = temp_model.from_map(m['external'])
        return self


class PatchHorizontalPodAutoscalerHPAScalingPolicy(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
        period_seconds: int = None,
    ):
        # {"en":"type is used to specify the scaling policy", "zh_CN":"type 用于指定扩缩策略"}
        self.type = type
        # {"en":"value contains the amount of change which is permitted by the policy. It must be greater than zero", "zh_CN":"value 包含策略允许的更改量。它必须大于零"}
        self.value = value
        # {"en":"periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min)", "zh_CN":"periodSeconds 表示策略应该保持为 true 的时间窗口长度。 periodSeconds 必须大于零且小于或等于 1800（30 分钟）"}
        self.period_seconds = period_seconds

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.period_seconds, 'period_seconds')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        return self


class PatchHorizontalPodAutoscalerHPAScalingRules(TeaModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
        select_policy: str = None,
        policies: List[PatchHorizontalPodAutoscalerHPAScalingPolicy] = None,
    ):
        # {"en":"stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long)", "zh_CN":"stabilizationWindowSeconds 是在扩缩容时应考虑的之前建议的秒数。stabilizationWindowSeconds 必须大于或等于零且小于或等于 3600（一小时）。如果未设置，则使用默认值：扩容：0（不设置稳定窗口）。缩容：300（即稳定窗口为 300 秒）"}
        self.stabilization_window_seconds = stabilization_window_seconds
        # {"en":"selectPolicy is used to specify which policy should be used. If not set, the default value Max is used", "zh_CN":"selectPolicy 用于指定应该使用哪个策略。如果未设置，则使用默认值 Max"}
        self.select_policy = select_policy
        # {"en":"policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the PatchHorizontalPodAutoscalerHPAScalingRules will be discarded as invalid", "zh_CN":"policies 是可在扩缩容过程中使用的潜在扩缩策略的列表。必须至少指定一个策略，否则 PatchHorizontalPodAutoscalerHPAScalingRules 将被视为无效而丢弃"}
        self.policies = policies

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.select_policy is not None:
            result['selectPolicy'] = self.select_policy
        if self.policies is not None:
            result['policies'] = []
            for k in self.policies:
                result['policies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')
        if m.get('selectPolicy') is not None:
            self.select_policy = m.get('selectPolicy')
        if m.get('policies') is not None:
            self.policies = []
            for k in m.get('policies'):
                temp_model = PatchHorizontalPodAutoscalerHPAScalingPolicy()
                self.policies.append(temp_model.from_map(k))
        return self


class PatchHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior(TeaModel):
    def __init__(
        self,
        scale_up: PatchHorizontalPodAutoscalerHPAScalingRules = None,
        scale_down: PatchHorizontalPodAutoscalerHPAScalingRules = None,
    ):
        # {"en":"scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:- increase no more than 4 pods per 60 seconds- double the number of pods per 60 seconds No stabilization is used", "zh_CN":"scaleUp 是用于扩容的扩缩策略。如果未设置，则默认值为以下值中的较高者：- 每 60 秒增加不超过 4 个 Pod- 每 60 秒 Pod 数量翻倍。不使用稳定窗口"}
        self.scale_up = scale_up
        # {"en":"scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used)", "zh_CN":"scaleDown 是缩容策略。如果未设置，则默认值允许缩减到 minReplicas 数量的 Pod， 具有 300 秒的稳定窗口（使用最近 300 秒的最高推荐值）"}
        self.scale_down = scale_down

    def validate(self):
        if self.scale_up:
            self.scale_up.validate()
        if self.scale_down:
            self.scale_down.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_up is not None:
            result['scaleUp'] = self.scale_up.to_map()
        if self.scale_down is not None:
            result['scaleDown'] = self.scale_down.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleUp') is not None:
            temp_model = PatchHorizontalPodAutoscalerHPAScalingRules()
            self.scale_up = temp_model.from_map(m['scaleUp'])
        if m.get('scaleDown') is not None:
            temp_model = PatchHorizontalPodAutoscalerHPAScalingRules()
            self.scale_down = temp_model.from_map(m['scaleDown'])
        return self


class PatchHorizontalPodAutoscalerHorizontalPodAutoscalerSpec(TeaModel):
    def __init__(
        self,
        scale_target_ref: PatchHorizontalPodAutoscalerCrossVersionObjectReference = None,
        min_replicas: int = None,
        max_replicas: int = None,
        metrics: List[PatchHorizontalPodAutoscalerMetricSpec] = None,
        behavior: PatchHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior = None,
    ):
        # {"en":"reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource", "zh_CN":"对被扩缩资源的引用； 水平 Pod 自动缩放器将了解当前的资源消耗，并使用其 scale 子资源设置所需的 Pod 数量"}
        self.scale_target_ref = scale_target_ref
        # {"en":"the lower limit for the number of replicas to which the autoscaler can scale down. It defaults to 1 pod. minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured. Scaling is active as long as at least one metric value is available", "zh_CN":"自动缩放器可以缩减的副本数的下限。 它默认为 1 个 Pod。 如果启用了 alpha 特性门禁 HPAScaleToZero 并且配置了至少一个 Object 或 External 度量标准， 则 minReplicas 允许为 0。 只要至少有一个度量值可用，缩放就处于活动状态"}
        self.min_replicas = min_replicas
        # {"en":"the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas", "zh_CN":"自动扩缩器可以设置的 Pod 数量上限； 不能小于 minReplicas"}
        self.max_replicas = max_replicas
        # {"en":"metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used). The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa. See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization", "zh_CN":"metrics 包含用于计算预期副本数的规约（将使用所有指标的最大副本数）。 预期副本数是通过将目标值与当前值之间的比率乘以当前 Pod 数来计算的。 因此，使用的指标必须随着 Pod 数量的增加而减少，反之亦然。 有关每种类别的指标必须如何响应的更多信息，请参阅各个指标源类别。 如果未设置，默认指标将设置为 80% 的平均 CPU 利用率"}
        self.metrics = metrics
        # {"en":"behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default PatchHorizontalPodAutoscalerHPAScalingRules for scale up and scale down are used", "zh_CN":"behavior 配置目标在扩容（Up）和缩容（Down）两个方向的扩缩行为（分别用 scaleUp 和 scaleDown 字段）。 如果未设置，则会使用默认的 PatchHorizontalPodAutoscalerHPAScalingRules 进行扩缩容"}
        self.behavior = behavior

    def validate(self):
        self.validate_required(self.scale_target_ref, 'scale_target_ref')
        if self.scale_target_ref:
            self.scale_target_ref.validate()
        self.validate_required(self.max_replicas, 'max_replicas')
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.behavior:
            self.behavior.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_target_ref is not None:
            result['scaleTargetRef'] = self.scale_target_ref.to_map()
        if self.min_replicas is not None:
            result['minReplicas'] = self.min_replicas
        if self.max_replicas is not None:
            result['maxReplicas'] = self.max_replicas
        if self.metrics is not None:
            result['metrics'] = []
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.behavior is not None:
            result['behavior'] = self.behavior.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleTargetRef') is not None:
            temp_model = PatchHorizontalPodAutoscalerCrossVersionObjectReference()
            self.scale_target_ref = temp_model.from_map(m['scaleTargetRef'])
        if m.get('minReplicas') is not None:
            self.min_replicas = m.get('minReplicas')
        if m.get('maxReplicas') is not None:
            self.max_replicas = m.get('maxReplicas')
        if m.get('metrics') is not None:
            self.metrics = []
            for k in m.get('metrics'):
                temp_model = PatchHorizontalPodAutoscalerMetricSpec()
                self.metrics.append(temp_model.from_map(k))
        if m.get('behavior') is not None:
            temp_model = PatchHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior()
            self.behavior = temp_model.from_map(m['behavior'])
        return self


class PatchHorizontalPodAutoscalerRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PatchHorizontalPodAutoscalerObjectMeta = None,
        spec: PatchHorizontalPodAutoscalerHorizontalPodAutoscalerSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"spec defines the behaviour of autoscaler.", "zh_CN":"spec 定义自动缩放器的规约"}
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
            temp_model = PatchHorizontalPodAutoscalerObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PatchHorizontalPodAutoscalerHorizontalPodAutoscalerSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class PatchHorizontalPodAutoscalerHorizontalPodAutoscalerStatus(TeaModel):
    def __init__(
        self,
        observed_generation: int = None,
        current_replicas: int = None,
        desired_replicas: int = None,
    ):
        # {"en":"the most recent generation observed by this autoscaler", "zh_CN":"observedGeneration 是此自动缩放器观察到的最新一代"}
        self.observed_generation = observed_generation
        # {"en":"the current number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 的当前副本数"}
        self.current_replicas = current_replicas
        # {"en":"the desired number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 副本的所需数量"}
        self.desired_replicas = desired_replicas

    def validate(self):
        self.validate_required(self.current_replicas, 'current_replicas')
        self.validate_required(self.desired_replicas, 'desired_replicas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.current_replicas is not None:
            result['currentReplicas'] = self.current_replicas
        if self.desired_replicas is not None:
            result['desiredReplicas'] = self.desired_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('currentReplicas') is not None:
            self.current_replicas = m.get('currentReplicas')
        if m.get('desiredReplicas') is not None:
            self.desired_replicas = m.get('desiredReplicas')
        return self


class PatchHorizontalPodAutoscalerHorizontalPodAutoscaler(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PatchHorizontalPodAutoscalerObjectMeta = None,
        spec: PatchHorizontalPodAutoscalerHorizontalPodAutoscalerSpec = None,
        status: PatchHorizontalPodAutoscalerHorizontalPodAutoscalerStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"spec defines the behaviour of autoscaler.", "zh_CN":"spec 定义自动缩放器的规约"}
        self.spec = spec
        # {"en":"the current information about the autoscaler", "zh_CN":"自动缩放器的当前信息"}
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
            temp_model = PatchHorizontalPodAutoscalerObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PatchHorizontalPodAutoscalerHorizontalPodAutoscalerSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = PatchHorizontalPodAutoscalerHorizontalPodAutoscalerStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class PatchHorizontalPodAutoscalerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: PatchHorizontalPodAutoscalerHorizontalPodAutoscaler = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"PatchHorizontalPodAutoscalerHorizontalPodAutoscaler", "zh_CN":"PatchHorizontalPodAutoscalerHorizontalPodAutoscaler"}
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
            temp_model = PatchHorizontalPodAutoscalerHorizontalPodAutoscaler()
            self.data = temp_model.from_map(m['data'])
        return self


class PatchHorizontalPodAutoscalerPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"资源name", "zh_CN":"资源名称"}
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


class PatchHorizontalPodAutoscalerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PatchHorizontalPodAutoscalerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PatchHorizontalPodAutoscalerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateHorizontalPodAutoscalerOwnerReference(TeaModel):
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


class CreateHorizontalPodAutoscalerFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateHorizontalPodAutoscalerManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: CreateHorizontalPodAutoscalerFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this CreateHorizontalPodAutoscalerManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'CreateHorizontalPodAutoscalerFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“CreateHorizontalPodAutoscalerFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"CreateHorizontalPodAutoscalerFieldsV1 holds the first JSON version format as described in the 'CreateHorizontalPodAutoscalerFieldsV1' type", "zh_CN":"CreateHorizontalPodAutoscalerFieldsV1 包含类型 “CreateHorizontalPodAutoscalerFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = CreateHorizontalPodAutoscalerFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class CreateHorizontalPodAutoscalerObjectMeta(TeaModel):
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
        owner_references: List[CreateHorizontalPodAutoscalerOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[CreateHorizontalPodAutoscalerManagedFieldsEntry] = None,
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
                temp_model = CreateHorizontalPodAutoscalerOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = CreateHorizontalPodAutoscalerManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class CreateHorizontalPodAutoscalerCrossVersionObjectReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the API version of the referent", "zh_CN":"被引用对象的 API 版本"}
        self.api_version = api_version
        # {"en":"the kind of the referent", "zh_CN":"被引用对象的类别"}
        self.kind = kind
        # {"en":"the name of the referent", "zh_CN":"被引用对象的名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.name, 'name')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateHorizontalPodAutoscalerMetricTarget(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        average_value: str = None,
        average_utilization: int = None,
    ):
        # {"en":"type represents whether the metric type is Utilization, Value, or AverageValue", "zh_CN":"type 表示指标类别是 Utilization、Value 或 AverageValue"}
        self.type = type
        # {"en":"the target value of the metric (as a quantity)", "zh_CN":"value 是指标的目标值（以数量形式给出）"}
        self.value = value
        # {"en":"the target value of the average of the metric across all relevant pods (as a quantity)", "zh_CN":"averageValue 是跨所有 Pod 得出的指标均值的目标值（以数量形式给出）"}
        self.average_value = average_value
        # {"en":"the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type", "zh_CN":"averageUtilization 是跨所有相关 Pod 得出的资源指标均值的目标值， 表示为 Pod 资源请求值的百分比。目前仅对 “Resource” 指标源类别有效"}
        self.average_utilization = average_utilization

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.average_value is not None:
            result['averageValue'] = self.average_value
        if self.average_utilization is not None:
            result['averageUtilization'] = self.average_utilization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('averageValue') is not None:
            self.average_value = m.get('averageValue')
        if m.get('averageUtilization') is not None:
            self.average_utilization = m.get('averageUtilization')
        return self


class CreateHorizontalPodAutoscalerLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"the label key that the selector applies to", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist", "zh_CN":"表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateHorizontalPodAutoscalerLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[CreateHorizontalPodAutoscalerLabelSelectorRequirement] = None,
    ):
        # {"en":"a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is 'key', the operator is 'In', and the values array contains only 'value'. The requirements are ANDed", "zh_CN":"matchLabels 是 {key,value} 键值对的映射。matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。所表达的需求最终要按逻辑与的关系组合"}
        self.match_labels = match_labels
        # {"en":"a list of label selector requirements. The requirements are ANDed", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = CreateHorizontalPodAutoscalerLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class CreateHorizontalPodAutoscalerMetricIdentifier(TeaModel):
    def __init__(
        self,
        name: str = None,
        selector: CreateHorizontalPodAutoscalerLabelSelector = None,
    ):
        # {"en":"the name of the given metric", "zh_CN":"给定指标的名称"}
        self.name = name
        # {"en":"the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics", "zh_CN":"给定指标的标准 Kubernetes 标签选择算符的字符串编码形式。 设置后，它作为附加参数传递给指标服务器，以获取更具体的指标范围。 未设置时，仅 metricName 参数将用于收集指标"}
        self.selector = selector

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.selector:
            self.selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('selector') is not None:
            temp_model = CreateHorizontalPodAutoscalerLabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        return self


class CreateHorizontalPodAutoscalerObjectMetricSource(TeaModel):
    def __init__(
        self,
        described_object: CreateHorizontalPodAutoscalerCrossVersionObjectReference = None,
        target: CreateHorizontalPodAutoscalerMetricTarget = None,
        metric: CreateHorizontalPodAutoscalerMetricIdentifier = None,
    ):
        # {"en":"describedObject specifies the descriptions of a object,such as kind,name apiVersion", "zh_CN":"describeObject 表示对象的描述，如对象的 kind、name、apiVersion"}
        self.described_object = described_object
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric

    def validate(self):
        self.validate_required(self.described_object, 'described_object')
        if self.described_object:
            self.described_object.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.described_object is not None:
            result['describedObject'] = self.described_object.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('describedObject') is not None:
            temp_model = CreateHorizontalPodAutoscalerCrossVersionObjectReference()
            self.described_object = temp_model.from_map(m['describedObject'])
        if m.get('target') is not None:
            temp_model = CreateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('metric') is not None:
            temp_model = CreateHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        return self


class CreateHorizontalPodAutoscalerPodsMetricSource(TeaModel):
    def __init__(
        self,
        metric: CreateHorizontalPodAutoscalerMetricIdentifier = None,
        target: CreateHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = CreateHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = CreateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class CreateHorizontalPodAutoscalerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: CreateHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = CreateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class CreateHorizontalPodAutoscalerContainerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: CreateHorizontalPodAutoscalerMetricTarget = None,
        container: str = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target
        # {"en":"the name of the container in the pods of the scaling target", "zh_CN":"扩缩目标的 Pod 中容器的名称"}
        self.container = container

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.container, 'container')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.container is not None:
            result['container'] = self.container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = CreateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('container') is not None:
            self.container = m.get('container')
        return self


class CreateHorizontalPodAutoscalerExternalMetricSource(TeaModel):
    def __init__(
        self,
        metric: CreateHorizontalPodAutoscalerMetricIdentifier = None,
        target: CreateHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = CreateHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = CreateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class CreateHorizontalPodAutoscalerMetricSpec(TeaModel):
    def __init__(
        self,
        type: str = None,
        object: CreateHorizontalPodAutoscalerObjectMetricSource = None,
        pods: CreateHorizontalPodAutoscalerPodsMetricSource = None,
        resource: CreateHorizontalPodAutoscalerResourceMetricSource = None,
        container_resource: CreateHorizontalPodAutoscalerContainerResourceMetricSource = None,
        external: CreateHorizontalPodAutoscalerExternalMetricSource = None,
    ):
        # {"en":"the type of metric source. It should be one of 'ContainerResource', 'External', 'Object', 'Pods' or 'Resource', each mapping to a matching field in the object. Note: 'ContainerResource' type is available on when the feature-gate HPAContainerMetrics is enabled", "zh_CN":"type 是指标源的类别。它取值是 “ContainerResource”、“External”、“Object”、“Pods” 或 “Resource” 之一， 每个类别映射到对象中的一个对应的字段。注意：“ContainerResource” 类别在特性门控 HPAContainerMetrics 启用时可用"}
        self.type = type
        # {"en":"refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object)", "zh_CN":"指描述单个 Kubernetes 对象的指标"}
        self.object = object
        # {"en":"refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value", "zh_CN":"指描述当前扩缩目标中每个 Pod 的指标（例如，transactions-processed-per-second）。 在与目标值进行比较之前，这些指标值将被平均"}
        self.pods = pods
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 此结构描述当前扩缩目标中的每个 Pod（例如 CPU 或内存）。此类指标内置于 Kubernetes 中， 并且在使用 “Pods” 源的、按 Pod 统计的普通指标之外支持一些特殊的扩缩选项"}
        self.resource = resource
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 描述当前扩缩目标中每个 Pod 中的单个容器（例如 CPU 或内存）。 此类指标内置于 Kubernetes 中，在使用 “pods” 源的、按 Pod 计算的普通指标之外，还具有一些特殊的扩缩选项。 这是一个 Alpha 特性，可以通过 HPAContainerMetrics 特性标志启用"}
        self.container_resource = container_resource
        # {"en":"refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)", "zh_CN":"指的是不与任何 Kubernetes 对象关联的全局指标。 这一字段允许基于来自集群外部运行的组件（例如云消息服务中的队列长度，或来自运行在集群外部的负载均衡器的 QPS）的信息进行自动扩缩容"}
        self.external = external

    def validate(self):
        self.validate_required(self.type, 'type')
        if self.object:
            self.object.validate()
        if self.pods:
            self.pods.validate()
        if self.resource:
            self.resource.validate()
        if self.container_resource:
            self.container_resource.validate()
        if self.external:
            self.external.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.object is not None:
            result['object'] = self.object.to_map()
        if self.pods is not None:
            result['pods'] = self.pods.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.container_resource is not None:
            result['containerResource'] = self.container_resource.to_map()
        if self.external is not None:
            result['external'] = self.external.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('object') is not None:
            temp_model = CreateHorizontalPodAutoscalerObjectMetricSource()
            self.object = temp_model.from_map(m['object'])
        if m.get('pods') is not None:
            temp_model = CreateHorizontalPodAutoscalerPodsMetricSource()
            self.pods = temp_model.from_map(m['pods'])
        if m.get('resource') is not None:
            temp_model = CreateHorizontalPodAutoscalerResourceMetricSource()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('containerResource') is not None:
            temp_model = CreateHorizontalPodAutoscalerContainerResourceMetricSource()
            self.container_resource = temp_model.from_map(m['containerResource'])
        if m.get('external') is not None:
            temp_model = CreateHorizontalPodAutoscalerExternalMetricSource()
            self.external = temp_model.from_map(m['external'])
        return self


class CreateHorizontalPodAutoscalerHPAScalingPolicy(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
        period_seconds: int = None,
    ):
        # {"en":"type is used to specify the scaling policy", "zh_CN":"type 用于指定扩缩策略"}
        self.type = type
        # {"en":"value contains the amount of change which is permitted by the policy. It must be greater than zero", "zh_CN":"value 包含策略允许的更改量。它必须大于零"}
        self.value = value
        # {"en":"periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min)", "zh_CN":"periodSeconds 表示策略应该保持为 true 的时间窗口长度。 periodSeconds 必须大于零且小于或等于 1800（30 分钟）"}
        self.period_seconds = period_seconds

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.period_seconds, 'period_seconds')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        return self


class CreateHorizontalPodAutoscalerHPAScalingRules(TeaModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
        select_policy: str = None,
        policies: List[CreateHorizontalPodAutoscalerHPAScalingPolicy] = None,
    ):
        # {"en":"stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long)", "zh_CN":"stabilizationWindowSeconds 是在扩缩容时应考虑的之前建议的秒数。stabilizationWindowSeconds 必须大于或等于零且小于或等于 3600（一小时）。如果未设置，则使用默认值：扩容：0（不设置稳定窗口）。缩容：300（即稳定窗口为 300 秒）"}
        self.stabilization_window_seconds = stabilization_window_seconds
        # {"en":"selectPolicy is used to specify which policy should be used. If not set, the default value Max is used", "zh_CN":"selectPolicy 用于指定应该使用哪个策略。如果未设置，则使用默认值 Max"}
        self.select_policy = select_policy
        # {"en":"policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the CreateHorizontalPodAutoscalerHPAScalingRules will be discarded as invalid", "zh_CN":"policies 是可在扩缩容过程中使用的潜在扩缩策略的列表。必须至少指定一个策略，否则 CreateHorizontalPodAutoscalerHPAScalingRules 将被视为无效而丢弃"}
        self.policies = policies

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.select_policy is not None:
            result['selectPolicy'] = self.select_policy
        if self.policies is not None:
            result['policies'] = []
            for k in self.policies:
                result['policies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')
        if m.get('selectPolicy') is not None:
            self.select_policy = m.get('selectPolicy')
        if m.get('policies') is not None:
            self.policies = []
            for k in m.get('policies'):
                temp_model = CreateHorizontalPodAutoscalerHPAScalingPolicy()
                self.policies.append(temp_model.from_map(k))
        return self


class CreateHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior(TeaModel):
    def __init__(
        self,
        scale_up: CreateHorizontalPodAutoscalerHPAScalingRules = None,
        scale_down: CreateHorizontalPodAutoscalerHPAScalingRules = None,
    ):
        # {"en":"scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:- increase no more than 4 pods per 60 seconds- double the number of pods per 60 seconds No stabilization is used", "zh_CN":"scaleUp 是用于扩容的扩缩策略。如果未设置，则默认值为以下值中的较高者：- 每 60 秒增加不超过 4 个 Pod- 每 60 秒 Pod 数量翻倍。不使用稳定窗口"}
        self.scale_up = scale_up
        # {"en":"scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used)", "zh_CN":"scaleDown 是缩容策略。如果未设置，则默认值允许缩减到 minReplicas 数量的 Pod， 具有 300 秒的稳定窗口（使用最近 300 秒的最高推荐值）"}
        self.scale_down = scale_down

    def validate(self):
        if self.scale_up:
            self.scale_up.validate()
        if self.scale_down:
            self.scale_down.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_up is not None:
            result['scaleUp'] = self.scale_up.to_map()
        if self.scale_down is not None:
            result['scaleDown'] = self.scale_down.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleUp') is not None:
            temp_model = CreateHorizontalPodAutoscalerHPAScalingRules()
            self.scale_up = temp_model.from_map(m['scaleUp'])
        if m.get('scaleDown') is not None:
            temp_model = CreateHorizontalPodAutoscalerHPAScalingRules()
            self.scale_down = temp_model.from_map(m['scaleDown'])
        return self


class CreateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec(TeaModel):
    def __init__(
        self,
        scale_target_ref: CreateHorizontalPodAutoscalerCrossVersionObjectReference = None,
        min_replicas: int = None,
        max_replicas: int = None,
        metrics: List[CreateHorizontalPodAutoscalerMetricSpec] = None,
        behavior: CreateHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior = None,
    ):
        # {"en":"reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource", "zh_CN":"对被扩缩资源的引用； 水平 Pod 自动缩放器将了解当前的资源消耗，并使用其 scale 子资源设置所需的 Pod 数量"}
        self.scale_target_ref = scale_target_ref
        # {"en":"the lower limit for the number of replicas to which the autoscaler can scale down. It defaults to 1 pod. minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured. Scaling is active as long as at least one metric value is available", "zh_CN":"自动缩放器可以缩减的副本数的下限。 它默认为 1 个 Pod。 如果启用了 alpha 特性门禁 HPAScaleToZero 并且配置了至少一个 Object 或 External 度量标准， 则 minReplicas 允许为 0。 只要至少有一个度量值可用，缩放就处于活动状态"}
        self.min_replicas = min_replicas
        # {"en":"the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas", "zh_CN":"自动扩缩器可以设置的 Pod 数量上限； 不能小于 minReplicas"}
        self.max_replicas = max_replicas
        # {"en":"metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used). The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa. See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization", "zh_CN":"metrics 包含用于计算预期副本数的规约（将使用所有指标的最大副本数）。 预期副本数是通过将目标值与当前值之间的比率乘以当前 Pod 数来计算的。 因此，使用的指标必须随着 Pod 数量的增加而减少，反之亦然。 有关每种类别的指标必须如何响应的更多信息，请参阅各个指标源类别。 如果未设置，默认指标将设置为 80% 的平均 CPU 利用率"}
        self.metrics = metrics
        # {"en":"behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default CreateHorizontalPodAutoscalerHPAScalingRules for scale up and scale down are used", "zh_CN":"behavior 配置目标在扩容（Up）和缩容（Down）两个方向的扩缩行为（分别用 scaleUp 和 scaleDown 字段）。 如果未设置，则会使用默认的 CreateHorizontalPodAutoscalerHPAScalingRules 进行扩缩容"}
        self.behavior = behavior

    def validate(self):
        self.validate_required(self.scale_target_ref, 'scale_target_ref')
        if self.scale_target_ref:
            self.scale_target_ref.validate()
        self.validate_required(self.max_replicas, 'max_replicas')
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.behavior:
            self.behavior.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_target_ref is not None:
            result['scaleTargetRef'] = self.scale_target_ref.to_map()
        if self.min_replicas is not None:
            result['minReplicas'] = self.min_replicas
        if self.max_replicas is not None:
            result['maxReplicas'] = self.max_replicas
        if self.metrics is not None:
            result['metrics'] = []
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.behavior is not None:
            result['behavior'] = self.behavior.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleTargetRef') is not None:
            temp_model = CreateHorizontalPodAutoscalerCrossVersionObjectReference()
            self.scale_target_ref = temp_model.from_map(m['scaleTargetRef'])
        if m.get('minReplicas') is not None:
            self.min_replicas = m.get('minReplicas')
        if m.get('maxReplicas') is not None:
            self.max_replicas = m.get('maxReplicas')
        if m.get('metrics') is not None:
            self.metrics = []
            for k in m.get('metrics'):
                temp_model = CreateHorizontalPodAutoscalerMetricSpec()
                self.metrics.append(temp_model.from_map(k))
        if m.get('behavior') is not None:
            temp_model = CreateHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior()
            self.behavior = temp_model.from_map(m['behavior'])
        return self


class CreateHorizontalPodAutoscalerRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateHorizontalPodAutoscalerObjectMeta = None,
        spec: CreateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"spec defines the behaviour of autoscaler.", "zh_CN":"spec 定义自动缩放器的规约"}
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
            temp_model = CreateHorizontalPodAutoscalerObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreateHorizontalPodAutoscalerHorizontalPodAutoscalerStatus(TeaModel):
    def __init__(
        self,
        observed_generation: int = None,
        current_replicas: int = None,
        desired_replicas: int = None,
    ):
        # {"en":"the most recent generation observed by this autoscaler", "zh_CN":"observedGeneration 是此自动缩放器观察到的最新一代"}
        self.observed_generation = observed_generation
        # {"en":"the current number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 的当前副本数"}
        self.current_replicas = current_replicas
        # {"en":"the desired number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 副本的所需数量"}
        self.desired_replicas = desired_replicas

    def validate(self):
        self.validate_required(self.current_replicas, 'current_replicas')
        self.validate_required(self.desired_replicas, 'desired_replicas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.current_replicas is not None:
            result['currentReplicas'] = self.current_replicas
        if self.desired_replicas is not None:
            result['desiredReplicas'] = self.desired_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('currentReplicas') is not None:
            self.current_replicas = m.get('currentReplicas')
        if m.get('desiredReplicas') is not None:
            self.desired_replicas = m.get('desiredReplicas')
        return self


class CreateHorizontalPodAutoscalerHorizontalPodAutoscaler(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateHorizontalPodAutoscalerObjectMeta = None,
        spec: CreateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec = None,
        status: CreateHorizontalPodAutoscalerHorizontalPodAutoscalerStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"spec defines the behaviour of autoscaler.", "zh_CN":"spec 定义自动缩放器的规约"}
        self.spec = spec
        # {"en":"the current information about the autoscaler", "zh_CN":"自动缩放器的当前信息"}
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
            temp_model = CreateHorizontalPodAutoscalerObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = CreateHorizontalPodAutoscalerHorizontalPodAutoscalerStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class CreateHorizontalPodAutoscalerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateHorizontalPodAutoscalerHorizontalPodAutoscaler = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"CreateHorizontalPodAutoscalerHorizontalPodAutoscaler", "zh_CN":"CreateHorizontalPodAutoscalerHorizontalPodAutoscaler"}
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
            temp_model = CreateHorizontalPodAutoscalerHorizontalPodAutoscaler()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateHorizontalPodAutoscalerPaths(TeaModel):
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


class CreateHorizontalPodAutoscalerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateHorizontalPodAutoscalerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateHorizontalPodAutoscalerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteOverridepolicyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteOverridepolicyStatusDetails(TeaModel):
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


class DeleteOverridepolicyStatus(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        status: str = None,
        code: int = None,
        details: DeleteOverridepolicyStatusDetails = None,
    ):
        # {"en":"APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values", "zh_CN":"APIVersion 定义对象表示的版本化模式。 服务器应将已识别的模式转换为最新的内部值，并可能拒绝无法识别的值"}
        self.api_version = api_version
        # {"en":"Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase", "zh_CN":"Kind 是一个字符串值，表示此对象表示的 REST 资源。 服务器可以从客户端提交请求的端点推断出这一点。 无法更新。驼峰式规则"}
        self.kind = kind
        # {"en":"DeleteOverridepolicyStatus of the operation. One of: 'Success' or 'Failure'", "zh_CN":"操作状态。“Success”或“Failure” 之一"}
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
            temp_model = DeleteOverridepolicyStatusDetails()
            self.details = temp_model.from_map(m['details'])
        return self


class DeleteOverridepolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: DeleteOverridepolicyStatus = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"delete status", "zh_CN":"删除结果详情"}
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
            temp_model = DeleteOverridepolicyStatus()
            self.data = temp_model.from_map(m['data'])
        return self


class DeleteOverridepolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"The name of overridePolicy", "zh_CN":"overridePolicy 名称"}
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


class DeleteOverridepolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteOverridepolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteOverridepolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateHorizontalPodAutoscalerOwnerReference(TeaModel):
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


class UpdateHorizontalPodAutoscalerFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateHorizontalPodAutoscalerManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: UpdateHorizontalPodAutoscalerFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this UpdateHorizontalPodAutoscalerManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'UpdateHorizontalPodAutoscalerFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“UpdateHorizontalPodAutoscalerFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"UpdateHorizontalPodAutoscalerFieldsV1 holds the first JSON version format as described in the 'UpdateHorizontalPodAutoscalerFieldsV1' type", "zh_CN":"UpdateHorizontalPodAutoscalerFieldsV1 包含类型 “UpdateHorizontalPodAutoscalerFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = UpdateHorizontalPodAutoscalerFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class UpdateHorizontalPodAutoscalerObjectMeta(TeaModel):
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
        owner_references: List[UpdateHorizontalPodAutoscalerOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[UpdateHorizontalPodAutoscalerManagedFieldsEntry] = None,
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
                temp_model = UpdateHorizontalPodAutoscalerOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = UpdateHorizontalPodAutoscalerManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class UpdateHorizontalPodAutoscalerCrossVersionObjectReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the API version of the referent", "zh_CN":"被引用对象的 API 版本"}
        self.api_version = api_version
        # {"en":"the kind of the referent", "zh_CN":"被引用对象的类别"}
        self.kind = kind
        # {"en":"the name of the referent", "zh_CN":"被引用对象的名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.name, 'name')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateHorizontalPodAutoscalerMetricTarget(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        average_value: str = None,
        average_utilization: int = None,
    ):
        # {"en":"type represents whether the metric type is Utilization, Value, or AverageValue", "zh_CN":"type 表示指标类别是 Utilization、Value 或 AverageValue"}
        self.type = type
        # {"en":"the target value of the metric (as a quantity)", "zh_CN":"value 是指标的目标值（以数量形式给出）"}
        self.value = value
        # {"en":"the target value of the average of the metric across all relevant pods (as a quantity)", "zh_CN":"averageValue 是跨所有 Pod 得出的指标均值的目标值（以数量形式给出）"}
        self.average_value = average_value
        # {"en":"the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type", "zh_CN":"averageUtilization 是跨所有相关 Pod 得出的资源指标均值的目标值， 表示为 Pod 资源请求值的百分比。目前仅对 “Resource” 指标源类别有效"}
        self.average_utilization = average_utilization

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.average_value is not None:
            result['averageValue'] = self.average_value
        if self.average_utilization is not None:
            result['averageUtilization'] = self.average_utilization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('averageValue') is not None:
            self.average_value = m.get('averageValue')
        if m.get('averageUtilization') is not None:
            self.average_utilization = m.get('averageUtilization')
        return self


class UpdateHorizontalPodAutoscalerLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"the label key that the selector applies to", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist", "zh_CN":"表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdateHorizontalPodAutoscalerLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[UpdateHorizontalPodAutoscalerLabelSelectorRequirement] = None,
    ):
        # {"en":"a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is 'key', the operator is 'In', and the values array contains only 'value'. The requirements are ANDed", "zh_CN":"matchLabels 是 {key,value} 键值对的映射。matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。所表达的需求最终要按逻辑与的关系组合"}
        self.match_labels = match_labels
        # {"en":"a list of label selector requirements. The requirements are ANDed", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = UpdateHorizontalPodAutoscalerLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class UpdateHorizontalPodAutoscalerMetricIdentifier(TeaModel):
    def __init__(
        self,
        name: str = None,
        selector: UpdateHorizontalPodAutoscalerLabelSelector = None,
    ):
        # {"en":"the name of the given metric", "zh_CN":"给定指标的名称"}
        self.name = name
        # {"en":"the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics", "zh_CN":"给定指标的标准 Kubernetes 标签选择算符的字符串编码形式。 设置后，它作为附加参数传递给指标服务器，以获取更具体的指标范围。 未设置时，仅 metricName 参数将用于收集指标"}
        self.selector = selector

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.selector:
            self.selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('selector') is not None:
            temp_model = UpdateHorizontalPodAutoscalerLabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        return self


class UpdateHorizontalPodAutoscalerObjectMetricSource(TeaModel):
    def __init__(
        self,
        described_object: UpdateHorizontalPodAutoscalerCrossVersionObjectReference = None,
        target: UpdateHorizontalPodAutoscalerMetricTarget = None,
        metric: UpdateHorizontalPodAutoscalerMetricIdentifier = None,
    ):
        # {"en":"describedObject specifies the descriptions of a object,such as kind,name apiVersion", "zh_CN":"describeObject 表示对象的描述，如对象的 kind、name、apiVersion"}
        self.described_object = described_object
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric

    def validate(self):
        self.validate_required(self.described_object, 'described_object')
        if self.described_object:
            self.described_object.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.described_object is not None:
            result['describedObject'] = self.described_object.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('describedObject') is not None:
            temp_model = UpdateHorizontalPodAutoscalerCrossVersionObjectReference()
            self.described_object = temp_model.from_map(m['describedObject'])
        if m.get('target') is not None:
            temp_model = UpdateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('metric') is not None:
            temp_model = UpdateHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        return self


class UpdateHorizontalPodAutoscalerPodsMetricSource(TeaModel):
    def __init__(
        self,
        metric: UpdateHorizontalPodAutoscalerMetricIdentifier = None,
        target: UpdateHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = UpdateHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = UpdateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class UpdateHorizontalPodAutoscalerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: UpdateHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = UpdateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class UpdateHorizontalPodAutoscalerContainerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: UpdateHorizontalPodAutoscalerMetricTarget = None,
        container: str = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target
        # {"en":"the name of the container in the pods of the scaling target", "zh_CN":"扩缩目标的 Pod 中容器的名称"}
        self.container = container

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.container, 'container')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.container is not None:
            result['container'] = self.container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = UpdateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('container') is not None:
            self.container = m.get('container')
        return self


class UpdateHorizontalPodAutoscalerExternalMetricSource(TeaModel):
    def __init__(
        self,
        metric: UpdateHorizontalPodAutoscalerMetricIdentifier = None,
        target: UpdateHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = UpdateHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = UpdateHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class UpdateHorizontalPodAutoscalerMetricSpec(TeaModel):
    def __init__(
        self,
        type: str = None,
        object: UpdateHorizontalPodAutoscalerObjectMetricSource = None,
        pods: UpdateHorizontalPodAutoscalerPodsMetricSource = None,
        resource: UpdateHorizontalPodAutoscalerResourceMetricSource = None,
        container_resource: UpdateHorizontalPodAutoscalerContainerResourceMetricSource = None,
        external: UpdateHorizontalPodAutoscalerExternalMetricSource = None,
    ):
        # {"en":"the type of metric source. It should be one of 'ContainerResource', 'External', 'Object', 'Pods' or 'Resource', each mapping to a matching field in the object. Note: 'ContainerResource' type is available on when the feature-gate HPAContainerMetrics is enabled", "zh_CN":"type 是指标源的类别。它取值是 “ContainerResource”、“External”、“Object”、“Pods” 或 “Resource” 之一， 每个类别映射到对象中的一个对应的字段。注意：“ContainerResource” 类别在特性门控 HPAContainerMetrics 启用时可用"}
        self.type = type
        # {"en":"refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object)", "zh_CN":"指描述单个 Kubernetes 对象的指标"}
        self.object = object
        # {"en":"refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value", "zh_CN":"指描述当前扩缩目标中每个 Pod 的指标（例如，transactions-processed-per-second）。 在与目标值进行比较之前，这些指标值将被平均"}
        self.pods = pods
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 此结构描述当前扩缩目标中的每个 Pod（例如 CPU 或内存）。此类指标内置于 Kubernetes 中， 并且在使用 “Pods” 源的、按 Pod 统计的普通指标之外支持一些特殊的扩缩选项"}
        self.resource = resource
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 描述当前扩缩目标中每个 Pod 中的单个容器（例如 CPU 或内存）。 此类指标内置于 Kubernetes 中，在使用 “pods” 源的、按 Pod 计算的普通指标之外，还具有一些特殊的扩缩选项。 这是一个 Alpha 特性，可以通过 HPAContainerMetrics 特性标志启用"}
        self.container_resource = container_resource
        # {"en":"refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)", "zh_CN":"指的是不与任何 Kubernetes 对象关联的全局指标。 这一字段允许基于来自集群外部运行的组件（例如云消息服务中的队列长度，或来自运行在集群外部的负载均衡器的 QPS）的信息进行自动扩缩容"}
        self.external = external

    def validate(self):
        self.validate_required(self.type, 'type')
        if self.object:
            self.object.validate()
        if self.pods:
            self.pods.validate()
        if self.resource:
            self.resource.validate()
        if self.container_resource:
            self.container_resource.validate()
        if self.external:
            self.external.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.object is not None:
            result['object'] = self.object.to_map()
        if self.pods is not None:
            result['pods'] = self.pods.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.container_resource is not None:
            result['containerResource'] = self.container_resource.to_map()
        if self.external is not None:
            result['external'] = self.external.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('object') is not None:
            temp_model = UpdateHorizontalPodAutoscalerObjectMetricSource()
            self.object = temp_model.from_map(m['object'])
        if m.get('pods') is not None:
            temp_model = UpdateHorizontalPodAutoscalerPodsMetricSource()
            self.pods = temp_model.from_map(m['pods'])
        if m.get('resource') is not None:
            temp_model = UpdateHorizontalPodAutoscalerResourceMetricSource()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('containerResource') is not None:
            temp_model = UpdateHorizontalPodAutoscalerContainerResourceMetricSource()
            self.container_resource = temp_model.from_map(m['containerResource'])
        if m.get('external') is not None:
            temp_model = UpdateHorizontalPodAutoscalerExternalMetricSource()
            self.external = temp_model.from_map(m['external'])
        return self


class UpdateHorizontalPodAutoscalerHPAScalingPolicy(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
        period_seconds: int = None,
    ):
        # {"en":"type is used to specify the scaling policy", "zh_CN":"type 用于指定扩缩策略"}
        self.type = type
        # {"en":"value contains the amount of change which is permitted by the policy. It must be greater than zero", "zh_CN":"value 包含策略允许的更改量。它必须大于零"}
        self.value = value
        # {"en":"periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min)", "zh_CN":"periodSeconds 表示策略应该保持为 true 的时间窗口长度。 periodSeconds 必须大于零且小于或等于 1800（30 分钟）"}
        self.period_seconds = period_seconds

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.period_seconds, 'period_seconds')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        return self


class UpdateHorizontalPodAutoscalerHPAScalingRules(TeaModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
        select_policy: str = None,
        policies: List[UpdateHorizontalPodAutoscalerHPAScalingPolicy] = None,
    ):
        # {"en":"stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long)", "zh_CN":"stabilizationWindowSeconds 是在扩缩容时应考虑的之前建议的秒数。stabilizationWindowSeconds 必须大于或等于零且小于或等于 3600（一小时）。如果未设置，则使用默认值：扩容：0（不设置稳定窗口）。缩容：300（即稳定窗口为 300 秒）"}
        self.stabilization_window_seconds = stabilization_window_seconds
        # {"en":"selectPolicy is used to specify which policy should be used. If not set, the default value Max is used", "zh_CN":"selectPolicy 用于指定应该使用哪个策略。如果未设置，则使用默认值 Max"}
        self.select_policy = select_policy
        # {"en":"policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the UpdateHorizontalPodAutoscalerHPAScalingRules will be discarded as invalid", "zh_CN":"policies 是可在扩缩容过程中使用的潜在扩缩策略的列表。必须至少指定一个策略，否则 UpdateHorizontalPodAutoscalerHPAScalingRules 将被视为无效而丢弃"}
        self.policies = policies

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.select_policy is not None:
            result['selectPolicy'] = self.select_policy
        if self.policies is not None:
            result['policies'] = []
            for k in self.policies:
                result['policies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')
        if m.get('selectPolicy') is not None:
            self.select_policy = m.get('selectPolicy')
        if m.get('policies') is not None:
            self.policies = []
            for k in m.get('policies'):
                temp_model = UpdateHorizontalPodAutoscalerHPAScalingPolicy()
                self.policies.append(temp_model.from_map(k))
        return self


class UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior(TeaModel):
    def __init__(
        self,
        scale_up: UpdateHorizontalPodAutoscalerHPAScalingRules = None,
        scale_down: UpdateHorizontalPodAutoscalerHPAScalingRules = None,
    ):
        # {"en":"scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:- increase no more than 4 pods per 60 seconds- double the number of pods per 60 seconds No stabilization is used", "zh_CN":"scaleUp 是用于扩容的扩缩策略。如果未设置，则默认值为以下值中的较高者：- 每 60 秒增加不超过 4 个 Pod- 每 60 秒 Pod 数量翻倍。不使用稳定窗口"}
        self.scale_up = scale_up
        # {"en":"scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used)", "zh_CN":"scaleDown 是缩容策略。如果未设置，则默认值允许缩减到 minReplicas 数量的 Pod， 具有 300 秒的稳定窗口（使用最近 300 秒的最高推荐值）"}
        self.scale_down = scale_down

    def validate(self):
        if self.scale_up:
            self.scale_up.validate()
        if self.scale_down:
            self.scale_down.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_up is not None:
            result['scaleUp'] = self.scale_up.to_map()
        if self.scale_down is not None:
            result['scaleDown'] = self.scale_down.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleUp') is not None:
            temp_model = UpdateHorizontalPodAutoscalerHPAScalingRules()
            self.scale_up = temp_model.from_map(m['scaleUp'])
        if m.get('scaleDown') is not None:
            temp_model = UpdateHorizontalPodAutoscalerHPAScalingRules()
            self.scale_down = temp_model.from_map(m['scaleDown'])
        return self


class UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec(TeaModel):
    def __init__(
        self,
        scale_target_ref: UpdateHorizontalPodAutoscalerCrossVersionObjectReference = None,
        min_replicas: int = None,
        max_replicas: int = None,
        metrics: List[UpdateHorizontalPodAutoscalerMetricSpec] = None,
        behavior: UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior = None,
    ):
        # {"en":"reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource", "zh_CN":"对被扩缩资源的引用； 水平 Pod 自动缩放器将了解当前的资源消耗，并使用其 scale 子资源设置所需的 Pod 数量"}
        self.scale_target_ref = scale_target_ref
        # {"en":"the lower limit for the number of replicas to which the autoscaler can scale down. It defaults to 1 pod. minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured. Scaling is active as long as at least one metric value is available", "zh_CN":"自动缩放器可以缩减的副本数的下限。 它默认为 1 个 Pod。 如果启用了 alpha 特性门禁 HPAScaleToZero 并且配置了至少一个 Object 或 External 度量标准， 则 minReplicas 允许为 0。 只要至少有一个度量值可用，缩放就处于活动状态"}
        self.min_replicas = min_replicas
        # {"en":"the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas", "zh_CN":"自动扩缩器可以设置的 Pod 数量上限； 不能小于 minReplicas"}
        self.max_replicas = max_replicas
        # {"en":"metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used). The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa. See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization", "zh_CN":"metrics 包含用于计算预期副本数的规约（将使用所有指标的最大副本数）。 预期副本数是通过将目标值与当前值之间的比率乘以当前 Pod 数来计算的。 因此，使用的指标必须随着 Pod 数量的增加而减少，反之亦然。 有关每种类别的指标必须如何响应的更多信息，请参阅各个指标源类别。 如果未设置，默认指标将设置为 80% 的平均 CPU 利用率"}
        self.metrics = metrics
        # {"en":"behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default UpdateHorizontalPodAutoscalerHPAScalingRules for scale up and scale down are used", "zh_CN":"behavior 配置目标在扩容（Up）和缩容（Down）两个方向的扩缩行为（分别用 scaleUp 和 scaleDown 字段）。 如果未设置，则会使用默认的 UpdateHorizontalPodAutoscalerHPAScalingRules 进行扩缩容"}
        self.behavior = behavior

    def validate(self):
        self.validate_required(self.scale_target_ref, 'scale_target_ref')
        if self.scale_target_ref:
            self.scale_target_ref.validate()
        self.validate_required(self.max_replicas, 'max_replicas')
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.behavior:
            self.behavior.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_target_ref is not None:
            result['scaleTargetRef'] = self.scale_target_ref.to_map()
        if self.min_replicas is not None:
            result['minReplicas'] = self.min_replicas
        if self.max_replicas is not None:
            result['maxReplicas'] = self.max_replicas
        if self.metrics is not None:
            result['metrics'] = []
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.behavior is not None:
            result['behavior'] = self.behavior.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleTargetRef') is not None:
            temp_model = UpdateHorizontalPodAutoscalerCrossVersionObjectReference()
            self.scale_target_ref = temp_model.from_map(m['scaleTargetRef'])
        if m.get('minReplicas') is not None:
            self.min_replicas = m.get('minReplicas')
        if m.get('maxReplicas') is not None:
            self.max_replicas = m.get('maxReplicas')
        if m.get('metrics') is not None:
            self.metrics = []
            for k in m.get('metrics'):
                temp_model = UpdateHorizontalPodAutoscalerMetricSpec()
                self.metrics.append(temp_model.from_map(k))
        if m.get('behavior') is not None:
            temp_model = UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior()
            self.behavior = temp_model.from_map(m['behavior'])
        return self


class UpdateHorizontalPodAutoscalerRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateHorizontalPodAutoscalerObjectMeta = None,
        spec: UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"spec defines the behaviour of autoscaler.", "zh_CN":"spec 定义自动缩放器的规约"}
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
            temp_model = UpdateHorizontalPodAutoscalerObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerStatus(TeaModel):
    def __init__(
        self,
        observed_generation: int = None,
        current_replicas: int = None,
        desired_replicas: int = None,
    ):
        # {"en":"the most recent generation observed by this autoscaler", "zh_CN":"observedGeneration 是此自动缩放器观察到的最新一代"}
        self.observed_generation = observed_generation
        # {"en":"the current number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 的当前副本数"}
        self.current_replicas = current_replicas
        # {"en":"the desired number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 副本的所需数量"}
        self.desired_replicas = desired_replicas

    def validate(self):
        self.validate_required(self.current_replicas, 'current_replicas')
        self.validate_required(self.desired_replicas, 'desired_replicas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.current_replicas is not None:
            result['currentReplicas'] = self.current_replicas
        if self.desired_replicas is not None:
            result['desiredReplicas'] = self.desired_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('currentReplicas') is not None:
            self.current_replicas = m.get('currentReplicas')
        if m.get('desiredReplicas') is not None:
            self.desired_replicas = m.get('desiredReplicas')
        return self


class UpdateHorizontalPodAutoscalerHorizontalPodAutoscaler(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdateHorizontalPodAutoscalerObjectMeta = None,
        spec: UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec = None,
        status: UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"spec defines the behaviour of autoscaler.", "zh_CN":"spec 定义自动缩放器的规约"}
        self.spec = spec
        # {"en":"the current information about the autoscaler", "zh_CN":"自动缩放器的当前信息"}
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
            temp_model = UpdateHorizontalPodAutoscalerObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = UpdateHorizontalPodAutoscalerHorizontalPodAutoscalerStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class UpdateHorizontalPodAutoscalerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdateHorizontalPodAutoscalerHorizontalPodAutoscaler = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"UpdateHorizontalPodAutoscalerHorizontalPodAutoscaler", "zh_CN":"UpdateHorizontalPodAutoscalerHorizontalPodAutoscaler"}
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
            temp_model = UpdateHorizontalPodAutoscalerHorizontalPodAutoscaler()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdateHorizontalPodAutoscalerPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"资源name", "zh_CN":"资源名称"}
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


class UpdateHorizontalPodAutoscalerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateHorizontalPodAutoscalerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateHorizontalPodAutoscalerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetHorizontalPodAutoscalerRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHorizontalPodAutoscalerOwnerReference(TeaModel):
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


class GetHorizontalPodAutoscalerFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHorizontalPodAutoscalerManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: GetHorizontalPodAutoscalerFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this GetHorizontalPodAutoscalerManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'GetHorizontalPodAutoscalerFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“GetHorizontalPodAutoscalerFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"GetHorizontalPodAutoscalerFieldsV1 holds the first JSON version format as described in the 'GetHorizontalPodAutoscalerFieldsV1' type", "zh_CN":"GetHorizontalPodAutoscalerFieldsV1 包含类型 “GetHorizontalPodAutoscalerFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = GetHorizontalPodAutoscalerFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class GetHorizontalPodAutoscalerObjectMeta(TeaModel):
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
        owner_references: List[GetHorizontalPodAutoscalerOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[GetHorizontalPodAutoscalerManagedFieldsEntry] = None,
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
                temp_model = GetHorizontalPodAutoscalerOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = GetHorizontalPodAutoscalerManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class GetHorizontalPodAutoscalerCrossVersionObjectReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the API version of the referent", "zh_CN":"被引用对象的 API 版本"}
        self.api_version = api_version
        # {"en":"the kind of the referent", "zh_CN":"被引用对象的类别"}
        self.kind = kind
        # {"en":"the name of the referent", "zh_CN":"被引用对象的名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.name, 'name')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetHorizontalPodAutoscalerMetricTarget(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        average_value: str = None,
        average_utilization: int = None,
    ):
        # {"en":"type represents whether the metric type is Utilization, Value, or AverageValue", "zh_CN":"type 表示指标类别是 Utilization、Value 或 AverageValue"}
        self.type = type
        # {"en":"the target value of the metric (as a quantity)", "zh_CN":"value 是指标的目标值（以数量形式给出）"}
        self.value = value
        # {"en":"the target value of the average of the metric across all relevant pods (as a quantity)", "zh_CN":"averageValue 是跨所有 Pod 得出的指标均值的目标值（以数量形式给出）"}
        self.average_value = average_value
        # {"en":"the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type", "zh_CN":"averageUtilization 是跨所有相关 Pod 得出的资源指标均值的目标值， 表示为 Pod 资源请求值的百分比。目前仅对 “Resource” 指标源类别有效"}
        self.average_utilization = average_utilization

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.average_value is not None:
            result['averageValue'] = self.average_value
        if self.average_utilization is not None:
            result['averageUtilization'] = self.average_utilization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('averageValue') is not None:
            self.average_value = m.get('averageValue')
        if m.get('averageUtilization') is not None:
            self.average_utilization = m.get('averageUtilization')
        return self


class GetHorizontalPodAutoscalerLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"the label key that the selector applies to", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist", "zh_CN":"表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetHorizontalPodAutoscalerLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[GetHorizontalPodAutoscalerLabelSelectorRequirement] = None,
    ):
        # {"en":"a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is 'key', the operator is 'In', and the values array contains only 'value'. The requirements are ANDed", "zh_CN":"matchLabels 是 {key,value} 键值对的映射。matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。所表达的需求最终要按逻辑与的关系组合"}
        self.match_labels = match_labels
        # {"en":"a list of label selector requirements. The requirements are ANDed", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = GetHorizontalPodAutoscalerLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class GetHorizontalPodAutoscalerMetricIdentifier(TeaModel):
    def __init__(
        self,
        name: str = None,
        selector: GetHorizontalPodAutoscalerLabelSelector = None,
    ):
        # {"en":"the name of the given metric", "zh_CN":"给定指标的名称"}
        self.name = name
        # {"en":"the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics", "zh_CN":"给定指标的标准 Kubernetes 标签选择算符的字符串编码形式。 设置后，它作为附加参数传递给指标服务器，以获取更具体的指标范围。 未设置时，仅 metricName 参数将用于收集指标"}
        self.selector = selector

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.selector:
            self.selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('selector') is not None:
            temp_model = GetHorizontalPodAutoscalerLabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        return self


class GetHorizontalPodAutoscalerObjectMetricSource(TeaModel):
    def __init__(
        self,
        described_object: GetHorizontalPodAutoscalerCrossVersionObjectReference = None,
        target: GetHorizontalPodAutoscalerMetricTarget = None,
        metric: GetHorizontalPodAutoscalerMetricIdentifier = None,
    ):
        # {"en":"describedObject specifies the descriptions of a object,such as kind,name apiVersion", "zh_CN":"describeObject 表示对象的描述，如对象的 kind、name、apiVersion"}
        self.described_object = described_object
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric

    def validate(self):
        self.validate_required(self.described_object, 'described_object')
        if self.described_object:
            self.described_object.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.described_object is not None:
            result['describedObject'] = self.described_object.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('describedObject') is not None:
            temp_model = GetHorizontalPodAutoscalerCrossVersionObjectReference()
            self.described_object = temp_model.from_map(m['describedObject'])
        if m.get('target') is not None:
            temp_model = GetHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('metric') is not None:
            temp_model = GetHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        return self


class GetHorizontalPodAutoscalerPodsMetricSource(TeaModel):
    def __init__(
        self,
        metric: GetHorizontalPodAutoscalerMetricIdentifier = None,
        target: GetHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = GetHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = GetHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class GetHorizontalPodAutoscalerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: GetHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = GetHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class GetHorizontalPodAutoscalerContainerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: GetHorizontalPodAutoscalerMetricTarget = None,
        container: str = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target
        # {"en":"the name of the container in the pods of the scaling target", "zh_CN":"扩缩目标的 Pod 中容器的名称"}
        self.container = container

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.container, 'container')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.container is not None:
            result['container'] = self.container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = GetHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('container') is not None:
            self.container = m.get('container')
        return self


class GetHorizontalPodAutoscalerExternalMetricSource(TeaModel):
    def __init__(
        self,
        metric: GetHorizontalPodAutoscalerMetricIdentifier = None,
        target: GetHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = GetHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = GetHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class GetHorizontalPodAutoscalerMetricSpec(TeaModel):
    def __init__(
        self,
        type: str = None,
        object: GetHorizontalPodAutoscalerObjectMetricSource = None,
        pods: GetHorizontalPodAutoscalerPodsMetricSource = None,
        resource: GetHorizontalPodAutoscalerResourceMetricSource = None,
        container_resource: GetHorizontalPodAutoscalerContainerResourceMetricSource = None,
        external: GetHorizontalPodAutoscalerExternalMetricSource = None,
    ):
        # {"en":"the type of metric source. It should be one of 'ContainerResource', 'External', 'Object', 'Pods' or 'Resource', each mapping to a matching field in the object. Note: 'ContainerResource' type is available on when the feature-gate HPAContainerMetrics is enabled", "zh_CN":"type 是指标源的类别。它取值是 “ContainerResource”、“External”、“Object”、“Pods” 或 “Resource” 之一， 每个类别映射到对象中的一个对应的字段。注意：“ContainerResource” 类别在特性门控 HPAContainerMetrics 启用时可用"}
        self.type = type
        # {"en":"refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object)", "zh_CN":"指描述单个 Kubernetes 对象的指标"}
        self.object = object
        # {"en":"refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value", "zh_CN":"指描述当前扩缩目标中每个 Pod 的指标（例如，transactions-processed-per-second）。 在与目标值进行比较之前，这些指标值将被平均"}
        self.pods = pods
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 此结构描述当前扩缩目标中的每个 Pod（例如 CPU 或内存）。此类指标内置于 Kubernetes 中， 并且在使用 “Pods” 源的、按 Pod 统计的普通指标之外支持一些特殊的扩缩选项"}
        self.resource = resource
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 描述当前扩缩目标中每个 Pod 中的单个容器（例如 CPU 或内存）。 此类指标内置于 Kubernetes 中，在使用 “pods” 源的、按 Pod 计算的普通指标之外，还具有一些特殊的扩缩选项。 这是一个 Alpha 特性，可以通过 HPAContainerMetrics 特性标志启用"}
        self.container_resource = container_resource
        # {"en":"refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)", "zh_CN":"指的是不与任何 Kubernetes 对象关联的全局指标。 这一字段允许基于来自集群外部运行的组件（例如云消息服务中的队列长度，或来自运行在集群外部的负载均衡器的 QPS）的信息进行自动扩缩容"}
        self.external = external

    def validate(self):
        self.validate_required(self.type, 'type')
        if self.object:
            self.object.validate()
        if self.pods:
            self.pods.validate()
        if self.resource:
            self.resource.validate()
        if self.container_resource:
            self.container_resource.validate()
        if self.external:
            self.external.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.object is not None:
            result['object'] = self.object.to_map()
        if self.pods is not None:
            result['pods'] = self.pods.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.container_resource is not None:
            result['containerResource'] = self.container_resource.to_map()
        if self.external is not None:
            result['external'] = self.external.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('object') is not None:
            temp_model = GetHorizontalPodAutoscalerObjectMetricSource()
            self.object = temp_model.from_map(m['object'])
        if m.get('pods') is not None:
            temp_model = GetHorizontalPodAutoscalerPodsMetricSource()
            self.pods = temp_model.from_map(m['pods'])
        if m.get('resource') is not None:
            temp_model = GetHorizontalPodAutoscalerResourceMetricSource()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('containerResource') is not None:
            temp_model = GetHorizontalPodAutoscalerContainerResourceMetricSource()
            self.container_resource = temp_model.from_map(m['containerResource'])
        if m.get('external') is not None:
            temp_model = GetHorizontalPodAutoscalerExternalMetricSource()
            self.external = temp_model.from_map(m['external'])
        return self


class GetHorizontalPodAutoscalerHPAScalingPolicy(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
        period_seconds: int = None,
    ):
        # {"en":"type is used to specify the scaling policy", "zh_CN":"type 用于指定扩缩策略"}
        self.type = type
        # {"en":"value contains the amount of change which is permitted by the policy. It must be greater than zero", "zh_CN":"value 包含策略允许的更改量。它必须大于零"}
        self.value = value
        # {"en":"periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min)", "zh_CN":"periodSeconds 表示策略应该保持为 true 的时间窗口长度。 periodSeconds 必须大于零且小于或等于 1800（30 分钟）"}
        self.period_seconds = period_seconds

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.period_seconds, 'period_seconds')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        return self


class GetHorizontalPodAutoscalerHPAScalingRules(TeaModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
        select_policy: str = None,
        policies: List[GetHorizontalPodAutoscalerHPAScalingPolicy] = None,
    ):
        # {"en":"stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long)", "zh_CN":"stabilizationWindowSeconds 是在扩缩容时应考虑的之前建议的秒数。stabilizationWindowSeconds 必须大于或等于零且小于或等于 3600（一小时）。如果未设置，则使用默认值：扩容：0（不设置稳定窗口）。缩容：300（即稳定窗口为 300 秒）"}
        self.stabilization_window_seconds = stabilization_window_seconds
        # {"en":"selectPolicy is used to specify which policy should be used. If not set, the default value Max is used", "zh_CN":"selectPolicy 用于指定应该使用哪个策略。如果未设置，则使用默认值 Max"}
        self.select_policy = select_policy
        # {"en":"policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the GetHorizontalPodAutoscalerHPAScalingRules will be discarded as invalid", "zh_CN":"policies 是可在扩缩容过程中使用的潜在扩缩策略的列表。必须至少指定一个策略，否则 GetHorizontalPodAutoscalerHPAScalingRules 将被视为无效而丢弃"}
        self.policies = policies

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.select_policy is not None:
            result['selectPolicy'] = self.select_policy
        if self.policies is not None:
            result['policies'] = []
            for k in self.policies:
                result['policies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')
        if m.get('selectPolicy') is not None:
            self.select_policy = m.get('selectPolicy')
        if m.get('policies') is not None:
            self.policies = []
            for k in m.get('policies'):
                temp_model = GetHorizontalPodAutoscalerHPAScalingPolicy()
                self.policies.append(temp_model.from_map(k))
        return self


class GetHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior(TeaModel):
    def __init__(
        self,
        scale_up: GetHorizontalPodAutoscalerHPAScalingRules = None,
        scale_down: GetHorizontalPodAutoscalerHPAScalingRules = None,
    ):
        # {"en":"scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:- increase no more than 4 pods per 60 seconds- double the number of pods per 60 seconds No stabilization is used", "zh_CN":"scaleUp 是用于扩容的扩缩策略。如果未设置，则默认值为以下值中的较高者：- 每 60 秒增加不超过 4 个 Pod- 每 60 秒 Pod 数量翻倍。不使用稳定窗口"}
        self.scale_up = scale_up
        # {"en":"scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used)", "zh_CN":"scaleDown 是缩容策略。如果未设置，则默认值允许缩减到 minReplicas 数量的 Pod， 具有 300 秒的稳定窗口（使用最近 300 秒的最高推荐值）"}
        self.scale_down = scale_down

    def validate(self):
        if self.scale_up:
            self.scale_up.validate()
        if self.scale_down:
            self.scale_down.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_up is not None:
            result['scaleUp'] = self.scale_up.to_map()
        if self.scale_down is not None:
            result['scaleDown'] = self.scale_down.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleUp') is not None:
            temp_model = GetHorizontalPodAutoscalerHPAScalingRules()
            self.scale_up = temp_model.from_map(m['scaleUp'])
        if m.get('scaleDown') is not None:
            temp_model = GetHorizontalPodAutoscalerHPAScalingRules()
            self.scale_down = temp_model.from_map(m['scaleDown'])
        return self


class GetHorizontalPodAutoscalerHorizontalPodAutoscalerSpec(TeaModel):
    def __init__(
        self,
        scale_target_ref: GetHorizontalPodAutoscalerCrossVersionObjectReference = None,
        min_replicas: int = None,
        max_replicas: int = None,
        metrics: List[GetHorizontalPodAutoscalerMetricSpec] = None,
        behavior: GetHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior = None,
    ):
        # {"en":"reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource", "zh_CN":"对被扩缩资源的引用； 水平 Pod 自动缩放器将了解当前的资源消耗，并使用其 scale 子资源设置所需的 Pod 数量"}
        self.scale_target_ref = scale_target_ref
        # {"en":"the lower limit for the number of replicas to which the autoscaler can scale down. It defaults to 1 pod. minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured. Scaling is active as long as at least one metric value is available", "zh_CN":"自动缩放器可以缩减的副本数的下限。 它默认为 1 个 Pod。 如果启用了 alpha 特性门禁 HPAScaleToZero 并且配置了至少一个 Object 或 External 度量标准， 则 minReplicas 允许为 0。 只要至少有一个度量值可用，缩放就处于活动状态"}
        self.min_replicas = min_replicas
        # {"en":"the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas", "zh_CN":"自动扩缩器可以设置的 Pod 数量上限； 不能小于 minReplicas"}
        self.max_replicas = max_replicas
        # {"en":"metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used). The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa. See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization", "zh_CN":"metrics 包含用于计算预期副本数的规约（将使用所有指标的最大副本数）。 预期副本数是通过将目标值与当前值之间的比率乘以当前 Pod 数来计算的。 因此，使用的指标必须随着 Pod 数量的增加而减少，反之亦然。 有关每种类别的指标必须如何响应的更多信息，请参阅各个指标源类别。 如果未设置，默认指标将设置为 80% 的平均 CPU 利用率"}
        self.metrics = metrics
        # {"en":"behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default GetHorizontalPodAutoscalerHPAScalingRules for scale up and scale down are used", "zh_CN":"behavior 配置目标在扩容（Up）和缩容（Down）两个方向的扩缩行为（分别用 scaleUp 和 scaleDown 字段）。 如果未设置，则会使用默认的 GetHorizontalPodAutoscalerHPAScalingRules 进行扩缩容"}
        self.behavior = behavior

    def validate(self):
        self.validate_required(self.scale_target_ref, 'scale_target_ref')
        if self.scale_target_ref:
            self.scale_target_ref.validate()
        self.validate_required(self.max_replicas, 'max_replicas')
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.behavior:
            self.behavior.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_target_ref is not None:
            result['scaleTargetRef'] = self.scale_target_ref.to_map()
        if self.min_replicas is not None:
            result['minReplicas'] = self.min_replicas
        if self.max_replicas is not None:
            result['maxReplicas'] = self.max_replicas
        if self.metrics is not None:
            result['metrics'] = []
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.behavior is not None:
            result['behavior'] = self.behavior.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleTargetRef') is not None:
            temp_model = GetHorizontalPodAutoscalerCrossVersionObjectReference()
            self.scale_target_ref = temp_model.from_map(m['scaleTargetRef'])
        if m.get('minReplicas') is not None:
            self.min_replicas = m.get('minReplicas')
        if m.get('maxReplicas') is not None:
            self.max_replicas = m.get('maxReplicas')
        if m.get('metrics') is not None:
            self.metrics = []
            for k in m.get('metrics'):
                temp_model = GetHorizontalPodAutoscalerMetricSpec()
                self.metrics.append(temp_model.from_map(k))
        if m.get('behavior') is not None:
            temp_model = GetHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior()
            self.behavior = temp_model.from_map(m['behavior'])
        return self


class GetHorizontalPodAutoscalerHorizontalPodAutoscalerStatus(TeaModel):
    def __init__(
        self,
        observed_generation: int = None,
        current_replicas: int = None,
        desired_replicas: int = None,
    ):
        # {"en":"the most recent generation observed by this autoscaler", "zh_CN":"observedGeneration 是此自动缩放器观察到的最新一代"}
        self.observed_generation = observed_generation
        # {"en":"the current number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 的当前副本数"}
        self.current_replicas = current_replicas
        # {"en":"the desired number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 副本的所需数量"}
        self.desired_replicas = desired_replicas

    def validate(self):
        self.validate_required(self.current_replicas, 'current_replicas')
        self.validate_required(self.desired_replicas, 'desired_replicas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.current_replicas is not None:
            result['currentReplicas'] = self.current_replicas
        if self.desired_replicas is not None:
            result['desiredReplicas'] = self.desired_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('currentReplicas') is not None:
            self.current_replicas = m.get('currentReplicas')
        if m.get('desiredReplicas') is not None:
            self.desired_replicas = m.get('desiredReplicas')
        return self


class GetHorizontalPodAutoscalerHorizontalPodAutoscaler(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: GetHorizontalPodAutoscalerObjectMeta = None,
        spec: GetHorizontalPodAutoscalerHorizontalPodAutoscalerSpec = None,
        status: GetHorizontalPodAutoscalerHorizontalPodAutoscalerStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"spec defines the behaviour of autoscaler.", "zh_CN":"spec 定义自动缩放器的规约"}
        self.spec = spec
        # {"en":"the current information about the autoscaler", "zh_CN":"自动缩放器的当前信息"}
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
            temp_model = GetHorizontalPodAutoscalerObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = GetHorizontalPodAutoscalerHorizontalPodAutoscalerSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = GetHorizontalPodAutoscalerHorizontalPodAutoscalerStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class GetHorizontalPodAutoscalerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetHorizontalPodAutoscalerHorizontalPodAutoscaler = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"GetHorizontalPodAutoscalerHorizontalPodAutoscaler", "zh_CN":"GetHorizontalPodAutoscalerHorizontalPodAutoscaler"}
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
            temp_model = GetHorizontalPodAutoscalerHorizontalPodAutoscaler()
            self.data = temp_model.from_map(m['data'])
        return self


class GetHorizontalPodAutoscalerPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"hpa name", "zh_CN":"hpa名称"}
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


class GetHorizontalPodAutoscalerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHorizontalPodAutoscalerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetHorizontalPodAutoscalerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetPropagationPoliciesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPropagationPoliciesOwnerReference(TeaModel):
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


class GetPropagationPoliciesFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPropagationPoliciesManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: GetPropagationPoliciesFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this GetPropagationPoliciesManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'GetPropagationPoliciesFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“GetPropagationPoliciesFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"GetPropagationPoliciesFieldsV1 holds the first JSON version format as described in the 'GetPropagationPoliciesFieldsV1' type", "zh_CN":"GetPropagationPoliciesFieldsV1 包含类型 “GetPropagationPoliciesFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = GetPropagationPoliciesFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class GetPropagationPoliciesObjectMeta(TeaModel):
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
        owner_references: List[GetPropagationPoliciesOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[GetPropagationPoliciesManagedFieldsEntry] = None,
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
                temp_model = GetPropagationPoliciesOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = GetPropagationPoliciesManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class GetPropagationPoliciesLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetPropagationPoliciesMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[GetPropagationPoliciesLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = GetPropagationPoliciesLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class GetPropagationPoliciesResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        namespace: str = None,
        name: str = None,
        label_selector: GetPropagationPoliciesMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = GetPropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class GetPropagationPoliciesCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetPropagationPoliciesFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[GetPropagationPoliciesCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = GetPropagationPoliciesCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class GetPropagationPoliciesClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: GetPropagationPoliciesMetaV1LabelSelector = None,
        field_selector: GetPropagationPoliciesFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = GetPropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = GetPropagationPoliciesFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class GetPropagationPoliciesToleration(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
        effect: str = None,
        toleration_seconds: int = None,
    ):
        # {"en":"The taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.", "zh_CN":"容忍度所适用的污点的键名。此字段为空意味着匹配所有的污点键。 如果 key 为空，则 operator 必须为 Exists；这种组合意味着匹配所有值和所有键。"}
        self.key = key
        # {"en":"Represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.", "zh_CN":"表示 key 与 value 之间的关系。有效的 operator 取值是 Exists 和 Equal。默认为 Equal。 Exists 相当于 value 为某种通配符，因此 Pod 可以容忍特定类别的所有污点。"}
        self.operator = operator
        # {"en":"The taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.", "zh_CN":"容忍度所匹配的污点值。如果 operator 为 Exists，则此 value 值应该为空， 否则 value 值应该是一个正常的字符串。"}
        self.value = value
        # {"en":"Indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.", "zh_CN":"指示要匹配的污点效果。空值意味著匹配所有污点效果。如果要设置此字段，允许的值为 NoSchedule、PreferNoSchedule 和 NoExecute 之一。"}
        self.effect = effect
        # {"en":"Represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.", "zh_CN":" 表示容忍度（effect 必须是 NoExecute，否则此字段被忽略）容忍污点的时间长度。 默认情况下，此字段未被设置，这意味着会一直能够容忍对应污点（不会发生驱逐操作）。 零值和负值会被系统当做 0 值处理（立即触发驱逐）。"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        if self.effect is not None:
            result['effect'] = self.effect
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class GetPropagationPoliciesSpreadConstraint(TeaModel):
    def __init__(
        self,
        spread_by_field: str = None,
        spread_by_label: str = None,
        max_groups: int = None,
        min_groups: int = None,
    ):
        # {"en":"The member clusters in the cluster federation are divided into multiple groups based on an attribute of the member cluster (currently, only cluster is supported, and the region, zone, and provider attributes may be supported in the future)", "zh_CN":"根据成员集群的某个属性（当前仅支持cluster、后续可能增加对成员集群region、zone、provider等属性支持）将集群联邦中的成员集群分为多个小组"}
        self.spread_by_field = spread_by_field
        # {"en":"The member cluster is divided into groups based on labels", "zh_CN":"根据label将成员集群分为多个小组"}
        self.spread_by_label = spread_by_label
        # {"en":"Maximum number of groups", "zh_CN":"最大分组数"}
        self.max_groups = max_groups
        # {"en":"Minimum number of groups", "zh_CN":"最小分组数"}
        self.min_groups = min_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spread_by_field is not None:
            result['spreadByField'] = self.spread_by_field
        if self.spread_by_label is not None:
            result['spreadByLabel'] = self.spread_by_label
        if self.max_groups is not None:
            result['maxGroups'] = self.max_groups
        if self.min_groups is not None:
            result['minGroups'] = self.min_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spreadByField') is not None:
            self.spread_by_field = m.get('spreadByField')
        if m.get('spreadByLabel') is not None:
            self.spread_by_label = m.get('spreadByLabel')
        if m.get('maxGroups') is not None:
            self.max_groups = m.get('maxGroups')
        if m.get('minGroups') is not None:
            self.min_groups = m.get('minGroups')
        return self


class GetPropagationPoliciesStaticClusterWeight(TeaModel):
    def __init__(
        self,
        target_cluster: GetPropagationPoliciesClusterAffinity = None,
        weight: int = None,
    ):
        # {"en":"affected clusters by the weight", "zh_CN":"比重生效的目标集群"}
        self.target_cluster = target_cluster
        # {"en":"proportion of replicas in total", "zh_CN":"集群实例数占比"}
        self.weight = weight

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetCluster') is not None:
            temp_model = GetPropagationPoliciesClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class GetPropagationPoliciesClusterPreferences(TeaModel):
    def __init__(
        self,
        static_weight_list: List[GetPropagationPoliciesStaticClusterWeight] = None,
        dynamic_weight: str = None,
    ):
        # {"en":"static proportion of cluster replicas in total", "zh_CN":"集群副本数占比"}
        self.static_weight_list = static_weight_list
        # {"en":"dynamic proportion of replicas in total", "zh_CN":"动态比重"}
        self.dynamic_weight = dynamic_weight

    def validate(self):
        if self.static_weight_list:
            for k in self.static_weight_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.static_weight_list is not None:
            result['staticWeightList'] = []
            for k in self.static_weight_list:
                result['staticWeightList'].append(k.to_map() if k else None)
        if self.dynamic_weight is not None:
            result['dynamicWeight'] = self.dynamic_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('staticWeightList') is not None:
            self.static_weight_list = []
            for k in m.get('staticWeightList'):
                temp_model = GetPropagationPoliciesStaticClusterWeight()
                self.static_weight_list.append(temp_model.from_map(k))
        if m.get('dynamicWeight') is not None:
            self.dynamic_weight = m.get('dynamicWeight')
        return self


class GetPropagationPoliciesReplicaSchedulingStrategy(TeaModel):
    def __init__(
        self,
        replica_scheduling_type: str = None,
        replica_division_preference: str = None,
        weight_preference: GetPropagationPoliciesClusterPreferences = None,
    ):
        # {"en":"scheduling type of replicas", "zh_CN":"副本调度类型"}
        self.replica_scheduling_type = replica_scheduling_type
        # {"en":"division preference of replicas", "zh_CN":"副本数切分方式"}
        self.replica_division_preference = replica_division_preference
        # {"en":"weight preference", "zh_CN":"权重配置"}
        self.weight_preference = weight_preference

    def validate(self):
        if self.weight_preference:
            self.weight_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.replica_scheduling_type is not None:
            result['replicaSchedulingType'] = self.replica_scheduling_type
        if self.replica_division_preference is not None:
            result['replicaDivisionPreference'] = self.replica_division_preference
        if self.weight_preference is not None:
            result['weightPreference'] = self.weight_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('replicaSchedulingType') is not None:
            self.replica_scheduling_type = m.get('replicaSchedulingType')
        if m.get('replicaDivisionPreference') is not None:
            self.replica_division_preference = m.get('replicaDivisionPreference')
        if m.get('weightPreference') is not None:
            temp_model = GetPropagationPoliciesClusterPreferences()
            self.weight_preference = temp_model.from_map(m['weightPreference'])
        return self


class GetPropagationPoliciesPlacement(TeaModel):
    def __init__(
        self,
        cluster_affinity: GetPropagationPoliciesClusterAffinity = None,
        cluster_tolerations: GetPropagationPoliciesToleration = None,
        spread_constraints: List[GetPropagationPoliciesSpreadConstraint] = None,
        replica_scheduling: GetPropagationPoliciesReplicaSchedulingStrategy = None,
    ):
        # {"en":"the policy that only applies to resources propagated to the matching clusters", "zh_CN":"策略应用到成员集群的目标选择"}
        self.cluster_affinity = cluster_affinity
        # {"en":"toleration of cluster", "zh_CN":"集群容忍度"}
        self.cluster_tolerations = cluster_tolerations
        # {"en":"Cluster grouping constraint", "zh_CN":"根据约束对集群进行分组，把资源分散到多个小组"}
        self.spread_constraints = spread_constraints
        # {"en":"scheduling strategy of replicas", "zh_CN":"副本调度策略"}
        self.replica_scheduling = replica_scheduling

    def validate(self):
        if self.cluster_affinity:
            self.cluster_affinity.validate()
        if self.cluster_tolerations:
            self.cluster_tolerations.validate()
        if self.spread_constraints:
            for k in self.spread_constraints:
                if k:
                    k.validate()
        if self.replica_scheduling:
            self.replica_scheduling.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_affinity is not None:
            result['clusterAffinity'] = self.cluster_affinity.to_map()
        if self.cluster_tolerations is not None:
            result['clusterTolerations'] = self.cluster_tolerations.to_map()
        if self.spread_constraints is not None:
            result['spreadConstraints'] = []
            for k in self.spread_constraints:
                result['spreadConstraints'].append(k.to_map() if k else None)
        if self.replica_scheduling is not None:
            result['replicaScheduling'] = self.replica_scheduling.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterAffinity') is not None:
            temp_model = GetPropagationPoliciesClusterAffinity()
            self.cluster_affinity = temp_model.from_map(m['clusterAffinity'])
        if m.get('clusterTolerations') is not None:
            temp_model = GetPropagationPoliciesToleration()
            self.cluster_tolerations = temp_model.from_map(m['clusterTolerations'])
        if m.get('spreadConstraints') is not None:
            self.spread_constraints = []
            for k in m.get('spreadConstraints'):
                temp_model = GetPropagationPoliciesSpreadConstraint()
                self.spread_constraints.append(temp_model.from_map(k))
        if m.get('replicaScheduling') is not None:
            temp_model = GetPropagationPoliciesReplicaSchedulingStrategy()
            self.replica_scheduling = temp_model.from_map(m['replicaScheduling'])
        return self


class GetPropagationPoliciesDecisionConditions(TeaModel):
    def __init__(
        self,
        toleration_seconds: int = None,
    ):
        # {"en":"represents the period of time Karmada should wait", "zh_CN":"应用经过多长时间后算失败"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class GetPropagationPoliciesApplicationFailoverBehavior(TeaModel):
    def __init__(
        self,
        decision_conditions: GetPropagationPoliciesDecisionConditions = None,
        purge_mode: str = None,
        grace_period_seconds: int = None,
    ):
        # {"en":"indicates the decision conditions of performing the failover process.", "zh_CN":"程序经过多长时间的失败,才属于不健康"}
        self.decision_conditions = decision_conditions
        # {"en":"represents how to deal with the legacy applications on the cluster from which the application is migrated. there are three options: Immediately,Graciously and Never. Graciously by defautl", "zh_CN":"应用在失败后的驱逐方式,有3个可填值: Immediately,Graciously and Never 默认:Graciously "}
        self.purge_mode = purge_mode
        # {"en":"the maximum waiting duration in seconds before application on the migrated cluster should be deleted.", "zh_CN":"平滑删除时间"}
        self.grace_period_seconds = grace_period_seconds

    def validate(self):
        if self.decision_conditions:
            self.decision_conditions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decision_conditions is not None:
            result['decisionConditions'] = self.decision_conditions.to_map()
        if self.purge_mode is not None:
            result['purgeMode'] = self.purge_mode
        if self.grace_period_seconds is not None:
            result['gracePeriodSeconds'] = self.grace_period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('decisionConditions') is not None:
            temp_model = GetPropagationPoliciesDecisionConditions()
            self.decision_conditions = temp_model.from_map(m['decisionConditions'])
        if m.get('purgeMode') is not None:
            self.purge_mode = m.get('purgeMode')
        if m.get('gracePeriodSeconds') is not None:
            self.grace_period_seconds = m.get('gracePeriodSeconds')
        return self


class GetPropagationPoliciesFailoverBehavior(TeaModel):
    def __init__(
        self,
        application: GetPropagationPoliciesApplicationFailoverBehavior = None,
    ):
        # {"en":"indicates failover behaviors in case of application failure", "zh_CN":"failover 重调度策略"}
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('application') is not None:
            temp_model = GetPropagationPoliciesApplicationFailoverBehavior()
            self.application = temp_model.from_map(m['application'])
        return self


class GetPropagationPoliciesPropagationSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[GetPropagationPoliciesResourceSelector] = None,
        association: bool = None,
        placement: GetPropagationPoliciesPlacement = None,
        dependent_overrides: List[str] = None,
        scheduler_name: str = None,
        failover: GetPropagationPoliciesFailoverBehavior = None,
    ):
        # {"en":"resource that this propagation policy applies to", "zh_CN":"策略应用的资源"}
        self.resource_selectors = resource_selectors
        # {"en":"association", "zh_CN":"association"}
        self.association = association
        # {"en":"scheduling strategy", "zh_CN":"调度策略"}
        self.placement = placement
        # {"en":"dependent overrides", "zh_CN":"依赖的覆盖策略"}
        self.dependent_overrides = dependent_overrides
        # {"en":"name of scheduler", "zh_CN":"调度器名称"}
        self.scheduler_name = scheduler_name
        # {"en":"indicates how Karmada migrates applications in case of failures", "zh_CN":"failover 重调度策略"}
        self.failover = failover

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.placement:
            self.placement.validate()
        if self.failover:
            self.failover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.association is not None:
            result['association'] = self.association
        if self.placement is not None:
            result['placement'] = self.placement.to_map()
        if self.dependent_overrides is not None:
            result['dependentOverrides'] = self.dependent_overrides
        if self.scheduler_name is not None:
            result['schedulerName'] = self.scheduler_name
        if self.failover is not None:
            result['failover'] = self.failover.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = GetPropagationPoliciesResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('association') is not None:
            self.association = m.get('association')
        if m.get('placement') is not None:
            temp_model = GetPropagationPoliciesPlacement()
            self.placement = temp_model.from_map(m['placement'])
        if m.get('dependentOverrides') is not None:
            self.dependent_overrides = m.get('dependentOverrides')
        if m.get('schedulerName') is not None:
            self.scheduler_name = m.get('schedulerName')
        if m.get('failover') is not None:
            temp_model = GetPropagationPoliciesFailoverBehavior()
            self.failover = temp_model.from_map(m['failover'])
        return self


class GetPropagationPoliciesPropagationPolicy(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: GetPropagationPoliciesObjectMeta = None,
        spec: GetPropagationPoliciesPropagationSpec = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a GetPropagationPoliciesPropagationPolicy", "zh_CN":"spec 定义 GetPropagationPoliciesPropagationPolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

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
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = GetPropagationPoliciesObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = GetPropagationPoliciesPropagationSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class GetPropagationPoliciesResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetPropagationPoliciesPropagationPolicy = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"propagationPolicy ", "zh_CN":"propagationPolicy 对象"}
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
            temp_model = GetPropagationPoliciesPropagationPolicy()
            self.data = temp_model.from_map(m['data'])
        return self


class GetPropagationPoliciesPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"The name of propagationPolicy", "zh_CN":"propagationPolicy 名称"}
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


class GetPropagationPoliciesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPropagationPoliciesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPropagationPoliciesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class WsPatchOverridepolicyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WsPatchOverridepolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: dict = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"WsPatchOverridepolicyOverridePolicy", "zh_CN":"WsPatchOverridepolicyOverridePolicy"}
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


class WsPatchOverridepolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"The name of WsPatchOverridepolicyOverridePolicy", "zh_CN":"WsPatchOverridepolicyOverridePolicy 名称"}
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


class WsPatchOverridepolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WsPatchOverridepolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WsPatchOverridepolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WsPatchOverridepolicyOwnerReference(TeaModel):
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


class WsPatchOverridepolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class WsPatchOverridepolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: WsPatchOverridepolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this WsPatchOverridepolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'WsPatchOverridepolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“WsPatchOverridepolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"WsPatchOverridepolicyFieldsV1 holds the first WsPatchOverridepolicyJSON version format as described in the 'WsPatchOverridepolicyFieldsV1' type", "zh_CN":"WsPatchOverridepolicyFieldsV1 包含类型 “WsPatchOverridepolicyFieldsV1” 中描述的第一个 WsPatchOverridepolicyJSON 版本格式"}
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
            temp_model = WsPatchOverridepolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class WsPatchOverridepolicyObjectMeta(TeaModel):
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
        owner_references: List[WsPatchOverridepolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[WsPatchOverridepolicyManagedFieldsEntry] = None,
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
                temp_model = WsPatchOverridepolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = WsPatchOverridepolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class WsPatchOverridepolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class WsPatchOverridepolicyMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[WsPatchOverridepolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = WsPatchOverridepolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class WsPatchOverridepolicyResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        namespace: str = None,
        name: str = None,
        label_selector: WsPatchOverridepolicyMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = WsPatchOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class WsPatchOverridepolicyCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class WsPatchOverridepolicyFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[WsPatchOverridepolicyCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = WsPatchOverridepolicyCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class WsPatchOverridepolicyClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: WsPatchOverridepolicyMetaV1LabelSelector = None,
        field_selector: WsPatchOverridepolicyFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = WsPatchOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = WsPatchOverridepolicyFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class WsPatchOverridepolicyJSON(TeaModel):
    def __init__(
        self,
        raw: List[bytes] = None,
    ):
        # {"en":"value", "zh_CN":"字段值"}
        self.raw = raw

    def validate(self):
        self.validate_required(self.raw, 'raw')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw is not None:
            result['raw'] = self.raw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('raw') is not None:
            self.raw = m.get('raw')
        return self


class WsPatchOverridepolicyPlaintextOverrider(TeaModel):
    def __init__(
        self,
        path: str = None,
        operator: str = None,
        value: WsPatchOverridepolicyJSON = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path
        # {"en":"type of operation on the target field", "zh_CN":"对目标字段操作类型"}
        self.operator = operator
        # {"en":"the value applied to the target field,when operator is remove, value must be empty", "zh_CN":"应用在目标字段的值，当 Operator 为 remove 时，此字段必须为空"}
        self.value = value

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.operator, 'operator')
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            temp_model = WsPatchOverridepolicyJSON()
            self.value = temp_model.from_map(m['value'])
        return self


class WsPatchOverridepolicyImagePredicate(TeaModel):
    def __init__(
        self,
        path: str = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path

    def validate(self):
        self.validate_required(self.path, 'path')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class WsPatchOverridepolicyImageOverrider(TeaModel):
    def __init__(
        self,
        predicate: WsPatchOverridepolicyImagePredicate = None,
        component: str = None,
        operator: str = None,
        value: str = None,
    ):
        # {"en":"The default is nil. If the resource is a Pod, ReplicaSet, Deployment, StatefulSet system detects the image automatically. If the resource object has multiple containers, all the images will be processed. If it is not empty, only matched mirrors are processed", "zh_CN":"默认为空,如果资源是Pod, ReplicaSet, Deployment, StatefulSet系统自动检测镜像，如果资源对象有多个容器，所有镜像都将被处理。如果不为空，则只处理匹配到的镜像"}
        self.predicate = predicate
        # {"en":"component of image: [registry/]repository[:tag]", "zh_CN":"假设镜像组成成分：[registry/]repository[:tag]"}
        self.component = component
        # {"en":"type of operation on the image", "zh_CN":"对镜像进行的操作"}
        self.operator = operator
        # {"en":"value could not be empty when operator is add or replace. Default is empty. ignored when operator is remove", "zh_CN":"当 Operator 为 add 或 replace 时不能为空，默认为空，当 operator 为 remove 时忽略"}
        self.value = value

    def validate(self):
        if self.predicate:
            self.predicate.validate()
        self.validate_required(self.component, 'component')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predicate is not None:
            result['predicate'] = self.predicate.to_map()
        if self.component is not None:
            result['component'] = self.component
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('predicate') is not None:
            temp_model = WsPatchOverridepolicyImagePredicate()
            self.predicate = temp_model.from_map(m['predicate'])
        if m.get('component') is not None:
            self.component = m.get('component')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class WsPatchOverridepolicyCommandArgsOverrider(TeaModel):
    def __init__(
        self,
        container_name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # {"en":"name of container", "zh_CN":"容器名"}
        self.container_name = container_name
        # {"en":"operation to be applied to command/args", "zh_CN":"应用在commad/args上的操作"}
        self.operator = operator
        # {"en":"The value applied to command/args is append to commad/args when operator is add. The value is removed from command/args when operator is remove. If the value is empty, command/args remains unchanged", "zh_CN":"应用在command/args上的值，当operator为add时该值append到commad/args，当operator为remove时，该值从command/args移除，如果该值为空command/args维持原状"}
        self.value = value

    def validate(self):
        self.validate_required(self.container_name, 'container_name')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['containerName'] = self.container_name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containerName') is not None:
            self.container_name = m.get('containerName')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class WsPatchOverridepolicyOverriders(TeaModel):
    def __init__(
        self,
        plaintext: List[WsPatchOverridepolicyPlaintextOverrider] = None,
        image_overrider: List[WsPatchOverridepolicyImageOverrider] = None,
        command_overrider: List[WsPatchOverridepolicyCommandArgsOverrider] = None,
        args_overrider: List[WsPatchOverridepolicyCommandArgsOverrider] = None,
    ):
        # {"en":"a general-purpose tool to override any kind of resources", "zh_CN":"覆盖任何类型资源的通用工具"}
        self.plaintext = plaintext
        # {"en":"overrides images for workloads", "zh_CN":"覆盖负载的镜像"}
        self.image_overrider = image_overrider
        # {"en":"overrides commands for workloads", "zh_CN":"覆盖工作负载的命令"}
        self.command_overrider = command_overrider
        # {"en":"overrides args for workloads", "zh_CN":"覆盖工作负载参数"}
        self.args_overrider = args_overrider

    def validate(self):
        if self.plaintext:
            for k in self.plaintext:
                if k:
                    k.validate()
        if self.image_overrider:
            for k in self.image_overrider:
                if k:
                    k.validate()
        if self.command_overrider:
            for k in self.command_overrider:
                if k:
                    k.validate()
        if self.args_overrider:
            for k in self.args_overrider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plaintext is not None:
            result['plaintext'] = []
            for k in self.plaintext:
                result['plaintext'].append(k.to_map() if k else None)
        if self.image_overrider is not None:
            result['imageOverrider'] = []
            for k in self.image_overrider:
                result['imageOverrider'].append(k.to_map() if k else None)
        if self.command_overrider is not None:
            result['commandOverrider'] = []
            for k in self.command_overrider:
                result['commandOverrider'].append(k.to_map() if k else None)
        if self.args_overrider is not None:
            result['argsOverrider'] = []
            for k in self.args_overrider:
                result['argsOverrider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('plaintext') is not None:
            self.plaintext = []
            for k in m.get('plaintext'):
                temp_model = WsPatchOverridepolicyPlaintextOverrider()
                self.plaintext.append(temp_model.from_map(k))
        if m.get('imageOverrider') is not None:
            self.image_overrider = []
            for k in m.get('imageOverrider'):
                temp_model = WsPatchOverridepolicyImageOverrider()
                self.image_overrider.append(temp_model.from_map(k))
        if m.get('commandOverrider') is not None:
            self.command_overrider = []
            for k in m.get('commandOverrider'):
                temp_model = WsPatchOverridepolicyCommandArgsOverrider()
                self.command_overrider.append(temp_model.from_map(k))
        if m.get('argsOverrider') is not None:
            self.args_overrider = []
            for k in m.get('argsOverrider'):
                temp_model = WsPatchOverridepolicyCommandArgsOverrider()
                self.args_overrider.append(temp_model.from_map(k))
        return self


class WsPatchOverridepolicyRuleWithCluster(TeaModel):
    def __init__(
        self,
        target_cluster: WsPatchOverridepolicyClusterAffinity = None,
        overriders: WsPatchOverridepolicyOverriders = None,
    ):
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"the override policy to be applied to resources", "zh_CN":"应用于资源的覆盖规则"}
        self.overriders = overriders

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()
        self.validate_required(self.overriders, 'overriders')
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['TargetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['WsPatchOverridepolicyOverriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetCluster') is not None:
            temp_model = WsPatchOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['TargetCluster'])
        if m.get('WsPatchOverridepolicyOverriders') is not None:
            temp_model = WsPatchOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['WsPatchOverridepolicyOverriders'])
        return self


class WsPatchOverridepolicyOverrideSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[WsPatchOverridepolicyResourceSelector] = None,
        override_rules: List[WsPatchOverridepolicyRuleWithCluster] = None,
        target_cluster: WsPatchOverridepolicyClusterAffinity = None,
        overriders: WsPatchOverridepolicyOverriders = None,
    ):
        # {"en":"restricts resource types that this override policy applies to. If you ignore this field it means matching all resources.", "zh_CN":"限制此覆盖策略应用的资源类型。如果忽略此字段，则表示匹配所有资源"}
        self.resource_selectors = resource_selectors
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.override_rules = override_rules
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"represents the override policy to be applied to resources", "zh_CN":"表示将应用于资源的覆盖规则，已弃用，请使用OverrideRules"}
        self.overriders = overriders

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.override_rules:
            for k in self.override_rules:
                if k:
                    k.validate()
        if self.target_cluster:
            self.target_cluster.validate()
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.override_rules is not None:
            result['overrideRules'] = []
            for k in self.override_rules:
                result['overrideRules'].append(k.to_map() if k else None)
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['overriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = WsPatchOverridepolicyResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('overrideRules') is not None:
            self.override_rules = []
            for k in m.get('overrideRules'):
                temp_model = WsPatchOverridepolicyRuleWithCluster()
                self.override_rules.append(temp_model.from_map(k))
        if m.get('targetCluster') is not None:
            temp_model = WsPatchOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('overriders') is not None:
            temp_model = WsPatchOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['overriders'])
        return self


class WsPatchOverridepolicyOverridePolicy(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: WsPatchOverridepolicyObjectMeta = None,
        spec: WsPatchOverridepolicyOverrideSpec = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a WsPatchOverridepolicyOverridePolicy", "zh_CN":"spec 定义 WsPatchOverridepolicyOverridePolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

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
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = WsPatchOverridepolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = WsPatchOverridepolicyOverrideSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self






class PutPatchPropagationPoliciesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchPropagationPoliciesOwnerReference(TeaModel):
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


class PutPatchPropagationPoliciesFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchPropagationPoliciesManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: PutPatchPropagationPoliciesFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this PutPatchPropagationPoliciesManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'PutPatchPropagationPoliciesFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“PutPatchPropagationPoliciesFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"PutPatchPropagationPoliciesFieldsV1 holds the first JSON version format as described in the 'PutPatchPropagationPoliciesFieldsV1' type", "zh_CN":"PutPatchPropagationPoliciesFieldsV1 包含类型 “PutPatchPropagationPoliciesFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = PutPatchPropagationPoliciesFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class PutPatchPropagationPoliciesObjectMeta(TeaModel):
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
        owner_references: List[PutPatchPropagationPoliciesOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[PutPatchPropagationPoliciesManagedFieldsEntry] = None,
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
                temp_model = PutPatchPropagationPoliciesOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = PutPatchPropagationPoliciesManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class PutPatchPropagationPoliciesLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class PutPatchPropagationPoliciesMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[PutPatchPropagationPoliciesLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = PutPatchPropagationPoliciesLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class PutPatchPropagationPoliciesResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        label_selector: PutPatchPropagationPoliciesMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

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
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = PutPatchPropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class PutPatchPropagationPoliciesCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class PutPatchPropagationPoliciesFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[PutPatchPropagationPoliciesCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = PutPatchPropagationPoliciesCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class PutPatchPropagationPoliciesClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: PutPatchPropagationPoliciesMetaV1LabelSelector = None,
        field_selector: PutPatchPropagationPoliciesFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = PutPatchPropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = PutPatchPropagationPoliciesFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class PutPatchPropagationPoliciesToleration(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
        effect: str = None,
        toleration_seconds: int = None,
    ):
        # {"en":"The taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.", "zh_CN":"容忍度所适用的污点的键名。此字段为空意味着匹配所有的污点键。 如果 key 为空，则 operator 必须为 Exists；这种组合意味着匹配所有值和所有键。"}
        self.key = key
        # {"en":"Represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.", "zh_CN":"表示 key 与 value 之间的关系。有效的 operator 取值是 Exists 和 Equal。默认为 Equal。 Exists 相当于 value 为某种通配符，因此 Pod 可以容忍特定类别的所有污点。"}
        self.operator = operator
        # {"en":"The taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.", "zh_CN":"容忍度所匹配的污点值。如果 operator 为 Exists，则此 value 值应该为空， 否则 value 值应该是一个正常的字符串。"}
        self.value = value
        # {"en":"Indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.", "zh_CN":"指示要匹配的污点效果。空值意味著匹配所有污点效果。如果要设置此字段，允许的值为 NoSchedule、PreferNoSchedule 和 NoExecute 之一。"}
        self.effect = effect
        # {"en":"Represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.", "zh_CN":" 表示容忍度（effect 必须是 NoExecute，否则此字段被忽略）容忍污点的时间长度。 默认情况下，此字段未被设置，这意味着会一直能够容忍对应污点（不会发生驱逐操作）。 零值和负值会被系统当做 0 值处理（立即触发驱逐）。"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        if self.effect is not None:
            result['effect'] = self.effect
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class PutPatchPropagationPoliciesSpreadConstraint(TeaModel):
    def __init__(
        self,
        spread_by_field: str = None,
        spread_by_label: str = None,
        max_groups: int = None,
        min_groups: int = None,
    ):
        # {"en":"The member clusters in the cluster federation are divided into multiple groups based on an attribute of the member cluster (currently, only cluster is supported, and the region, zone, and provider attributes may be supported in the future)", "zh_CN":"根据成员集群的某个属性（当前仅支持cluster、后续可能增加对成员集群region、zone、provider等属性支持）将集群联邦中的成员集群分为多个小组"}
        self.spread_by_field = spread_by_field
        # {"en":"The member cluster is divided into groups based on labels", "zh_CN":"根据label将成员集群分为多个小组"}
        self.spread_by_label = spread_by_label
        # {"en":"Maximum number of groups", "zh_CN":"最大分组数"}
        self.max_groups = max_groups
        # {"en":"Minimum number of groups", "zh_CN":"最小分组数"}
        self.min_groups = min_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spread_by_field is not None:
            result['spreadByField'] = self.spread_by_field
        if self.spread_by_label is not None:
            result['spreadByLabel'] = self.spread_by_label
        if self.max_groups is not None:
            result['maxGroups'] = self.max_groups
        if self.min_groups is not None:
            result['minGroups'] = self.min_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spreadByField') is not None:
            self.spread_by_field = m.get('spreadByField')
        if m.get('spreadByLabel') is not None:
            self.spread_by_label = m.get('spreadByLabel')
        if m.get('maxGroups') is not None:
            self.max_groups = m.get('maxGroups')
        if m.get('minGroups') is not None:
            self.min_groups = m.get('minGroups')
        return self


class PutPatchPropagationPoliciesStaticClusterWeight(TeaModel):
    def __init__(
        self,
        target_cluster: PutPatchPropagationPoliciesClusterAffinity = None,
        weight: int = None,
    ):
        # {"en":"affected clusters by the weight", "zh_CN":"比重生效的目标集群"}
        self.target_cluster = target_cluster
        # {"en":"proportion of replicas in total", "zh_CN":"集群实例数占比"}
        self.weight = weight

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetCluster') is not None:
            temp_model = PutPatchPropagationPoliciesClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class PutPatchPropagationPoliciesClusterPreferences(TeaModel):
    def __init__(
        self,
        static_weight_list: List[PutPatchPropagationPoliciesStaticClusterWeight] = None,
        dynamic_weight: str = None,
    ):
        # {"en":"static proportion of cluster replicas in total", "zh_CN":"集群副本数占比"}
        self.static_weight_list = static_weight_list
        # {"en":"dynamic proportion of replicas in total", "zh_CN":"动态比重"}
        self.dynamic_weight = dynamic_weight

    def validate(self):
        if self.static_weight_list:
            for k in self.static_weight_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.static_weight_list is not None:
            result['staticWeightList'] = []
            for k in self.static_weight_list:
                result['staticWeightList'].append(k.to_map() if k else None)
        if self.dynamic_weight is not None:
            result['dynamicWeight'] = self.dynamic_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('staticWeightList') is not None:
            self.static_weight_list = []
            for k in m.get('staticWeightList'):
                temp_model = PutPatchPropagationPoliciesStaticClusterWeight()
                self.static_weight_list.append(temp_model.from_map(k))
        if m.get('dynamicWeight') is not None:
            self.dynamic_weight = m.get('dynamicWeight')
        return self


class PutPatchPropagationPoliciesReplicaSchedulingStrategy(TeaModel):
    def __init__(
        self,
        replica_scheduling_type: str = None,
        replica_division_preference: str = None,
        weight_preference: PutPatchPropagationPoliciesClusterPreferences = None,
    ):
        # {"en":"scheduling type of replicas", "zh_CN":"副本调度类型"}
        self.replica_scheduling_type = replica_scheduling_type
        # {"en":"division preference of replicas", "zh_CN":"副本数切分方式"}
        self.replica_division_preference = replica_division_preference
        # {"en":"weight preference", "zh_CN":"权重配置"}
        self.weight_preference = weight_preference

    def validate(self):
        if self.weight_preference:
            self.weight_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.replica_scheduling_type is not None:
            result['replicaSchedulingType'] = self.replica_scheduling_type
        if self.replica_division_preference is not None:
            result['replicaDivisionPreference'] = self.replica_division_preference
        if self.weight_preference is not None:
            result['weightPreference'] = self.weight_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('replicaSchedulingType') is not None:
            self.replica_scheduling_type = m.get('replicaSchedulingType')
        if m.get('replicaDivisionPreference') is not None:
            self.replica_division_preference = m.get('replicaDivisionPreference')
        if m.get('weightPreference') is not None:
            temp_model = PutPatchPropagationPoliciesClusterPreferences()
            self.weight_preference = temp_model.from_map(m['weightPreference'])
        return self


class PutPatchPropagationPoliciesPlacement(TeaModel):
    def __init__(
        self,
        cluster_affinity: PutPatchPropagationPoliciesClusterAffinity = None,
        cluster_tolerations: PutPatchPropagationPoliciesToleration = None,
        spread_constraints: List[PutPatchPropagationPoliciesSpreadConstraint] = None,
        replica_scheduling: PutPatchPropagationPoliciesReplicaSchedulingStrategy = None,
    ):
        # {"en":"the policy that only applies to resources propagated to the matching clusters", "zh_CN":"策略应用到成员集群的目标选择"}
        self.cluster_affinity = cluster_affinity
        # {"en":"toleration of cluster", "zh_CN":"集群容忍度"}
        self.cluster_tolerations = cluster_tolerations
        # {"en":"Cluster grouping constraint", "zh_CN":"根据约束对集群进行分组，把资源分散到多个小组"}
        self.spread_constraints = spread_constraints
        # {"en":"scheduling strategy of replicas", "zh_CN":"副本调度策略"}
        self.replica_scheduling = replica_scheduling

    def validate(self):
        if self.cluster_affinity:
            self.cluster_affinity.validate()
        if self.cluster_tolerations:
            self.cluster_tolerations.validate()
        if self.spread_constraints:
            for k in self.spread_constraints:
                if k:
                    k.validate()
        if self.replica_scheduling:
            self.replica_scheduling.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_affinity is not None:
            result['clusterAffinity'] = self.cluster_affinity.to_map()
        if self.cluster_tolerations is not None:
            result['clusterTolerations'] = self.cluster_tolerations.to_map()
        if self.spread_constraints is not None:
            result['spreadConstraints'] = []
            for k in self.spread_constraints:
                result['spreadConstraints'].append(k.to_map() if k else None)
        if self.replica_scheduling is not None:
            result['replicaScheduling'] = self.replica_scheduling.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterAffinity') is not None:
            temp_model = PutPatchPropagationPoliciesClusterAffinity()
            self.cluster_affinity = temp_model.from_map(m['clusterAffinity'])
        if m.get('clusterTolerations') is not None:
            temp_model = PutPatchPropagationPoliciesToleration()
            self.cluster_tolerations = temp_model.from_map(m['clusterTolerations'])
        if m.get('spreadConstraints') is not None:
            self.spread_constraints = []
            for k in m.get('spreadConstraints'):
                temp_model = PutPatchPropagationPoliciesSpreadConstraint()
                self.spread_constraints.append(temp_model.from_map(k))
        if m.get('replicaScheduling') is not None:
            temp_model = PutPatchPropagationPoliciesReplicaSchedulingStrategy()
            self.replica_scheduling = temp_model.from_map(m['replicaScheduling'])
        return self


class PutPatchPropagationPoliciesDecisionConditions(TeaModel):
    def __init__(
        self,
        toleration_seconds: int = None,
    ):
        # {"en":"represents the period of time Karmada should wait", "zh_CN":"应用经过多长时间后算失败"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class PutPatchPropagationPoliciesApplicationFailoverBehavior(TeaModel):
    def __init__(
        self,
        decision_conditions: PutPatchPropagationPoliciesDecisionConditions = None,
        purge_mode: str = None,
        grace_period_seconds: int = None,
    ):
        # {"en":"indicates the decision conditions of performing the failover process.", "zh_CN":"程序经过多长时间的失败,才属于不健康"}
        self.decision_conditions = decision_conditions
        # {"en":"represents how to deal with the legacy applications on the cluster from which the application is migrated. there are three options: Immediately,Graciously and Never. Graciously by defautl", "zh_CN":"应用在失败后的驱逐方式,有3个可填值: Immediately,Graciously and Never 默认:Graciously "}
        self.purge_mode = purge_mode
        # {"en":"the maximum waiting duration in seconds before application on the migrated cluster should be deleted.", "zh_CN":"平滑删除时间"}
        self.grace_period_seconds = grace_period_seconds

    def validate(self):
        if self.decision_conditions:
            self.decision_conditions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decision_conditions is not None:
            result['decisionConditions'] = self.decision_conditions.to_map()
        if self.purge_mode is not None:
            result['purgeMode'] = self.purge_mode
        if self.grace_period_seconds is not None:
            result['gracePeriodSeconds'] = self.grace_period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('decisionConditions') is not None:
            temp_model = PutPatchPropagationPoliciesDecisionConditions()
            self.decision_conditions = temp_model.from_map(m['decisionConditions'])
        if m.get('purgeMode') is not None:
            self.purge_mode = m.get('purgeMode')
        if m.get('gracePeriodSeconds') is not None:
            self.grace_period_seconds = m.get('gracePeriodSeconds')
        return self


class PutPatchPropagationPoliciesFailoverBehavior(TeaModel):
    def __init__(
        self,
        application: PutPatchPropagationPoliciesApplicationFailoverBehavior = None,
    ):
        # {"en":"indicates failover behaviors in case of application failure", "zh_CN":"failover 重调度策略"}
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('application') is not None:
            temp_model = PutPatchPropagationPoliciesApplicationFailoverBehavior()
            self.application = temp_model.from_map(m['application'])
        return self


class PutPatchPropagationPoliciesPropagationSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[PutPatchPropagationPoliciesResourceSelector] = None,
        association: bool = None,
        placement: PutPatchPropagationPoliciesPlacement = None,
        dependent_overrides: List[str] = None,
        scheduler_name: str = None,
        failover: PutPatchPropagationPoliciesFailoverBehavior = None,
    ):
        # {"en":"resource that this propagation policy applies to", "zh_CN":"策略应用的资源"}
        self.resource_selectors = resource_selectors
        # {"en":"association", "zh_CN":"association"}
        self.association = association
        # {"en":"scheduling strategy", "zh_CN":"调度策略"}
        self.placement = placement
        # {"en":"dependent overrides", "zh_CN":"依赖的覆盖策略"}
        self.dependent_overrides = dependent_overrides
        # {"en":"name of scheduler", "zh_CN":"调度器名称"}
        self.scheduler_name = scheduler_name
        # {"en":"indicates how Karmada migrates applications in case of failures", "zh_CN":"failover 重调度策略"}
        self.failover = failover

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.placement:
            self.placement.validate()
        if self.failover:
            self.failover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.association is not None:
            result['association'] = self.association
        if self.placement is not None:
            result['placement'] = self.placement.to_map()
        if self.dependent_overrides is not None:
            result['dependentOverrides'] = self.dependent_overrides
        if self.scheduler_name is not None:
            result['schedulerName'] = self.scheduler_name
        if self.failover is not None:
            result['failover'] = self.failover.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = PutPatchPropagationPoliciesResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('association') is not None:
            self.association = m.get('association')
        if m.get('placement') is not None:
            temp_model = PutPatchPropagationPoliciesPlacement()
            self.placement = temp_model.from_map(m['placement'])
        if m.get('dependentOverrides') is not None:
            self.dependent_overrides = m.get('dependentOverrides')
        if m.get('schedulerName') is not None:
            self.scheduler_name = m.get('schedulerName')
        if m.get('failover') is not None:
            temp_model = PutPatchPropagationPoliciesFailoverBehavior()
            self.failover = temp_model.from_map(m['failover'])
        return self


class PutPatchPropagationPoliciesPropagationPolicy(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: PutPatchPropagationPoliciesObjectMeta = None,
        spec: PutPatchPropagationPoliciesPropagationSpec = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a PutPatchPropagationPoliciesPropagationPolicy", "zh_CN":"spec 定义 PutPatchPropagationPoliciesPropagationPolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

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
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = PutPatchPropagationPoliciesObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PutPatchPropagationPoliciesPropagationSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class PutPatchPropagationPoliciesResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: PutPatchPropagationPoliciesPropagationPolicy = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"PutPatchPropagationPoliciesPropagationPolicy object", "zh_CN":"PropagationPolicy对象"}
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
            temp_model = PutPatchPropagationPoliciesPropagationPolicy()
            self.data = temp_model.from_map(m['data'])
        return self


class PutPatchPropagationPoliciesPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"The name of propagationPolicy", "zh_CN":"propagationPolicy 名称"}
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


class PutPatchPropagationPoliciesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchPropagationPoliciesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchPropagationPoliciesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListOverridepolicyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListOverridepolicyListMeta(TeaModel):
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


class ListOverridepolicyOwnerReference(TeaModel):
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


class ListOverridepolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListOverridepolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: ListOverridepolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this ListOverridepolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'ListOverridepolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“ListOverridepolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"ListOverridepolicyFieldsV1 holds the first ListOverridepolicyJSON version format as described in the 'ListOverridepolicyFieldsV1' type", "zh_CN":"ListOverridepolicyFieldsV1 包含类型 “ListOverridepolicyFieldsV1” 中描述的第一个 ListOverridepolicyJSON 版本格式"}
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
            temp_model = ListOverridepolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class ListOverridepolicyObjectMeta(TeaModel):
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
        owner_references: List[ListOverridepolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[ListOverridepolicyManagedFieldsEntry] = None,
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
                temp_model = ListOverridepolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = ListOverridepolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class ListOverridepolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListOverridepolicyMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[ListOverridepolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = ListOverridepolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class ListOverridepolicyResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        namespace: str = None,
        name: str = None,
        label_selector: ListOverridepolicyMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = ListOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class ListOverridepolicyCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListOverridepolicyFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[ListOverridepolicyCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = ListOverridepolicyCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class ListOverridepolicyClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: ListOverridepolicyMetaV1LabelSelector = None,
        field_selector: ListOverridepolicyFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = ListOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = ListOverridepolicyFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class ListOverridepolicyJSON(TeaModel):
    def __init__(
        self,
        raw: List[bytes] = None,
    ):
        # {"en":"value", "zh_CN":"字段值"}
        self.raw = raw

    def validate(self):
        self.validate_required(self.raw, 'raw')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw is not None:
            result['raw'] = self.raw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('raw') is not None:
            self.raw = m.get('raw')
        return self


class ListOverridepolicyPlaintextOverrider(TeaModel):
    def __init__(
        self,
        path: str = None,
        operator: str = None,
        value: ListOverridepolicyJSON = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path
        # {"en":"type of operation on the target field", "zh_CN":"对目标字段操作类型"}
        self.operator = operator
        # {"en":"the value applied to the target field,when operator is remove, value must be empty", "zh_CN":"应用在目标字段的值，当 Operator 为 remove 时，此字段必须为空"}
        self.value = value

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.operator, 'operator')
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            temp_model = ListOverridepolicyJSON()
            self.value = temp_model.from_map(m['value'])
        return self


class ListOverridepolicyImagePredicate(TeaModel):
    def __init__(
        self,
        path: str = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path

    def validate(self):
        self.validate_required(self.path, 'path')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class ListOverridepolicyImageOverrider(TeaModel):
    def __init__(
        self,
        predicate: ListOverridepolicyImagePredicate = None,
        component: str = None,
        operator: str = None,
        value: str = None,
    ):
        # {"en":"The default is nil. If the resource is a Pod, ReplicaSet, Deployment, StatefulSet system detects the image automatically. If the resource object has multiple containers, all the images will be processed. If it is not empty, only matched mirrors are processed", "zh_CN":"默认为空,如果资源是Pod, ReplicaSet, Deployment, StatefulSet系统自动检测镜像，如果资源对象有多个容器，所有镜像都将被处理。如果不为空，则只处理匹配到的镜像"}
        self.predicate = predicate
        # {"en":"component of image: [registry/]repository[:tag]", "zh_CN":"假设镜像组成成分：[registry/]repository[:tag]"}
        self.component = component
        # {"en":"type of operation on the image", "zh_CN":"对镜像进行的操作"}
        self.operator = operator
        # {"en":"value could not be empty when operator is add or replace. Default is empty. ignored when operator is remove", "zh_CN":"当 Operator 为 add 或 replace 时不能为空，默认为空，当 operator 为 remove 时忽略"}
        self.value = value

    def validate(self):
        if self.predicate:
            self.predicate.validate()
        self.validate_required(self.component, 'component')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predicate is not None:
            result['predicate'] = self.predicate.to_map()
        if self.component is not None:
            result['component'] = self.component
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('predicate') is not None:
            temp_model = ListOverridepolicyImagePredicate()
            self.predicate = temp_model.from_map(m['predicate'])
        if m.get('component') is not None:
            self.component = m.get('component')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListOverridepolicyCommandArgsOverrider(TeaModel):
    def __init__(
        self,
        container_name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # {"en":"name of container", "zh_CN":"容器名"}
        self.container_name = container_name
        # {"en":"operation to be applied to command/args", "zh_CN":"应用在commad/args上的操作"}
        self.operator = operator
        # {"en":"The value applied to command/args is append to commad/args when operator is add. The value is removed from command/args when operator is remove. If the value is empty, command/args remains unchanged", "zh_CN":"应用在command/args上的值，当operator为add时该值append到commad/args，当operator为remove时，该值从command/args移除，如果该值为空command/args维持原状"}
        self.value = value

    def validate(self):
        self.validate_required(self.container_name, 'container_name')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['containerName'] = self.container_name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containerName') is not None:
            self.container_name = m.get('containerName')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListOverridepolicyOverriders(TeaModel):
    def __init__(
        self,
        plaintext: List[ListOverridepolicyPlaintextOverrider] = None,
        image_overrider: List[ListOverridepolicyImageOverrider] = None,
        command_overrider: List[ListOverridepolicyCommandArgsOverrider] = None,
        args_overrider: List[ListOverridepolicyCommandArgsOverrider] = None,
    ):
        # {"en":"a general-purpose tool to override any kind of resources", "zh_CN":"覆盖任何类型资源的通用工具"}
        self.plaintext = plaintext
        # {"en":"overrides images for workloads", "zh_CN":"覆盖负载的镜像"}
        self.image_overrider = image_overrider
        # {"en":"overrides commands for workloads", "zh_CN":"覆盖工作负载的命令"}
        self.command_overrider = command_overrider
        # {"en":"overrides args for workloads", "zh_CN":"覆盖工作负载参数"}
        self.args_overrider = args_overrider

    def validate(self):
        if self.plaintext:
            for k in self.plaintext:
                if k:
                    k.validate()
        if self.image_overrider:
            for k in self.image_overrider:
                if k:
                    k.validate()
        if self.command_overrider:
            for k in self.command_overrider:
                if k:
                    k.validate()
        if self.args_overrider:
            for k in self.args_overrider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plaintext is not None:
            result['plaintext'] = []
            for k in self.plaintext:
                result['plaintext'].append(k.to_map() if k else None)
        if self.image_overrider is not None:
            result['imageOverrider'] = []
            for k in self.image_overrider:
                result['imageOverrider'].append(k.to_map() if k else None)
        if self.command_overrider is not None:
            result['commandOverrider'] = []
            for k in self.command_overrider:
                result['commandOverrider'].append(k.to_map() if k else None)
        if self.args_overrider is not None:
            result['argsOverrider'] = []
            for k in self.args_overrider:
                result['argsOverrider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('plaintext') is not None:
            self.plaintext = []
            for k in m.get('plaintext'):
                temp_model = ListOverridepolicyPlaintextOverrider()
                self.plaintext.append(temp_model.from_map(k))
        if m.get('imageOverrider') is not None:
            self.image_overrider = []
            for k in m.get('imageOverrider'):
                temp_model = ListOverridepolicyImageOverrider()
                self.image_overrider.append(temp_model.from_map(k))
        if m.get('commandOverrider') is not None:
            self.command_overrider = []
            for k in m.get('commandOverrider'):
                temp_model = ListOverridepolicyCommandArgsOverrider()
                self.command_overrider.append(temp_model.from_map(k))
        if m.get('argsOverrider') is not None:
            self.args_overrider = []
            for k in m.get('argsOverrider'):
                temp_model = ListOverridepolicyCommandArgsOverrider()
                self.args_overrider.append(temp_model.from_map(k))
        return self


class ListOverridepolicyRuleWithCluster(TeaModel):
    def __init__(
        self,
        target_cluster: ListOverridepolicyClusterAffinity = None,
        overriders: ListOverridepolicyOverriders = None,
    ):
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"the override policy to be applied to resources", "zh_CN":"应用于资源的覆盖规则"}
        self.overriders = overriders

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()
        self.validate_required(self.overriders, 'overriders')
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['TargetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['ListOverridepolicyOverriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetCluster') is not None:
            temp_model = ListOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['TargetCluster'])
        if m.get('ListOverridepolicyOverriders') is not None:
            temp_model = ListOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['ListOverridepolicyOverriders'])
        return self


class ListOverridepolicyOverrideSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[ListOverridepolicyResourceSelector] = None,
        override_rules: List[ListOverridepolicyRuleWithCluster] = None,
        target_cluster: ListOverridepolicyClusterAffinity = None,
        overriders: ListOverridepolicyOverriders = None,
    ):
        # {"en":"restricts resource types that this override policy applies to. If you ignore this field it means matching all resources.", "zh_CN":"限制此覆盖策略应用的资源类型。如果忽略此字段，则表示匹配所有资源"}
        self.resource_selectors = resource_selectors
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.override_rules = override_rules
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"represents the override policy to be applied to resources", "zh_CN":"表示将应用于资源的覆盖规则，已弃用，请使用OverrideRules"}
        self.overriders = overriders

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.override_rules:
            for k in self.override_rules:
                if k:
                    k.validate()
        if self.target_cluster:
            self.target_cluster.validate()
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.override_rules is not None:
            result['overrideRules'] = []
            for k in self.override_rules:
                result['overrideRules'].append(k.to_map() if k else None)
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['overriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = ListOverridepolicyResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('overrideRules') is not None:
            self.override_rules = []
            for k in m.get('overrideRules'):
                temp_model = ListOverridepolicyRuleWithCluster()
                self.override_rules.append(temp_model.from_map(k))
        if m.get('targetCluster') is not None:
            temp_model = ListOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('overriders') is not None:
            temp_model = ListOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['overriders'])
        return self


class ListOverridepolicyOverridePolicy(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListOverridepolicyObjectMeta = None,
        spec: ListOverridepolicyOverrideSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a ListOverridepolicyOverridePolicy", "zh_CN":"spec 定义 ListOverridepolicyOverridePolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
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
            temp_model = ListOverridepolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = ListOverridepolicyOverrideSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class ListOverridepolicyOverridePolicyList(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListOverridepolicyListMeta = None,
        items: List[ListOverridepolicyOverridePolicy] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard list metadata", "zh_CN":"标准列表元数据"}
        self.metadata = metadata
        # {"en":"List of ListOverridepolicyOverridePolicy", "zh_CN":"ListOverridepolicyOverridePolicy 列表"}
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
            temp_model = ListOverridepolicyListMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListOverridepolicyOverridePolicy()
                self.items.append(temp_model.from_map(k))
        return self


class ListOverridepolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListOverridepolicyOverridePolicyList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ListOverridepolicyOverridePolicyList", "zh_CN":"ListOverridepolicyOverridePolicyList"}
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
            temp_model = ListOverridepolicyOverridePolicyList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListOverridepolicyPaths(TeaModel):
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


class ListOverridepolicyParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        label_selector: str = None,
    ):
        # {"en":"The name of deployment", "zh_CN":"deployment 名称"}
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


class ListOverridepolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListOverridepolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeletePropagationPoliciesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePropagationPoliciesStatusDetails(TeaModel):
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


class DeletePropagationPoliciesStatus(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        status: str = None,
        code: int = None,
        details: DeletePropagationPoliciesStatusDetails = None,
    ):
        # {"en":"APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values", "zh_CN":"APIVersion 定义对象表示的版本化模式。 服务器应将已识别的模式转换为最新的内部值，并可能拒绝无法识别的值"}
        self.api_version = api_version
        # {"en":"Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase", "zh_CN":"Kind 是一个字符串值，表示此对象表示的 REST 资源。 服务器可以从客户端提交请求的端点推断出这一点。 无法更新。驼峰式规则"}
        self.kind = kind
        # {"en":"DeletePropagationPoliciesStatus of the operation. One of: 'Success' or 'Failure'", "zh_CN":"操作状态。“Success”或“Failure” 之一"}
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
            temp_model = DeletePropagationPoliciesStatusDetails()
            self.details = temp_model.from_map(m['details'])
        return self


class DeletePropagationPoliciesResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: DeletePropagationPoliciesStatus = None,
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
            temp_model = DeletePropagationPoliciesStatus()
            self.data = temp_model.from_map(m['data'])
        return self


class DeletePropagationPoliciesPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"The name of propagationPolicy", "zh_CN":"propagationPolicy 名称"}
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


class DeletePropagationPoliciesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePropagationPoliciesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePropagationPoliciesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteHorizontalPodAutoscalerRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHorizontalPodAutoscalerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DeleteHorizontalPodAutoscalerPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"hpa name", "zh_CN":"hpa 名称"}
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


class DeleteHorizontalPodAutoscalerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHorizontalPodAutoscalerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteHorizontalPodAutoscalerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListPropagationPoliciesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListPropagationPoliciesListMeta(TeaModel):
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


class ListPropagationPoliciesOwnerReference(TeaModel):
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


class ListPropagationPoliciesFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListPropagationPoliciesManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: ListPropagationPoliciesFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this ListPropagationPoliciesManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'ListPropagationPoliciesFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“ListPropagationPoliciesFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"ListPropagationPoliciesFieldsV1 holds the first JSON version format as described in the 'ListPropagationPoliciesFieldsV1' type", "zh_CN":"ListPropagationPoliciesFieldsV1 包含类型 “ListPropagationPoliciesFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = ListPropagationPoliciesFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class ListPropagationPoliciesObjectMeta(TeaModel):
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
        owner_references: List[ListPropagationPoliciesOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[ListPropagationPoliciesManagedFieldsEntry] = None,
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
                temp_model = ListPropagationPoliciesOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = ListPropagationPoliciesManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class ListPropagationPoliciesLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListPropagationPoliciesMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[ListPropagationPoliciesLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = ListPropagationPoliciesLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class ListPropagationPoliciesResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        namespace: str = None,
        name: str = None,
        label_selector: ListPropagationPoliciesMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = ListPropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class ListPropagationPoliciesCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListPropagationPoliciesFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[ListPropagationPoliciesCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = ListPropagationPoliciesCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class ListPropagationPoliciesClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: ListPropagationPoliciesMetaV1LabelSelector = None,
        field_selector: ListPropagationPoliciesFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = ListPropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = ListPropagationPoliciesFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class ListPropagationPoliciesToleration(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
        effect: str = None,
        toleration_seconds: int = None,
    ):
        # {"en":"The taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.", "zh_CN":"容忍度所适用的污点的键名。此字段为空意味着匹配所有的污点键。 如果 key 为空，则 operator 必须为 Exists；这种组合意味着匹配所有值和所有键。"}
        self.key = key
        # {"en":"Represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.", "zh_CN":"表示 key 与 value 之间的关系。有效的 operator 取值是 Exists 和 Equal。默认为 Equal。 Exists 相当于 value 为某种通配符，因此 Pod 可以容忍特定类别的所有污点。"}
        self.operator = operator
        # {"en":"The taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.", "zh_CN":"容忍度所匹配的污点值。如果 operator 为 Exists，则此 value 值应该为空， 否则 value 值应该是一个正常的字符串。"}
        self.value = value
        # {"en":"Indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.", "zh_CN":"指示要匹配的污点效果。空值意味著匹配所有污点效果。如果要设置此字段，允许的值为 NoSchedule、PreferNoSchedule 和 NoExecute 之一。"}
        self.effect = effect
        # {"en":"Represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.", "zh_CN":" 表示容忍度（effect 必须是 NoExecute，否则此字段被忽略）容忍污点的时间长度。 默认情况下，此字段未被设置，这意味着会一直能够容忍对应污点（不会发生驱逐操作）。 零值和负值会被系统当做 0 值处理（立即触发驱逐）。"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        if self.effect is not None:
            result['effect'] = self.effect
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class ListPropagationPoliciesSpreadConstraint(TeaModel):
    def __init__(
        self,
        spread_by_field: str = None,
        spread_by_label: str = None,
        max_groups: int = None,
        min_groups: int = None,
    ):
        # {"en":"The member clusters in the cluster federation are divided into multiple groups based on an attribute of the member cluster (currently, only cluster is supported, and the region, zone, and provider attributes may be supported in the future)", "zh_CN":"根据成员集群的某个属性（当前仅支持cluster、后续可能增加对成员集群region、zone、provider等属性支持）将集群联邦中的成员集群分为多个小组"}
        self.spread_by_field = spread_by_field
        # {"en":"The member cluster is divided into groups based on labels", "zh_CN":"根据label将成员集群分为多个小组"}
        self.spread_by_label = spread_by_label
        # {"en":"Maximum number of groups", "zh_CN":"最大分组数"}
        self.max_groups = max_groups
        # {"en":"Minimum number of groups", "zh_CN":"最小分组数"}
        self.min_groups = min_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spread_by_field is not None:
            result['spreadByField'] = self.spread_by_field
        if self.spread_by_label is not None:
            result['spreadByLabel'] = self.spread_by_label
        if self.max_groups is not None:
            result['maxGroups'] = self.max_groups
        if self.min_groups is not None:
            result['minGroups'] = self.min_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spreadByField') is not None:
            self.spread_by_field = m.get('spreadByField')
        if m.get('spreadByLabel') is not None:
            self.spread_by_label = m.get('spreadByLabel')
        if m.get('maxGroups') is not None:
            self.max_groups = m.get('maxGroups')
        if m.get('minGroups') is not None:
            self.min_groups = m.get('minGroups')
        return self


class ListPropagationPoliciesStaticClusterWeight(TeaModel):
    def __init__(
        self,
        target_cluster: ListPropagationPoliciesClusterAffinity = None,
        weight: int = None,
    ):
        # {"en":"affected clusters by the weight", "zh_CN":"比重生效的目标集群"}
        self.target_cluster = target_cluster
        # {"en":"proportion of replicas in total", "zh_CN":"集群实例数占比"}
        self.weight = weight

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetCluster') is not None:
            temp_model = ListPropagationPoliciesClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class ListPropagationPoliciesClusterPreferences(TeaModel):
    def __init__(
        self,
        static_weight_list: List[ListPropagationPoliciesStaticClusterWeight] = None,
        dynamic_weight: str = None,
    ):
        # {"en":"static proportion of cluster replicas in total", "zh_CN":"集群副本数占比"}
        self.static_weight_list = static_weight_list
        # {"en":"dynamic proportion of replicas in total", "zh_CN":"动态比重"}
        self.dynamic_weight = dynamic_weight

    def validate(self):
        if self.static_weight_list:
            for k in self.static_weight_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.static_weight_list is not None:
            result['staticWeightList'] = []
            for k in self.static_weight_list:
                result['staticWeightList'].append(k.to_map() if k else None)
        if self.dynamic_weight is not None:
            result['dynamicWeight'] = self.dynamic_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('staticWeightList') is not None:
            self.static_weight_list = []
            for k in m.get('staticWeightList'):
                temp_model = ListPropagationPoliciesStaticClusterWeight()
                self.static_weight_list.append(temp_model.from_map(k))
        if m.get('dynamicWeight') is not None:
            self.dynamic_weight = m.get('dynamicWeight')
        return self


class ListPropagationPoliciesReplicaSchedulingStrategy(TeaModel):
    def __init__(
        self,
        replica_scheduling_type: str = None,
        replica_division_preference: str = None,
        weight_preference: ListPropagationPoliciesClusterPreferences = None,
    ):
        # {"en":"scheduling type of replicas", "zh_CN":"副本调度类型"}
        self.replica_scheduling_type = replica_scheduling_type
        # {"en":"division preference of replicas", "zh_CN":"副本数切分方式"}
        self.replica_division_preference = replica_division_preference
        # {"en":"weight preference", "zh_CN":"权重配置"}
        self.weight_preference = weight_preference

    def validate(self):
        if self.weight_preference:
            self.weight_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.replica_scheduling_type is not None:
            result['replicaSchedulingType'] = self.replica_scheduling_type
        if self.replica_division_preference is not None:
            result['replicaDivisionPreference'] = self.replica_division_preference
        if self.weight_preference is not None:
            result['weightPreference'] = self.weight_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('replicaSchedulingType') is not None:
            self.replica_scheduling_type = m.get('replicaSchedulingType')
        if m.get('replicaDivisionPreference') is not None:
            self.replica_division_preference = m.get('replicaDivisionPreference')
        if m.get('weightPreference') is not None:
            temp_model = ListPropagationPoliciesClusterPreferences()
            self.weight_preference = temp_model.from_map(m['weightPreference'])
        return self


class ListPropagationPoliciesPlacement(TeaModel):
    def __init__(
        self,
        cluster_affinity: ListPropagationPoliciesClusterAffinity = None,
        cluster_tolerations: ListPropagationPoliciesToleration = None,
        spread_constraints: List[ListPropagationPoliciesSpreadConstraint] = None,
        replica_scheduling: ListPropagationPoliciesReplicaSchedulingStrategy = None,
    ):
        # {"en":"the policy that only applies to resources propagated to the matching clusters", "zh_CN":"策略应用到成员集群的目标选择"}
        self.cluster_affinity = cluster_affinity
        # {"en":"toleration of cluster", "zh_CN":"集群容忍度"}
        self.cluster_tolerations = cluster_tolerations
        # {"en":"Cluster grouping constraint", "zh_CN":"根据约束对集群进行分组，把资源分散到多个小组"}
        self.spread_constraints = spread_constraints
        # {"en":"scheduling strategy of replicas", "zh_CN":"副本调度策略"}
        self.replica_scheduling = replica_scheduling

    def validate(self):
        if self.cluster_affinity:
            self.cluster_affinity.validate()
        if self.cluster_tolerations:
            self.cluster_tolerations.validate()
        if self.spread_constraints:
            for k in self.spread_constraints:
                if k:
                    k.validate()
        if self.replica_scheduling:
            self.replica_scheduling.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_affinity is not None:
            result['clusterAffinity'] = self.cluster_affinity.to_map()
        if self.cluster_tolerations is not None:
            result['clusterTolerations'] = self.cluster_tolerations.to_map()
        if self.spread_constraints is not None:
            result['spreadConstraints'] = []
            for k in self.spread_constraints:
                result['spreadConstraints'].append(k.to_map() if k else None)
        if self.replica_scheduling is not None:
            result['replicaScheduling'] = self.replica_scheduling.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterAffinity') is not None:
            temp_model = ListPropagationPoliciesClusterAffinity()
            self.cluster_affinity = temp_model.from_map(m['clusterAffinity'])
        if m.get('clusterTolerations') is not None:
            temp_model = ListPropagationPoliciesToleration()
            self.cluster_tolerations = temp_model.from_map(m['clusterTolerations'])
        if m.get('spreadConstraints') is not None:
            self.spread_constraints = []
            for k in m.get('spreadConstraints'):
                temp_model = ListPropagationPoliciesSpreadConstraint()
                self.spread_constraints.append(temp_model.from_map(k))
        if m.get('replicaScheduling') is not None:
            temp_model = ListPropagationPoliciesReplicaSchedulingStrategy()
            self.replica_scheduling = temp_model.from_map(m['replicaScheduling'])
        return self


class ListPropagationPoliciesDecisionConditions(TeaModel):
    def __init__(
        self,
        toleration_seconds: int = None,
    ):
        # {"en":"represents the period of time Karmada should wait", "zh_CN":"应用经过多长时间后算失败"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class ListPropagationPoliciesApplicationFailoverBehavior(TeaModel):
    def __init__(
        self,
        decision_conditions: ListPropagationPoliciesDecisionConditions = None,
        purge_mode: str = None,
        grace_period_seconds: int = None,
    ):
        # {"en":"indicates the decision conditions of performing the failover process.", "zh_CN":"程序经过多长时间的失败,才属于不健康"}
        self.decision_conditions = decision_conditions
        # {"en":"represents how to deal with the legacy applications on the cluster from which the application is migrated. there are three options: Immediately,Graciously and Never. Graciously by defautl", "zh_CN":"应用在失败后的驱逐方式,有3个可填值: Immediately,Graciously and Never 默认:Graciously "}
        self.purge_mode = purge_mode
        # {"en":"the maximum waiting duration in seconds before application on the migrated cluster should be deleted.", "zh_CN":"平滑删除时间"}
        self.grace_period_seconds = grace_period_seconds

    def validate(self):
        if self.decision_conditions:
            self.decision_conditions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decision_conditions is not None:
            result['decisionConditions'] = self.decision_conditions.to_map()
        if self.purge_mode is not None:
            result['purgeMode'] = self.purge_mode
        if self.grace_period_seconds is not None:
            result['gracePeriodSeconds'] = self.grace_period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('decisionConditions') is not None:
            temp_model = ListPropagationPoliciesDecisionConditions()
            self.decision_conditions = temp_model.from_map(m['decisionConditions'])
        if m.get('purgeMode') is not None:
            self.purge_mode = m.get('purgeMode')
        if m.get('gracePeriodSeconds') is not None:
            self.grace_period_seconds = m.get('gracePeriodSeconds')
        return self


class ListPropagationPoliciesFailoverBehavior(TeaModel):
    def __init__(
        self,
        application: ListPropagationPoliciesApplicationFailoverBehavior = None,
    ):
        # {"en":"indicates failover behaviors in case of application failure", "zh_CN":"failover 重调度策略"}
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('application') is not None:
            temp_model = ListPropagationPoliciesApplicationFailoverBehavior()
            self.application = temp_model.from_map(m['application'])
        return self


class ListPropagationPoliciesPropagationSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[ListPropagationPoliciesResourceSelector] = None,
        association: bool = None,
        placement: ListPropagationPoliciesPlacement = None,
        dependent_overrides: List[str] = None,
        scheduler_name: str = None,
        failover: ListPropagationPoliciesFailoverBehavior = None,
    ):
        # {"en":"resource that this propagation policy applies to", "zh_CN":"策略应用的资源"}
        self.resource_selectors = resource_selectors
        # {"en":"association", "zh_CN":"association"}
        self.association = association
        # {"en":"scheduling strategy", "zh_CN":"调度策略"}
        self.placement = placement
        # {"en":"dependent overrides", "zh_CN":"依赖的覆盖策略"}
        self.dependent_overrides = dependent_overrides
        # {"en":"name of scheduler", "zh_CN":"调度器名称"}
        self.scheduler_name = scheduler_name
        # {"en":"indicates how Karmada migrates applications in case of failures", "zh_CN":"failover 重调度策略"}
        self.failover = failover

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.placement:
            self.placement.validate()
        if self.failover:
            self.failover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.association is not None:
            result['association'] = self.association
        if self.placement is not None:
            result['placement'] = self.placement.to_map()
        if self.dependent_overrides is not None:
            result['dependentOverrides'] = self.dependent_overrides
        if self.scheduler_name is not None:
            result['schedulerName'] = self.scheduler_name
        if self.failover is not None:
            result['failover'] = self.failover.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = ListPropagationPoliciesResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('association') is not None:
            self.association = m.get('association')
        if m.get('placement') is not None:
            temp_model = ListPropagationPoliciesPlacement()
            self.placement = temp_model.from_map(m['placement'])
        if m.get('dependentOverrides') is not None:
            self.dependent_overrides = m.get('dependentOverrides')
        if m.get('schedulerName') is not None:
            self.scheduler_name = m.get('schedulerName')
        if m.get('failover') is not None:
            temp_model = ListPropagationPoliciesFailoverBehavior()
            self.failover = temp_model.from_map(m['failover'])
        return self


class ListPropagationPoliciesPropagationPolicy(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: ListPropagationPoliciesObjectMeta = None,
        spec: ListPropagationPoliciesPropagationSpec = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a ListPropagationPoliciesPropagationPolicy", "zh_CN":"spec 定义 ListPropagationPoliciesPropagationPolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

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
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = ListPropagationPoliciesObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = ListPropagationPoliciesPropagationSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class ListPropagationPoliciesPropagationPolicyList(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: ListPropagationPoliciesListMeta = None,
        items: List[ListPropagationPoliciesPropagationPolicy] = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard list metadata", "zh_CN":"标准列表元数据"}
        self.metadata = metadata
        # {"en":"List of ListPropagationPoliciesPropagationPolicy", "zh_CN":"ListPropagationPoliciesPropagationPolicy 列表"}
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
            temp_model = ListPropagationPoliciesListMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListPropagationPoliciesPropagationPolicy()
                self.items.append(temp_model.from_map(k))
        return self


class ListPropagationPoliciesResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListPropagationPoliciesPropagationPolicyList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"propagationPolicy list", "zh_CN":"propagationPolicy 列表"}
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
            temp_model = ListPropagationPoliciesPropagationPolicyList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListPropagationPoliciesPaths(TeaModel):
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


class ListPropagationPoliciesParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        label_selector: str = None,
    ):
        # {"en":"The name of deployment", "zh_CN":"deployment 名称"}
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


class ListPropagationPoliciesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListPropagationPoliciesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetOverridepolicyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOverridepolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: dict = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"GetOverridepolicyOverridePolicy", "zh_CN":"GetOverridepolicyOverridePolicy"}
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


class GetOverridepolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"The name of GetOverridepolicyOverridePolicy", "zh_CN":"GetOverridepolicyOverridePolicy 名称"}
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


class GetOverridepolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOverridepolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOverridepolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOverridepolicyOwnerReference(TeaModel):
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


class GetOverridepolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetOverridepolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: GetOverridepolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this GetOverridepolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'GetOverridepolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“GetOverridepolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"GetOverridepolicyFieldsV1 holds the first GetOverridepolicyJSON version format as described in the 'GetOverridepolicyFieldsV1' type", "zh_CN":"GetOverridepolicyFieldsV1 包含类型 “GetOverridepolicyFieldsV1” 中描述的第一个 GetOverridepolicyJSON 版本格式"}
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
            temp_model = GetOverridepolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class GetOverridepolicyObjectMeta(TeaModel):
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
        owner_references: List[GetOverridepolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[GetOverridepolicyManagedFieldsEntry] = None,
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
                temp_model = GetOverridepolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = GetOverridepolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class GetOverridepolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetOverridepolicyMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[GetOverridepolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = GetOverridepolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class GetOverridepolicyResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        namespace: str = None,
        name: str = None,
        label_selector: GetOverridepolicyMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = GetOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class GetOverridepolicyCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetOverridepolicyFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[GetOverridepolicyCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = GetOverridepolicyCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class GetOverridepolicyClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: GetOverridepolicyMetaV1LabelSelector = None,
        field_selector: GetOverridepolicyFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = GetOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = GetOverridepolicyFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class GetOverridepolicyJSON(TeaModel):
    def __init__(
        self,
        raw: List[bytes] = None,
    ):
        # {"en":"value", "zh_CN":"字段值"}
        self.raw = raw

    def validate(self):
        self.validate_required(self.raw, 'raw')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw is not None:
            result['raw'] = self.raw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('raw') is not None:
            self.raw = m.get('raw')
        return self


class GetOverridepolicyPlaintextOverrider(TeaModel):
    def __init__(
        self,
        path: str = None,
        operator: str = None,
        value: GetOverridepolicyJSON = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path
        # {"en":"type of operation on the target field", "zh_CN":"对目标字段操作类型"}
        self.operator = operator
        # {"en":"the value applied to the target field,when operator is remove, value must be empty", "zh_CN":"应用在目标字段的值，当 Operator 为 remove 时，此字段必须为空"}
        self.value = value

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.operator, 'operator')
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            temp_model = GetOverridepolicyJSON()
            self.value = temp_model.from_map(m['value'])
        return self


class GetOverridepolicyImagePredicate(TeaModel):
    def __init__(
        self,
        path: str = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path

    def validate(self):
        self.validate_required(self.path, 'path')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class GetOverridepolicyImageOverrider(TeaModel):
    def __init__(
        self,
        predicate: GetOverridepolicyImagePredicate = None,
        component: str = None,
        operator: str = None,
        value: str = None,
    ):
        # {"en":"The default is nil. If the resource is a Pod, ReplicaSet, Deployment, StatefulSet system detects the image automatically. If the resource object has multiple containers, all the images will be processed. If it is not empty, only matched mirrors are processed", "zh_CN":"默认为空,如果资源是Pod, ReplicaSet, Deployment, StatefulSet系统自动检测镜像，如果资源对象有多个容器，所有镜像都将被处理。如果不为空，则只处理匹配到的镜像"}
        self.predicate = predicate
        # {"en":"component of image: [registry/]repository[:tag]", "zh_CN":"假设镜像组成成分：[registry/]repository[:tag]"}
        self.component = component
        # {"en":"type of operation on the image", "zh_CN":"对镜像进行的操作"}
        self.operator = operator
        # {"en":"value could not be empty when operator is add or replace. Default is empty. ignored when operator is remove", "zh_CN":"当 Operator 为 add 或 replace 时不能为空，默认为空，当 operator 为 remove 时忽略"}
        self.value = value

    def validate(self):
        if self.predicate:
            self.predicate.validate()
        self.validate_required(self.component, 'component')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predicate is not None:
            result['predicate'] = self.predicate.to_map()
        if self.component is not None:
            result['component'] = self.component
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('predicate') is not None:
            temp_model = GetOverridepolicyImagePredicate()
            self.predicate = temp_model.from_map(m['predicate'])
        if m.get('component') is not None:
            self.component = m.get('component')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetOverridepolicyCommandArgsOverrider(TeaModel):
    def __init__(
        self,
        container_name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # {"en":"name of container", "zh_CN":"容器名"}
        self.container_name = container_name
        # {"en":"operation to be applied to command/args", "zh_CN":"应用在commad/args上的操作"}
        self.operator = operator
        # {"en":"The value applied to command/args is append to commad/args when operator is add. The value is removed from command/args when operator is remove. If the value is empty, command/args remains unchanged", "zh_CN":"应用在command/args上的值，当operator为add时该值append到commad/args，当operator为remove时，该值从command/args移除，如果该值为空command/args维持原状"}
        self.value = value

    def validate(self):
        self.validate_required(self.container_name, 'container_name')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['containerName'] = self.container_name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containerName') is not None:
            self.container_name = m.get('containerName')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetOverridepolicyOverriders(TeaModel):
    def __init__(
        self,
        plaintext: List[GetOverridepolicyPlaintextOverrider] = None,
        image_overrider: List[GetOverridepolicyImageOverrider] = None,
        command_overrider: List[GetOverridepolicyCommandArgsOverrider] = None,
        args_overrider: List[GetOverridepolicyCommandArgsOverrider] = None,
    ):
        # {"en":"a general-purpose tool to override any kind of resources", "zh_CN":"覆盖任何类型资源的通用工具"}
        self.plaintext = plaintext
        # {"en":"overrides images for workloads", "zh_CN":"覆盖负载的镜像"}
        self.image_overrider = image_overrider
        # {"en":"overrides commands for workloads", "zh_CN":"覆盖工作负载的命令"}
        self.command_overrider = command_overrider
        # {"en":"overrides args for workloads", "zh_CN":"覆盖工作负载参数"}
        self.args_overrider = args_overrider

    def validate(self):
        if self.plaintext:
            for k in self.plaintext:
                if k:
                    k.validate()
        if self.image_overrider:
            for k in self.image_overrider:
                if k:
                    k.validate()
        if self.command_overrider:
            for k in self.command_overrider:
                if k:
                    k.validate()
        if self.args_overrider:
            for k in self.args_overrider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plaintext is not None:
            result['plaintext'] = []
            for k in self.plaintext:
                result['plaintext'].append(k.to_map() if k else None)
        if self.image_overrider is not None:
            result['imageOverrider'] = []
            for k in self.image_overrider:
                result['imageOverrider'].append(k.to_map() if k else None)
        if self.command_overrider is not None:
            result['commandOverrider'] = []
            for k in self.command_overrider:
                result['commandOverrider'].append(k.to_map() if k else None)
        if self.args_overrider is not None:
            result['argsOverrider'] = []
            for k in self.args_overrider:
                result['argsOverrider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('plaintext') is not None:
            self.plaintext = []
            for k in m.get('plaintext'):
                temp_model = GetOverridepolicyPlaintextOverrider()
                self.plaintext.append(temp_model.from_map(k))
        if m.get('imageOverrider') is not None:
            self.image_overrider = []
            for k in m.get('imageOverrider'):
                temp_model = GetOverridepolicyImageOverrider()
                self.image_overrider.append(temp_model.from_map(k))
        if m.get('commandOverrider') is not None:
            self.command_overrider = []
            for k in m.get('commandOverrider'):
                temp_model = GetOverridepolicyCommandArgsOverrider()
                self.command_overrider.append(temp_model.from_map(k))
        if m.get('argsOverrider') is not None:
            self.args_overrider = []
            for k in m.get('argsOverrider'):
                temp_model = GetOverridepolicyCommandArgsOverrider()
                self.args_overrider.append(temp_model.from_map(k))
        return self


class GetOverridepolicyRuleWithCluster(TeaModel):
    def __init__(
        self,
        target_cluster: GetOverridepolicyClusterAffinity = None,
        overriders: GetOverridepolicyOverriders = None,
    ):
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"the override policy to be applied to resources", "zh_CN":"应用于资源的覆盖规则"}
        self.overriders = overriders

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()
        self.validate_required(self.overriders, 'overriders')
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['TargetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['GetOverridepolicyOverriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetCluster') is not None:
            temp_model = GetOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['TargetCluster'])
        if m.get('GetOverridepolicyOverriders') is not None:
            temp_model = GetOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['GetOverridepolicyOverriders'])
        return self


class GetOverridepolicyOverrideSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[GetOverridepolicyResourceSelector] = None,
        override_rules: List[GetOverridepolicyRuleWithCluster] = None,
        target_cluster: GetOverridepolicyClusterAffinity = None,
        overriders: GetOverridepolicyOverriders = None,
    ):
        # {"en":"restricts resource types that this override policy applies to. If you ignore this field it means matching all resources.", "zh_CN":"限制此覆盖策略应用的资源类型。如果忽略此字段，则表示匹配所有资源"}
        self.resource_selectors = resource_selectors
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.override_rules = override_rules
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"represents the override policy to be applied to resources", "zh_CN":"表示将应用于资源的覆盖规则，已弃用，请使用OverrideRules"}
        self.overriders = overriders

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.override_rules:
            for k in self.override_rules:
                if k:
                    k.validate()
        if self.target_cluster:
            self.target_cluster.validate()
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.override_rules is not None:
            result['overrideRules'] = []
            for k in self.override_rules:
                result['overrideRules'].append(k.to_map() if k else None)
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['overriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = GetOverridepolicyResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('overrideRules') is not None:
            self.override_rules = []
            for k in m.get('overrideRules'):
                temp_model = GetOverridepolicyRuleWithCluster()
                self.override_rules.append(temp_model.from_map(k))
        if m.get('targetCluster') is not None:
            temp_model = GetOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('overriders') is not None:
            temp_model = GetOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['overriders'])
        return self


class GetOverridepolicyOverridePolicy(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: GetOverridepolicyObjectMeta = None,
        spec: GetOverridepolicyOverrideSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a GetOverridepolicyOverridePolicy", "zh_CN":"spec 定义 GetOverridepolicyOverridePolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
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
            temp_model = GetOverridepolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = GetOverridepolicyOverrideSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self






class CreateOverridepolicyOwnerReference(TeaModel):
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


class CreateOverridepolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateOverridepolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: CreateOverridepolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this CreateOverridepolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'CreateOverridepolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“CreateOverridepolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"CreateOverridepolicyFieldsV1 holds the first CreateOverridepolicyJSON version format as described in the 'CreateOverridepolicyFieldsV1' type", "zh_CN":"CreateOverridepolicyFieldsV1 包含类型 “CreateOverridepolicyFieldsV1” 中描述的第一个 CreateOverridepolicyJSON 版本格式"}
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
            temp_model = CreateOverridepolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class CreateOverridepolicyObjectMeta(TeaModel):
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
        owner_references: List[CreateOverridepolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[CreateOverridepolicyManagedFieldsEntry] = None,
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
                temp_model = CreateOverridepolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = CreateOverridepolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class CreateOverridepolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateOverridepolicyMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[CreateOverridepolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = CreateOverridepolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class CreateOverridepolicyResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        namespace: str = None,
        name: str = None,
        label_selector: CreateOverridepolicyMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = CreateOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class CreateOverridepolicyCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateOverridepolicyFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[CreateOverridepolicyCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = CreateOverridepolicyCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class CreateOverridepolicyClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: CreateOverridepolicyMetaV1LabelSelector = None,
        field_selector: CreateOverridepolicyFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = CreateOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = CreateOverridepolicyFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class CreateOverridepolicyJSON(TeaModel):
    def __init__(
        self,
        raw: List[bytes] = None,
    ):
        # {"en":"value", "zh_CN":"字段值"}
        self.raw = raw

    def validate(self):
        self.validate_required(self.raw, 'raw')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw is not None:
            result['raw'] = self.raw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('raw') is not None:
            self.raw = m.get('raw')
        return self


class CreateOverridepolicyPlaintextOverrider(TeaModel):
    def __init__(
        self,
        path: str = None,
        operator: str = None,
        value: CreateOverridepolicyJSON = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path
        # {"en":"type of operation on the target field", "zh_CN":"对目标字段操作类型"}
        self.operator = operator
        # {"en":"the value applied to the target field,when operator is remove, value must be empty", "zh_CN":"应用在目标字段的值，当 Operator 为 remove 时，此字段必须为空"}
        self.value = value

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.operator, 'operator')
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            temp_model = CreateOverridepolicyJSON()
            self.value = temp_model.from_map(m['value'])
        return self


class CreateOverridepolicyImagePredicate(TeaModel):
    def __init__(
        self,
        path: str = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path

    def validate(self):
        self.validate_required(self.path, 'path')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class CreateOverridepolicyImageOverrider(TeaModel):
    def __init__(
        self,
        predicate: CreateOverridepolicyImagePredicate = None,
        component: str = None,
        operator: str = None,
        value: str = None,
    ):
        # {"en":"The default is nil. If the resource is a Pod, ReplicaSet, Deployment, StatefulSet system detects the image automatically. If the resource object has multiple containers, all the images will be processed. If it is not empty, only matched mirrors are processed", "zh_CN":"默认为空,如果资源是Pod, ReplicaSet, Deployment, StatefulSet系统自动检测镜像，如果资源对象有多个容器，所有镜像都将被处理。如果不为空，则只处理匹配到的镜像"}
        self.predicate = predicate
        # {"en":"component of image: [registry/]repository[:tag]", "zh_CN":"假设镜像组成成分：[registry/]repository[:tag]"}
        self.component = component
        # {"en":"type of operation on the image", "zh_CN":"对镜像进行的操作"}
        self.operator = operator
        # {"en":"value could not be empty when operator is add or replace. Default is empty. ignored when operator is remove", "zh_CN":"当 Operator 为 add 或 replace 时不能为空，默认为空，当 operator 为 remove 时忽略"}
        self.value = value

    def validate(self):
        if self.predicate:
            self.predicate.validate()
        self.validate_required(self.component, 'component')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predicate is not None:
            result['predicate'] = self.predicate.to_map()
        if self.component is not None:
            result['component'] = self.component
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('predicate') is not None:
            temp_model = CreateOverridepolicyImagePredicate()
            self.predicate = temp_model.from_map(m['predicate'])
        if m.get('component') is not None:
            self.component = m.get('component')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateOverridepolicyCommandArgsOverrider(TeaModel):
    def __init__(
        self,
        container_name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # {"en":"name of container", "zh_CN":"容器名"}
        self.container_name = container_name
        # {"en":"operation to be applied to command/args", "zh_CN":"应用在commad/args上的操作"}
        self.operator = operator
        # {"en":"The value applied to command/args is append to commad/args when operator is add. The value is removed from command/args when operator is remove. If the value is empty, command/args remains unchanged", "zh_CN":"应用在command/args上的值，当operator为add时该值append到commad/args，当operator为remove时，该值从command/args移除，如果该值为空command/args维持原状"}
        self.value = value

    def validate(self):
        self.validate_required(self.container_name, 'container_name')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['containerName'] = self.container_name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containerName') is not None:
            self.container_name = m.get('containerName')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateOverridepolicyOverriders(TeaModel):
    def __init__(
        self,
        plaintext: List[CreateOverridepolicyPlaintextOverrider] = None,
        image_overrider: List[CreateOverridepolicyImageOverrider] = None,
        command_overrider: List[CreateOverridepolicyCommandArgsOverrider] = None,
        args_overrider: List[CreateOverridepolicyCommandArgsOverrider] = None,
    ):
        # {"en":"a general-purpose tool to override any kind of resources", "zh_CN":"覆盖任何类型资源的通用工具"}
        self.plaintext = plaintext
        # {"en":"overrides images for workloads", "zh_CN":"覆盖负载的镜像"}
        self.image_overrider = image_overrider
        # {"en":"overrides commands for workloads", "zh_CN":"覆盖工作负载的命令"}
        self.command_overrider = command_overrider
        # {"en":"overrides args for workloads", "zh_CN":"覆盖工作负载参数"}
        self.args_overrider = args_overrider

    def validate(self):
        if self.plaintext:
            for k in self.plaintext:
                if k:
                    k.validate()
        if self.image_overrider:
            for k in self.image_overrider:
                if k:
                    k.validate()
        if self.command_overrider:
            for k in self.command_overrider:
                if k:
                    k.validate()
        if self.args_overrider:
            for k in self.args_overrider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plaintext is not None:
            result['plaintext'] = []
            for k in self.plaintext:
                result['plaintext'].append(k.to_map() if k else None)
        if self.image_overrider is not None:
            result['imageOverrider'] = []
            for k in self.image_overrider:
                result['imageOverrider'].append(k.to_map() if k else None)
        if self.command_overrider is not None:
            result['commandOverrider'] = []
            for k in self.command_overrider:
                result['commandOverrider'].append(k.to_map() if k else None)
        if self.args_overrider is not None:
            result['argsOverrider'] = []
            for k in self.args_overrider:
                result['argsOverrider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('plaintext') is not None:
            self.plaintext = []
            for k in m.get('plaintext'):
                temp_model = CreateOverridepolicyPlaintextOverrider()
                self.plaintext.append(temp_model.from_map(k))
        if m.get('imageOverrider') is not None:
            self.image_overrider = []
            for k in m.get('imageOverrider'):
                temp_model = CreateOverridepolicyImageOverrider()
                self.image_overrider.append(temp_model.from_map(k))
        if m.get('commandOverrider') is not None:
            self.command_overrider = []
            for k in m.get('commandOverrider'):
                temp_model = CreateOverridepolicyCommandArgsOverrider()
                self.command_overrider.append(temp_model.from_map(k))
        if m.get('argsOverrider') is not None:
            self.args_overrider = []
            for k in m.get('argsOverrider'):
                temp_model = CreateOverridepolicyCommandArgsOverrider()
                self.args_overrider.append(temp_model.from_map(k))
        return self


class CreateOverridepolicyRuleWithCluster(TeaModel):
    def __init__(
        self,
        target_cluster: CreateOverridepolicyClusterAffinity = None,
        overriders: CreateOverridepolicyOverriders = None,
    ):
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"the override policy to be applied to resources", "zh_CN":"应用于资源的覆盖规则"}
        self.overriders = overriders

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()
        self.validate_required(self.overriders, 'overriders')
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['TargetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['CreateOverridepolicyOverriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetCluster') is not None:
            temp_model = CreateOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['TargetCluster'])
        if m.get('CreateOverridepolicyOverriders') is not None:
            temp_model = CreateOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['CreateOverridepolicyOverriders'])
        return self


class CreateOverridepolicyOverrideSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[CreateOverridepolicyResourceSelector] = None,
        override_rules: List[CreateOverridepolicyRuleWithCluster] = None,
        target_cluster: CreateOverridepolicyClusterAffinity = None,
        overriders: CreateOverridepolicyOverriders = None,
    ):
        # {"en":"restricts resource types that this override policy applies to. If you ignore this field it means matching all resources.", "zh_CN":"限制此覆盖策略应用的资源类型。如果忽略此字段，则表示匹配所有资源"}
        self.resource_selectors = resource_selectors
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.override_rules = override_rules
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"represents the override policy to be applied to resources", "zh_CN":"表示将应用于资源的覆盖规则，已弃用，请使用OverrideRules"}
        self.overriders = overriders

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.override_rules:
            for k in self.override_rules:
                if k:
                    k.validate()
        if self.target_cluster:
            self.target_cluster.validate()
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.override_rules is not None:
            result['overrideRules'] = []
            for k in self.override_rules:
                result['overrideRules'].append(k.to_map() if k else None)
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['overriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = CreateOverridepolicyResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('overrideRules') is not None:
            self.override_rules = []
            for k in m.get('overrideRules'):
                temp_model = CreateOverridepolicyRuleWithCluster()
                self.override_rules.append(temp_model.from_map(k))
        if m.get('targetCluster') is not None:
            temp_model = CreateOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('overriders') is not None:
            temp_model = CreateOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['overriders'])
        return self


class CreateOverridepolicyRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateOverridepolicyObjectMeta = None,
        spec: CreateOverridepolicyOverrideSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a CreateOverridepolicyOverridePolicy", "zh_CN":"spec 定义 CreateOverridepolicyOverridePolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
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
            temp_model = CreateOverridepolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateOverridepolicyOverrideSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreateOverridepolicyOverridePolicy(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreateOverridepolicyObjectMeta = None,
        spec: CreateOverridepolicyOverrideSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a CreateOverridepolicyOverridePolicy", "zh_CN":"spec 定义 CreateOverridepolicyOverridePolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
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
            temp_model = CreateOverridepolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreateOverridepolicyOverrideSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreateOverridepolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreateOverridepolicyOverridePolicy = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"CreateOverridepolicyOverridePolicy", "zh_CN":"CreateOverridepolicyOverridePolicy"}
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
            temp_model = CreateOverridepolicyOverridePolicy()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateOverridepolicyPaths(TeaModel):
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


class CreateOverridepolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateOverridepolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateOverridepolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PutOverridepolicyOwnerReference(TeaModel):
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


class PutOverridepolicyFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutOverridepolicyManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: PutOverridepolicyFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this PutOverridepolicyManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'PutOverridepolicyFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“PutOverridepolicyFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"PutOverridepolicyFieldsV1 holds the first PutOverridepolicyJSON version format as described in the 'PutOverridepolicyFieldsV1' type", "zh_CN":"PutOverridepolicyFieldsV1 包含类型 “PutOverridepolicyFieldsV1” 中描述的第一个 PutOverridepolicyJSON 版本格式"}
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
            temp_model = PutOverridepolicyFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class PutOverridepolicyObjectMeta(TeaModel):
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
        owner_references: List[PutOverridepolicyOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[PutOverridepolicyManagedFieldsEntry] = None,
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
                temp_model = PutOverridepolicyOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = PutOverridepolicyManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class PutOverridepolicyLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class PutOverridepolicyMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[PutOverridepolicyLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = PutOverridepolicyLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class PutOverridepolicyResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        namespace: str = None,
        name: str = None,
        label_selector: PutOverridepolicyMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.kind is not None:
            result['kind'] = self.kind
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.name is not None:
            result['name'] = self.name
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = PutOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class PutOverridepolicyCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class PutOverridepolicyFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[PutOverridepolicyCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = PutOverridepolicyCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class PutOverridepolicyClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: PutOverridepolicyMetaV1LabelSelector = None,
        field_selector: PutOverridepolicyFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = PutOverridepolicyMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = PutOverridepolicyFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class PutOverridepolicyJSON(TeaModel):
    def __init__(
        self,
        raw: List[bytes] = None,
    ):
        # {"en":"value", "zh_CN":"字段值"}
        self.raw = raw

    def validate(self):
        self.validate_required(self.raw, 'raw')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw is not None:
            result['raw'] = self.raw
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('raw') is not None:
            self.raw = m.get('raw')
        return self


class PutOverridepolicyPlaintextOverrider(TeaModel):
    def __init__(
        self,
        path: str = None,
        operator: str = None,
        value: PutOverridepolicyJSON = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path
        # {"en":"type of operation on the target field", "zh_CN":"对目标字段操作类型"}
        self.operator = operator
        # {"en":"the value applied to the target field,when operator is remove, value must be empty", "zh_CN":"应用在目标字段的值，当 Operator 为 remove 时，此字段必须为空"}
        self.value = value

    def validate(self):
        self.validate_required(self.path, 'path')
        self.validate_required(self.operator, 'operator')
        if self.value:
            self.value.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            temp_model = PutOverridepolicyJSON()
            self.value = temp_model.from_map(m['value'])
        return self


class PutOverridepolicyImagePredicate(TeaModel):
    def __init__(
        self,
        path: str = None,
    ):
        # {"en":"path of the target field", "zh_CN":"目标字段的路径"}
        self.path = path

    def validate(self):
        self.validate_required(self.path, 'path')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.path is not None:
            result['path'] = self.path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('path') is not None:
            self.path = m.get('path')
        return self


class PutOverridepolicyImageOverrider(TeaModel):
    def __init__(
        self,
        predicate: PutOverridepolicyImagePredicate = None,
        component: str = None,
        operator: str = None,
        value: str = None,
    ):
        # {"en":"The default is nil. If the resource is a Pod, ReplicaSet, Deployment, StatefulSet system detects the image automatically. If the resource object has multiple containers, all the images will be processed. If it is not empty, only matched mirrors are processed", "zh_CN":"默认为空,如果资源是Pod, ReplicaSet, Deployment, StatefulSet系统自动检测镜像，如果资源对象有多个容器，所有镜像都将被处理。如果不为空，则只处理匹配到的镜像"}
        self.predicate = predicate
        # {"en":"component of image: [registry/]repository[:tag]", "zh_CN":"假设镜像组成成分：[registry/]repository[:tag]"}
        self.component = component
        # {"en":"type of operation on the image", "zh_CN":"对镜像进行的操作"}
        self.operator = operator
        # {"en":"value could not be empty when operator is add or replace. Default is empty. ignored when operator is remove", "zh_CN":"当 Operator 为 add 或 replace 时不能为空，默认为空，当 operator 为 remove 时忽略"}
        self.value = value

    def validate(self):
        if self.predicate:
            self.predicate.validate()
        self.validate_required(self.component, 'component')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.predicate is not None:
            result['predicate'] = self.predicate.to_map()
        if self.component is not None:
            result['component'] = self.component
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('predicate') is not None:
            temp_model = PutOverridepolicyImagePredicate()
            self.predicate = temp_model.from_map(m['predicate'])
        if m.get('component') is not None:
            self.component = m.get('component')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class PutOverridepolicyCommandArgsOverrider(TeaModel):
    def __init__(
        self,
        container_name: str = None,
        operator: str = None,
        value: List[str] = None,
    ):
        # {"en":"name of container", "zh_CN":"容器名"}
        self.container_name = container_name
        # {"en":"operation to be applied to command/args", "zh_CN":"应用在commad/args上的操作"}
        self.operator = operator
        # {"en":"The value applied to command/args is append to commad/args when operator is add. The value is removed from command/args when operator is remove. If the value is empty, command/args remains unchanged", "zh_CN":"应用在command/args上的值，当operator为add时该值append到commad/args，当operator为remove时，该值从command/args移除，如果该值为空command/args维持原状"}
        self.value = value

    def validate(self):
        self.validate_required(self.container_name, 'container_name')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.container_name is not None:
            result['containerName'] = self.container_name
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('containerName') is not None:
            self.container_name = m.get('containerName')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class PutOverridepolicyOverriders(TeaModel):
    def __init__(
        self,
        plaintext: List[PutOverridepolicyPlaintextOverrider] = None,
        image_overrider: List[PutOverridepolicyImageOverrider] = None,
        command_overrider: List[PutOverridepolicyCommandArgsOverrider] = None,
        args_overrider: List[PutOverridepolicyCommandArgsOverrider] = None,
    ):
        # {"en":"a general-purpose tool to override any kind of resources", "zh_CN":"覆盖任何类型资源的通用工具"}
        self.plaintext = plaintext
        # {"en":"overrides images for workloads", "zh_CN":"覆盖负载的镜像"}
        self.image_overrider = image_overrider
        # {"en":"overrides commands for workloads", "zh_CN":"覆盖工作负载的命令"}
        self.command_overrider = command_overrider
        # {"en":"overrides args for workloads", "zh_CN":"覆盖工作负载参数"}
        self.args_overrider = args_overrider

    def validate(self):
        if self.plaintext:
            for k in self.plaintext:
                if k:
                    k.validate()
        if self.image_overrider:
            for k in self.image_overrider:
                if k:
                    k.validate()
        if self.command_overrider:
            for k in self.command_overrider:
                if k:
                    k.validate()
        if self.args_overrider:
            for k in self.args_overrider:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plaintext is not None:
            result['plaintext'] = []
            for k in self.plaintext:
                result['plaintext'].append(k.to_map() if k else None)
        if self.image_overrider is not None:
            result['imageOverrider'] = []
            for k in self.image_overrider:
                result['imageOverrider'].append(k.to_map() if k else None)
        if self.command_overrider is not None:
            result['commandOverrider'] = []
            for k in self.command_overrider:
                result['commandOverrider'].append(k.to_map() if k else None)
        if self.args_overrider is not None:
            result['argsOverrider'] = []
            for k in self.args_overrider:
                result['argsOverrider'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('plaintext') is not None:
            self.plaintext = []
            for k in m.get('plaintext'):
                temp_model = PutOverridepolicyPlaintextOverrider()
                self.plaintext.append(temp_model.from_map(k))
        if m.get('imageOverrider') is not None:
            self.image_overrider = []
            for k in m.get('imageOverrider'):
                temp_model = PutOverridepolicyImageOverrider()
                self.image_overrider.append(temp_model.from_map(k))
        if m.get('commandOverrider') is not None:
            self.command_overrider = []
            for k in m.get('commandOverrider'):
                temp_model = PutOverridepolicyCommandArgsOverrider()
                self.command_overrider.append(temp_model.from_map(k))
        if m.get('argsOverrider') is not None:
            self.args_overrider = []
            for k in m.get('argsOverrider'):
                temp_model = PutOverridepolicyCommandArgsOverrider()
                self.args_overrider.append(temp_model.from_map(k))
        return self


class PutOverridepolicyRuleWithCluster(TeaModel):
    def __init__(
        self,
        target_cluster: PutOverridepolicyClusterAffinity = None,
        overriders: PutOverridepolicyOverriders = None,
    ):
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"the override policy to be applied to resources", "zh_CN":"应用于资源的覆盖规则"}
        self.overriders = overriders

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()
        self.validate_required(self.overriders, 'overriders')
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['TargetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['PutOverridepolicyOverriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetCluster') is not None:
            temp_model = PutOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['TargetCluster'])
        if m.get('PutOverridepolicyOverriders') is not None:
            temp_model = PutOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['PutOverridepolicyOverriders'])
        return self


class PutOverridepolicyOverrideSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[PutOverridepolicyResourceSelector] = None,
        override_rules: List[PutOverridepolicyRuleWithCluster] = None,
        target_cluster: PutOverridepolicyClusterAffinity = None,
        overriders: PutOverridepolicyOverriders = None,
    ):
        # {"en":"restricts resource types that this override policy applies to. If you ignore this field it means matching all resources.", "zh_CN":"限制此覆盖策略应用的资源类型。如果忽略此字段，则表示匹配所有资源"}
        self.resource_selectors = resource_selectors
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.override_rules = override_rules
        # {"en":"defines restrictions on the override policy that only applies to resources propagated to the matching clusters. If you ignore this field it means matching all clusters", "zh_CN":"定义了对此覆盖策略应用到成员集群的目标选择。如果忽略此字段，则表示匹配所有集群"}
        self.target_cluster = target_cluster
        # {"en":"represents the override policy to be applied to resources", "zh_CN":"表示将应用于资源的覆盖规则，已弃用，请使用OverrideRules"}
        self.overriders = overriders

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.override_rules:
            for k in self.override_rules:
                if k:
                    k.validate()
        if self.target_cluster:
            self.target_cluster.validate()
        if self.overriders:
            self.overriders.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.override_rules is not None:
            result['overrideRules'] = []
            for k in self.override_rules:
                result['overrideRules'].append(k.to_map() if k else None)
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.overriders is not None:
            result['overriders'] = self.overriders.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = PutOverridepolicyResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('overrideRules') is not None:
            self.override_rules = []
            for k in m.get('overrideRules'):
                temp_model = PutOverridepolicyRuleWithCluster()
                self.override_rules.append(temp_model.from_map(k))
        if m.get('targetCluster') is not None:
            temp_model = PutOverridepolicyClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('overriders') is not None:
            temp_model = PutOverridepolicyOverriders()
            self.overriders = temp_model.from_map(m['overriders'])
        return self


class PutOverridepolicyRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PutOverridepolicyObjectMeta = None,
        spec: PutOverridepolicyOverrideSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a PutOverridepolicyOverridePolicy", "zh_CN":"spec 定义 PutOverridepolicyOverridePolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
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
            temp_model = PutOverridepolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PutOverridepolicyOverrideSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class PutOverridepolicyResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: dict = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"PutOverridepolicyOverridePolicy", "zh_CN":"PutOverridepolicyOverridePolicy"}
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


class PutOverridepolicyPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"The name of PutOverridepolicyOverridePolicy", "zh_CN":"PutOverridepolicyOverridePolicy 名称"}
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


class PutOverridepolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutOverridepolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutOverridepolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutOverridepolicyOverridePolicy(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PutOverridepolicyObjectMeta = None,
        spec: PutOverridepolicyOverrideSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a PutOverridepolicyOverridePolicy", "zh_CN":"spec 定义 PutOverridepolicyOverridePolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
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
            temp_model = PutOverridepolicyObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PutOverridepolicyOverrideSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self






class ListHorizontalPodAutoscalerRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHorizontalPodAutoscalerListMeta(TeaModel):
    def __init__(
        self,
        self_link: str = None,
        resource_version: str = None,
        continue_: str = None,
        remaining_item_count: int = None,
    ):
        # {"en":"Deprecated: selfLink is a legacy read-only field that is no longer populated by the system", "zh_CN":"selfLink 表示此对象的 URL，由系统填充，只读。已弃用：selfLink 是一个遗留的只读字段，不再由系统填充"}
        self.self_link = self_link
        # {"en":"String that identifies the server's internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system", "zh_CN":"标识该对象的服务器内部版本的字符串，客户端可以用该字段来确定对象何时被更改。 该值对客户端是不透明的，并且应该原样传回给服务器。该值由系统填充，只读"}
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


class ListHorizontalPodAutoscalerOwnerReference(TeaModel):
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


class ListHorizontalPodAutoscalerFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHorizontalPodAutoscalerManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: ListHorizontalPodAutoscalerFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this ListHorizontalPodAutoscalerManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'ListHorizontalPodAutoscalerFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“ListHorizontalPodAutoscalerFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"ListHorizontalPodAutoscalerFieldsV1 holds the first JSON version format as described in the 'ListHorizontalPodAutoscalerFieldsV1' type", "zh_CN":"ListHorizontalPodAutoscalerFieldsV1 包含类型 “ListHorizontalPodAutoscalerFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = ListHorizontalPodAutoscalerFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class ListHorizontalPodAutoscalerObjectMeta(TeaModel):
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
        owner_references: List[ListHorizontalPodAutoscalerOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[ListHorizontalPodAutoscalerManagedFieldsEntry] = None,
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
                temp_model = ListHorizontalPodAutoscalerOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = ListHorizontalPodAutoscalerManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class ListHorizontalPodAutoscalerCrossVersionObjectReference(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the API version of the referent", "zh_CN":"被引用对象的 API 版本"}
        self.api_version = api_version
        # {"en":"the kind of the referent", "zh_CN":"被引用对象的类别"}
        self.kind = kind
        # {"en":"the name of the referent", "zh_CN":"被引用对象的名称"}
        self.name = name

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.name, 'name')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListHorizontalPodAutoscalerMetricTarget(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
        average_value: str = None,
        average_utilization: int = None,
    ):
        # {"en":"type represents whether the metric type is Utilization, Value, or AverageValue", "zh_CN":"type 表示指标类别是 Utilization、Value 或 AverageValue"}
        self.type = type
        # {"en":"the target value of the metric (as a quantity)", "zh_CN":"value 是指标的目标值（以数量形式给出）"}
        self.value = value
        # {"en":"the target value of the average of the metric across all relevant pods (as a quantity)", "zh_CN":"averageValue 是跨所有 Pod 得出的指标均值的目标值（以数量形式给出）"}
        self.average_value = average_value
        # {"en":"the target value of the average of the resource metric across all relevant pods, represented as a percentage of the requested value of the resource for the pods. Currently only valid for Resource metric source type", "zh_CN":"averageUtilization 是跨所有相关 Pod 得出的资源指标均值的目标值， 表示为 Pod 资源请求值的百分比。目前仅对 “Resource” 指标源类别有效"}
        self.average_utilization = average_utilization

    def validate(self):
        self.validate_required(self.type, 'type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.average_value is not None:
            result['averageValue'] = self.average_value
        if self.average_utilization is not None:
            result['averageUtilization'] = self.average_utilization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('averageValue') is not None:
            self.average_value = m.get('averageValue')
        if m.get('averageUtilization') is not None:
            self.average_utilization = m.get('averageUtilization')
        return self


class ListHorizontalPodAutoscalerLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"the label key that the selector applies to", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist", "zh_CN":"表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListHorizontalPodAutoscalerLabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[ListHorizontalPodAutoscalerLabelSelectorRequirement] = None,
    ):
        # {"en":"a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is 'key', the operator is 'In', and the values array contains only 'value'. The requirements are ANDed", "zh_CN":"matchLabels 是 {key,value} 键值对的映射。matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。所表达的需求最终要按逻辑与的关系组合"}
        self.match_labels = match_labels
        # {"en":"a list of label selector requirements. The requirements are ANDed", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = ListHorizontalPodAutoscalerLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class ListHorizontalPodAutoscalerMetricIdentifier(TeaModel):
    def __init__(
        self,
        name: str = None,
        selector: ListHorizontalPodAutoscalerLabelSelector = None,
    ):
        # {"en":"the name of the given metric", "zh_CN":"给定指标的名称"}
        self.name = name
        # {"en":"the string-encoded form of a standard kubernetes label selector for the given metric When set, it is passed as an additional parameter to the metrics server for more specific metrics scoping. When unset, just the metricName will be used to gather metrics", "zh_CN":"给定指标的标准 Kubernetes 标签选择算符的字符串编码形式。 设置后，它作为附加参数传递给指标服务器，以获取更具体的指标范围。 未设置时，仅 metricName 参数将用于收集指标"}
        self.selector = selector

    def validate(self):
        self.validate_required(self.name, 'name')
        if self.selector:
            self.selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('selector') is not None:
            temp_model = ListHorizontalPodAutoscalerLabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        return self


class ListHorizontalPodAutoscalerObjectMetricSource(TeaModel):
    def __init__(
        self,
        described_object: ListHorizontalPodAutoscalerCrossVersionObjectReference = None,
        target: ListHorizontalPodAutoscalerMetricTarget = None,
        metric: ListHorizontalPodAutoscalerMetricIdentifier = None,
    ):
        # {"en":"describedObject specifies the descriptions of a object,such as kind,name apiVersion", "zh_CN":"describeObject 表示对象的描述，如对象的 kind、name、apiVersion"}
        self.described_object = described_object
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric

    def validate(self):
        self.validate_required(self.described_object, 'described_object')
        if self.described_object:
            self.described_object.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.described_object is not None:
            result['describedObject'] = self.described_object.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('describedObject') is not None:
            temp_model = ListHorizontalPodAutoscalerCrossVersionObjectReference()
            self.described_object = temp_model.from_map(m['describedObject'])
        if m.get('target') is not None:
            temp_model = ListHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('metric') is not None:
            temp_model = ListHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        return self


class ListHorizontalPodAutoscalerPodsMetricSource(TeaModel):
    def __init__(
        self,
        metric: ListHorizontalPodAutoscalerMetricIdentifier = None,
        target: ListHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 表示给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = ListHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = ListHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class ListHorizontalPodAutoscalerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: ListHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = ListHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class ListHorizontalPodAutoscalerContainerResourceMetricSource(TeaModel):
    def __init__(
        self,
        name: str = None,
        target: ListHorizontalPodAutoscalerMetricTarget = None,
        container: str = None,
    ):
        # {"en":"the name of the resource in question", "zh_CN":"相关资源的名称"}
        self.name = name
        # {"en":"specifies the target value for the given metric", "zh_CN":"指定给定指标的目标值"}
        self.target = target
        # {"en":"the name of the container in the pods of the scaling target", "zh_CN":"扩缩目标的 Pod 中容器的名称"}
        self.container = container

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()
        self.validate_required(self.container, 'container')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.container is not None:
            result['container'] = self.container
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('target') is not None:
            temp_model = ListHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('container') is not None:
            self.container = m.get('container')
        return self


class ListHorizontalPodAutoscalerExternalMetricSource(TeaModel):
    def __init__(
        self,
        metric: ListHorizontalPodAutoscalerMetricIdentifier = None,
        target: ListHorizontalPodAutoscalerMetricTarget = None,
    ):
        # {"en":"metric identifies the target metric by name and selector", "zh_CN":"metric 通过名称和选择算符识别目标指标"}
        self.metric = metric
        # {"en":"target specifies the target value for the given metric", "zh_CN":"target 指定给定指标的目标值"}
        self.target = target

    def validate(self):
        self.validate_required(self.metric, 'metric')
        if self.metric:
            self.metric.validate()
        self.validate_required(self.target, 'target')
        if self.target:
            self.target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.metric is not None:
            result['metric'] = self.metric.to_map()
        if self.target is not None:
            result['target'] = self.target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('metric') is not None:
            temp_model = ListHorizontalPodAutoscalerMetricIdentifier()
            self.metric = temp_model.from_map(m['metric'])
        if m.get('target') is not None:
            temp_model = ListHorizontalPodAutoscalerMetricTarget()
            self.target = temp_model.from_map(m['target'])
        return self


class ListHorizontalPodAutoscalerMetricSpec(TeaModel):
    def __init__(
        self,
        type: str = None,
        object: ListHorizontalPodAutoscalerObjectMetricSource = None,
        pods: ListHorizontalPodAutoscalerPodsMetricSource = None,
        resource: ListHorizontalPodAutoscalerResourceMetricSource = None,
        container_resource: ListHorizontalPodAutoscalerContainerResourceMetricSource = None,
        external: ListHorizontalPodAutoscalerExternalMetricSource = None,
    ):
        # {"en":"the type of metric source. It should be one of 'ContainerResource', 'External', 'Object', 'Pods' or 'Resource', each mapping to a matching field in the object. Note: 'ContainerResource' type is available on when the feature-gate HPAContainerMetrics is enabled", "zh_CN":"type 是指标源的类别。它取值是 “ContainerResource”、“External”、“Object”、“Pods” 或 “Resource” 之一， 每个类别映射到对象中的一个对应的字段。注意：“ContainerResource” 类别在特性门控 HPAContainerMetrics 启用时可用"}
        self.type = type
        # {"en":"refers to a metric describing a single kubernetes object (for example, hits-per-second on an Ingress object)", "zh_CN":"指描述单个 Kubernetes 对象的指标"}
        self.object = object
        # {"en":"refers to a metric describing each pod in the current scale target (for example, transactions-processed-per-second). The values will be averaged together before being compared to the target value", "zh_CN":"指描述当前扩缩目标中每个 Pod 的指标（例如，transactions-processed-per-second）。 在与目标值进行比较之前，这些指标值将被平均"}
        self.pods = pods
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing each pod in the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 此结构描述当前扩缩目标中的每个 Pod（例如 CPU 或内存）。此类指标内置于 Kubernetes 中， 并且在使用 “Pods” 源的、按 Pod 统计的普通指标之外支持一些特殊的扩缩选项"}
        self.resource = resource
        # {"en":"refers to a resource metric (such as those specified in requests and limits) known to Kubernetes describing a single container in each pod of the current scale target (e.g. CPU or memory). Such metrics are built in to Kubernetes, and have special scaling options on top of those available to normal per-pod metrics using the 'pods' source. This is an alpha feature and can be enabled by the HPAContainerMetrics feature flag", "zh_CN":"指 Kubernetes 已知的资源指标（例如在请求和限制中指定的那些）， 描述当前扩缩目标中每个 Pod 中的单个容器（例如 CPU 或内存）。 此类指标内置于 Kubernetes 中，在使用 “pods” 源的、按 Pod 计算的普通指标之外，还具有一些特殊的扩缩选项。 这是一个 Alpha 特性，可以通过 HPAContainerMetrics 特性标志启用"}
        self.container_resource = container_resource
        # {"en":"refers to a global metric that is not associated with any Kubernetes object. It allows autoscaling based on information coming from components running outside of cluster (for example length of queue in cloud messaging service, or QPS from loadbalancer running outside of cluster)", "zh_CN":"指的是不与任何 Kubernetes 对象关联的全局指标。 这一字段允许基于来自集群外部运行的组件（例如云消息服务中的队列长度，或来自运行在集群外部的负载均衡器的 QPS）的信息进行自动扩缩容"}
        self.external = external

    def validate(self):
        self.validate_required(self.type, 'type')
        if self.object:
            self.object.validate()
        if self.pods:
            self.pods.validate()
        if self.resource:
            self.resource.validate()
        if self.container_resource:
            self.container_resource.validate()
        if self.external:
            self.external.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.object is not None:
            result['object'] = self.object.to_map()
        if self.pods is not None:
            result['pods'] = self.pods.to_map()
        if self.resource is not None:
            result['resource'] = self.resource.to_map()
        if self.container_resource is not None:
            result['containerResource'] = self.container_resource.to_map()
        if self.external is not None:
            result['external'] = self.external.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('object') is not None:
            temp_model = ListHorizontalPodAutoscalerObjectMetricSource()
            self.object = temp_model.from_map(m['object'])
        if m.get('pods') is not None:
            temp_model = ListHorizontalPodAutoscalerPodsMetricSource()
            self.pods = temp_model.from_map(m['pods'])
        if m.get('resource') is not None:
            temp_model = ListHorizontalPodAutoscalerResourceMetricSource()
            self.resource = temp_model.from_map(m['resource'])
        if m.get('containerResource') is not None:
            temp_model = ListHorizontalPodAutoscalerContainerResourceMetricSource()
            self.container_resource = temp_model.from_map(m['containerResource'])
        if m.get('external') is not None:
            temp_model = ListHorizontalPodAutoscalerExternalMetricSource()
            self.external = temp_model.from_map(m['external'])
        return self


class ListHorizontalPodAutoscalerHPAScalingPolicy(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
        period_seconds: int = None,
    ):
        # {"en":"type is used to specify the scaling policy", "zh_CN":"type 用于指定扩缩策略"}
        self.type = type
        # {"en":"value contains the amount of change which is permitted by the policy. It must be greater than zero", "zh_CN":"value 包含策略允许的更改量。它必须大于零"}
        self.value = value
        # {"en":"periodSeconds specifies the window of time for which the policy should hold true. PeriodSeconds must be greater than zero and less than or equal to 1800 (30 min)", "zh_CN":"periodSeconds 表示策略应该保持为 true 的时间窗口长度。 periodSeconds 必须大于零且小于或等于 1800（30 分钟）"}
        self.period_seconds = period_seconds

    def validate(self):
        self.validate_required(self.value, 'value')
        self.validate_required(self.period_seconds, 'period_seconds')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.period_seconds is not None:
            result['periodSeconds'] = self.period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('periodSeconds') is not None:
            self.period_seconds = m.get('periodSeconds')
        return self


class ListHorizontalPodAutoscalerHPAScalingRules(TeaModel):
    def __init__(
        self,
        stabilization_window_seconds: int = None,
        select_policy: str = None,
        policies: List[ListHorizontalPodAutoscalerHPAScalingPolicy] = None,
    ):
        # {"en":"stabilizationWindowSeconds is the number of seconds for which past recommendations should be considered while scaling up or scaling down. StabilizationWindowSeconds must be greater than or equal to zero and less than or equal to 3600 (one hour). If not set, use the default values: - For scale up: 0 (i.e. no stabilization is done). - For scale down: 300 (i.e. the stabilization window is 300 seconds long)", "zh_CN":"stabilizationWindowSeconds 是在扩缩容时应考虑的之前建议的秒数。stabilizationWindowSeconds 必须大于或等于零且小于或等于 3600（一小时）。如果未设置，则使用默认值：扩容：0（不设置稳定窗口）。缩容：300（即稳定窗口为 300 秒）"}
        self.stabilization_window_seconds = stabilization_window_seconds
        # {"en":"selectPolicy is used to specify which policy should be used. If not set, the default value Max is used", "zh_CN":"selectPolicy 用于指定应该使用哪个策略。如果未设置，则使用默认值 Max"}
        self.select_policy = select_policy
        # {"en":"policies is a list of potential scaling polices which can be used during scaling. At least one policy must be specified, otherwise the ListHorizontalPodAutoscalerHPAScalingRules will be discarded as invalid", "zh_CN":"policies 是可在扩缩容过程中使用的潜在扩缩策略的列表。必须至少指定一个策略，否则 ListHorizontalPodAutoscalerHPAScalingRules 将被视为无效而丢弃"}
        self.policies = policies

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.stabilization_window_seconds is not None:
            result['stabilizationWindowSeconds'] = self.stabilization_window_seconds
        if self.select_policy is not None:
            result['selectPolicy'] = self.select_policy
        if self.policies is not None:
            result['policies'] = []
            for k in self.policies:
                result['policies'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('stabilizationWindowSeconds') is not None:
            self.stabilization_window_seconds = m.get('stabilizationWindowSeconds')
        if m.get('selectPolicy') is not None:
            self.select_policy = m.get('selectPolicy')
        if m.get('policies') is not None:
            self.policies = []
            for k in m.get('policies'):
                temp_model = ListHorizontalPodAutoscalerHPAScalingPolicy()
                self.policies.append(temp_model.from_map(k))
        return self


class ListHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior(TeaModel):
    def __init__(
        self,
        scale_up: ListHorizontalPodAutoscalerHPAScalingRules = None,
        scale_down: ListHorizontalPodAutoscalerHPAScalingRules = None,
    ):
        # {"en":"scaleUp is scaling policy for scaling Up. If not set, the default value is the higher of:- increase no more than 4 pods per 60 seconds- double the number of pods per 60 seconds No stabilization is used", "zh_CN":"scaleUp 是用于扩容的扩缩策略。如果未设置，则默认值为以下值中的较高者：- 每 60 秒增加不超过 4 个 Pod- 每 60 秒 Pod 数量翻倍。不使用稳定窗口"}
        self.scale_up = scale_up
        # {"en":"scaleDown is scaling policy for scaling Down. If not set, the default value is to allow to scale down to minReplicas pods, with a 300 second stabilization window (i.e., the highest recommendation for the last 300sec is used)", "zh_CN":"scaleDown 是缩容策略。如果未设置，则默认值允许缩减到 minReplicas 数量的 Pod， 具有 300 秒的稳定窗口（使用最近 300 秒的最高推荐值）"}
        self.scale_down = scale_down

    def validate(self):
        if self.scale_up:
            self.scale_up.validate()
        if self.scale_down:
            self.scale_down.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_up is not None:
            result['scaleUp'] = self.scale_up.to_map()
        if self.scale_down is not None:
            result['scaleDown'] = self.scale_down.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleUp') is not None:
            temp_model = ListHorizontalPodAutoscalerHPAScalingRules()
            self.scale_up = temp_model.from_map(m['scaleUp'])
        if m.get('scaleDown') is not None:
            temp_model = ListHorizontalPodAutoscalerHPAScalingRules()
            self.scale_down = temp_model.from_map(m['scaleDown'])
        return self


class ListHorizontalPodAutoscalerHorizontalPodAutoscalerSpec(TeaModel):
    def __init__(
        self,
        scale_target_ref: ListHorizontalPodAutoscalerCrossVersionObjectReference = None,
        min_replicas: int = None,
        max_replicas: int = None,
        metrics: List[ListHorizontalPodAutoscalerMetricSpec] = None,
        behavior: ListHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior = None,
    ):
        # {"en":"reference to scaled resource; horizontal pod autoscaler will learn the current resource consumption and will set the desired number of pods by using its Scale subresource", "zh_CN":"对被扩缩资源的引用； 水平 Pod 自动缩放器将了解当前的资源消耗，并使用其 scale 子资源设置所需的 Pod 数量"}
        self.scale_target_ref = scale_target_ref
        # {"en":"the lower limit for the number of replicas to which the autoscaler can scale down. It defaults to 1 pod. minReplicas is allowed to be 0 if the alpha feature gate HPAScaleToZero is enabled and at least one Object or External metric is configured. Scaling is active as long as at least one metric value is available", "zh_CN":"自动缩放器可以缩减的副本数的下限。 它默认为 1 个 Pod。 如果启用了 alpha 特性门禁 HPAScaleToZero 并且配置了至少一个 Object 或 External 度量标准， 则 minReplicas 允许为 0。 只要至少有一个度量值可用，缩放就处于活动状态"}
        self.min_replicas = min_replicas
        # {"en":"the upper limit for the number of pods that can be set by the autoscaler; cannot be smaller than MinReplicas", "zh_CN":"自动扩缩器可以设置的 Pod 数量上限； 不能小于 minReplicas"}
        self.max_replicas = max_replicas
        # {"en":"metrics contains the specifications for which to use to calculate the desired replica count (the maximum replica count across all metrics will be used). The desired replica count is calculated multiplying the ratio between the target value and the current value by the current number of pods. Ergo, metrics used must decrease as the pod count is increased, and vice-versa. See the individual metric source types for more information about how each type of metric must respond. If not set, the default metric will be set to 80% average CPU utilization", "zh_CN":"metrics 包含用于计算预期副本数的规约（将使用所有指标的最大副本数）。 预期副本数是通过将目标值与当前值之间的比率乘以当前 Pod 数来计算的。 因此，使用的指标必须随着 Pod 数量的增加而减少，反之亦然。 有关每种类别的指标必须如何响应的更多信息，请参阅各个指标源类别。 如果未设置，默认指标将设置为 80% 的平均 CPU 利用率"}
        self.metrics = metrics
        # {"en":"behavior configures the scaling behavior of the target in both Up and Down directions (scaleUp and scaleDown fields respectively). If not set, the default ListHorizontalPodAutoscalerHPAScalingRules for scale up and scale down are used", "zh_CN":"behavior 配置目标在扩容（Up）和缩容（Down）两个方向的扩缩行为（分别用 scaleUp 和 scaleDown 字段）。 如果未设置，则会使用默认的 ListHorizontalPodAutoscalerHPAScalingRules 进行扩缩容"}
        self.behavior = behavior

    def validate(self):
        self.validate_required(self.scale_target_ref, 'scale_target_ref')
        if self.scale_target_ref:
            self.scale_target_ref.validate()
        self.validate_required(self.max_replicas, 'max_replicas')
        if self.metrics:
            for k in self.metrics:
                if k:
                    k.validate()
        if self.behavior:
            self.behavior.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scale_target_ref is not None:
            result['scaleTargetRef'] = self.scale_target_ref.to_map()
        if self.min_replicas is not None:
            result['minReplicas'] = self.min_replicas
        if self.max_replicas is not None:
            result['maxReplicas'] = self.max_replicas
        if self.metrics is not None:
            result['metrics'] = []
            for k in self.metrics:
                result['metrics'].append(k.to_map() if k else None)
        if self.behavior is not None:
            result['behavior'] = self.behavior.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scaleTargetRef') is not None:
            temp_model = ListHorizontalPodAutoscalerCrossVersionObjectReference()
            self.scale_target_ref = temp_model.from_map(m['scaleTargetRef'])
        if m.get('minReplicas') is not None:
            self.min_replicas = m.get('minReplicas')
        if m.get('maxReplicas') is not None:
            self.max_replicas = m.get('maxReplicas')
        if m.get('metrics') is not None:
            self.metrics = []
            for k in m.get('metrics'):
                temp_model = ListHorizontalPodAutoscalerMetricSpec()
                self.metrics.append(temp_model.from_map(k))
        if m.get('behavior') is not None:
            temp_model = ListHorizontalPodAutoscalerHorizontalPodAutoscalerBehavior()
            self.behavior = temp_model.from_map(m['behavior'])
        return self


class ListHorizontalPodAutoscalerHorizontalPodAutoscalerStatus(TeaModel):
    def __init__(
        self,
        observed_generation: int = None,
        current_replicas: int = None,
        desired_replicas: int = None,
    ):
        # {"en":"the most recent generation observed by this autoscaler", "zh_CN":"observedGeneration 是此自动缩放器观察到的最新一代"}
        self.observed_generation = observed_generation
        # {"en":"the current number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 的当前副本数"}
        self.current_replicas = current_replicas
        # {"en":"the desired number of replicas of pods managed by this autoscaler", "zh_CN":"此自动缩放器管理的 Pod 副本的所需数量"}
        self.desired_replicas = desired_replicas

    def validate(self):
        self.validate_required(self.current_replicas, 'current_replicas')
        self.validate_required(self.desired_replicas, 'desired_replicas')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.observed_generation is not None:
            result['observedGeneration'] = self.observed_generation
        if self.current_replicas is not None:
            result['currentReplicas'] = self.current_replicas
        if self.desired_replicas is not None:
            result['desiredReplicas'] = self.desired_replicas
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('observedGeneration') is not None:
            self.observed_generation = m.get('observedGeneration')
        if m.get('currentReplicas') is not None:
            self.current_replicas = m.get('currentReplicas')
        if m.get('desiredReplicas') is not None:
            self.desired_replicas = m.get('desiredReplicas')
        return self


class ListHorizontalPodAutoscalerHorizontalPodAutoscaler(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListHorizontalPodAutoscalerObjectMeta = None,
        spec: ListHorizontalPodAutoscalerHorizontalPodAutoscalerSpec = None,
        status: ListHorizontalPodAutoscalerHorizontalPodAutoscalerStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"spec defines the behaviour of autoscaler.", "zh_CN":"spec 定义自动缩放器的规约"}
        self.spec = spec
        # {"en":"the current information about the autoscaler", "zh_CN":"自动缩放器的当前信息"}
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
            temp_model = ListHorizontalPodAutoscalerObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = ListHorizontalPodAutoscalerHorizontalPodAutoscalerSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ListHorizontalPodAutoscalerHorizontalPodAutoscalerStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class ListHorizontalPodAutoscalerHorizontalPodAutoscalerList(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: ListHorizontalPodAutoscalerListMeta = None,
        items: List[ListHorizontalPodAutoscalerHorizontalPodAutoscaler] = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"metadata is the standard list metadata", "zh_CN":"metadata 是标准的列表元数据"}
        self.metadata = metadata
        # {"en":"the list of horizontal pod autoscaler objects", "zh_CN":"items 是水平 Pod 自动扩缩器对象的列表"}
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
            temp_model = ListHorizontalPodAutoscalerListMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListHorizontalPodAutoscalerHorizontalPodAutoscaler()
                self.items.append(temp_model.from_map(k))
        return self


class ListHorizontalPodAutoscalerResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListHorizontalPodAutoscalerHorizontalPodAutoscalerList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"ListHorizontalPodAutoscalerHorizontalPodAutoscaler", "zh_CN":"ListHorizontalPodAutoscalerHorizontalPodAutoscaler"}
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
            temp_model = ListHorizontalPodAutoscalerHorizontalPodAutoscalerList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListHorizontalPodAutoscalerPaths(TeaModel):
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


class ListHorizontalPodAutoscalerParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHorizontalPodAutoscalerRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListHorizontalPodAutoscalerResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreatePropagationPoliciesOwnerReference(TeaModel):
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


class CreatePropagationPoliciesFieldsV1(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePropagationPoliciesManagedFieldsEntry(TeaModel):
    def __init__(
        self,
        manager: str = None,
        operation: str = None,
        api_version: str = None,
        time: str = None,
        fields_type: str = None,
        fields_v1: CreatePropagationPoliciesFieldsV1 = None,
        subresource: str = None,
    ):
        # {"en":"an identifier of the workflow managing these fields", "zh_CN":"管理这些字段的工作流的标识符"}
        self.manager = manager
        # {"en":"the type of operation which lead to this CreatePropagationPoliciesManagedFieldsEntry being created. The only valid values for this field are 'Apply' and 'Update'", "zh_CN":"导致创建此 managedFields 表项的操作类型。 此字段的仅有合法值是 “Apply” 和 “Update”"}
        self.operation = operation
        # {"en":"defines the version of this resource that this field set applies to. The format is \"group\/version\" just like the top-level APIVersion field. It is necessary to track the version of a field set because it cannot be automatically converted", "zh_CN":"定义此字段集适用的资源的版本。 格式是 “group\/version”，就像顶级 apiVersion 字段一样。 必须跟踪字段集的版本，因为它不能自动转换"}
        self.api_version = api_version
        # {"en":"the timestamp of when the ManagedFields entry was added", "zh_CN":"添加 managedFields 条目时的时间戳"}
        self.time = time
        # {"en":"the discriminator for the different fields format and version. There is currently only one possible value: 'CreatePropagationPoliciesFieldsV1'", "zh_CN":"不同字段格式和版本的鉴别器。 目前只有一个可能的值：“CreatePropagationPoliciesFieldsV1”"}
        self.fields_type = fields_type
        # {"en":"CreatePropagationPoliciesFieldsV1 holds the first JSON version format as described in the 'CreatePropagationPoliciesFieldsV1' type", "zh_CN":"CreatePropagationPoliciesFieldsV1 包含类型 “CreatePropagationPoliciesFieldsV1” 中描述的第一个 JSON 版本格式"}
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
            temp_model = CreatePropagationPoliciesFieldsV1()
            self.fields_v1 = temp_model.from_map(m['fieldsV1'])
        if m.get('subresource') is not None:
            self.subresource = m.get('subresource')
        return self


class CreatePropagationPoliciesObjectMeta(TeaModel):
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
        owner_references: List[CreatePropagationPoliciesOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
        managed_fields: List[CreatePropagationPoliciesManagedFieldsEntry] = None,
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
                temp_model = CreatePropagationPoliciesOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('managedFields') is not None:
            self.managed_fields = []
            for k in m.get('managedFields'):
                temp_model = CreatePropagationPoliciesManagedFieldsEntry()
                self.managed_fields.append(temp_model.from_map(k))
        return self


class CreatePropagationPoliciesLabelSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"key is the label key that the selector applies to.", "zh_CN":"选择器应用的标签键"}
        self.key = key
        # {"en":"operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.", "zh_CN":"operator 表示键与一组值的关系。有效的运算符包括 In、NotIn、Exists 和 DoesNotExist。"}
        self.operator = operator
        # {"en":"values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.", "zh_CN":"values 是一个字符串值数组。如果运算符为 In 或 NotIn，则 values 数组必须为非空。如果运算符是 Exists 或 DoesNotExist，则 values 数组必须为空。该数组在策略性合并补丁（Strategic Merge Patch）期间被替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreatePropagationPoliciesMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[CreatePropagationPoliciesLabelSelectorRequirement] = None,
    ):
        # {"en":"A map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is \"key\", the operator is \"In\", and the values array contains only \"value\". The requirements are ANDed.", "zh_CN":"matchLabels 映射中的单个 {key,value} 键值对相当于 matchExpressions 的一个元素，其键字段为 key，运算符为 In，values 数组仅包含 value。"}
        self.match_labels = match_labels
        # {"en":"A list of label selector requirements. The requirements are ANDed.", "zh_CN":"标签选择器要求的列表，这些要求的结果按逻辑与的关系来计算。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_labels is not None:
            result['matchLabels'] = self.match_labels
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchLabels') is not None:
            self.match_labels = m.get('matchLabels')
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = CreatePropagationPoliciesLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class CreatePropagationPoliciesResourceSelector(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        name: str = None,
        label_selector: CreatePropagationPoliciesMetaV1LabelSelector = None,
    ):
        # {"en":"represents the API version of the target resources", "zh_CN":"表示目标资源的API版本"}
        self.api_version = api_version
        # {"en":"represents the Kind of the target resources", "zh_CN":"表示目标资源的类型"}
        self.kind = kind
        # {"en":"name of the target resource", "zh_CN":"目标资源的名称"}
        self.name = name
        # {"en":"A label query over a set of resources", "zh_CN":"对一组资源的标签查询"}
        self.label_selector = label_selector

    def validate(self):
        self.validate_required(self.api_version, 'api_version')
        self.validate_required(self.kind, 'kind')
        if self.label_selector:
            self.label_selector.validate()

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
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('labelSelector') is not None:
            temp_model = CreatePropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        return self


class CreatePropagationPoliciesCoreV1NodeSelectorRequirement(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        values: List[str] = None,
    ):
        # {"en":"The label key that the selector applies to.", "zh_CN":"选择算符所适用的标签主键。"}
        self.key = key
        # {"en":"Represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. Gt, and Lt.", "zh_CN":"代表主键与值集之间的关系。合法的 operator 值包括 In、NotIn、Exists、DoesNotExist、Gt 和 Lt。"}
        self.operator = operator
        # {"en":"An array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. If the operator is Gt or Lt, the values array must have a single element, which will be interpreted as an integer. This array is replaced during a strategic merge patch.", "zh_CN":"一个由字符串值组成的数组。如果 operator 是 In 或 NotIn，则 values 数组不能为空。 如果 operator 为 Exists 或 DoesNotExist，则 values 数组只能为空。 如果 operator 为 Gt 或 Lt，则 values 数组只能包含一个元素，并且该元素会被解释为整数。 在执行策略性合并补丁操作时，此数组会被整体替换。"}
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreatePropagationPoliciesFieldSelector(TeaModel):
    def __init__(
        self,
        match_expressions: List[CreatePropagationPoliciesCoreV1NodeSelectorRequirement] = None,
    ):
        # {"en":"A list of node selector requirements by node's labels.", "zh_CN":"按节点标签列出的节点选择器需求列表。"}
        self.match_expressions = match_expressions

    def validate(self):
        if self.match_expressions:
            for k in self.match_expressions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_expressions is not None:
            result['matchExpressions'] = []
            for k in self.match_expressions:
                result['matchExpressions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('matchExpressions') is not None:
            self.match_expressions = []
            for k in m.get('matchExpressions'):
                temp_model = CreatePropagationPoliciesCoreV1NodeSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class CreatePropagationPoliciesClusterAffinity(TeaModel):
    def __init__(
        self,
        label_selector: CreatePropagationPoliciesMetaV1LabelSelector = None,
        field_selector: CreatePropagationPoliciesFieldSelector = None,
        cluster_names: List[str] = None,
        exclude: List[str] = None,
    ):
        # {"en":"a filter to select member clusters by labels", "zh_CN":"一个用来选中集群的标签过滤器"}
        self.label_selector = label_selector
        # {"en":"a filter to select member clusters by fields. Currently only three fields of provider(cluster.spec.provider), zone(cluster.spec.zone), and region(cluster.spec.region) are supported", "zh_CN":"一个用来选中集群的字段过滤器，目前支持的字段只有三个：提供商（cluster.spec.provider），区域（cluster.spec.zone），地区（cluster.spec.region）"}
        self.field_selector = field_selector
        # {"en":"the list of clusters to be selected", "zh_CN":"选中的集群列表"}
        self.cluster_names = cluster_names
        # {"en":"the list of clusters to be ignored", "zh_CN":"要忽略的集群列表"}
        self.exclude = exclude

    def validate(self):
        if self.label_selector:
            self.label_selector.validate()
        if self.field_selector:
            self.field_selector.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_selector is not None:
            result['labelSelector'] = self.label_selector.to_map()
        if self.field_selector is not None:
            result['fieldSelector'] = self.field_selector.to_map()
        if self.cluster_names is not None:
            result['clusterNames'] = self.cluster_names
        if self.exclude is not None:
            result['exclude'] = self.exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelSelector') is not None:
            temp_model = CreatePropagationPoliciesMetaV1LabelSelector()
            self.label_selector = temp_model.from_map(m['labelSelector'])
        if m.get('fieldSelector') is not None:
            temp_model = CreatePropagationPoliciesFieldSelector()
            self.field_selector = temp_model.from_map(m['fieldSelector'])
        if m.get('clusterNames') is not None:
            self.cluster_names = m.get('clusterNames')
        if m.get('exclude') is not None:
            self.exclude = m.get('exclude')
        return self


class CreatePropagationPoliciesToleration(TeaModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
        effect: str = None,
        toleration_seconds: int = None,
    ):
        # {"en":"The taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.", "zh_CN":"容忍度所适用的污点的键名。此字段为空意味着匹配所有的污点键。 如果 key 为空，则 operator 必须为 Exists；这种组合意味着匹配所有值和所有键。"}
        self.key = key
        # {"en":"Represents a key's relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.", "zh_CN":"表示 key 与 value 之间的关系。有效的 operator 取值是 Exists 和 Equal。默认为 Equal。 Exists 相当于 value 为某种通配符，因此 Pod 可以容忍特定类别的所有污点。"}
        self.operator = operator
        # {"en":"The taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.", "zh_CN":"容忍度所匹配的污点值。如果 operator 为 Exists，则此 value 值应该为空， 否则 value 值应该是一个正常的字符串。"}
        self.value = value
        # {"en":"Indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.", "zh_CN":"指示要匹配的污点效果。空值意味著匹配所有污点效果。如果要设置此字段，允许的值为 NoSchedule、PreferNoSchedule 和 NoExecute 之一。"}
        self.effect = effect
        # {"en":"Represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.", "zh_CN":" 表示容忍度（effect 必须是 NoExecute，否则此字段被忽略）容忍污点的时间长度。 默认情况下，此字段未被设置，这意味着会一直能够容忍对应污点（不会发生驱逐操作）。 零值和负值会被系统当做 0 值处理（立即触发驱逐）。"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.operator is not None:
            result['operator'] = self.operator
        if self.value is not None:
            result['value'] = self.value
        if self.effect is not None:
            result['effect'] = self.effect
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class CreatePropagationPoliciesSpreadConstraint(TeaModel):
    def __init__(
        self,
        spread_by_field: str = None,
        spread_by_label: str = None,
        max_groups: int = None,
        min_groups: int = None,
    ):
        # {"en":"The member clusters in the cluster federation are divided into multiple groups based on an attribute of the member cluster (currently, only cluster is supported, and the region, zone, and provider attributes may be supported in the future)", "zh_CN":"根据成员集群的某个属性（当前仅支持cluster、后续可能增加对成员集群region、zone、provider等属性支持）将集群联邦中的成员集群分为多个小组"}
        self.spread_by_field = spread_by_field
        # {"en":"The member cluster is divided into groups based on labels", "zh_CN":"根据label将成员集群分为多个小组"}
        self.spread_by_label = spread_by_label
        # {"en":"Maximum number of groups", "zh_CN":"最大分组数"}
        self.max_groups = max_groups
        # {"en":"Minimum number of groups", "zh_CN":"最小分组数"}
        self.min_groups = min_groups

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.spread_by_field is not None:
            result['spreadByField'] = self.spread_by_field
        if self.spread_by_label is not None:
            result['spreadByLabel'] = self.spread_by_label
        if self.max_groups is not None:
            result['maxGroups'] = self.max_groups
        if self.min_groups is not None:
            result['minGroups'] = self.min_groups
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spreadByField') is not None:
            self.spread_by_field = m.get('spreadByField')
        if m.get('spreadByLabel') is not None:
            self.spread_by_label = m.get('spreadByLabel')
        if m.get('maxGroups') is not None:
            self.max_groups = m.get('maxGroups')
        if m.get('minGroups') is not None:
            self.min_groups = m.get('minGroups')
        return self


class CreatePropagationPoliciesStaticClusterWeight(TeaModel):
    def __init__(
        self,
        target_cluster: CreatePropagationPoliciesClusterAffinity = None,
        weight: int = None,
    ):
        # {"en":"affected clusters by the weight", "zh_CN":"比重生效的目标集群"}
        self.target_cluster = target_cluster
        # {"en":"proportion of replicas in total", "zh_CN":"集群实例数占比"}
        self.weight = weight

    def validate(self):
        if self.target_cluster:
            self.target_cluster.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_cluster is not None:
            result['targetCluster'] = self.target_cluster.to_map()
        if self.weight is not None:
            result['weight'] = self.weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('targetCluster') is not None:
            temp_model = CreatePropagationPoliciesClusterAffinity()
            self.target_cluster = temp_model.from_map(m['targetCluster'])
        if m.get('weight') is not None:
            self.weight = m.get('weight')
        return self


class CreatePropagationPoliciesClusterPreferences(TeaModel):
    def __init__(
        self,
        static_weight_list: List[CreatePropagationPoliciesStaticClusterWeight] = None,
        dynamic_weight: str = None,
    ):
        # {"en":"static proportion of cluster replicas in total", "zh_CN":"集群副本数占比"}
        self.static_weight_list = static_weight_list
        # {"en":"dynamic proportion of replicas in total", "zh_CN":"动态比重"}
        self.dynamic_weight = dynamic_weight

    def validate(self):
        if self.static_weight_list:
            for k in self.static_weight_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.static_weight_list is not None:
            result['staticWeightList'] = []
            for k in self.static_weight_list:
                result['staticWeightList'].append(k.to_map() if k else None)
        if self.dynamic_weight is not None:
            result['dynamicWeight'] = self.dynamic_weight
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('staticWeightList') is not None:
            self.static_weight_list = []
            for k in m.get('staticWeightList'):
                temp_model = CreatePropagationPoliciesStaticClusterWeight()
                self.static_weight_list.append(temp_model.from_map(k))
        if m.get('dynamicWeight') is not None:
            self.dynamic_weight = m.get('dynamicWeight')
        return self


class CreatePropagationPoliciesReplicaSchedulingStrategy(TeaModel):
    def __init__(
        self,
        replica_scheduling_type: str = None,
        replica_division_preference: str = None,
        weight_preference: CreatePropagationPoliciesClusterPreferences = None,
    ):
        # {"en":"scheduling type of replicas", "zh_CN":"副本调度类型"}
        self.replica_scheduling_type = replica_scheduling_type
        # {"en":"division preference of replicas", "zh_CN":"副本数切分方式"}
        self.replica_division_preference = replica_division_preference
        # {"en":"weight preference", "zh_CN":"权重配置"}
        self.weight_preference = weight_preference

    def validate(self):
        if self.weight_preference:
            self.weight_preference.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.replica_scheduling_type is not None:
            result['replicaSchedulingType'] = self.replica_scheduling_type
        if self.replica_division_preference is not None:
            result['replicaDivisionPreference'] = self.replica_division_preference
        if self.weight_preference is not None:
            result['weightPreference'] = self.weight_preference.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('replicaSchedulingType') is not None:
            self.replica_scheduling_type = m.get('replicaSchedulingType')
        if m.get('replicaDivisionPreference') is not None:
            self.replica_division_preference = m.get('replicaDivisionPreference')
        if m.get('weightPreference') is not None:
            temp_model = CreatePropagationPoliciesClusterPreferences()
            self.weight_preference = temp_model.from_map(m['weightPreference'])
        return self


class CreatePropagationPoliciesPlacement(TeaModel):
    def __init__(
        self,
        cluster_affinity: CreatePropagationPoliciesClusterAffinity = None,
        cluster_tolerations: CreatePropagationPoliciesToleration = None,
        spread_constraints: List[CreatePropagationPoliciesSpreadConstraint] = None,
        replica_scheduling: CreatePropagationPoliciesReplicaSchedulingStrategy = None,
    ):
        # {"en":"the policy that only applies to resources propagated to the matching clusters", "zh_CN":"策略应用到成员集群的目标选择"}
        self.cluster_affinity = cluster_affinity
        # {"en":"toleration of cluster", "zh_CN":"集群容忍度"}
        self.cluster_tolerations = cluster_tolerations
        # {"en":"Cluster grouping constraint", "zh_CN":"根据约束对集群进行分组，把资源分散到多个小组"}
        self.spread_constraints = spread_constraints
        # {"en":"scheduling strategy of replicas", "zh_CN":"副本调度策略"}
        self.replica_scheduling = replica_scheduling

    def validate(self):
        if self.cluster_affinity:
            self.cluster_affinity.validate()
        if self.cluster_tolerations:
            self.cluster_tolerations.validate()
        if self.spread_constraints:
            for k in self.spread_constraints:
                if k:
                    k.validate()
        if self.replica_scheduling:
            self.replica_scheduling.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_affinity is not None:
            result['clusterAffinity'] = self.cluster_affinity.to_map()
        if self.cluster_tolerations is not None:
            result['clusterTolerations'] = self.cluster_tolerations.to_map()
        if self.spread_constraints is not None:
            result['spreadConstraints'] = []
            for k in self.spread_constraints:
                result['spreadConstraints'].append(k.to_map() if k else None)
        if self.replica_scheduling is not None:
            result['replicaScheduling'] = self.replica_scheduling.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterAffinity') is not None:
            temp_model = CreatePropagationPoliciesClusterAffinity()
            self.cluster_affinity = temp_model.from_map(m['clusterAffinity'])
        if m.get('clusterTolerations') is not None:
            temp_model = CreatePropagationPoliciesToleration()
            self.cluster_tolerations = temp_model.from_map(m['clusterTolerations'])
        if m.get('spreadConstraints') is not None:
            self.spread_constraints = []
            for k in m.get('spreadConstraints'):
                temp_model = CreatePropagationPoliciesSpreadConstraint()
                self.spread_constraints.append(temp_model.from_map(k))
        if m.get('replicaScheduling') is not None:
            temp_model = CreatePropagationPoliciesReplicaSchedulingStrategy()
            self.replica_scheduling = temp_model.from_map(m['replicaScheduling'])
        return self


class CreatePropagationPoliciesDecisionConditions(TeaModel):
    def __init__(
        self,
        toleration_seconds: int = None,
    ):
        # {"en":"represents the period of time Karmada should wait", "zh_CN":"应用经过多长时间后算失败"}
        self.toleration_seconds = toleration_seconds

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.toleration_seconds is not None:
            result['tolerationSeconds'] = self.toleration_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tolerationSeconds') is not None:
            self.toleration_seconds = m.get('tolerationSeconds')
        return self


class CreatePropagationPoliciesApplicationFailoverBehavior(TeaModel):
    def __init__(
        self,
        decision_conditions: CreatePropagationPoliciesDecisionConditions = None,
        purge_mode: str = None,
        grace_period_seconds: int = None,
    ):
        # {"en":"indicates the decision conditions of performing the failover process.", "zh_CN":"程序经过多长时间的失败,才属于不健康"}
        self.decision_conditions = decision_conditions
        # {"en":"represents how to deal with the legacy applications on the cluster from which the application is migrated. there are three options: Immediately,Graciously and Never. Graciously by defautl", "zh_CN":"应用在失败后的驱逐方式,有3个可填值: Immediately,Graciously and Never 默认:Graciously "}
        self.purge_mode = purge_mode
        # {"en":"the maximum waiting duration in seconds before application on the migrated cluster should be deleted.", "zh_CN":"平滑删除时间"}
        self.grace_period_seconds = grace_period_seconds

    def validate(self):
        if self.decision_conditions:
            self.decision_conditions.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decision_conditions is not None:
            result['decisionConditions'] = self.decision_conditions.to_map()
        if self.purge_mode is not None:
            result['purgeMode'] = self.purge_mode
        if self.grace_period_seconds is not None:
            result['gracePeriodSeconds'] = self.grace_period_seconds
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('decisionConditions') is not None:
            temp_model = CreatePropagationPoliciesDecisionConditions()
            self.decision_conditions = temp_model.from_map(m['decisionConditions'])
        if m.get('purgeMode') is not None:
            self.purge_mode = m.get('purgeMode')
        if m.get('gracePeriodSeconds') is not None:
            self.grace_period_seconds = m.get('gracePeriodSeconds')
        return self


class CreatePropagationPoliciesFailoverBehavior(TeaModel):
    def __init__(
        self,
        application: CreatePropagationPoliciesApplicationFailoverBehavior = None,
    ):
        # {"en":"indicates failover behaviors in case of application failure", "zh_CN":"failover 重调度策略"}
        self.application = application

    def validate(self):
        if self.application:
            self.application.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.application is not None:
            result['application'] = self.application.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('application') is not None:
            temp_model = CreatePropagationPoliciesApplicationFailoverBehavior()
            self.application = temp_model.from_map(m['application'])
        return self


class CreatePropagationPoliciesPropagationSpec(TeaModel):
    def __init__(
        self,
        resource_selectors: List[CreatePropagationPoliciesResourceSelector] = None,
        association: bool = None,
        placement: CreatePropagationPoliciesPlacement = None,
        dependent_overrides: List[str] = None,
        scheduler_name: str = None,
        failover: CreatePropagationPoliciesFailoverBehavior = None,
    ):
        # {"en":"resource that this propagation policy applies to", "zh_CN":"策略应用的资源"}
        self.resource_selectors = resource_selectors
        # {"en":"association", "zh_CN":"association"}
        self.association = association
        # {"en":"scheduling strategy", "zh_CN":"调度策略"}
        self.placement = placement
        # {"en":"dependent overrides", "zh_CN":"依赖的覆盖策略"}
        self.dependent_overrides = dependent_overrides
        # {"en":"name of scheduler", "zh_CN":"调度器名称"}
        self.scheduler_name = scheduler_name
        # {"en":"indicates how Karmada migrates applications in case of failures", "zh_CN":"failover 重调度策略"}
        self.failover = failover

    def validate(self):
        if self.resource_selectors:
            for k in self.resource_selectors:
                if k:
                    k.validate()
        if self.placement:
            self.placement.validate()
        if self.failover:
            self.failover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_selectors is not None:
            result['resourceSelectors'] = []
            for k in self.resource_selectors:
                result['resourceSelectors'].append(k.to_map() if k else None)
        if self.association is not None:
            result['association'] = self.association
        if self.placement is not None:
            result['placement'] = self.placement.to_map()
        if self.dependent_overrides is not None:
            result['dependentOverrides'] = self.dependent_overrides
        if self.scheduler_name is not None:
            result['schedulerName'] = self.scheduler_name
        if self.failover is not None:
            result['failover'] = self.failover.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceSelectors') is not None:
            self.resource_selectors = []
            for k in m.get('resourceSelectors'):
                temp_model = CreatePropagationPoliciesResourceSelector()
                self.resource_selectors.append(temp_model.from_map(k))
        if m.get('association') is not None:
            self.association = m.get('association')
        if m.get('placement') is not None:
            temp_model = CreatePropagationPoliciesPlacement()
            self.placement = temp_model.from_map(m['placement'])
        if m.get('dependentOverrides') is not None:
            self.dependent_overrides = m.get('dependentOverrides')
        if m.get('schedulerName') is not None:
            self.scheduler_name = m.get('schedulerName')
        if m.get('failover') is not None:
            temp_model = CreatePropagationPoliciesFailoverBehavior()
            self.failover = temp_model.from_map(m['failover'])
        return self


class CreatePropagationPoliciesRequest(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: CreatePropagationPoliciesObjectMeta = None,
        spec: CreatePropagationPoliciesPropagationSpec = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a CreatePropagationPoliciesPropagationPolicy", "zh_CN":"spec 定义 CreatePropagationPoliciesPropagationPolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

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
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = CreatePropagationPoliciesObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreatePropagationPoliciesPropagationSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreatePropagationPoliciesPropagationPolicy(TeaModel):
    def __init__(
        self,
        kind: str = None,
        api_version: str = None,
        metadata: CreatePropagationPoliciesObjectMeta = None,
        spec: CreatePropagationPoliciesPropagationSpec = None,
    ):
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"Standard object metadata.", "zh_CN":"标准的对象元数据。"}
        self.metadata = metadata
        # {"en":"Spec defines the behavior of a CreatePropagationPoliciesPropagationPolicy", "zh_CN":"spec 定义 CreatePropagationPoliciesPropagationPolicy 的行为"}
        self.spec = spec

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.api_version, 'api_version')
        if self.metadata:
            self.metadata.validate()
        self.validate_required(self.spec, 'spec')
        if self.spec:
            self.spec.validate()

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
        if self.spec is not None:
            result['spec'] = self.spec.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('metadata') is not None:
            temp_model = CreatePropagationPoliciesObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreatePropagationPoliciesPropagationSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreatePropagationPoliciesResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreatePropagationPoliciesPropagationPolicy = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"CreatePropagationPoliciesPropagationPolicy object", "zh_CN":"PropagationPolicy对象"}
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
            temp_model = CreatePropagationPoliciesPropagationPolicy()
            self.data = temp_model.from_map(m['data'])
        return self


class CreatePropagationPoliciesPaths(TeaModel):
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


class CreatePropagationPoliciesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePropagationPoliciesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePropagationPoliciesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




