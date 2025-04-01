# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class UpdatePvcsOwnerReference(TeaModel):
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


class UpdatePvcsObjectMeta(TeaModel):
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
        owner_references: List[UpdatePvcsOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
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

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
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
                temp_model = UpdatePvcsOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        return self


class UpdatePvcsLabelSelectorRequirement(TeaModel):
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


class UpdatePvcsMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[UpdatePvcsLabelSelectorRequirement] = None,
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
                temp_model = UpdatePvcsLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class UpdatePvcsResourceRequirements(TeaModel):
    def __init__(
        self,
        limits: Dict[str, str] = None,
        requests: Dict[str, str] = None,
    ):
        # {"en":"describes the maximum amount of compute resources allowed", "zh_CN":"描述所允许的最大计算资源用量"}
        self.limits = limits
        # {"en":"describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits", "zh_CN":"requests 描述所需的最小计算资源量。如果容器省略了 requests，但明确设定了 limits， 则 requests 默认值为 limits 值，否则为实现定义的值。请求不能超过限制"}
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['limits'] = self.limits
        if self.requests is not None:
            result['requests'] = self.requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limits') is not None:
            self.limits = m.get('limits')
        if m.get('requests') is not None:
            self.requests = m.get('requests')
        return self


class UpdatePvcsTypedLocalObjectReference(TeaModel):
    def __init__(
        self,
        api_group: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required", "zh_CN":"被引用资源的组。如果不指定 APIGroup，则指定的 Kind 必须在核心 API 组中。对于任何其它第三方类型，都需要 APIGroup"}
        self.api_group = api_group
        # {"en":" the type of resource being referenced", "zh_CN":"被引用的资源的类型"}
        self.kind = kind
        # {"en":"the name of resource being referenced", "zh_CN":"被引用的资源的名称"}
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_group is not None:
            result['apiGroup'] = self.api_group
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroup') is not None:
            self.api_group = m.get('apiGroup')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdatePvcsPersistentVolumeClaimSpec(TeaModel):
    def __init__(
        self,
        access_modes: List[str] = None,
        selector: UpdatePvcsMetaV1LabelSelector = None,
        resources: UpdatePvcsResourceRequirements = None,
        volume_name: str = None,
        storage_class_name: str = None,
        volume_mode: str = None,
        data_source: UpdatePvcsTypedLocalObjectReference = None,
    ):
        # {"en":"contains the desired access modes the volume should have", "zh_CN":"包含卷应具备的预期访问模式"}
        self.access_modes = access_modes
        # {"en":"a label query over volumes to consider for binding", "zh_CN":"在绑定时对卷进行选择所执行的标签查询"}
        self.selector = selector
        # {"en":"represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim", "zh_CN":"表示卷应拥有的最小资源。 如果启用了 RecoverVolumeExpansionFailure 功能特性，则允许用户指定这些资源要求， 此值必须低于之前的值，但必须高于申领的状态字段中记录的容量"}
        self.resources = resources
        # {"en":"the binding reference to the PersistentVolume backing this claim", "zh_CN":"对此申领所对应的 PersistentVolume 的绑定引用"}
        self.volume_name = volume_name
        # {"en":"the name of the StorageClass required by the claim", "zh_CN":"此申领所要求的 StorageClass 名称"}
        self.storage_class_name = storage_class_name
        # {"en":"defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec", "zh_CN":"定义申领需要哪种类别的卷。当申领规约中未包含此字段时，意味着取值为 Filesystem"}
        self.volume_mode = volume_mode
        # {"en":"dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (UpdatePvcsPersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource", "zh_CN":"dataSource 字段可用于二选一：- 现有的 VolumeSnapshot 对象（snapshot.storage.k8s.io/VolumeSnapshot）- 现有的 PVC (UpdatePvcsPersistentVolumeClaim)。如果制备器或外部控制器可以支持指定的数据源，则它将根据指定数据源的内容创建新的卷。 当 AnyVolumeDataSource 特性门控被启用时，dataSource 内容将被复制到 dataSourceRef， 当 dataSourceRef.namespace 未被指定时，dataSourceRef 内容将被复制到 dataSource。 如果名字空间被指定，则 dataSourceRef 不会被复制到 dataSource"}
        self.data_source = data_source

    def validate(self):
        if self.selector:
            self.selector.validate()
        if self.resources:
            self.resources.validate()
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        if self.resources is not None:
            result['resources'] = self.resources.to_map()
        if self.volume_name is not None:
            result['volumeName'] = self.volume_name
        if self.storage_class_name is not None:
            result['storageClassName'] = self.storage_class_name
        if self.volume_mode is not None:
            result['volumeMode'] = self.volume_mode
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('selector') is not None:
            temp_model = UpdatePvcsMetaV1LabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        if m.get('resources') is not None:
            temp_model = UpdatePvcsResourceRequirements()
            self.resources = temp_model.from_map(m['resources'])
        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')
        if m.get('storageClassName') is not None:
            self.storage_class_name = m.get('storageClassName')
        if m.get('volumeMode') is not None:
            self.volume_mode = m.get('volumeMode')
        if m.get('dataSource') is not None:
            temp_model = UpdatePvcsTypedLocalObjectReference()
            self.data_source = temp_model.from_map(m['dataSource'])
        return self


class UpdatePvcsRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdatePvcsObjectMeta = None,
        spec: UpdatePvcsPersistentVolumeClaimSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"defines the desired characteristics of a volume requested by a pod author", "zh_CN":"定义 Pod 作者所请求的卷的预期特征"}
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
            temp_model = UpdatePvcsObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdatePvcsPersistentVolumeClaimSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class UpdatePvcsPersistentVolumeClaimCondition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type, required", "zh_CN":"类型，必需"}
        self.type = type
        # {"en":"status, required", "zh_CN":"状态，必需"}
        self.status = status
        # {"en":"reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports 'ResizeStarted' that means the underlying persistent volume is being resized", "zh_CN":"reason 是唯一的，它应该是一个机器可理解的简短字符串，指明上次状况转换的原因。 如果它报告 “ResizeStarted”，则意味着正在调整底层持久卷的大小"}
        self.reason = reason
        # {"en":" the human-readable message indicating details about last transition", "zh_CN":"人类可读的消息，指示有关上一次转换的详细信息"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdatePvcsPersistentVolumeClaimStatus(TeaModel):
    def __init__(
        self,
        phase: str = None,
        access_modes: List[str] = None,
        capacity: Dict[str, int] = None,
        conditions: List[UpdatePvcsPersistentVolumeClaimCondition] = None,
    ):
        # {"en":"represents the current phase of UpdatePvcsPersistentVolumeClaim", "zh_CN":"表示 UpdatePvcsPersistentVolumeClaim 的当前阶段"}
        self.phase = phase
        # {"en":"contains the actual access modes the volume backing the PVC has", "zh_CN":"包含支持 PVC 的卷所具有的实际访问模式"}
        self.access_modes = access_modes
        # {"en":"represents the actual resources of the underlying volume", "zh_CN":"表示底层卷的实际资源"}
        self.capacity = capacity
        # {"en":"the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'", "zh_CN":"持久卷声明的当前的状况。 如果正在调整底层持久卷的大小，则状况将被设为 “ResizeStarted”"}
        self.conditions = conditions

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = UpdatePvcsPersistentVolumeClaimCondition()
                self.conditions.append(temp_model.from_map(k))
        return self


class UpdatePvcsPersistentVolumeClaim(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: UpdatePvcsObjectMeta = None,
        spec: UpdatePvcsPersistentVolumeClaimSpec = None,
        status: UpdatePvcsPersistentVolumeClaimStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"defines the desired characteristics of a volume requested by a pod author", "zh_CN":"定义 Pod 作者所请求的卷的预期特征"}
        self.spec = spec
        # {"en":"represents the current information/status of a persistent volume claim. Read-only", "zh_CN":"表示一个持久卷申领的当前信息/状态。只读"}
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
            temp_model = UpdatePvcsObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = UpdatePvcsPersistentVolumeClaimSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = UpdatePvcsPersistentVolumeClaimStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class UpdatePvcsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: UpdatePvcsPersistentVolumeClaim = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"pvc", "zh_CN":"pvc"}
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
            temp_model = UpdatePvcsPersistentVolumeClaim()
            self.data = temp_model.from_map(m['data'])
        return self


class UpdatePvcsPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"deployment name", "zh_CN":"pvc 名称"}
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


class UpdatePvcsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdatePvcsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdatePvcsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListStorageClassRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListStorageClassScInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        name_cn: str = None,
    ):
        # {"en":"storageClass name", "zh_CN":"storageClass名称"}
        self.name = name
        # {"en":"storageClass cn name", "zh_CN":"storageClass中文名称"}
        self.name_cn = name_cn

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.name_cn, 'name_cn')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.name_cn is not None:
            result['nameCn'] = self.name_cn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameCn') is not None:
            self.name_cn = m.get('nameCn')
        return self


class ListStorageClassResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: List[ListStorageClassScInfo] = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"storageClass list", "zh_CN":"storageClass列表"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
            self.data = []
            for k in m.get('data'):
                temp_model = ListStorageClassScInfo()
                self.data.append(temp_model.from_map(k))
        return self


class ListStorageClassPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListStorageClassParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListStorageClassRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListStorageClassResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PagingPvcsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PagingPvcsCluster(TeaModel):
    def __init__(
        self,
        name: str = None,
        name_cn: str = None,
        status: str = None,
    ):
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.name = name
        # {"en":"cluster cn name", "zh_CN":"集群中文名称"}
        self.name_cn = name_cn
        # {"en":"pvc status", "zh_CN":"pvc在集群的状态"}
        self.status = status

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.name_cn, 'name_cn')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.name_cn is not None:
            result['nameCn'] = self.name_cn
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameCn') is not None:
            self.name_cn = m.get('nameCn')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class PagingPvcsWorkLoad(TeaModel):
    def __init__(
        self,
        kind: str = None,
        name: str = None,
        namespace: str = None,
    ):
        # {"en":"workload kind", "zh_CN":"负载类型"}
        self.kind = kind
        # {"en":"workload name", "zh_CN":"负载名称"}
        self.name = name
        # {"en":"workload namespace", "zh_CN":"负载命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.name, 'name')
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class PagingPvcsPvcInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        i_otype: str = None,
        clusters: List[PagingPvcsCluster] = None,
        work_loads: List[PagingPvcsWorkLoad] = None,
        create_time: int = None,
        storage: int = None,
        storage_class: str = None,
    ):
        # {"en":"pvcs name", "zh_CN":"pvc名称"}
        self.name = name
        # {"en":"namespace info", "zh_CN":"pvc namespace"}
        self.namespace = namespace
        # {"en":"pvc io type", "zh_CN":"pvc IO类型"}
        self.i_otype = i_otype
        # {"en":"pvc in every cluster info", "zh_CN":"pvc在各集群信息"}
        self.clusters = clusters
        # {"en":"pvc workload", "zh_CN":"pvc绑定的负载"}
        self.work_loads = work_loads
        # {"en":"createTime", "zh_CN":"pvc创建时间"}
        self.create_time = create_time
        # {"en":"pvc storage", "zh_CN":"pvc存储大小"}
        self.storage = storage
        # {"en":"pvc storageClass", "zh_CN":"pvc storageClass"}
        self.storage_class = storage_class

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.i_otype, 'i_otype')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()
        self.validate_required(self.work_loads, 'work_loads')
        if self.work_loads:
            for k in self.work_loads:
                if k:
                    k.validate()
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.storage, 'storage')
        self.validate_required(self.storage_class, 'storage_class')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.i_otype is not None:
            result['iOType'] = self.i_otype
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        if self.work_loads is not None:
            result['workLoads'] = []
            for k in self.work_loads:
                result['workLoads'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.storage is not None:
            result['storage'] = self.storage
        if self.storage_class is not None:
            result['storageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('iOType') is not None:
            self.i_otype = m.get('iOType')
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = PagingPvcsCluster()
                self.clusters.append(temp_model.from_map(k))
        if m.get('workLoads') is not None:
            self.work_loads = []
            for k in m.get('workLoads'):
                temp_model = PagingPvcsWorkLoad()
                self.work_loads.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        if m.get('storageClass') is not None:
            self.storage_class = m.get('storageClass')
        return self


class PagingPvcsPvcList(TeaModel):
    def __init__(
        self,
        items: List[PagingPvcsPvcInfo] = None,
        total: int = None,
    ):
        # {"en":"pvcs info", "zh_CN":"pvc信息"}
        self.items = items
        # {"en":"total size", "zh_CN":"总条数"}
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
                temp_model = PagingPvcsPvcInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class PagingPvcsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: PagingPvcsPvcList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"pvc list", "zh_CN":"pvc列表"}
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
            temp_model = PagingPvcsPvcList()
            self.data = temp_model.from_map(m['data'])
        return self


class PagingPvcsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PagingPvcsParameters(TeaModel):
    def __init__(
        self,
        storageclass: str = None,
        createbyedge: str = None,
    ):
        # {"en":"pvc storageclass", "zh_CN":"pvc storageclass，多个以逗号隔开"}
        self.storageclass = storageclass
        # {"en":"create by sts volumeClaimTemplates", "zh_CN":"是否由sts volumeClaimTemplates直接创建"}
        self.createbyedge = createbyedge

    def validate(self):
        self.validate_required(self.storageclass, 'storageclass')
        self.validate_required(self.createbyedge, 'createbyedge')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storageclass is not None:
            result['storageclass'] = self.storageclass
        if self.createbyedge is not None:
            result['createbyedge'] = self.createbyedge
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('storageclass') is not None:
            self.storageclass = m.get('storageclass')
        if m.get('createbyedge') is not None:
            self.createbyedge = m.get('createbyedge')
        return self


class PagingPvcsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PagingPvcsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PvcInNamespaceRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PvcInNamespaceCluster(TeaModel):
    def __init__(
        self,
        name: str = None,
        name_cn: str = None,
        status: str = None,
    ):
        # {"en":"cluster name", "zh_CN":"集群名称"}
        self.name = name
        # {"en":"cluster cn name", "zh_CN":"集群中文名称"}
        self.name_cn = name_cn
        # {"en":"pvc status", "zh_CN":"pvc在集群的状态"}
        self.status = status

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.name_cn, 'name_cn')
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.name_cn is not None:
            result['nameCn'] = self.name_cn
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nameCn') is not None:
            self.name_cn = m.get('nameCn')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class PvcInNamespaceWorkLoad(TeaModel):
    def __init__(
        self,
        kind: str = None,
        name: str = None,
        namespace: str = None,
    ):
        # {"en":"workload kind", "zh_CN":"负载类型"}
        self.kind = kind
        # {"en":"workload name", "zh_CN":"负载名称"}
        self.name = name
        # {"en":"workload namespace", "zh_CN":"负载命名空间"}
        self.namespace = namespace

    def validate(self):
        self.validate_required(self.kind, 'kind')
        self.validate_required(self.name, 'name')
        self.validate_required(self.namespace, 'namespace')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        return self


class PvcInNamespacePvcInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        i_otype: str = None,
        clusters: List[PvcInNamespaceCluster] = None,
        work_loads: List[PvcInNamespaceWorkLoad] = None,
        create_time: int = None,
        storage: int = None,
        storage_class: str = None,
    ):
        # {"en":"pvcs name", "zh_CN":"pvc名称"}
        self.name = name
        # {"en":"namespace info", "zh_CN":"pvc namespace"}
        self.namespace = namespace
        # {"en":"pvc io type", "zh_CN":"pvc IO类型"}
        self.i_otype = i_otype
        # {"en":"pvc in every cluster info", "zh_CN":"pvc在各集群信息"}
        self.clusters = clusters
        # {"en":"pvc workload", "zh_CN":"pvc绑定的负载"}
        self.work_loads = work_loads
        # {"en":"createTime", "zh_CN":"pvc创建时间"}
        self.create_time = create_time
        # {"en":"pvc storage", "zh_CN":"pvc存储大小"}
        self.storage = storage
        # {"en":"pvc storageClass", "zh_CN":"pvc storageClass"}
        self.storage_class = storage_class

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.namespace, 'namespace')
        self.validate_required(self.i_otype, 'i_otype')
        self.validate_required(self.clusters, 'clusters')
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()
        self.validate_required(self.work_loads, 'work_loads')
        if self.work_loads:
            for k in self.work_loads:
                if k:
                    k.validate()
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.storage, 'storage')
        self.validate_required(self.storage_class, 'storage_class')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.i_otype is not None:
            result['iOType'] = self.i_otype
        if self.clusters is not None:
            result['clusters'] = []
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        if self.work_loads is not None:
            result['workLoads'] = []
            for k in self.work_loads:
                result['workLoads'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.storage is not None:
            result['storage'] = self.storage
        if self.storage_class is not None:
            result['storageClass'] = self.storage_class
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('iOType') is not None:
            self.i_otype = m.get('iOType')
        if m.get('clusters') is not None:
            self.clusters = []
            for k in m.get('clusters'):
                temp_model = PvcInNamespaceCluster()
                self.clusters.append(temp_model.from_map(k))
        if m.get('workLoads') is not None:
            self.work_loads = []
            for k in m.get('workLoads'):
                temp_model = PvcInNamespaceWorkLoad()
                self.work_loads.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('storage') is not None:
            self.storage = m.get('storage')
        if m.get('storageClass') is not None:
            self.storage_class = m.get('storageClass')
        return self


class PvcInNamespaceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: List[PvcInNamespacePvcInfo] = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"pvc list", "zh_CN":"pvc列表"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
        self.validate_required(self.request_id, 'request_id')
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
            self.data = []
            for k in m.get('data'):
                temp_model = PvcInNamespacePvcInfo()
                self.data.append(temp_model.from_map(k))
        return self


class PvcInNamespacePaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
    ):
        # {"en":"namespace info", "zh_CN":"pvc namespace"}
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


class PvcInNamespaceParameters(TeaModel):
    def __init__(
        self,
        storageclass: str = None,
        filterused: str = None,
    ):
        # {"en":"pvc storageclass,multiple separated by commas", "zh_CN":"pvc storageclass，多个以逗号隔开"}
        self.storageclass = storageclass
        # {"en":"filter has been used", "zh_CN":"过滤已被使用的pvc"}
        self.filterused = filterused

    def validate(self):
        self.validate_required(self.storageclass, 'storageclass')
        self.validate_required(self.filterused, 'filterused')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.storageclass is not None:
            result['storageclass'] = self.storageclass
        if self.filterused is not None:
            result['filterused'] = self.filterused
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('storageclass') is not None:
            self.storageclass = m.get('storageclass')
        if m.get('filterused') is not None:
            self.filterused = m.get('filterused')
        return self


class PvcInNamespaceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PvcInNamespaceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class PutPatchPvcsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchPvcsOwnerReference(TeaModel):
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


class PutPatchPvcsObjectMeta(TeaModel):
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
        owner_references: List[PutPatchPvcsOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
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

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
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
                temp_model = PutPatchPvcsOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        return self


class PutPatchPvcsLabelSelectorRequirement(TeaModel):
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


class PutPatchPvcsMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[PutPatchPvcsLabelSelectorRequirement] = None,
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
                temp_model = PutPatchPvcsLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class PutPatchPvcsResourceRequirements(TeaModel):
    def __init__(
        self,
        limits: Dict[str, str] = None,
        requests: Dict[str, str] = None,
    ):
        # {"en":"describes the maximum amount of compute resources allowed", "zh_CN":"描述所允许的最大计算资源用量"}
        self.limits = limits
        # {"en":"describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits", "zh_CN":"requests 描述所需的最小计算资源量。如果容器省略了 requests，但明确设定了 limits， 则 requests 默认值为 limits 值，否则为实现定义的值。请求不能超过限制"}
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['limits'] = self.limits
        if self.requests is not None:
            result['requests'] = self.requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limits') is not None:
            self.limits = m.get('limits')
        if m.get('requests') is not None:
            self.requests = m.get('requests')
        return self


class PutPatchPvcsTypedLocalObjectReference(TeaModel):
    def __init__(
        self,
        api_group: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required", "zh_CN":"被引用资源的组。如果不指定 APIGroup，则指定的 Kind 必须在核心 API 组中。对于任何其它第三方类型，都需要 APIGroup"}
        self.api_group = api_group
        # {"en":" the type of resource being referenced", "zh_CN":"被引用的资源的类型"}
        self.kind = kind
        # {"en":"the name of resource being referenced", "zh_CN":"被引用的资源的名称"}
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_group is not None:
            result['apiGroup'] = self.api_group
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroup') is not None:
            self.api_group = m.get('apiGroup')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class PutPatchPvcsPersistentVolumeClaimSpec(TeaModel):
    def __init__(
        self,
        access_modes: List[str] = None,
        selector: PutPatchPvcsMetaV1LabelSelector = None,
        resources: PutPatchPvcsResourceRequirements = None,
        volume_name: str = None,
        storage_class_name: str = None,
        volume_mode: str = None,
        data_source: PutPatchPvcsTypedLocalObjectReference = None,
    ):
        # {"en":"contains the desired access modes the volume should have", "zh_CN":"包含卷应具备的预期访问模式"}
        self.access_modes = access_modes
        # {"en":"a label query over volumes to consider for binding", "zh_CN":"在绑定时对卷进行选择所执行的标签查询"}
        self.selector = selector
        # {"en":"represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim", "zh_CN":"表示卷应拥有的最小资源。 如果启用了 RecoverVolumeExpansionFailure 功能特性，则允许用户指定这些资源要求， 此值必须低于之前的值，但必须高于申领的状态字段中记录的容量"}
        self.resources = resources
        # {"en":"the binding reference to the PersistentVolume backing this claim", "zh_CN":"对此申领所对应的 PersistentVolume 的绑定引用"}
        self.volume_name = volume_name
        # {"en":"the name of the StorageClass required by the claim", "zh_CN":"此申领所要求的 StorageClass 名称"}
        self.storage_class_name = storage_class_name
        # {"en":"defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec", "zh_CN":"定义申领需要哪种类别的卷。当申领规约中未包含此字段时，意味着取值为 Filesystem"}
        self.volume_mode = volume_mode
        # {"en":"dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (PutPatchPvcsPersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource", "zh_CN":"dataSource 字段可用于二选一：- 现有的 VolumeSnapshot 对象（snapshot.storage.k8s.io/VolumeSnapshot）- 现有的 PVC (PutPatchPvcsPersistentVolumeClaim)。如果制备器或外部控制器可以支持指定的数据源，则它将根据指定数据源的内容创建新的卷。 当 AnyVolumeDataSource 特性门控被启用时，dataSource 内容将被复制到 dataSourceRef， 当 dataSourceRef.namespace 未被指定时，dataSourceRef 内容将被复制到 dataSource。 如果名字空间被指定，则 dataSourceRef 不会被复制到 dataSource"}
        self.data_source = data_source

    def validate(self):
        if self.selector:
            self.selector.validate()
        if self.resources:
            self.resources.validate()
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        if self.resources is not None:
            result['resources'] = self.resources.to_map()
        if self.volume_name is not None:
            result['volumeName'] = self.volume_name
        if self.storage_class_name is not None:
            result['storageClassName'] = self.storage_class_name
        if self.volume_mode is not None:
            result['volumeMode'] = self.volume_mode
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('selector') is not None:
            temp_model = PutPatchPvcsMetaV1LabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        if m.get('resources') is not None:
            temp_model = PutPatchPvcsResourceRequirements()
            self.resources = temp_model.from_map(m['resources'])
        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')
        if m.get('storageClassName') is not None:
            self.storage_class_name = m.get('storageClassName')
        if m.get('volumeMode') is not None:
            self.volume_mode = m.get('volumeMode')
        if m.get('dataSource') is not None:
            temp_model = PutPatchPvcsTypedLocalObjectReference()
            self.data_source = temp_model.from_map(m['dataSource'])
        return self


class PutPatchPvcsPersistentVolumeClaimCondition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type, required", "zh_CN":"类型，必需"}
        self.type = type
        # {"en":"status, required", "zh_CN":"状态，必需"}
        self.status = status
        # {"en":"reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports 'ResizeStarted' that means the underlying persistent volume is being resized", "zh_CN":"reason 是唯一的，它应该是一个机器可理解的简短字符串，指明上次状况转换的原因。 如果它报告 “ResizeStarted”，则意味着正在调整底层持久卷的大小"}
        self.reason = reason
        # {"en":" the human-readable message indicating details about last transition", "zh_CN":"人类可读的消息，指示有关上一次转换的详细信息"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class PutPatchPvcsPersistentVolumeClaimStatus(TeaModel):
    def __init__(
        self,
        phase: str = None,
        access_modes: List[str] = None,
        capacity: Dict[str, int] = None,
        conditions: List[PutPatchPvcsPersistentVolumeClaimCondition] = None,
    ):
        # {"en":"represents the current phase of PutPatchPvcsPersistentVolumeClaim", "zh_CN":"表示 PutPatchPvcsPersistentVolumeClaim 的当前阶段"}
        self.phase = phase
        # {"en":"contains the actual access modes the volume backing the PVC has", "zh_CN":"包含支持 PVC 的卷所具有的实际访问模式"}
        self.access_modes = access_modes
        # {"en":"represents the actual resources of the underlying volume", "zh_CN":"表示底层卷的实际资源"}
        self.capacity = capacity
        # {"en":"the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'", "zh_CN":"持久卷声明的当前的状况。 如果正在调整底层持久卷的大小，则状况将被设为 “ResizeStarted”"}
        self.conditions = conditions

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = PutPatchPvcsPersistentVolumeClaimCondition()
                self.conditions.append(temp_model.from_map(k))
        return self


class PutPatchPvcsPersistentVolumeClaim(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: PutPatchPvcsObjectMeta = None,
        spec: PutPatchPvcsPersistentVolumeClaimSpec = None,
        status: PutPatchPvcsPersistentVolumeClaimStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"defines the desired characteristics of a volume requested by a pod author", "zh_CN":"定义 Pod 作者所请求的卷的预期特征"}
        self.spec = spec
        # {"en":"represents the current information/status of a persistent volume claim. Read-only", "zh_CN":"表示一个持久卷申领的当前信息/状态。只读"}
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
            temp_model = PutPatchPvcsObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = PutPatchPvcsPersistentVolumeClaimSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = PutPatchPvcsPersistentVolumeClaimStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class PutPatchPvcsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: PutPatchPvcsPersistentVolumeClaim = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"pvc", "zh_CN":"pvc"}
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
            temp_model = PutPatchPvcsPersistentVolumeClaim()
            self.data = temp_model.from_map(m['data'])
        return self


class PutPatchPvcsPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"deployment name", "zh_CN":"pvc 名称"}
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


class PutPatchPvcsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchPvcsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class PutPatchPvcsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetPvcsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPvcsOwnerReference(TeaModel):
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


class GetPvcsObjectMeta(TeaModel):
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
        owner_references: List[GetPvcsOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
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

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
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
                temp_model = GetPvcsOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        return self


class GetPvcsLabelSelectorRequirement(TeaModel):
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


class GetPvcsMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[GetPvcsLabelSelectorRequirement] = None,
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
                temp_model = GetPvcsLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class GetPvcsResourceRequirements(TeaModel):
    def __init__(
        self,
        limits: Dict[str, str] = None,
        requests: Dict[str, str] = None,
    ):
        # {"en":"describes the maximum amount of compute resources allowed", "zh_CN":"描述所允许的最大计算资源用量"}
        self.limits = limits
        # {"en":"describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits", "zh_CN":"requests 描述所需的最小计算资源量。如果容器省略了 requests，但明确设定了 limits， 则 requests 默认值为 limits 值，否则为实现定义的值。请求不能超过限制"}
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['limits'] = self.limits
        if self.requests is not None:
            result['requests'] = self.requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limits') is not None:
            self.limits = m.get('limits')
        if m.get('requests') is not None:
            self.requests = m.get('requests')
        return self


class GetPvcsTypedLocalObjectReference(TeaModel):
    def __init__(
        self,
        api_group: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required", "zh_CN":"被引用资源的组。如果不指定 APIGroup，则指定的 Kind 必须在核心 API 组中。对于任何其它第三方类型，都需要 APIGroup"}
        self.api_group = api_group
        # {"en":" the type of resource being referenced", "zh_CN":"被引用的资源的类型"}
        self.kind = kind
        # {"en":"the name of resource being referenced", "zh_CN":"被引用的资源的名称"}
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_group is not None:
            result['apiGroup'] = self.api_group
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroup') is not None:
            self.api_group = m.get('apiGroup')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GetPvcsPersistentVolumeClaimSpec(TeaModel):
    def __init__(
        self,
        access_modes: List[str] = None,
        selector: GetPvcsMetaV1LabelSelector = None,
        resources: GetPvcsResourceRequirements = None,
        volume_name: str = None,
        storage_class_name: str = None,
        volume_mode: str = None,
        data_source: GetPvcsTypedLocalObjectReference = None,
    ):
        # {"en":"contains the desired access modes the volume should have", "zh_CN":"包含卷应具备的预期访问模式"}
        self.access_modes = access_modes
        # {"en":"a label query over volumes to consider for binding", "zh_CN":"在绑定时对卷进行选择所执行的标签查询"}
        self.selector = selector
        # {"en":"represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim", "zh_CN":"表示卷应拥有的最小资源。 如果启用了 RecoverVolumeExpansionFailure 功能特性，则允许用户指定这些资源要求， 此值必须低于之前的值，但必须高于申领的状态字段中记录的容量"}
        self.resources = resources
        # {"en":"the binding reference to the PersistentVolume backing this claim", "zh_CN":"对此申领所对应的 PersistentVolume 的绑定引用"}
        self.volume_name = volume_name
        # {"en":"the name of the StorageClass required by the claim", "zh_CN":"此申领所要求的 StorageClass 名称"}
        self.storage_class_name = storage_class_name
        # {"en":"defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec", "zh_CN":"定义申领需要哪种类别的卷。当申领规约中未包含此字段时，意味着取值为 Filesystem"}
        self.volume_mode = volume_mode
        # {"en":"dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (GetPvcsPersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource", "zh_CN":"dataSource 字段可用于二选一：- 现有的 VolumeSnapshot 对象（snapshot.storage.k8s.io/VolumeSnapshot）- 现有的 PVC (GetPvcsPersistentVolumeClaim)。如果制备器或外部控制器可以支持指定的数据源，则它将根据指定数据源的内容创建新的卷。 当 AnyVolumeDataSource 特性门控被启用时，dataSource 内容将被复制到 dataSourceRef， 当 dataSourceRef.namespace 未被指定时，dataSourceRef 内容将被复制到 dataSource。 如果名字空间被指定，则 dataSourceRef 不会被复制到 dataSource"}
        self.data_source = data_source

    def validate(self):
        if self.selector:
            self.selector.validate()
        if self.resources:
            self.resources.validate()
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        if self.resources is not None:
            result['resources'] = self.resources.to_map()
        if self.volume_name is not None:
            result['volumeName'] = self.volume_name
        if self.storage_class_name is not None:
            result['storageClassName'] = self.storage_class_name
        if self.volume_mode is not None:
            result['volumeMode'] = self.volume_mode
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('selector') is not None:
            temp_model = GetPvcsMetaV1LabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        if m.get('resources') is not None:
            temp_model = GetPvcsResourceRequirements()
            self.resources = temp_model.from_map(m['resources'])
        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')
        if m.get('storageClassName') is not None:
            self.storage_class_name = m.get('storageClassName')
        if m.get('volumeMode') is not None:
            self.volume_mode = m.get('volumeMode')
        if m.get('dataSource') is not None:
            temp_model = GetPvcsTypedLocalObjectReference()
            self.data_source = temp_model.from_map(m['dataSource'])
        return self


class GetPvcsPersistentVolumeClaimCondition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type, required", "zh_CN":"类型，必需"}
        self.type = type
        # {"en":"status, required", "zh_CN":"状态，必需"}
        self.status = status
        # {"en":"reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports 'ResizeStarted' that means the underlying persistent volume is being resized", "zh_CN":"reason 是唯一的，它应该是一个机器可理解的简短字符串，指明上次状况转换的原因。 如果它报告 “ResizeStarted”，则意味着正在调整底层持久卷的大小"}
        self.reason = reason
        # {"en":" the human-readable message indicating details about last transition", "zh_CN":"人类可读的消息，指示有关上一次转换的详细信息"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetPvcsPersistentVolumeClaimStatus(TeaModel):
    def __init__(
        self,
        phase: str = None,
        access_modes: List[str] = None,
        capacity: Dict[str, int] = None,
        conditions: List[GetPvcsPersistentVolumeClaimCondition] = None,
    ):
        # {"en":"represents the current phase of GetPvcsPersistentVolumeClaim", "zh_CN":"表示 GetPvcsPersistentVolumeClaim 的当前阶段"}
        self.phase = phase
        # {"en":"contains the actual access modes the volume backing the PVC has", "zh_CN":"包含支持 PVC 的卷所具有的实际访问模式"}
        self.access_modes = access_modes
        # {"en":"represents the actual resources of the underlying volume", "zh_CN":"表示底层卷的实际资源"}
        self.capacity = capacity
        # {"en":"the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'", "zh_CN":"持久卷声明的当前的状况。 如果正在调整底层持久卷的大小，则状况将被设为 “ResizeStarted”"}
        self.conditions = conditions

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = GetPvcsPersistentVolumeClaimCondition()
                self.conditions.append(temp_model.from_map(k))
        return self


class GetPvcsPersistentVolumeClaim(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: GetPvcsObjectMeta = None,
        spec: GetPvcsPersistentVolumeClaimSpec = None,
        status: GetPvcsPersistentVolumeClaimStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"defines the desired characteristics of a volume requested by a pod author", "zh_CN":"定义 Pod 作者所请求的卷的预期特征"}
        self.spec = spec
        # {"en":"represents the current information/status of a persistent volume claim. Read-only", "zh_CN":"表示一个持久卷申领的当前信息/状态。只读"}
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
            temp_model = GetPvcsObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = GetPvcsPersistentVolumeClaimSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = GetPvcsPersistentVolumeClaimStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class GetPvcsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: GetPvcsPersistentVolumeClaim = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"pvc", "zh_CN":"pvc"}
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
            temp_model = GetPvcsPersistentVolumeClaim()
            self.data = temp_model.from_map(m['data'])
        return self


class GetPvcsPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"pvc name", "zh_CN":"pvc 名称"}
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


class GetPvcsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPvcsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPvcsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListPvcsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListPvcsListMeta(TeaModel):
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


class ListPvcsOwnerReference(TeaModel):
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


class ListPvcsObjectMeta(TeaModel):
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
        owner_references: List[ListPvcsOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
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

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
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
                temp_model = ListPvcsOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        return self


class ListPvcsLabelSelectorRequirement(TeaModel):
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


class ListPvcsMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[ListPvcsLabelSelectorRequirement] = None,
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
                temp_model = ListPvcsLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class ListPvcsResourceRequirements(TeaModel):
    def __init__(
        self,
        limits: Dict[str, str] = None,
        requests: Dict[str, str] = None,
    ):
        # {"en":"describes the maximum amount of compute resources allowed", "zh_CN":"描述所允许的最大计算资源用量"}
        self.limits = limits
        # {"en":"describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits", "zh_CN":"requests 描述所需的最小计算资源量。如果容器省略了 requests，但明确设定了 limits， 则 requests 默认值为 limits 值，否则为实现定义的值。请求不能超过限制"}
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['limits'] = self.limits
        if self.requests is not None:
            result['requests'] = self.requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limits') is not None:
            self.limits = m.get('limits')
        if m.get('requests') is not None:
            self.requests = m.get('requests')
        return self


class ListPvcsTypedLocalObjectReference(TeaModel):
    def __init__(
        self,
        api_group: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required", "zh_CN":"被引用资源的组。如果不指定 APIGroup，则指定的 Kind 必须在核心 API 组中。对于任何其它第三方类型，都需要 APIGroup"}
        self.api_group = api_group
        # {"en":" the type of resource being referenced", "zh_CN":"被引用的资源的类型"}
        self.kind = kind
        # {"en":"the name of resource being referenced", "zh_CN":"被引用的资源的名称"}
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_group is not None:
            result['apiGroup'] = self.api_group
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroup') is not None:
            self.api_group = m.get('apiGroup')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ListPvcsPersistentVolumeClaimSpec(TeaModel):
    def __init__(
        self,
        access_modes: List[str] = None,
        selector: ListPvcsMetaV1LabelSelector = None,
        resources: ListPvcsResourceRequirements = None,
        volume_name: str = None,
        storage_class_name: str = None,
        volume_mode: str = None,
        data_source: ListPvcsTypedLocalObjectReference = None,
    ):
        # {"en":"contains the desired access modes the volume should have", "zh_CN":"包含卷应具备的预期访问模式"}
        self.access_modes = access_modes
        # {"en":"a label query over volumes to consider for binding", "zh_CN":"在绑定时对卷进行选择所执行的标签查询"}
        self.selector = selector
        # {"en":"represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim", "zh_CN":"表示卷应拥有的最小资源。 如果启用了 RecoverVolumeExpansionFailure 功能特性，则允许用户指定这些资源要求， 此值必须低于之前的值，但必须高于申领的状态字段中记录的容量"}
        self.resources = resources
        # {"en":"the binding reference to the PersistentVolume backing this claim", "zh_CN":"对此申领所对应的 PersistentVolume 的绑定引用"}
        self.volume_name = volume_name
        # {"en":"the name of the StorageClass required by the claim", "zh_CN":"此申领所要求的 StorageClass 名称"}
        self.storage_class_name = storage_class_name
        # {"en":"defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec", "zh_CN":"定义申领需要哪种类别的卷。当申领规约中未包含此字段时，意味着取值为 Filesystem"}
        self.volume_mode = volume_mode
        # {"en":"dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (ListPvcsPersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource", "zh_CN":"dataSource 字段可用于二选一：- 现有的 VolumeSnapshot 对象（snapshot.storage.k8s.io/VolumeSnapshot）- 现有的 PVC (ListPvcsPersistentVolumeClaim)。如果制备器或外部控制器可以支持指定的数据源，则它将根据指定数据源的内容创建新的卷。 当 AnyVolumeDataSource 特性门控被启用时，dataSource 内容将被复制到 dataSourceRef， 当 dataSourceRef.namespace 未被指定时，dataSourceRef 内容将被复制到 dataSource。 如果名字空间被指定，则 dataSourceRef 不会被复制到 dataSource"}
        self.data_source = data_source

    def validate(self):
        if self.selector:
            self.selector.validate()
        if self.resources:
            self.resources.validate()
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        if self.resources is not None:
            result['resources'] = self.resources.to_map()
        if self.volume_name is not None:
            result['volumeName'] = self.volume_name
        if self.storage_class_name is not None:
            result['storageClassName'] = self.storage_class_name
        if self.volume_mode is not None:
            result['volumeMode'] = self.volume_mode
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('selector') is not None:
            temp_model = ListPvcsMetaV1LabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        if m.get('resources') is not None:
            temp_model = ListPvcsResourceRequirements()
            self.resources = temp_model.from_map(m['resources'])
        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')
        if m.get('storageClassName') is not None:
            self.storage_class_name = m.get('storageClassName')
        if m.get('volumeMode') is not None:
            self.volume_mode = m.get('volumeMode')
        if m.get('dataSource') is not None:
            temp_model = ListPvcsTypedLocalObjectReference()
            self.data_source = temp_model.from_map(m['dataSource'])
        return self


class ListPvcsPersistentVolumeClaimCondition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type, required", "zh_CN":"类型，必需"}
        self.type = type
        # {"en":"status, required", "zh_CN":"状态，必需"}
        self.status = status
        # {"en":"reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports 'ResizeStarted' that means the underlying persistent volume is being resized", "zh_CN":"reason 是唯一的，它应该是一个机器可理解的简短字符串，指明上次状况转换的原因。 如果它报告 “ResizeStarted”，则意味着正在调整底层持久卷的大小"}
        self.reason = reason
        # {"en":" the human-readable message indicating details about last transition", "zh_CN":"人类可读的消息，指示有关上一次转换的详细信息"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListPvcsPersistentVolumeClaimStatus(TeaModel):
    def __init__(
        self,
        phase: str = None,
        access_modes: List[str] = None,
        capacity: Dict[str, int] = None,
        conditions: List[ListPvcsPersistentVolumeClaimCondition] = None,
    ):
        # {"en":"represents the current phase of ListPvcsPersistentVolumeClaim", "zh_CN":"表示 ListPvcsPersistentVolumeClaim 的当前阶段"}
        self.phase = phase
        # {"en":"contains the actual access modes the volume backing the PVC has", "zh_CN":"包含支持 PVC 的卷所具有的实际访问模式"}
        self.access_modes = access_modes
        # {"en":"represents the actual resources of the underlying volume", "zh_CN":"表示底层卷的实际资源"}
        self.capacity = capacity
        # {"en":"the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'", "zh_CN":"持久卷声明的当前的状况。 如果正在调整底层持久卷的大小，则状况将被设为 “ResizeStarted”"}
        self.conditions = conditions

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = ListPvcsPersistentVolumeClaimCondition()
                self.conditions.append(temp_model.from_map(k))
        return self


class ListPvcsPersistentVolumeClaim(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListPvcsObjectMeta = None,
        spec: ListPvcsPersistentVolumeClaimSpec = None,
        status: ListPvcsPersistentVolumeClaimStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"defines the desired characteristics of a volume requested by a pod author", "zh_CN":"定义 Pod 作者所请求的卷的预期特征"}
        self.spec = spec
        # {"en":"represents the current information/status of a persistent volume claim. Read-only", "zh_CN":"表示一个持久卷申领的当前信息/状态。只读"}
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
            temp_model = ListPvcsObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = ListPvcsPersistentVolumeClaimSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = ListPvcsPersistentVolumeClaimStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class ListPvcsPvcList(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: ListPvcsListMeta = None,
        items: List[ListPvcsPersistentVolumeClaim] = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"Standard list metadata", "zh_CN":"标准列表元数据"}
        self.metadata = metadata
        # {"en":"List of ListPvcsPersistentVolumeClaim", "zh_CN":"ListPvcsPersistentVolumeClaim 列表"}
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
            temp_model = ListPvcsListMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('items') is not None:
            self.items = []
            for k in m.get('items'):
                temp_model = ListPvcsPersistentVolumeClaim()
                self.items.append(temp_model.from_map(k))
        return self


class ListPvcsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: ListPvcsPvcList = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"pvc list", "zh_CN":"pvc列表"}
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
            temp_model = ListPvcsPvcList()
            self.data = temp_model.from_map(m['data'])
        return self


class ListPvcsPaths(TeaModel):
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


class ListPvcsParameters(TeaModel):
    def __init__(
        self,
        name: str = None,
        label_selector: str = None,
    ):
        # {"en":"The name of pvc", "zh_CN":"pvc 名称"}
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


class ListPvcsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListPvcsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryChannelRecordFilesRequest(TeaModel):
    def __init__(
        self,
        date_from: str = None,
        date_to: str = None,
        device_id: str = None,
        channel_id: str = None,
        page_size: int = None,
        page_index: int = None,
    ):
        # {"en":"Start time:
        # 1. The format is yyyyy-MM-ddTHH: mm: SS + 08:00, for example, 2024-01-23T10:00 + 08:00 (10:00:00 Beijing time on January 23, 2024);
        # 2. Can not exceed the current time;", "zh_CN":"开始时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00，例如，2024-01-23T10:00:00+08:00（为北京时间2024年01月23日10点0分0秒）；
        # 2.不能大于当前时间"}
        self.date_from = date_from
        # {"en":"End time:
        # 1. The format is yyyy-MM-ddTHH:mm:ss+08:00;
        # 2. The end time is greater than the start time.
        # 3. If the end time is greater than the current time, the current time is taken.
        # 4. DateFrom and dateTo are not uploaded, defaulting to query the past 24 hours; if only one is not uploaded, throw an exception;
        # 5. Maximum query interval allowed: 30 days, that is, the difference between dateFrom and dateTo can not exceed 30 days. ", "zh_CN":"结束时间：
        # 1.格式为yyyy-MM-ddTHH:mm:ss+08:00；
        # 2.结束时间需大于开始时间；
        # 3.结束时间如果大于当前时间，取当前时间；
        # 4.dateFrom，dateTo二者都未传，默认查询过去的24小时；如仅有一个未传，抛异常；
        # 5.允许查询最大间隔：30天，即dateFrom和dateTo相差不能超过30天。"}
        self.date_to = date_to
        # {"en":"Device GB28181 Id", "zh_CN":"设备国标ID"}
        self.device_id = device_id
        # {"en":"ChannelGB28181 Id", "zh_CN":"通道国标ID"}
        self.channel_id = channel_id
        # {"en":"Paging Size.
        # 1. Default 10, maximum 50", "zh_CN":"分页大小。
        # 1、默认10，最大50"}
        self.page_size = page_size
        # {"en":"Page index
        #  1. The default value is 1, indicating the initial page.", "zh_CN":"第几页
        # 1、默认为1，表示第一页"}
        self.page_index = page_index

    def validate(self):
        self.validate_required(self.device_id, 'device_id')
        self.validate_required(self.channel_id, 'channel_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date_from is not None:
            result['dateFrom'] = self.date_from
        if self.date_to is not None:
            result['dateTo'] = self.date_to
        if self.device_id is not None:
            result['deviceId'] = self.device_id
        if self.channel_id is not None:
            result['channelId'] = self.channel_id
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dateFrom') is not None:
            self.date_from = m.get('dateFrom')
        if m.get('dateTo') is not None:
            self.date_to = m.get('dateTo')
        if m.get('deviceId') is not None:
            self.device_id = m.get('deviceId')
        if m.get('channelId') is not None:
            self.channel_id = m.get('channelId')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        return self


class QueryChannelRecordFilesFile(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_size: str = None,
        duration: int = None,
        start_time: str = None,
        expire_time: str = None,
        file_url: str = None,
    ):
        # {"en":"QueryChannelRecordFilesFile name", "zh_CN":"文件名"}
        self.file_name = file_name
        # {"en":"QueryChannelRecordFilesFile size
        # 1. Unit (M)", "zh_CN":"文件大小
        # 1、单位（M）"}
        self.file_size = file_size
        # {"en":"QueryChannelRecordFilesFile duration
        # 1. Unit (second)", "zh_CN":"文件时长
        # 1、单位(秒)"}
        self.duration = duration
        # {"en":"QueryChannelRecordFilesFile start time
        # 1. Timestamp format", "zh_CN":"文件开始时间
        # 1、时间戳格式"}
        self.start_time = start_time
        # {"en":"QueryChannelRecordFilesFile expiration time
        # 1. Timestamp format", "zh_CN":"文件过期时间
        # 1、时间戳格式"}
        self.expire_time = expire_time
        # {"en":"QueryChannelRecordFilesFile url", "zh_CN":"文件url"}
        self.file_url = file_url

    def validate(self):
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.duration, 'duration')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.expire_time, 'expire_time')
        self.validate_required(self.file_url, 'file_url')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.duration is not None:
            result['duration'] = self.duration
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.expire_time is not None:
            result['expireTime'] = self.expire_time
        if self.file_url is not None:
            result['fileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('expireTime') is not None:
            self.expire_time = m.get('expireTime')
        if m.get('fileUrl') is not None:
            self.file_url = m.get('fileUrl')
        return self


class QueryChannelRecordFilesData(TeaModel):
    def __init__(
        self,
        rows: List[QueryChannelRecordFilesFile] = None,
        page_index: int = None,
        page_size: int = None,
        total: int = None,
    ):
        # {"en":"QueryChannelRecordFilesFile List", "zh_CN":"文件列表"}
        self.rows = rows
        # {"en":"Page Index", "zh_CN":"第几页"}
        self.page_index = page_index
        # {"en":"Paging Size", "zh_CN":"分页大小"}
        self.page_size = page_size
        # {"en":"Total", "zh_CN":"总数"}
        self.total = total

    def validate(self):
        self.validate_required(self.rows, 'rows')
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()
        self.validate_required(self.page_index, 'page_index')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.total, 'total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rows is not None:
            result['rows'] = []
            for k in self.rows:
                result['rows'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rows') is not None:
            self.rows = []
            for k in m.get('rows'):
                temp_model = QueryChannelRecordFilesFile()
                self.rows.append(temp_model.from_map(k))
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryChannelRecordFilesResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: QueryChannelRecordFilesData = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
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
            temp_model = QueryChannelRecordFilesData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryChannelRecordFilesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryChannelRecordFilesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryChannelRecordFilesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryChannelRecordFilesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeletePvcsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePvcsStatusDetails(TeaModel):
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


class DeletePvcsStatus(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        status: str = None,
        code: int = None,
        details: DeletePvcsStatusDetails = None,
    ):
        # {"en":"APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values", "zh_CN":"APIVersion 定义对象表示的版本化模式。 服务器应将已识别的模式转换为最新的内部值，并可能拒绝无法识别的值"}
        self.api_version = api_version
        # {"en":"Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase", "zh_CN":"Kind 是一个字符串值，表示此对象表示的 REST 资源。 服务器可以从客户端提交请求的端点推断出这一点。 无法更新。驼峰式规则"}
        self.kind = kind
        # {"en":"DeletePvcsStatus of the operation. One of: 'Success' or 'Failure'", "zh_CN":"操作状态。“Success”或“Failure” 之一"}
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
            temp_model = DeletePvcsStatusDetails()
            self.details = temp_model.from_map(m['details'])
        return self


class DeletePvcsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: DeletePvcsStatus = None,
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
            temp_model = DeletePvcsStatus()
            self.data = temp_model.from_map(m['data'])
        return self


class DeletePvcsPaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace", "zh_CN":"命名空间"}
        self.namespace = namespace
        # {"en":"deployment name", "zh_CN":"pvc 名称"}
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


class DeletePvcsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePvcsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePvcsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreatePvcsOwnerReference(TeaModel):
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


class CreatePvcsObjectMeta(TeaModel):
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
        owner_references: List[CreatePvcsOwnerReference] = None,
        finalizers: List[str] = None,
        cluster_name: str = None,
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

    def validate(self):
        if self.owner_references:
            for k in self.owner_references:
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
                temp_model = CreatePvcsOwnerReference()
                self.owner_references.append(temp_model.from_map(k))
        if m.get('finalizers') is not None:
            self.finalizers = m.get('finalizers')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        return self


class CreatePvcsLabelSelectorRequirement(TeaModel):
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


class CreatePvcsMetaV1LabelSelector(TeaModel):
    def __init__(
        self,
        match_labels: Dict[str, str] = None,
        match_expressions: List[CreatePvcsLabelSelectorRequirement] = None,
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
                temp_model = CreatePvcsLabelSelectorRequirement()
                self.match_expressions.append(temp_model.from_map(k))
        return self


class CreatePvcsResourceRequirements(TeaModel):
    def __init__(
        self,
        limits: Dict[str, str] = None,
        requests: Dict[str, str] = None,
    ):
        # {"en":"describes the maximum amount of compute resources allowed", "zh_CN":"描述所允许的最大计算资源用量"}
        self.limits = limits
        # {"en":"describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits", "zh_CN":"requests 描述所需的最小计算资源量。如果容器省略了 requests，但明确设定了 limits， 则 requests 默认值为 limits 值，否则为实现定义的值。请求不能超过限制"}
        self.requests = requests

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limits is not None:
            result['limits'] = self.limits
        if self.requests is not None:
            result['requests'] = self.requests
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limits') is not None:
            self.limits = m.get('limits')
        if m.get('requests') is not None:
            self.requests = m.get('requests')
        return self


class CreatePvcsTypedLocalObjectReference(TeaModel):
    def __init__(
        self,
        api_group: str = None,
        kind: str = None,
        name: str = None,
    ):
        # {"en":"the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required", "zh_CN":"被引用资源的组。如果不指定 APIGroup，则指定的 Kind 必须在核心 API 组中。对于任何其它第三方类型，都需要 APIGroup"}
        self.api_group = api_group
        # {"en":" the type of resource being referenced", "zh_CN":"被引用的资源的类型"}
        self.kind = kind
        # {"en":"the name of resource being referenced", "zh_CN":"被引用的资源的名称"}
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_group is not None:
            result['apiGroup'] = self.api_group
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiGroup') is not None:
            self.api_group = m.get('apiGroup')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreatePvcsPersistentVolumeClaimSpec(TeaModel):
    def __init__(
        self,
        access_modes: List[str] = None,
        selector: CreatePvcsMetaV1LabelSelector = None,
        resources: CreatePvcsResourceRequirements = None,
        volume_name: str = None,
        storage_class_name: str = None,
        volume_mode: str = None,
        data_source: CreatePvcsTypedLocalObjectReference = None,
    ):
        # {"en":"contains the desired access modes the volume should have", "zh_CN":"包含卷应具备的预期访问模式"}
        self.access_modes = access_modes
        # {"en":"a label query over volumes to consider for binding", "zh_CN":"在绑定时对卷进行选择所执行的标签查询"}
        self.selector = selector
        # {"en":"represents the minimum resources the volume should have. If RecoverVolumeExpansionFailure feature is enabled users are allowed to specify resource requirements that are lower than previous value but must still be higher than capacity recorded in the status field of the claim", "zh_CN":"表示卷应拥有的最小资源。 如果启用了 RecoverVolumeExpansionFailure 功能特性，则允许用户指定这些资源要求， 此值必须低于之前的值，但必须高于申领的状态字段中记录的容量"}
        self.resources = resources
        # {"en":"the binding reference to the PersistentVolume backing this claim", "zh_CN":"对此申领所对应的 PersistentVolume 的绑定引用"}
        self.volume_name = volume_name
        # {"en":"the name of the StorageClass required by the claim", "zh_CN":"此申领所要求的 StorageClass 名称"}
        self.storage_class_name = storage_class_name
        # {"en":"defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec", "zh_CN":"定义申领需要哪种类别的卷。当申领规约中未包含此字段时，意味着取值为 Filesystem"}
        self.volume_mode = volume_mode
        # {"en":"dataSource field can be used to specify either: * An existing VolumeSnapshot object (snapshot.storage.k8s.io/VolumeSnapshot) * An existing PVC (CreatePvcsPersistentVolumeClaim) If the provisioner or an external controller can support the specified data source, it will create a new volume based on the contents of the specified data source. When the AnyVolumeDataSource feature gate is enabled, dataSource contents will be copied to dataSourceRef, and dataSourceRef contents will be copied to dataSource when dataSourceRef.namespace is not specified. If the namespace is specified, then dataSourceRef will not be copied to dataSource", "zh_CN":"dataSource 字段可用于二选一：- 现有的 VolumeSnapshot 对象（snapshot.storage.k8s.io/VolumeSnapshot）- 现有的 PVC (CreatePvcsPersistentVolumeClaim)。如果制备器或外部控制器可以支持指定的数据源，则它将根据指定数据源的内容创建新的卷。 当 AnyVolumeDataSource 特性门控被启用时，dataSource 内容将被复制到 dataSourceRef， 当 dataSourceRef.namespace 未被指定时，dataSourceRef 内容将被复制到 dataSource。 如果名字空间被指定，则 dataSourceRef 不会被复制到 dataSource"}
        self.data_source = data_source

    def validate(self):
        if self.selector:
            self.selector.validate()
        if self.resources:
            self.resources.validate()
        if self.data_source:
            self.data_source.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.selector is not None:
            result['selector'] = self.selector.to_map()
        if self.resources is not None:
            result['resources'] = self.resources.to_map()
        if self.volume_name is not None:
            result['volumeName'] = self.volume_name
        if self.storage_class_name is not None:
            result['storageClassName'] = self.storage_class_name
        if self.volume_mode is not None:
            result['volumeMode'] = self.volume_mode
        if self.data_source is not None:
            result['dataSource'] = self.data_source.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('selector') is not None:
            temp_model = CreatePvcsMetaV1LabelSelector()
            self.selector = temp_model.from_map(m['selector'])
        if m.get('resources') is not None:
            temp_model = CreatePvcsResourceRequirements()
            self.resources = temp_model.from_map(m['resources'])
        if m.get('volumeName') is not None:
            self.volume_name = m.get('volumeName')
        if m.get('storageClassName') is not None:
            self.storage_class_name = m.get('storageClassName')
        if m.get('volumeMode') is not None:
            self.volume_mode = m.get('volumeMode')
        if m.get('dataSource') is not None:
            temp_model = CreatePvcsTypedLocalObjectReference()
            self.data_source = temp_model.from_map(m['dataSource'])
        return self


class CreatePvcsRequest(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreatePvcsObjectMeta = None,
        spec: CreatePvcsPersistentVolumeClaimSpec = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"defines the desired characteristics of a volume requested by a pod author", "zh_CN":"定义 Pod 作者所请求的卷的预期特征"}
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
            temp_model = CreatePvcsObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreatePvcsPersistentVolumeClaimSpec()
            self.spec = temp_model.from_map(m['spec'])
        return self


class CreatePvcsPersistentVolumeClaimCondition(TeaModel):
    def __init__(
        self,
        type: str = None,
        status: str = None,
        reason: str = None,
        message: str = None,
    ):
        # {"en":"type, required", "zh_CN":"类型，必需"}
        self.type = type
        # {"en":"status, required", "zh_CN":"状态，必需"}
        self.status = status
        # {"en":"reason is a unique, this should be a short, machine understandable string that gives the reason for condition's last transition. If it reports 'ResizeStarted' that means the underlying persistent volume is being resized", "zh_CN":"reason 是唯一的，它应该是一个机器可理解的简短字符串，指明上次状况转换的原因。 如果它报告 “ResizeStarted”，则意味着正在调整底层持久卷的大小"}
        self.reason = reason
        # {"en":" the human-readable message indicating details about last transition", "zh_CN":"人类可读的消息，指示有关上一次转换的详细信息"}
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.status is not None:
            result['status'] = self.status
        if self.reason is not None:
            result['reason'] = self.reason
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreatePvcsPersistentVolumeClaimStatus(TeaModel):
    def __init__(
        self,
        phase: str = None,
        access_modes: List[str] = None,
        capacity: Dict[str, int] = None,
        conditions: List[CreatePvcsPersistentVolumeClaimCondition] = None,
    ):
        # {"en":"represents the current phase of CreatePvcsPersistentVolumeClaim", "zh_CN":"表示 CreatePvcsPersistentVolumeClaim 的当前阶段"}
        self.phase = phase
        # {"en":"contains the actual access modes the volume backing the PVC has", "zh_CN":"包含支持 PVC 的卷所具有的实际访问模式"}
        self.access_modes = access_modes
        # {"en":"represents the actual resources of the underlying volume", "zh_CN":"表示底层卷的实际资源"}
        self.capacity = capacity
        # {"en":"the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'ResizeStarted'", "zh_CN":"持久卷声明的当前的状况。 如果正在调整底层持久卷的大小，则状况将被设为 “ResizeStarted”"}
        self.conditions = conditions

    def validate(self):
        if self.conditions:
            for k in self.conditions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phase is not None:
            result['phase'] = self.phase
        if self.access_modes is not None:
            result['accessModes'] = self.access_modes
        if self.capacity is not None:
            result['capacity'] = self.capacity
        if self.conditions is not None:
            result['conditions'] = []
            for k in self.conditions:
                result['conditions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('phase') is not None:
            self.phase = m.get('phase')
        if m.get('accessModes') is not None:
            self.access_modes = m.get('accessModes')
        if m.get('capacity') is not None:
            self.capacity = m.get('capacity')
        if m.get('conditions') is not None:
            self.conditions = []
            for k in m.get('conditions'):
                temp_model = CreatePvcsPersistentVolumeClaimCondition()
                self.conditions.append(temp_model.from_map(k))
        return self


class CreatePvcsPersistentVolumeClaim(TeaModel):
    def __init__(
        self,
        api_version: str = None,
        kind: str = None,
        metadata: CreatePvcsObjectMeta = None,
        spec: CreatePvcsPersistentVolumeClaimSpec = None,
        status: CreatePvcsPersistentVolumeClaimStatus = None,
    ):
        # {"en":"apiVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values.", "zh_CN":"APIVersion定义了表示对象的版本化模式。服务器应该将认可的模式转换为最新的内部值，并可以拒绝不被认可的值。"}
        self.api_version = api_version
        # {"en":"kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.", "zh_CN":"kind是一个字符串值，表示此对象所代表的REST资源。服务器可以根据客户端提交请求的终点推断出这个值。不能更新。"}
        self.kind = kind
        # {"en":"standard object metadata.", "zh_CN":"标准的对象元数据"}
        self.metadata = metadata
        # {"en":"defines the desired characteristics of a volume requested by a pod author", "zh_CN":"定义 Pod 作者所请求的卷的预期特征"}
        self.spec = spec
        # {"en":"represents the current information/status of a persistent volume claim. Read-only", "zh_CN":"表示一个持久卷申领的当前信息/状态。只读"}
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
            temp_model = CreatePvcsObjectMeta()
            self.metadata = temp_model.from_map(m['metadata'])
        if m.get('spec') is not None:
            temp_model = CreatePvcsPersistentVolumeClaimSpec()
            self.spec = temp_model.from_map(m['spec'])
        if m.get('status') is not None:
            temp_model = CreatePvcsPersistentVolumeClaimStatus()
            self.status = temp_model.from_map(m['status'])
        return self


class CreatePvcsResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        msg: str = None,
        request_id: str = None,
        data: CreatePvcsPersistentVolumeClaim = None,
    ):
        # {"en":"response code", "zh_CN":"请求返回码"}
        self.code = code
        # {"en":"response message", "zh_CN":"请求返回信息"}
        self.msg = msg
        # {"en":"requestId", "zh_CN":"请求识别码"}
        self.request_id = request_id
        # {"en":"pvc object", "zh_CN":"pvc对象"}
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
            temp_model = CreatePvcsPersistentVolumeClaim()
            self.data = temp_model.from_map(m['data'])
        return self


class CreatePvcsPaths(TeaModel):
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


class CreatePvcsParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePvcsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePvcsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeletePvcFromEdgeRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePvcFromEdgeResponse(TeaModel):
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


class DeletePvcFromEdgePaths(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        name: str = None,
    ):
        # {"en":"namespace info", "zh_CN":"pvc namespace"}
        self.namespace = namespace
        # {"en":"pvc name", "zh_CN":"pvc name"}
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


class DeletePvcFromEdgeParameters(TeaModel):
    def __init__(
        self,
        clusters: str = None,
    ):
        # {"en":"pvc clusters,multiple separated by commas", "zh_CN":"pvc所在的集群，多个以逗号隔开"}
        self.clusters = clusters

    def validate(self):
        self.validate_required(self.clusters, 'clusters')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clusters is not None:
            result['clusters'] = self.clusters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusters') is not None:
            self.clusters = m.get('clusters')
        return self


class DeletePvcFromEdgeRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePvcFromEdgeResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




