# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetListOfPropertyVersionsPaths(TeaModel):
    def __init__(
        self,
        property_id: str = None,
    ):
        # {"en" : "ID of a property", "zh_CN": "加速项目ID。"}
        self.property_id = property_id

    def validate(self):
        self.validate_required(self.property_id, 'property_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        return self


class GetListOfPropertyVersionsParameters(TeaModel):
    def __init__(
        self,
        search: str = None,
        limit: int = None,
        offset: int = None,
        sort_order: str = None,
        sort_by: str = None,
    ):
        # {"en" : "The search parameter is used to match against the description field to filter the results.", "zh_CN": "根据搜索关键字匹配加速项目版本的描述字段来过滤结果。"}
        self.search = search
        # {"en" : "Default: 100 Range: [ 1 .. 200 ] 
        # Controls the number of versions to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "Default: 0 Range: >= 0 
        # Returns property versions beginning with this index instead of the default first one.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Enum: asc,desc 
        # Default: asc 
        # Order of property versions to return.", "zh_CN": "取值范围: asc,desc 
        # 默认值: asc 
        # 返回结果的顺序。默认按版本号升序排列。"}
        self.sort_order = sort_order
        # {"en" : "Enum: version,lastUpdateTime 
        # Default: version 
        # Returns results in sorted order.", "zh_CN": "取值范围: version,lastUpdateTime 
        # 默认值: version 
        # 返回结果的排序依据。支持按版本号和版本最后更新时间进行排序。"}
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.limit is not None:
            result['limit'] = self.limit
        if self.offset is not None:
            result['offset'] = self.offset
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        return self


class GetListOfPropertyVersionsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertyVersionsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertyVersionsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertyVersionsResponsePropertyVersions(TeaModel):
    def __init__(
        self,
        version: int = None,
        description: str = None,
        creation_time: str = None,
        hostnames: List[str] = None,
        frozen: bool = None,
        last_update_time: str = None,
        last_validation_status: str = None,
    ):
        # {"en" : "Range: >= 1 
        # A version number.", "zh_CN": "取值范围: >= 1 
        # 版本号。"}
        self.version = version
        # {"en" : "A description of the property version.", "zh_CN": "加速项目版本描述。"}
        self.description = description
        # {"en" : "RFC 3339 format date indicating when the property version was created. Example: 2016-12-28T23:10:42Z", "zh_CN": "RFC 3339格式的日期，表示创建加速项目版本的时间。示例：2016-12-28T23:10:42Z"}
        self.creation_time = creation_time
        # {"en" : "Hostnames associated with the property.", "zh_CN": "加速项目下的加速域名。"}
        self.hostnames = hostnames
        # {"en" : "Default: False 
        # Indicates whether the property version is frozen or can still be updated. A property version is frozen once it has been deployed.", "zh_CN": "默认值: False 
        # 该加速项目版本是否处于冻结状态。当加速项目版本部署后即进入冻结状态，不可再更新该版本。"}
        self.frozen = frozen
        # {"en" : "RFC 3339 format date indicating when the property version was last updated. Example: 2016-12-28T23:10:42Z", "zh_CN": "RFC 3339格式的日期，表示加速项目版本的最近更新时间。示例：2016-12-28T23:10:42Z"}
        self.last_update_time = last_update_time
        # {"en" : "Enum: NotValidated,InProgress,Validated,Failed 
        # Indicates the status of the most recent validation of the property version.", "zh_CN": "取值范围: NotValidated,InProgress,Validated,Failed 
        # 加速项目版本最近一次验证的状态，包括未验证，验证中，已验证，验证失败等状态。"}
        self.last_validation_status = last_validation_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.description is not None:
            result['description'] = self.description
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.frozen is not None:
            result['frozen'] = self.frozen
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.last_validation_status is not None:
            result['lastValidationStatus'] = self.last_validation_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('frozen') is not None:
            self.frozen = m.get('frozen')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('lastValidationStatus') is not None:
            self.last_validation_status = m.get('lastValidationStatus')
        return self


class GetListOfPropertyVersionsResponse(TeaModel):
    def __init__(
        self,
        property_versions: List[GetListOfPropertyVersionsResponsePropertyVersions] = None,
        count: int = None,
    ):
        # {"en" : "A summary of each version of the property.", "zh_CN": "加速项目每个版本的摘要。"}
        self.property_versions = property_versions
        # {"en" : "Range: >= 0 
        # Indicates the number of versions of the property.", "zh_CN": "取值范围: >= 0 
        # 加速项目的版本数量。"}
        self.count = count

    def validate(self):
        self.validate_required(self.property_versions, 'property_versions')
        if self.property_versions:
            for k in self.property_versions:
                if k:
                    k.validate()
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_versions is not None:
            result['propertyVersions'] = []
            for k in self.property_versions:
                result['propertyVersions'].append(k.to_map() if k else None)
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyVersions') is not None:
            self.property_versions = []
            for k in m.get('propertyVersions'):
                temp_model = GetListOfPropertyVersionsResponsePropertyVersions()
                self.property_versions.append(temp_model.from_map(k))
        if m.get('count') is not None:
            self.count = m.get('count')
        return self






class DeleteAPropertyPaths(TeaModel):
    def __init__(
        self,
        property_id: str = None,
    ):
        # {"en" : "ID of a property
        # ", "zh_CN": ""}
        self.property_id = property_id

    def validate(self):
        self.validate_required(self.property_id, 'property_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        return self


class DeleteAPropertyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAPropertyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAPropertyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAPropertyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAPropertyResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteAPropertyVersionPaths(TeaModel):
    def __init__(
        self,
        property_id: str = None,
        version: str = None,
    ):
        # {"en" : "ID of a property.", "zh_CN": "加速项目ID。"}
        self.property_id = property_id
        # {"en" : "A property version. It must be an integer value >=1. The Get a property version API also permits you to specify the word 'latest' to obtain the most recent version.", "zh_CN": "加速项目版本。必须是大于等于1的整数值。"}
        self.version = version

    def validate(self):
        self.validate_required(self.property_id, 'property_id')
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DeleteAPropertyVersionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAPropertyVersionRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAPropertyVersionRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAPropertyVersionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAPropertyVersionResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetAPropertyPaths(TeaModel):
    def __init__(
        self,
        property_id: str = None,
    ):
        # {"en" : "ID of a property
        # ", "zh_CN": ""}
        self.property_id = property_id

    def validate(self):
        self.validate_required(self.property_id, 'property_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        return self


class GetAPropertyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAPropertyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAPropertyRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAPropertyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAPropertyResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        version_in_production: int = None,
        version_in_staging: int = None,
        creation_time: str = None,
        last_update_time: str = None,
        versions: int = None,
        legacy_type: str = None,
    ):
        # {"en" : "Name of the property.
        # ", "zh_CN": "加速项目的名称。"}
        self.name = name
        # {"en" : "A description of the property.
        # ", "zh_CN": "加速项目的描述。"}
        self.description = description
        # {"en" : "Indicates the version of the property deployed to production. The field will be omitted if the property was not yet deployed.", "zh_CN": "部署到生产环境的加速项目版本。如果尚未部署加速项目，则将省略该字段。"}
        self.version_in_production = version_in_production
        # {"en" : "Indicates the version of the property deployed to staging. The field will be omitted if the property was not yet deployed.", "zh_CN": "部署到演练环境的加速项目版本。如果尚未部署加速项目，则将省略该字段。"}
        self.version_in_staging = version_in_staging
        # {"en" : "An RFC 3339 date indicating when the property was created.", "zh_CN": "RFC 3339格式的日期，表示创建加速项目的时间。"}
        self.creation_time = creation_time
        # {"en" : "An RFC 3339 date indicating when the property was last updated.", "zh_CN": "RFC 3339格式的日期，表示加速项目的最近更新时间。"}
        self.last_update_time = last_update_time
        # {"en" : "Number of versions of the property.
        # ", "zh_CN": "加速项目的版本数量。"}
        self.versions = versions
        # {"en" : "Enum: wsapro,webpro,vodpro,downloadpro 
        # Service type, one of wsapro, webpro, vodpro , downloadpro , 1523.", "zh_CN": "取值范围: wsapro,webpro,vodpro,downloadpro 
        # 服务类型，即全站加速，网页加速，点播加速及下载加速。"}
        self.legacy_type = legacy_type

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.version_in_production, 'version_in_production')
        self.validate_required(self.version_in_staging, 'version_in_staging')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.last_update_time, 'last_update_time')
        self.validate_required(self.versions, 'versions')
        self.validate_required(self.legacy_type, 'legacy_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.version_in_production is not None:
            result['versionInProduction'] = self.version_in_production
        if self.version_in_staging is not None:
            result['versionInStaging'] = self.version_in_staging
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.versions is not None:
            result['versions'] = self.versions
        if self.legacy_type is not None:
            result['legacyType'] = self.legacy_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('versionInProduction') is not None:
            self.version_in_production = m.get('versionInProduction')
        if m.get('versionInStaging') is not None:
            self.version_in_staging = m.get('versionInStaging')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('versions') is not None:
            self.versions = m.get('versions')
        if m.get('legacyType') is not None:
            self.legacy_type = m.get('legacyType')
        return self






class UpdateAPropertyPaths(TeaModel):
    def __init__(
        self,
        property_id: str = None,
    ):
        # {"en" : "ID of a property
        # ", "zh_CN": "加速项目ID。"}
        self.property_id = property_id

    def validate(self):
        self.validate_required(self.property_id, 'property_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        return self


class UpdateAPropertyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAPropertyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAPropertyRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
    ):
        # {"en" : "Name of the property.", "zh_CN": "加速项目的名称。"}
        self.name = name
        # {"en" : "Description of the property. If unspecified, the description will not be updated.", "zh_CN": "加速项目的描述。"}
        self.description = description

    def validate(self):
        self.validate_required(self.name, 'name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateAPropertyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAPropertyResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetAPropertyVersionPaths(TeaModel):
    def __init__(
        self,
        property_id: str = None,
        version: str = None,
    ):
        # {"en" : "ID of a property.", "zh_CN": "加速项目ID。"}
        self.property_id = property_id
        # {"en" : "A property version. It must be an integer value >=1. The Get a property version API also permits you to specify the word 'latest' to obtain the most recent version.", "zh_CN": "加速项目版本。必须是大于等于1的整数值，但可以指定'latest'来查询最新版本。"}
        self.version = version

    def validate(self):
        self.validate_required(self.property_id, 'property_id')
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetAPropertyVersionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAPropertyVersionRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAPropertyVersionRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAPropertyVersionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAPropertyVersionResponseConfigsRealTimeLogHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # {"en" : "Name of an HTTP header.", "zh_CN": "HTTP标头名称"}
        self.name = name
        # {"en" : "Value of an HTTP header.", "zh_CN": "HTTP标头值"}
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetAPropertyVersionResponseConfigsRealTimeLog(TeaModel):
    def __init__(
        self,
        log_url: str = None,
        sample_rate: int = None,
        escape: str = None,
        format: str = None,
        headers: List[GetAPropertyVersionResponseConfigsRealTimeLogHeaders] = None,
    ):
        # {"en" : "The URL that receives the notifications. It must begin with 'http' or 'https'. The server should support the POST method. This is a required field.", "zh_CN": "接收通知的服务器URL地址。必须以'http'或'https'开头。服务器须支持POST方法。这是必填字段。"}
        self.log_url = log_url
        # {"en" : "Default: 1 Range: [ 1 .. 65536 ] 
        # An integer between [1, 65536]. n means one notification for every n edge requests. 1 means every edge request will generate a notification. This is optional. Default is 1.", "zh_CN": "默认值: 1 取值范围: [ 1 .. 65536 ] 
        # 采样率。介于[1, 65536]之间的整数。n表示每n个边缘请求发送1条通知。1表示每个边缘请求都会发送。这是可选字段。默认值为1。"}
        self.sample_rate = sample_rate
        # {"en" : "Enum: json,none 
        # Specify json to enable JSON character escaping in variables or none to disable escaping.", "zh_CN": "取值范围: json,none 
        # 指定json以开启变量中的json字符转义。如果要禁用转义则指定none。"}
        self.escape = escape
        # {"en" : "This is a required field to specify the notification body to be sent to the remote server. It can be any printable text that can be sent in the body of an HTTP POST request. 
        # 
        # The following built-in variables can be used within the format field. They will be replaced with the actual values in the notifications.
        # <table><tr><th>Name</th><th>Description</th></tr><tr><td>$body_bytes_sent</td><td>Size of the response body.</td></tr><tr><td>$bytes_sent</td><td>Size of the response, including body, headers and response line.</td></tr><tr><td>$client_country_code</td><td>An ISO 3166-1 country code representing the country of the client request, for example, 'US'. 'ZZ' is returned if the country is unknown.</td></tr><tr><td>$client_real_ip</td><td>IP address of the client request.</td></tr><tr><td>$cookie_x</td><td>This lets you obtain any cookie named x.  For example, $cookie_account would retrieve the value of a cookie named 'account'.</td></tr><tr><td>$http_x</td><td>Obtain any HTTP header named x from the original request. The header name is converted to lower case with dashes replaced by underscores. For example, specify $http_user_agent to get the value of User-Agent.</td></tr><tr><td>$msec</td><td>Current unix time in seconds with millisecond precision.</td></tr><tr><td>$qtl_req_id</td><td>Unique identifier representing the request.</td></tr><tr><td>$request_uri</td><td>HTTP request URI</td></tr><tr><td>$request_method</td><td>The HTTP request method used to access the origin.</td></tr><tr><td>$request_time</td><td>Response time in milliseconds. It is the time between receiving the request's  first byte and serving the last byte of the response.</td></tr><tr><td>$sc_completed</td><td>1 to indicate the last byte of the object was served to the user, 0 otherwise.</td></tr><tr><td>$sc_initial</td><td>1 to indicate the first byte of the object was served to the user, 0 otherwise.</td></tr><tr><td>$scheme</td><td>Indicates the protocol of the user's request ('http' or https').</td></tr><tr><td>$sent_http_content_length</td><td>the original file size.</td></tr><tr><td>$sent_http_x</td><td>Obtain the value of an HTTP header named x that is returned in the response to the client. The header name should be converted to lower case with dashes replaced by underscores. For example, $sent_http_etag would give you the value of the ETag header.</td></tr><tr><td>$server_addr</td><td>IP address of the edge node serving the user's request.</td></tr><tr><td>$server_protocol</td><td>Indicates the version of HTTP used in the user's request, either 'HTTP/1.0', 'HTTP/1.1', or 'HTTP/2.0'.</td></tr><tr><td>$ssl_cipher</td><td>Indicates the cipher suite used for the TLS (SSL) connection.</td></tr><tr><td>$ssl_server_name</td><td>The hostname that a client initiating a TLS (SSL) connection is attempting to connect to. It is only sent by clients supporting SNI (Server Name Indication).</td></tr><tr><td>$ssl_protocol</td><td>Indicates the TLS version used for the TLS (SSL) connection. Example versions include 'SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2', and 'unknown'.</td></tr><tr><td>$status</td><td>An HTTP response code for the user's request.</td></tr><tr><td>$tcpinfo_rtt</td><td>The time in microseconds taken by a packet to travel to the destination and back.</td></tr></table>", "zh_CN": "该字段用来定义要发送到远程服务器的通知的格式。通知正文可以包括任何能在HTTP POST请求体中发送的可打印文本。这是必填字段。
        # 
        # 可以使用以下内置变量定义通知的格式。发送通知时，它们将被替换为实际值。
        # <table><tr><th>变量名称</th><th>描述</th></tr><tr><td>$body_bytes_sent</td><td>响应体大小。</td></tr><tr><td>$bytes_sent</td><td>响应的大小，包括响应体、响应头和响应行。</td></tr><tr><td>$client_country_code</td><td>客户端请求来源国家，以ISO 3166-1国家代码表示。例如'US'。如果国家/地区未知，则返回'ZZ'。</td></tr><tr><td>$client_real_ip</td><td>客户端请求的IP地址。</td></tr><tr><td>$cookie_x</td><td>获取某个cookie。例如，指定$cookie_account可获取名为'account'的cookie值。</td></tr><tr><td>$http_x</td><td>从原始请求中获取某个HTTP请求头。请求头名称需转换为小写，并用下划线替换连字符。例如，指定$http_user_agent来获取User-Agent的值。</td></tr><tr><td>$msec</td><td>当前unix时间，以毫秒为单位。</td></tr><tr><td>$qtl_req_id</td><td>请求的唯一标识符。</td></tr><tr><td>$request_uri</td><td>HTTP请求URI。</td></tr><tr><td>$request_method</td><td>用于访问源站的HTTP请求方法。</td></tr><tr><td>$request_time</td><td>响应时间，以毫秒为单位。这是从接收到请求的第一个字节到服务端响应最后一个字节之间的时间。</td></tr><tr><td>$sc_completed</td><td>1表示对象的最后一个字节已返回给用户，否则为0。</td></tr><tr><td>$sc_initial</td><td>1表示对象的第一个字节已返回给用户，否则为0。</td></tr><tr><td>$scheme</td><td>表示用户请求的协议（'http'或'https'）。</td></tr><tr><td>$sent_http_content_length</td><td>原始文件大小。</td></tr><tr><td>$sent_http_x</td><td>获取在对客户端响应中某个HTTP响应头的值。响应头名称需转换为小写，并用下划线替换连字符。例如，$sent_http_etag可获取ETag头的值。</td></tr><tr><td>$server_addr</td><td>为用户请求提供服务的边缘节点的IP地址。</td></tr><tr><td>$server_protocol</td><td>表示用户请求中使用的HTTP版本，可以是'HTTP/1.0'、'HTTP/1.1'或'HTTP/2.0'。</td></tr><tr><td>$ssl_cipher</td><td>表示用于TLS（SSL）连接的加密算法套件。</td></tr><tr><td>$ssl_server_name</td><td>客户端发起TLS（SSL）连接所要连接的域名。仅由支持SNI（Server Name Indication）的客户端发送。</td></tr><tr><td>$ssl_protocol</td><td>表示用于TLS（SSL）连接的TLS版本。例如，'SSLv3'、'TLSv1'、'TLSv1.1'、'TLSv1.2'和'unknown'。</td></tr><tr><td>$status</td><td>用户请求的HTTP状态码。</td></tr><tr><td>$tcpinfo_rtt</td><td>数据包往返目的地所用的时间，以微秒为单位。</td></tr></table>"}
        self.format = format
        # {"en" : "HTTP header names and values to be sent to the notification server. A header name can contain any alphanumeric character or hyphen, '-'. A header value can contain any printable characters. It can also include any of the built-in variables supported in the format field of the realTimeLog object.", "zh_CN": "需要发送到远程服务器的HTTP请求头名称和值。请求头名称可以包含任何字母，数字或连字符'-'。值可以包含任何可打印字符，也可以使用realTimeLog对象format字段中支持的任何内置变量。"}
        self.headers = headers

    def validate(self):
        self.validate_required(self.log_url, 'log_url')
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_url is not None:
            result['logUrl'] = self.log_url
        if self.sample_rate is not None:
            result['sampleRate'] = self.sample_rate
        if self.escape is not None:
            result['escape'] = self.escape
        if self.format is not None:
            result['format'] = self.format
        if self.headers is not None:
            result['headers'] = []
            for k in self.headers:
                result['headers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logUrl') is not None:
            self.log_url = m.get('logUrl')
        if m.get('sampleRate') is not None:
            self.sample_rate = m.get('sampleRate')
        if m.get('escape') is not None:
            self.escape = m.get('escape')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('headers') is not None:
            self.headers = []
            for k in m.get('headers'):
                temp_model = GetAPropertyVersionResponseConfigsRealTimeLogHeaders()
                self.headers.append(temp_model.from_map(k))
        return self


class GetAPropertyVersionResponseConfigsOriginsAuthentication(TeaModel):
    def __init__(
        self,
        method_name: str = None,
    ):
        # {"en" : "Authentication method.", "zh_CN": "鉴权方法。"}
        self.method_name = method_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method_name is not None:
            result['methodName'] = self.method_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        return self


class GetAPropertyVersionResponseConfigsOrigins(TeaModel):
    def __init__(
        self,
        name: str = None,
        servers: List[str] = None,
        supported_protocol: str = None,
        direct_connection: str = None,
        host_header: str = None,
        verify_origin: bool = None,
        authentication: GetAPropertyVersionResponseConfigsOriginsAuthentication = None,
        keep_alive_timeout: int = None,
        peer_failure_timeout: str = None,
        tls_certificate_id: str = None,
        shield: str = None,
    ):
        # {"en" : "^[a-zA-z0-9_] 
        # Name of an origin. It must be unique within this property.
        # ", "zh_CN": "^[a-zA-z0-9_] 
        # 源站名称，在此加速项目中必须唯一。"}
        self.name = name
        # {"en" : "Each entry should be a string consisting of an address optionally followed by one or more parameters, separated by space characters. The address can take one of the following three forms:
        # {hostname or IP address}
        # {hostname or IP address}:{http port}
        # {hostname or IP address}:{http port},{https port}
        # Values for the HTTP and HTTPS ports should be integers in the range [1,65535]. 
        # Even if the value of supportedProtocol is 'https', the HTTPS port has to be specified after the comma.
        # In the third form, one of the two ports can be empty.
        # 
        # Supported parameters are 'backup' and 'weight'.
        # 
        # 'backup' is used to indicate the server is a backup server. It will be used when the primary servers are unavailable.
        # 
        # 'weight' is a value in the range [1, 100]. The default value is 1. It lets you control the likelihood that one origin server will be used relative to another.
        # 
        # There should be at least one primary server defined; it does not have the 'backup' parameter.
        # 
        # Example:
        # ['www.abc.com weight=1', 'www1.abc.com:8080 weight=4', 'www2.abc.com:880,4443 backup']
        # 
        # This example specifies two primary servers which are used in a 1:4 ratio meaning one gets about 20% of the requests to origin while the other gets 80% of the requests. In addition, a backup server is specified.
        # ", "zh_CN": "源站服务器列表。每个条目为一个字符串，由一个地址与一个或多个参数组成，参数之间以空格分隔。地址可以采用以下三种形式之一：
        # {域名或IP地址}
        # {域名或IP地址}:{HTTP端口}
        # {域名或IP地址}:{HTTP端口},{HTTPS端口}
        # HTTP和HTTPS端口的值应为[1,65535]范围内的整数。
        # 即使supportedProtocol的值设为'https'，也必须在此处指定HTTPS端口。
        # 在第三种形式中，两个端口中的一个可以为空。
        # 
        # 支持的参数包括'backup'和'weight'。
        # 'backup'用于标识备份服务器。它将在主服务器不可用时使用。
        # 'weight'是范围[1,100]内的值，默认值为1，用来设置服务器权重，控制一台源站服务器相对于另一台被使用的可能性。
        # 每个源站应至少定义一个主服务器（即不带'backup'参数的服务器）。
        # 
        # 示例：
        # ['www.abc.com weight=1', 'www1.abc.com:8080 weight=4', 'www2.abc.com:880,4443 backup']
        # 
        # 此示例指定了两个主服务器和一个备份服务器，其中，主服务器的权重为1:4，表示第一个服务器将获得约20%的回源请求，而另一个将获得约80%。"}
        self.servers = servers
        # {"en" : "Enum: http,https,both 
        # This optional field indicates the protocol supported by the origin server. If this property has a certificate attached to it, the value can be set to http if the allowProtocolDowngrade field is also set to true.", "zh_CN": "取值范围: http,https,both 
        # 此可选字段表示源站服务器支持的协议。如果此加速项目附加了证书，且allowProtocolDowngrade字段也设置为true，则可以将该值设置为http。"}
        self.supported_protocol = supported_protocol
        # {"en" : "Default: auto 
        # Optional. This parameter tells us how important it is to directly go to this origin without going through any intermediate cache to fetch content. The values can be 'noDirect', 'auto', 'alwaysDirect'. 
        # 
        # 'noDirect' means we always go through at least one intermediate cache. Customers who care particularly about the origin's workload can use this option. Our cache scheduler will dynamically pick the intermediate cache based on performance and resource availability.
        # 
        # 'auto' means the cache scheduler will make the choice dynamically based on performance and resource availability. This is the default behavior if not specified.
        # 
        # 'alwaysDirect' means we always directly connect to this origin.
        # ", "zh_CN": "默认值: auto 
        # 此可选字段用来指定回源方式，可以是'noDirect'、'auto'、'alwaysDirect'。
        # 
        # 'noDirect'指总是通过至少一个中间缓存节点回源。对于特别关心源站负载的客户可以使用此选项。我们的调度程序将根据性能和资源可用性动态选择中间缓存节点。
        # 'alwaysDirect'指总是直接回源。
        # 'auto'指自动选择直接回源或通过中间缓存节点回源。调度程序将根据性能和资源可用性动态做出选择。该字段未指定时，采用此默认行为。"}
        self.direct_connection = direct_connection
        # {"en" : "Optional. It should be a valid hostname. It will also be used as the SNI servername when contacting the HTTPS origin. We also allow it to be an nginx variable that begins with $ followed by [a-z_]{3,60}. Nginx variable names are case insensitive, so we only allow lowercase characters.
        # If not specified, the value of the HOST header in the request will be used. 
        # 
        # One constraint is that if 'aswS3' is specified for origin authentication, the value of hostHeader cannot be a variable or empty. It has to be a valid Amazon S3 hostname. Refer to https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html", "zh_CN": "可选，用来指定回源HOST头部。必须是有效的域名。当连接HTTPS源站时，该值也作为SNI域名。可以用nginx变量来指定，变量以'$'开头，后跟[a-z_]{3,60}。Nginx变量名不区分大小写，因此我们只允许小写字符。
        # 如果未指定，将使用请求中的HOST请求头的值。
        # 
        # 注意：如果指定了'awsS3'作为回源鉴权参数，则hostHeader的值不能为变量或为空，而必须是有效的Amazon S3主机名。参考：https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html"}
        self.host_header = host_header
        # {"en" : "Default: False 
        # Optional. It controls whether the cache will validate the certificate of the origin.", "zh_CN": "默认值: False 
        # 可选。用来设定CDN缓存节点是否验证源站证书。"}
        self.verify_origin = verify_origin
        # {"en" : "Optional. It is a structure to specify the parameters, such as password, for authentication with the origin servers. It should have at least one field: 'methodName', which should be a string indicating one of the predefined authentication methods. The only valid value at this time is 'awsS3'. When 'awsS3' is used, the following parameters are required:
        # awsS3.region
        # awsS3.accessKey
        # awsS3.secretKey
        # Also, the value of the hostHeader field cannot be a variable or empty. It must be a valid Amazon S3 hostname.
        # 
        # Example:
        # 
        # {'methodName':'awsS3',
        # 'awsS3':{
        # 'region':'us-west-1',
        # 'accessKey':'sdnu2932',
        # 'secretKey':'d12345678abcdefghi'
        # }}
        # ", "zh_CN": "可选。用于指定与源服务器进行身份验证（回源鉴权）的相关参数（如密码）。必须至少有'methodName'（字符串）字段，用来指定预定义的鉴权方法。目前仅支持源站为AWS S3的回源鉴权，因此唯一有效的值是'awsS3'。使用'awsS3'时，需要提供以下参数：
        # awsS3.region
        # awsS3.accessKey
        # awsS3.secretKey
        # 此外，hostHeader字段的值不能为变量或为空，必须是有效的Amazon S3主机名。
        # 
        # 示例：
        # 
        # {'methodName':'awsS3',
        # 'awsS3':{
        # 'region':'us-west-1',
        # 'accessKey':'sdnu2932',
        # 'secretKey':'d12345678abcdefghi'
        # }}
        # "}
        self.authentication = authentication
        # {"en" : "Default: 60 Range: [ 5 .. 600 ] 
        # Timeout in seconds during which an idle keepalive connection to an upstream server will stay open. A service quota setting of maxUpstreamKeepaliveTimeOut can change the maximum permitted value.", "zh_CN": "默认值: 60 取值范围: [ 5 .. 600 ] 
        # 该字段用于指定CDN Pro服务器和源站建连的Keep-Alive超时时间，单位为秒。通过maxUpstreamKeepaliveTimeOut 该服务设置项可以更改允许的最大值。如果需要调整最大值，请联系我们的技术支持。"}
        self.keep_alive_timeout = keep_alive_timeout
        # {"en" : "
        # This setting allows you to specify the number of unsuccessful attempts to reach one of the origin's IP addresses or peers before it is marked as unavailable for a period of time designated by the timeout. If all peers of all servers are unavailable, requests for content from the origin will receive an immediate 502 HTTP response. By default, six attempts to a peer are made, after which a one-second timeout applies to that peer. To disable this feature, set peerFailureTimeout to 'off'.", "zh_CN": "
        # 该字段用于设置源站故障剔除。开启此功能后，当连接某个源站服务器的失败次数达到设定阈值，该源站服务器将被标记为不可用，并保持该状态直到设定的超时时长。失败次数阈值和超时时长分别通过failureThreshold参数和timeout参数设置。CDN Pro回源时将剔除不可用的源站服务器。如果所有源站服务器都被标记为不可用，则对应的请求将立即响应502状态码。默认情况下，当连接某个源站服务器连续失败6次之后，该服务器将被标记为不可用，超时时长为1秒。如果要禁用此功能，请将peerFailureTimeout设置为'off'。开启源站故障剔除配置示例：<code>{'peerFailureTimeout':{'failureThreshold':10,'timeout':3}}</code>"}
        self.peer_failure_timeout = peer_failure_timeout
        # {"en" : "Refers to a certificate used to authenticate with the origin server. This certificate must also be deployed.", "zh_CN": "用于验证源站服务器的证书，该证书同样必须被部署。"}
        self.tls_certificate_id = tls_certificate_id
        # {"en" : "Refers to the ID of an origin shield representing a set of servers that will make requests to your origin servers rather than the CDN Pro edge servers. This can help further reduce traffic to your origin. This is an advanced feature that can be enabled by contacting our support team. The origin shields API provides a list of available shields along with their IP addresses. It is best to select a shield whose region is closest to your origin servers. Use of a shield in China requires your property have 'hasBeian' set to true. If your origin servers have an access control list, add the IPs of the shield you choose to use.", "zh_CN": "指定某个源站盾（origin shield）的ID。使用源站盾功能后，所有回源请求都会通过源站盾中转回源，这可以帮助收敛回源流量。源站盾是高级功能，如需使用请联系我们的技术支持开通。可通过调用‘获取源站盾列表’接口查询可用的源站盾及其对应的IP地址。您可根据源站的位置，选择合适的源站盾。如果您需使用中国大陆的源站盾，则该加速项目的所有域名必须已取得备案。如果您的源站开启了访问控制，请将所选择源站盾的IP地址加入白名单。"}
        self.shield = shield

    def validate(self):
        if self.authentication:
            self.authentication.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.servers is not None:
            result['servers'] = self.servers
        if self.supported_protocol is not None:
            result['supportedProtocol'] = self.supported_protocol
        if self.direct_connection is not None:
            result['directConnection'] = self.direct_connection
        if self.host_header is not None:
            result['hostHeader'] = self.host_header
        if self.verify_origin is not None:
            result['verifyOrigin'] = self.verify_origin
        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()
        if self.keep_alive_timeout is not None:
            result['keepAliveTimeout'] = self.keep_alive_timeout
        if self.peer_failure_timeout is not None:
            result['peerFailureTimeout'] = self.peer_failure_timeout
        if self.tls_certificate_id is not None:
            result['tlsCertificateId'] = self.tls_certificate_id
        if self.shield is not None:
            result['shield'] = self.shield
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('servers') is not None:
            self.servers = m.get('servers')
        if m.get('supportedProtocol') is not None:
            self.supported_protocol = m.get('supportedProtocol')
        if m.get('directConnection') is not None:
            self.direct_connection = m.get('directConnection')
        if m.get('hostHeader') is not None:
            self.host_header = m.get('hostHeader')
        if m.get('verifyOrigin') is not None:
            self.verify_origin = m.get('verifyOrigin')
        if m.get('authentication') is not None:
            temp_model = GetAPropertyVersionResponseConfigsOriginsAuthentication()
            self.authentication = temp_model.from_map(m['authentication'])
        if m.get('keepAliveTimeout') is not None:
            self.keep_alive_timeout = m.get('keepAliveTimeout')
        if m.get('peerFailureTimeout') is not None:
            self.peer_failure_timeout = m.get('peerFailureTimeout')
        if m.get('tlsCertificateId') is not None:
            self.tls_certificate_id = m.get('tlsCertificateId')
        if m.get('shield') is not None:
            self.shield = m.get('shield')
        return self


class GetAPropertyVersionResponseConfigsVideoSeek(TeaModel):
    def __init__(
        self,
        start_parameter: str = None,
        end_parameter: str = None,
    ):
        # {"en" : "Range: [ 1 .. 31 ] characters 
        # Name of the query parameter indicating the starting offset in bytes of the content to fetch. The parameter name should begin with a letter (a-z, A-Z) and may be followed by up to 30 letters and numbers.", "zh_CN": "取值范围: [ 1 .. 31 ] 字符 
        # 查询参数的名称，用来指定要获取的内容的起始位置（以字节计算）。参数名称应以字母（a-z，A-Z）开头，后面最多可以有30个字母和数字。"}
        self.start_parameter = start_parameter
        # {"en" : "Range: [ 0 .. 31 ] characters 
        # Name of the query parameter indicating the ending offset of the content to fetch. The parameter name should begin with a letter (a-z, A-Z) and may be followed by up to 30 letters and numbers.", "zh_CN": "取值范围: [ 0 .. 31 ] 字符 
        # 查询参数的名称，用来指定要获取的内容的结束位置（以字节计算）。参数名称应以字母（a-z，A-Z）开头，后面最多可以有30个字母和数字。"}
        self.end_parameter = end_parameter

    def validate(self):
        self.validate_required(self.start_parameter, 'start_parameter')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_parameter is not None:
            result['startParameter'] = self.start_parameter
        if self.end_parameter is not None:
            result['endParameter'] = self.end_parameter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startParameter') is not None:
            self.start_parameter = m.get('startParameter')
        if m.get('endParameter') is not None:
            self.end_parameter = m.get('endParameter')
        return self


class GetAPropertyVersionResponseConfigsAccessControlRulesConditions(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        hostname: str = None,
        uri: str = None,
        server_regions: List[str] = None,
        client_regions: List[str] = None,
        client_ip_range: List[str] = None,
    ):
        # {"en" : "Enum: https,http 
        # Indicates whether the incoming request uses HTTP or HTTPS.", "zh_CN": "取值范围: https,http 
        # 客户端请求的协议，HTTP或HTTPS。"}
        self.scheme = scheme
        # {"en" : "Indicates the hostname requested. It must be one of the hostnames defined in the property.", "zh_CN": "请求对应的加速域名。必须是加速项目中定义的加速域名之一。"}
        self.hostname = hostname
        # {"en" : "Range: <= 500 characters 
        # The URI begins with '/' and can end with '*' for prefix matching. ", "zh_CN": "取值范围: <= 500 字符 
        # 用于前缀匹配的URI，以'/'开头，可以以'*'结尾。"}
        self.uri = uri
        # {"en" : "An array of ISO-3166-1 alpha-2 codes indicating the countries of the servers, for example, 'US' to represent 'United States of America'.", "zh_CN": "服务器所在区域，以ISO-3166-1 两位国家代码表示。例如，'US'代表'美国'。"}
        self.server_regions = server_regions
        # {"en" : "An array of ISO-3166-1 alpha-2 codes indicating one or more countries which are the source of the client requests, for example, 'CN' to represent 'China'.", "zh_CN": "客户端请求来源区域，以ISO-3166-1 两位国家代码表示。例如，'CN'代表'中国'。"}
        self.client_regions = client_regions
        # {"en" : "Indicates the starting and ending IP addresses of the client requests to match against. They must be in IPv4 or IPv6 format.", "zh_CN": "用于指定要匹配的客户端请求的开始和结束IP地址。必须是IPv4或IPv6格式。"}
        self.client_ip_range = client_ip_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.uri is not None:
            result['uri'] = self.uri
        if self.server_regions is not None:
            result['serverRegions'] = self.server_regions
        if self.client_regions is not None:
            result['clientRegions'] = self.client_regions
        if self.client_ip_range is not None:
            result['clientIpRange'] = self.client_ip_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('serverRegions') is not None:
            self.server_regions = m.get('serverRegions')
        if m.get('clientRegions') is not None:
            self.client_regions = m.get('clientRegions')
        if m.get('clientIpRange') is not None:
            self.client_ip_range = m.get('clientIpRange')
        return self


class GetAPropertyVersionResponseConfigsAccessControlRulesAction(TeaModel):
    def __init__(
        self,
        status: str = None,
        message: str = None,
    ):
        # {"en" : "Indicates the HTTP status code to respond with. It must be in the range 300-309, 400-409, or 500-509 to indicate a redirection or error.", "zh_CN": "响应的HTTP状态码，范围必须在300-309、400-409或500-509之间，分别表示重定向或错误。"}
        self.status = status
        # {"en" : "Range: <= 200 characters 
        # If the value of the status field is in the range 300-309, the message field's value will be placed in a Location HTTP header returned to the client. If the status is in the range 400-409 or 500-509, the value will be returned in the response body to the client.", "zh_CN": "取值范围: <= 200 字符 
        # 如果status字段的值在300-309范围内，message字段的值将在返回给客户端的Location响应头中。如果status字段的值在400-409或500-509范围内，则message字段的值将在返回给客户端的响应体中。"}
        self.message = message

    def validate(self):
        self.validate_required(self.status, 'status')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetAPropertyVersionResponseConfigsAccessControlRules(TeaModel):
    def __init__(
        self,
        id: str = None,
        conditions: GetAPropertyVersionResponseConfigsAccessControlRulesConditions = None,
        action: GetAPropertyVersionResponseConfigsAccessControlRulesAction = None,
    ):
        # {"en" : "Range: [ 0 .. 60 ] characters 
        # An optional ID for the access control rule.", "zh_CN": "取值范围: [ 0 .. 60 ] 字符 
        # 访问控制规则ID。"}
        self.id = id
        # {"en" : "Specify the conditions that the incoming request must match. At least one condition must be specified. If multiple are specified, all must match.", "zh_CN": "指定客户端请求必须匹配的条件。必须至少指定一个条件。如果指定了多个条件，则必须全部匹配。"}
        self.conditions = conditions
        # {"en" : "Indicates the action to take in response to a request that matches the conditions of the access control rule.", "zh_CN": "对于匹配到以上条件的请求所采取的相应操作。"}
        self.action = action

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.conditions is not None:
            result['conditions'] = self.conditions.to_map()
        if self.action is not None:
            result['action'] = self.action.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('conditions') is not None:
            temp_model = GetAPropertyVersionResponseConfigsAccessControlRulesConditions()
            self.conditions = temp_model.from_map(m['conditions'])
        if m.get('action') is not None:
            temp_model = GetAPropertyVersionResponseConfigsAccessControlRulesAction()
            self.action = temp_model.from_map(m['action'])
        return self


class GetAPropertyVersionResponseConfigsExtraServicePorts(TeaModel):
    def __init__(
        self,
        http: List[str] = None,
        https: List[str] = None,
    ):
        # {"en" : "This is a list of ports other than 80 which are used to handle HTTP requests. The available values can be found in the systemConfigs API's response. If you need another port, please contact our support team.", "zh_CN": "指定用于处理HTTP请求的端口列表（80端口除外）。可通过调用'获取系统配置'接口来查询系统支持的端口。如果您需要开通其他端口，请联系技术支持。"}
        self.http = http
        # {"en" : "This is a list of ports other than 443 which are used to handle HTTPS requests. The available values can be found in the systemConfigs API's response. If you need another port, please contact our support team.", "zh_CN": "指定用于处理HTTPS请求的端口列表（443端口除外）。可通过调用'获取系统配置'接口来查询系统支持的端口。如果您需要开通其他端口，请联系技术支持。"}
        self.https = https

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http is not None:
            result['http'] = self.http
        if self.https is not None:
            result['https'] = self.https
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http') is not None:
            self.http = m.get('http')
        if m.get('https') is not None:
            self.https = m.get('https')
        return self


class GetAPropertyVersionResponseConfigs(TeaModel):
    def __init__(
        self,
        description: str = None,
        cache_key_hostname: str = None,
        hostnames: List[str] = None,
        real_time_log: GetAPropertyVersionResponseConfigsRealTimeLog = None,
        edge_logic: str = None,
        has_beian: bool = None,
        redirect_http_to_https: str = None,
        origins: List[GetAPropertyVersionResponseConfigsOrigins] = None,
        syntax_version: int = None,
        disable_http_2: bool = None,
        scheme_in_cache_key: bool = None,
        tls_max_version: str = None,
        load_balancer_hash_key: str = None,
        tls_certificate_id: str = None,
        tls_min_version: str = None,
        tls_ciphers: str = None,
        allow_protocol_downgrade: bool = None,
        tls_certificate_id_1: int = None,
        video_seek: GetAPropertyVersionResponseConfigsVideoSeek = None,
        tls_session_timeout: int = None,
        enable_ocsp_stapling: bool = None,
        beian_content_type: int = None,
        access_control_rules: List[GetAPropertyVersionResponseConfigsAccessControlRules] = None,
        disable_cert_automation: bool = None,
        cache_key_uri: str = None,
        extra_service_ports: GetAPropertyVersionResponseConfigsExtraServicePorts = None,
        load_balancer_logic: str = None,
        tls_0rtt: bool = None,
    ):
        # {"en" : "A description of the version.
        # ", "zh_CN": "版本描述。"}
        self.description = description
        # {"en" : "Range: <= 80 characters ^[a-z.-_]+\
        # The cachekey hostname must be a string made of lowercase letters, digits, dot, dash, and underscore. If not specified, the incoming Host header value will be used and the cache will not be shared across different hostnames in this property.
        # ", "zh_CN": "取值范围: <= 80 字符 ^[a-z.-_]+\
        # 用于缓存键（Cache Key）的主机名必须是由小写字母、数字、点、连字符和下划线组成的字符串。如果未指定，默认将使用传入的Host请求头值，并且此加速项目中的不同加速域名之间不共享缓存。"}
        self.cache_key_hostname = cache_key_hostname
        # {"en" : "Hostnames associated with the property. A valid value is a fully qualified hostname such as www.domain.com or a wildcard hostname such as *.domain.com. Any given hostname can only be in one deployed property at a particular time. However, a wildcard hostname is permitted to overlap other hostnames you own.", "zh_CN": "与加速项目关联的加速域名。必须是FQDN完全限定域名（如 www.domain.com），或泛域名（如*.domain.com）。
        # 同一个加速域名在同一时间只能存在于一个已部署的加速项目中，但泛域名可以与关联的完全限定域名一同部署。"}
        self.hostnames = hostnames
        # {"en" : "This optional field allows you to configure notifications about client requests to be sent to a remote server. It can be used only if you have access to our realtime_log_switch directive. Please contact our support team if you require this feature.", "zh_CN": "此可选字段用来配置发送消息通知（即实时日志）到您的远程服务器。当有客户端请求访问您的加速域名时，将触发通知。这是高级功能，如果您需要此功能，请联系我们的技术支持开通。"}
        self.real_time_log = real_time_log
        # {"en" : "Range: <= 65530 characters 
        # Refer to Edge Logic Introduction.", "zh_CN": "取值范围: <= 65530 字符 
        # 自定义边缘逻辑。参考边缘逻辑介绍。"}
        self.edge_logic = edge_logic
        # {"en" : "Default: False 
        # The value indicates whether all the hostnames in this property have Beian license on file with the Chinese government. This is required to serve this property from servers in mainland China. A value of false means servers outside of mainland China will be used to distribute content to visitors in China. If set to true you must also specify the content type in the beianContentType field.", "zh_CN": "默认值: False 
        # 此加速项目中的所有加速域名是否都已获得中国政府的ICP备案。只有获取备案的域名才能使用中国大陆节点来提供服务。如果设置为true，还必须在beianContentType字段中指定内容类型。"}
        self.has_beian = has_beian
        # {"en" : "Default: False 
        # This field can be set to either a boolean value or a string. If the value is set to true, the server will redirect all HTTP requests to HTTPS using status code 301. You can also specify string values '302', '307', or '308' instead if you wish to return a different status code when a request is redirected.", "zh_CN": "默认值: False 
        # 此字段可以设置为布尔值或字符串。如果设置为true，则CDN Pro服务器会将所有HTTP请求重定向到HTTPS，并返回301状态码。如果您希望在重定向请求时返回不同的状态码，可在此处指定需要的状态码，如'302'、'307'或'308'。"}
        self.redirect_http_to_https = redirect_http_to_https
        # {"en" : "Describes the origin servers for the property's content.", "zh_CN": "描述加速项目对应的源站。"}
        self.origins = origins
        # {"en" : "Default: 1 
        # The value must be set to 1 at this time.", "zh_CN": "默认值: 1 
        # 当前仅允许值为1。"}
        self.syntax_version = syntax_version
        # {"en" : "Default: False 
        # Set to true to disable support for HTTP/2 and support only HTTP 1.1.", "zh_CN": "默认值: False 
        # 当值为true时，禁用对HTTP/2的支持，仅支持HTTP/1.1。"}
        self.disable_http_2 = disable_http_2
        # {"en" : "Default: False 
        # Specifies whether the scheme ('http' or 'https') should be included in the cache key. Default behavior is false. Set to true if the content is known to be different for different schemes.
        # ", "zh_CN": "默认值: False 
        # 指定缓存键（Cache Key）是否区分协议（'http'或'https'）。默认为false。如果不同协议响应的内容不同，则设置为true。"}
        self.scheme_in_cache_key = scheme_in_cache_key
        # {"en" : "Enum: 1.1,1.2,1.3 
        # Default: 1.3 
        # Maximum supported TLS version.", "zh_CN": "取值范围: 1.1,1.2,1.3 
        # 默认值: 1.3 
        # 支持的TLS最高版本。"}
        self.tls_max_version = tls_max_version
        # {"en" : "Range: <= 100 characters 
        # Multiple tiers of load balancing are used in our CDN pops to distribute the client requests to different servers. We are using consistent hashing in many of those places. By default, the URL is used as the hash key, which should be good enough in most cases. Here you can define additional variables to be added to the hash key to distribute the requests more evenly. One typical use case is when all requests carry the same URL, but use a particular header to indicate the resources. 
        # 
        # This is an optional field. The default value is an empty string. A valid value is a string meeting the following criteria:
        # 
        # Consists of alphanumeric characters, underscore _, equal sign =, dollar sign $, and ampersand sign &.
        # The variable names can only be in one of the following formats: $http_name, $cookie_name, or $arg_name.
        # At least one variable must be specified. No more than three are permitted.
        # The total length should be no more than 100 characters.
        # 
        # The validator will treat any dollar sign and the string after it (before any = or & or $) as a variable. 
        # 
        # Here are some examples of valid values:
        # <table><tr><td>$http_abc</td></tr><tr><td>abc=$http_abc&def=$http_def&c_123=$cookie_123</td></tr><tr><td>abc=$http_abc=$http_def</td></tr><tr><td>$http_abc&$http_def</td></tr><tr><td>=$http_abd&</td></tr><tr><td>&&abc==$http_abc&&&===qwer</td></tr></table>
        # ", "zh_CN": "取值范围: <= 100 字符 
        # 我们的CDN使用了多层负载均衡架构，将客户端请求分发到不同的服务器。我们在架构中多处使用到一致性哈希。默认情况下，URL被用作哈希键，这对于大多数情况都适用。您可以在这里定义要添加到哈希键的其他变量，以更均匀地分配请求。一个典型的使用场景是，所有请求都携带相同的URL，但使用特定的请求头来区分资源。
        # 
        # 这是一个可选字段，默认值为空字符串。必须满足以下条件：
        # 
        # 由字母、数字、下划线_、等号=、美元符号$和符号&组成。
        # 变量名只能采用以下格式之一：$http_name、$cookie_name、$arg_name。
        # 必须至少指定一个变量，不允许超过三个。
        # 总长度不得超过100个字符。
        # 
        # 我们的配置验证器将把任何美元符号及其后的字符串（在任何=或&或$之前）视为变量。
        # 
        # 以下是一些有效值的示例：
        # <table><tr><td>$http_abc</td></tr><tr><td>abc=$http_abc&def=$http_def&c_123=$cookie_123</td></tr><tr><td>abc=$http_abc=$http_def</td></tr><tr><td>$http_abc&$http_def</td></tr><tr><td>=$http_abd&</td></tr><tr><td>&&abc==$http_abc&&&===qwer</td></tr></table>"}
        self.load_balancer_hash_key = load_balancer_hash_key
        # {"en" : "Refers to a certificate. It is invalid to only set the tlsCertificateId1 field without setting the tlsCertificateId field. If tlsCertificateId is not set, HTTPS will not be enabled for this property. This is a feature to enable you to specify two certificates of different types, i.e. one RSA, one EC. If two certificates of the same type are specified, the one specified by tlsCertificateId will be ignored. ", "zh_CN": "该加速项目用到的证书ID。仅设置tlsCertificateId1字段而不设置tlsCertificateId字段是无效的。如果未设置tlsCertificateId，则不会为此加速项目启用HTTPS。此功能允许您指定两个不同类型的证书，即一个RSA，一个EC。如果指定了两个相同类型的证书，则将忽略tlsCertificateId指定的证书。 "}
        self.tls_certificate_id = tls_certificate_id
        # {"en" : "Enum: 1.1,1.2,1.3,1 
        # Default: 1 
        # Minimum required TLS version.", "zh_CN": "取值范围: 1.1,1.2,1.3,1 
        # 默认值: 1 
        # 所需的TLS最低版本。"}
        self.tls_min_version = tls_min_version
        # {"en" : "Range: <= 2040 characters 
        # Any cipher list supported by 'openssl ciphers'. See https://www.openssl.org/docs/manmaster/man1/ciphers.html
        # ", "zh_CN": "取值范围: <= 2040 字符 
        # 'openssl ciphers'支持的任何加密算法套件。参考：https://www.openssl.org/docs/manmaster/man1/ciphers.html"}
        self.tls_ciphers = tls_ciphers
        # {"en" : "Default: False 
        # This setting applies only if the property has an attached certificate allowing client requests to use HTTPS. If the value of allowProtocolDowngrade is false, we require all the origin servers to support HTTPS. If the value is true, we allow origins that support only HTTP, which reduces security.
        # ", "zh_CN": "默认值: False 
        # 是否允许协议降级。仅当加速项目中存在允许客户端使用HTTPS请求的证书时，此设置才适用。如果allowProtocolDowngrade的值为false，则要求所有源服务器支持HTTPS。如果值为true，则允许仅支持HTTP的源，但这会降低安全性。"}
        self.allow_protocol_downgrade = allow_protocol_downgrade
        # {"en" : "Refers to a certificate. It is invalid to only set the tlsCertificateId1 field without setting the tlsCertificateId field. If tlsCertificateId is not set, HTTPS will not be enabled for this property. This is a feature to enable you to specify two certificates of different types, i.e. one RSA, one EC. If two certificates of the same type are specified, the one specified by tlsCertificateId will be ignored. 
        # ", "zh_CN": "指该加速项目用到的证书ID。仅设置tlsCertificateId1字段而不设置tlsCertificateId字段是无效的。如果未设置tlsCertificateId，则不会为此加速项目启用HTTPS。此功能允许您指定两个不同类型的证书，即一个RSA，一个EC。如果指定了两个相同类型的证书，则将忽略tlsCertificateId指定的证书。"}
        self.tls_certificate_id_1 = tls_certificate_id_1
        # {"en" : "This object allows you to support video players requesting partial content through query string parameters. If you specify videoSeek, you must enter a value for startParameter.", "zh_CN": "此对象用来支持视频播放器通过指定查询参数来请求部分内容。当videoSeek对象存在时，必须为startParameter设置一个值。"}
        self.video_seek = video_seek
        # {"en" : "Default: 1800 Range: [ 300 .. 86400 ] 
        # Lifespan of TLS session ticket in seconds.", "zh_CN": "默认值: 1800 取值范围: [ 300 .. 86400 ] 
        # TLS会话ticket的有效期（秒）。"}
        self.tls_session_timeout = tls_session_timeout
        # {"en" : "Default: False 
        # Enables Online Certificate Status Protocol (OCSP) stapling to check the revocation status of digital certificates. (Refer to https://en.wikipedia.org/wiki/OCSP_stapling)", "zh_CN": "默认值: False 
        # 是否启用在线证书状态协议（OCSP）装订以检查数字证书的吊销状态。参考：https://en.wikipedia.org/wiki/OCSP_stapling"}
        self.enable_ocsp_stapling = enable_ocsp_stapling
        # {"en" : "Range: [ 1 .. 24 ] 
        # If you are planning to distribute content through servers in mainland China, you will need to set the hasBeian field to true and also indicate the type of content you are distributing. Enter the value that best corresponds to your content:
        # 
        # <table><tr><th>Value</th><th>Content Type</th></tr><tr><td>1</td><td>Instant Messaging</td></tr><tr><td>2</td><td>Search Engine</td></tr><tr><td>3</td><td>Web Portal</td></tr><tr><td>4</td><td>Online Postal Service</td></tr><tr><td>5</td><td>Online News</td></tr><tr><td>6</td><td>Blog</td></tr><tr><td>7</td><td>Advertisement</td></tr><tr><td>8</td><td>Organization Web Portal</td></tr><tr><td>9</td><td>Shopping</td></tr><tr><td>10</td><td>Online Payment</td></tr><tr><td>11</td><td>Online Bank</td></tr><tr><td>12</td><td>Online Stock Market</td></tr><tr><td>13</td><td>Online Gaming</td></tr><tr><td>14</td><td>Online Music</td></tr><tr><td>15</td><td>Online Movie</td></tr><tr><td>16</td><td>Online Picture</td></tr><tr><td>17</td><td>Software Download</td></tr><tr><td>18</td><td>Job Hunting</td></tr><tr><td>19</td><td>Online Dating</td></tr><tr><td>20</td><td>Online Real Property</td></tr><tr><td>21</td><td>Online Education</td></tr><tr><td>22</td><td>Web Design</td></tr><tr><td>23</td><td>WAP</td></tr><tr><td>24</td><td>Others</td></tr></table>", "zh_CN": "取值范围: [ 1 .. 24 ] 
        # 如果您的域名已获得备案，希望通过中国大陆的服务器分发内容，则需要将hasBeian字段设置为true，并说明您分发的内容类型。请选择与您的内容最匹配的值：
        # 
        # <table><tr><th>值</th><th>内容类型</th></tr><tr><td>1</td><td>即时通信</td></tr><tr><td>2</td><td>搜索引擎</td></tr><tr><td>3</td><td>综合门户</td></tr><tr><td>4</td><td>网上邮局</td></tr><tr><td>5</td><td>网络新闻</td></tr><tr><td>6</td><td>博客/个人空间</td></tr><tr><td>7</td><td>网络广告</td></tr><tr><td>8</td><td>单位门户网站</td></tr><tr><td>9</td><td>网络购物</td></tr><tr><td>10</td><td>网上支付</td></tr><tr><td>11</td><td>网上银行</td></tr><tr><td>12</td><td>网上炒股</td></tr><tr><td>13</td><td>网络游戏</td></tr><tr><td>14</td><td>网络音乐</td></tr><tr><td>15</td><td>网络影视</td></tr><tr><td>16</td><td>网络图片</td></tr><tr><td>17</td><td>软件下载</td></tr><tr><td>18</td><td>网上求职</td></tr><tr><td>19</td><td>在线交友</td></tr><tr><td>20</td><td>网上房产</td></tr><tr><td>21</td><td>网络教育</td></tr><tr><td>22</td><td>网站建设</td></tr><tr><td>23</td><td>WAP</td></tr><tr><td>24</td><td>其他</td></tr></table>"}
        self.beian_content_type = beian_content_type
        # {"en" : "Specify one or more access control rules to restrict access to your content. More advanced configuration can be done using Edge Logic. These access control rules take precedence over Edge Logic if both are defined.", "zh_CN": "指定一个或多个访问控制规则以限制对内容的访问。可以使用边缘逻辑进行更高级的配置。此处定义的访问控制规则，优先级高于边缘逻辑。"}
        self.access_control_rules = access_control_rules
        # {"en" : "Default: False 
        # By default, CDN Pro takes control of the contents under the /.well-known/{acme-challenge, pki-validation} directories to support certificate auto-renew for properties. If for any reason you need to manage these two directories by yourself on the origin, for example, to implement your own certificate auto-renew mechanism, you can use this configuration option to disable the default behavior by setting its value to true. For more information about our support for certificate auto-renewal, refer to the description of the autoRenew field in the Create a certificate API.", "zh_CN": "默认值: False 
        # 默认情况下，CDN Pro控制/.well-known/{acme-challenge, pki-validation}目录下的内容，以支持加速项目的证书自动更新功能。如果您需要自己在源站管理这两个目录，例如，为了实现您自己的证书自动更新机制，您可以将此字段设置为true来禁用默认行为。关于证书自动更新的更多信息，请参考'创建证书'接口中autoRenew字段的说明。"}
        self.disable_cert_automation = disable_cert_automation
        # {"en" : "Enum: preRewrite,postRewrite 
        # Default: preRewrite 
        # This setting controls how the URI of the incoming request is incorporated into the cache key if you use a 'rewrite' directive in the property's Edge Logic. The default value, 'preRewrite', puts the unmodified URI into the cache key while 'postRewrite' uses the modified URI. If your rewrite directive converts multiple different URIs into the same value, using 'postRewrite' may result in a higher cache hit ratio.", "zh_CN": "取值范围: preRewrite,postRewrite 
        # 默认值: preRewrite 
        # 如果在加速项目的边缘逻辑中使用了'rewrite'指令，可使用该字段来控制客户端请求的URI如何合并到缓存键（Cache Key）中 。默认值'preRewrite'指将改写前的URI放入缓存键，而'postRewrite'则使用改写后的URI。如果您的'rewrite'指令将多个不同的URI改写为相同的值，则使用'postRewrite'可以提高缓存命中率。"}
        self.cache_key_uri = cache_key_uri
        # {"en" : "This field lists ports other than the default 80 used to handle HTTP requests and ports other than the default 443 used to handle HTTPS requests. ", "zh_CN": "除标准的80，443端口外，我们还支持一些扩展端口。可用该字段指定用于处理HTTP和HTTPS请求的扩展端口。"}
        self.extra_service_ports = extra_service_ports
        # {"en" : "Range: <= 65530 characters 
        # This field allows you to enter Edge Logic to customize load balancing. A subset of the  directives can be used. Refer to the basic directives listed in the baseLbDirectives field of the response to the system configuration API. Currently, these include 'if', 'else', 'elseif', 'set', 'return', 'add_header', 'deny', 'allow', 'access_log_sampling', and 'proxy_set_header.' In addition, some advanced Edge Logic directives, identified by the system configuration API's advancedLbDirectives, can be enabled for your account if needed. Please contact our support team if you require any of them. <br/> Example use: <br />
        # if ($http_user_agent = bot) { return 403;}
        # ", "zh_CN": "取值范围: <= 65530 字符 
        # 此字段可用来自定义边缘逻辑，控制负载均衡器的行为。支持使用 边缘逻辑指令中的部分指令。请参考'获取系统配置'接口中baseLbDirectives字段所列出的负载均衡基础指令。目前，这些基础指令包括'if'、'else'、'elseif'、'set'、'return'、'add_header'、'deny'、'allow'、'access_log_sampling'和'proxy_set_headers'。此外，我们还支持一些高级指令，请参考'获取系统配置'接口中advancedLbDirectives字段所列出的负载均衡高级指令。如果您需要使用这些高级指令，请联系技术支持。
        # 
        # <br/>示例：<br/>
        # 
        # if ($http_user_agent = bot) { return 403;}
        # "}
        self.load_balancer_logic = load_balancer_logic
        # {"en" : "Default: False 
        # Enable TLS zero round-trip time, a feature of TLS 1.3 that can improve performance for repeat visits to a site. If enabling it though, be sure your site is not vulnerable to the HTTP replay attack.", "zh_CN": "默认值: False 
        # 是否开启TLS 0-RTT功能。这是TLS 1.3版本支持的功能。启用该功能后，当用户频繁访问您的站点时，可提高访问响应速度。需要注意的是，启用该功能可能会加大站点遭受HTTP replay攻击的风险。"}
        self.tls_0rtt = tls_0rtt

    def validate(self):
        if self.real_time_log:
            self.real_time_log.validate()
        if self.origins:
            for k in self.origins:
                if k:
                    k.validate()
        if self.video_seek:
            self.video_seek.validate()
        if self.access_control_rules:
            for k in self.access_control_rules:
                if k:
                    k.validate()
        if self.extra_service_ports:
            self.extra_service_ports.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.cache_key_hostname is not None:
            result['cacheKeyHostname'] = self.cache_key_hostname
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.real_time_log is not None:
            result['realTimeLog'] = self.real_time_log.to_map()
        if self.edge_logic is not None:
            result['edgeLogic'] = self.edge_logic
        if self.has_beian is not None:
            result['hasBeian'] = self.has_beian
        if self.redirect_http_to_https is not None:
            result['redirectHttpToHttps'] = self.redirect_http_to_https
        if self.origins is not None:
            result['origins'] = []
            for k in self.origins:
                result['origins'].append(k.to_map() if k else None)
        if self.syntax_version is not None:
            result['syntaxVersion'] = self.syntax_version
        if self.disable_http_2 is not None:
            result['disableHttp2'] = self.disable_http_2
        if self.scheme_in_cache_key is not None:
            result['schemeInCacheKey'] = self.scheme_in_cache_key
        if self.tls_max_version is not None:
            result['tlsMaxVersion'] = self.tls_max_version
        if self.load_balancer_hash_key is not None:
            result['loadBalancerHashKey'] = self.load_balancer_hash_key
        if self.tls_certificate_id is not None:
            result['tlsCertificateId'] = self.tls_certificate_id
        if self.tls_min_version is not None:
            result['tlsMinVersion'] = self.tls_min_version
        if self.tls_ciphers is not None:
            result['tlsCiphers'] = self.tls_ciphers
        if self.allow_protocol_downgrade is not None:
            result['allowProtocolDowngrade'] = self.allow_protocol_downgrade
        if self.tls_certificate_id_1 is not None:
            result['tlsCertificateId1'] = self.tls_certificate_id_1
        if self.video_seek is not None:
            result['videoSeek'] = self.video_seek.to_map()
        if self.tls_session_timeout is not None:
            result['tlsSessionTimeout'] = self.tls_session_timeout
        if self.enable_ocsp_stapling is not None:
            result['enableOcspStapling'] = self.enable_ocsp_stapling
        if self.beian_content_type is not None:
            result['beianContentType'] = self.beian_content_type
        if self.access_control_rules is not None:
            result['accessControlRules'] = []
            for k in self.access_control_rules:
                result['accessControlRules'].append(k.to_map() if k else None)
        if self.disable_cert_automation is not None:
            result['disableCertAutomation'] = self.disable_cert_automation
        if self.cache_key_uri is not None:
            result['cacheKeyUri'] = self.cache_key_uri
        if self.extra_service_ports is not None:
            result['extraServicePorts'] = self.extra_service_ports.to_map()
        if self.load_balancer_logic is not None:
            result['loadBalancerLogic'] = self.load_balancer_logic
        if self.tls_0rtt is not None:
            result['tls0Rtt'] = self.tls_0rtt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('cacheKeyHostname') is not None:
            self.cache_key_hostname = m.get('cacheKeyHostname')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('realTimeLog') is not None:
            temp_model = GetAPropertyVersionResponseConfigsRealTimeLog()
            self.real_time_log = temp_model.from_map(m['realTimeLog'])
        if m.get('edgeLogic') is not None:
            self.edge_logic = m.get('edgeLogic')
        if m.get('hasBeian') is not None:
            self.has_beian = m.get('hasBeian')
        if m.get('redirectHttpToHttps') is not None:
            self.redirect_http_to_https = m.get('redirectHttpToHttps')
        if m.get('origins') is not None:
            self.origins = []
            for k in m.get('origins'):
                temp_model = GetAPropertyVersionResponseConfigsOrigins()
                self.origins.append(temp_model.from_map(k))
        if m.get('syntaxVersion') is not None:
            self.syntax_version = m.get('syntaxVersion')
        if m.get('disableHttp2') is not None:
            self.disable_http_2 = m.get('disableHttp2')
        if m.get('schemeInCacheKey') is not None:
            self.scheme_in_cache_key = m.get('schemeInCacheKey')
        if m.get('tlsMaxVersion') is not None:
            self.tls_max_version = m.get('tlsMaxVersion')
        if m.get('loadBalancerHashKey') is not None:
            self.load_balancer_hash_key = m.get('loadBalancerHashKey')
        if m.get('tlsCertificateId') is not None:
            self.tls_certificate_id = m.get('tlsCertificateId')
        if m.get('tlsMinVersion') is not None:
            self.tls_min_version = m.get('tlsMinVersion')
        if m.get('tlsCiphers') is not None:
            self.tls_ciphers = m.get('tlsCiphers')
        if m.get('allowProtocolDowngrade') is not None:
            self.allow_protocol_downgrade = m.get('allowProtocolDowngrade')
        if m.get('tlsCertificateId1') is not None:
            self.tls_certificate_id_1 = m.get('tlsCertificateId1')
        if m.get('videoSeek') is not None:
            temp_model = GetAPropertyVersionResponseConfigsVideoSeek()
            self.video_seek = temp_model.from_map(m['videoSeek'])
        if m.get('tlsSessionTimeout') is not None:
            self.tls_session_timeout = m.get('tlsSessionTimeout')
        if m.get('enableOcspStapling') is not None:
            self.enable_ocsp_stapling = m.get('enableOcspStapling')
        if m.get('beianContentType') is not None:
            self.beian_content_type = m.get('beianContentType')
        if m.get('accessControlRules') is not None:
            self.access_control_rules = []
            for k in m.get('accessControlRules'):
                temp_model = GetAPropertyVersionResponseConfigsAccessControlRules()
                self.access_control_rules.append(temp_model.from_map(k))
        if m.get('disableCertAutomation') is not None:
            self.disable_cert_automation = m.get('disableCertAutomation')
        if m.get('cacheKeyUri') is not None:
            self.cache_key_uri = m.get('cacheKeyUri')
        if m.get('extraServicePorts') is not None:
            temp_model = GetAPropertyVersionResponseConfigsExtraServicePorts()
            self.extra_service_ports = temp_model.from_map(m['extraServicePorts'])
        if m.get('loadBalancerLogic') is not None:
            self.load_balancer_logic = m.get('loadBalancerLogic')
        if m.get('tls0Rtt') is not None:
            self.tls_0rtt = m.get('tls0Rtt')
        return self


class GetAPropertyVersionResponseStatus(TeaModel):
    def __init__(
        self,
        last_validation_status: str = None,
        frozen: bool = None,
        creation_time: str = None,
        last_update_time: str = None,
        in_production: bool = None,
        in_staging: bool = None,
    ):
        # {"en" : "Result of the last validation of the property version.", "zh_CN": "该版本最近一次配置验证的结果。"}
        self.last_validation_status = last_validation_status
        # {"en" : "Flag indicating if the version is frozen. A property version will be freezed after it is deployed to either staging or production environment.", "zh_CN": "该版本是否被冻结。当一个版本部署到演练或生产环境后，该版本即被冻结，不可更改。"}
        self.frozen = frozen
        # {"en" : "The datetime when the version is created.", "zh_CN": "该版本创建时间。"}
        self.creation_time = creation_time
        # {"en" : "The datetime when the version is last updated.", "zh_CN": "该版本最近一次更新时间。"}
        self.last_update_time = last_update_time
        # {"en" : "Flag indicating if the version is deployed to production.", "zh_CN": "该版本是否部署到生产环境。"}
        self.in_production = in_production
        # {"en" : "Flag indicating if the version is deployed to staging.", "zh_CN": "该版本是否部署到演练环境。"}
        self.in_staging = in_staging

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_validation_status is not None:
            result['lastValidationStatus'] = self.last_validation_status
        if self.frozen is not None:
            result['frozen'] = self.frozen
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.in_production is not None:
            result['inProduction'] = self.in_production
        if self.in_staging is not None:
            result['inStaging'] = self.in_staging
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastValidationStatus') is not None:
            self.last_validation_status = m.get('lastValidationStatus')
        if m.get('frozen') is not None:
            self.frozen = m.get('frozen')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('inProduction') is not None:
            self.in_production = m.get('inProduction')
        if m.get('inStaging') is not None:
            self.in_staging = m.get('inStaging')
        return self


class GetAPropertyVersionResponse(TeaModel):
    def __init__(
        self,
        version: int = None,
        configs: GetAPropertyVersionResponseConfigs = None,
        status: GetAPropertyVersionResponseStatus = None,
    ):
        # {"en" : "Version number.", "zh_CN": "版本号。"}
        self.version = version
        # {"en" : "Describes a property configuration. This contains all the settings.", "zh_CN": "描述加速项目的所有配置信息。"}
        self.configs = configs
        # {"en" : "Status of the property version.", "zh_CN": "状态信息。"}
        self.status = status

    def validate(self):
        self.validate_required(self.version, 'version')
        self.validate_required(self.configs, 'configs')
        if self.configs:
            self.configs.validate()
        self.validate_required(self.status, 'status')
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.configs is not None:
            result['configs'] = self.configs.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('configs') is not None:
            temp_model = GetAPropertyVersionResponseConfigs()
            self.configs = temp_model.from_map(m['configs'])
        if m.get('status') is not None:
            temp_model = GetAPropertyVersionResponseStatus()
            self.status = temp_model.from_map(m['status'])
        return self






class GetListOfPropertiesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertiesParameters(TeaModel):
    def __init__(
        self,
        search: str = None,
        legacy_type: str = None,
        has_config: str = None,
        target: str = None,
        offset: int = None,
        limit: int = None,
        sort_order: str = None,
        sort_by: str = None,
    ):
        # {"en" : "The value of the search parameter is matched on the id, name, description, and hostnames fields of each property. A value like 'domain.com' would match on hostnames domain.com and abc.123domain.com.
        # 
        # Use a value beginning with the '^' character to narrow the matches to properties with name, description, or hostnames fields beginning with the text following the '^'. For example, '^domain' would match on hostnames domain.com and domain123.com but not abc.123domain.com. 
        # 
        # Since a limited number of characters are permitted in URIs, you must encode '^' as '%5E' when specifying a search parameter containing it in the URI, for example, curl -i --url 'https://ngapi.cdnetworks.com/cdn/properties?search=%5Edomain' ... .
        # 
        # Note that a property will be returned if the search matches on any version of the property which has not been deleted. Also, when searching for a property by its ID, you must specify the entire ID as partial matches are not supported.", "zh_CN": "根据搜索关键字匹配每个加速项目的id、name、description以及hostnames字段进行过滤。例如，'domain.com'将匹配到加速域名'domain.com'和'abc.123domain.com'。可以使用'^'字符限定只匹配以搜索关键字开头的值。例如，'^domain'将匹配到加速域名'domain.com'和'domain123.com'，但不会匹配到'abc.123domain.com'。由于URI仅允许有限数量的字符，当search参数包含^符号时，必须将'^'编码为'%5E'。例如，curl -i --url 'https://openapi.wangsu.com/cdn/properties?search=%5Edomain' ... 。注意，该搜索关键字将会对加速项目的所有未删除的版本进行匹配。当通过ID搜索加速项目时，必须指定完整ID，不支持部分匹配。"}
        self.search = search
        # {"en" : " Service type, one of wsapro, webpro, vodpro , downloadpro , 1523.", "zh_CN": "服务类型，根据实际服务类型传wsapro，webpro，vodpro或者downloadpro，分别指全站加速，网页加速，点播加速，下载加速。"}
        self.legacy_type = legacy_type
        # {"en" : "The value of hasConfig is used to filter the results. It can be any field name of a property version, optionally followed by a colon and a value. For example: 
        # 
        # hasConfig=hasBeian:true 
        # 
        # When a colon and value are specified, only properties whose configurations have that value for the field will be returned. The value can be preceded by an exclamation mark, '!', to invert the search.  For example: 
        # 
        # hasConfig=edgeLogic!sorted. In this case, we check that the edgeLogic field does not include the value 'sorted'. 
        # 
        # Searches for values of numeric or boolean fields require an exact match. However, partial matches are supported for string fields. For example, hasConfig=hostnames:domain returns all properties with a hostname containing the string 'domain' such as 'mydomain.com' and 'thedomains.com'. 
        # 
        # If a colon and value are omitted, all properties with a non-empty value for the field will be returned.
        # 
        # Specify multiple hasConfig parameters to filter on multiple conditions. Example: 
        # 
        # hasConfig=hasBeian:true&hasConfig=realTimeLog Only properties matching all the parameters will be returned.
        # 
        # If a property has multiple versions, the property will be included in the API response if any of its versions matches the hasConfig parameter.
        # 
        # Subfields of a property version can be specified by using the period symbol as a separator. Refer to additional examples below.
        # 
        # If matching against values with spaces or special characters, remember to encode them in the URL.
        # 
        # Additional examples:
        # 
        # <table><tr><th>Value</th><th>Description</th></tr><tr><td>hasConfig=disableHttp2:true</td><td>Return properties that don't support HTTP2</td></tr><tr><td>hasConfig=extraServicePorts.http:85</td><td>Return properties supporting port 85 for HTTP requests.</td></tr><tr><td>hasConfig=origins.servers:myorigin.com</td><td>Return properties using myorigin.com as an origin server.</td></tr></table>
        # ", "zh_CN": "通过hasConfig参数指定字段来过滤加速项目。支持使用加速项目版本的任何字段名，在字段名后跟上冒号和值（可选）进行过滤。例如：hasConfig=hasBeian:true。当指定冒号和值时，只返回匹配该字段值的加速项目。如果需要反向查询，可以在字段值前面加上感叹号'!'。例如：hasConfig=edgeLogic!sorted，这个查询将筛选出edgeLogic字段不包含值'sorted'的加速项目。查询数字或布尔类型字段的值时需要精确匹配，而字符串字段支持部分匹配。例如，hasConfig=hostnames:domain将返回加速域名包含字符串'domain'的所有加速项目，例如'mydomain.com'和'thedomains.com'。如果省略冒号和值，则将返回指定字段值为非空的所有加速项目。可以指定多个hasConfig参数使用多个条件进行查询。例如：hasConfig=hasBeian:true&hasConfig=realTimeLog，这个查询只返回与所有参数匹配的加速项目。如果一个加速项目有多个版本，只要该加速项目的任何版本与hasConfig参数匹配，则该加速项目将包含在该接口的响应中。可以使用点号作为分隔符来指定某个字段的子字段。如果要匹配的值带有空格或特殊字符，请在URL中对其进行编码。以下是一些示例： <table><tr><th>值</th><th>描述</th></tr><tr><td>hasConfig=disableHttp2:true</td><td>返回禁用HTTP2的加速项目。</td></tr><tr><td>hasConfig=extraServicePorts.http:85</td><td>返回支持HTTP请求端口85的加速项目。</td></tr><tr><td>hasConfig=origins.servers:myorigin.com</td><td>返回使用myorigin.com作为源站的加速项目。</td></tr></table>"}
        self.has_config = has_config
        # {"en" : "Enum: all,staging,production 
        # Default: all 
        # The value can be 'all', 'staging', or 'production' to filter the results based on where the property has been deployed. 
        # ", "zh_CN": "取值范围: all,staging,production 
        # 默认值: all 
        # 根据加速项目的部署环境过滤。该值可以是'all', 'staging', 或'production'，分别表示所有环境，演练环境和生产环境。"}
        self.target = target
        # {"en" : "Default: 0 
        # Indicates the first item to return. The default is '0'.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Default: 100 Range: <= 200 
        # Maximum number of properties to return. The default is to return a summary of all properties.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "Enum: asc,desc 
        # Default: desc 
        # Order of properties to return. The default is to return the last one updated first.", "zh_CN": "取值范围: asc,desc 
        # 默认值: desc 
        # 返回结果的顺序。默认按最后更新时间降序。"}
        self.sort_order = sort_order
        # {"en" : "Enum: creationTime,lastUpdateTime 
        # Default: lastUpdateTime 
        # Returns results in sorted order.", "zh_CN": "取值范围: creationTime,lastUpdateTime 
        # 默认值: lastUpdateTime 
        # 返回结果的排序依据。"}
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.search is not None:
            result['search'] = self.search
        if self.legacy_type is not None:
            result['legacyType'] = self.legacy_type
        if self.has_config is not None:
            result['hasConfig'] = self.has_config
        if self.target is not None:
            result['target'] = self.target
        if self.offset is not None:
            result['offset'] = self.offset
        if self.limit is not None:
            result['limit'] = self.limit
        if self.sort_order is not None:
            result['sortOrder'] = self.sort_order
        if self.sort_by is not None:
            result['sortBy'] = self.sort_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('search') is not None:
            self.search = m.get('search')
        if m.get('legacyType') is not None:
            self.legacy_type = m.get('legacyType')
        if m.get('hasConfig') is not None:
            self.has_config = m.get('hasConfig')
        if m.get('target') is not None:
            self.target = m.get('target')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('sortOrder') is not None:
            self.sort_order = m.get('sortOrder')
        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')
        return self


class GetListOfPropertiesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertiesRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertiesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetListOfPropertiesResponsePropertiesStagingVersion(TeaModel):
    def __init__(
        self,
        version: int = None,
        hostnames: List[str] = None,
    ):
        # {"en" : "Property version deployed to staging.", "zh_CN": "部署到演练环境的加速项目版本号。"}
        self.version = version
        # {"en" : "Hostnames of the property deployed to staging.", "zh_CN": "加速域名。"}
        self.hostnames = hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        return self


class GetListOfPropertiesResponsePropertiesProductionVersion(TeaModel):
    def __init__(
        self,
        version: int = None,
        hostnames: List[str] = None,
    ):
        # {"en" : "Property version deployed to production.", "zh_CN": "部署到生产环境的加速项目版本号。"}
        self.version = version
        # {"en" : "Hostnames of the property deployed to production.", "zh_CN": "加速域名。"}
        self.hostnames = hostnames

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.version is not None:
            result['version'] = self.version
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        return self


class GetListOfPropertiesResponseProperties(TeaModel):
    def __init__(
        self,
        id: str = None,
        description: str = None,
        name: str = None,
        creation_time: str = None,
        last_update_time: str = None,
        latest_version: int = None,
        legacy_type: str = None,
        staging_version: GetListOfPropertiesResponsePropertiesStagingVersion = None,
        production_version: GetListOfPropertiesResponsePropertiesProductionVersion = None,
    ):
        # {"en" : "ID of the property.", "zh_CN": "加速项目ID。"}
        self.id = id
        # {"en" : "A description of the property.
        # ", "zh_CN": "加速项目的描述。"}
        self.description = description
        # {"en" : "", "zh_CN": "加速项目名称。"}
        self.name = name
        # {"en" : "RFC3339 format date indicating when the property was created.", "zh_CN": "RFC 3339格式的日期，表示创建加速项目的时间。"}
        self.creation_time = creation_time
        # {"en" : "RFC3339 date indicating when the property was last updated.
        # ", "zh_CN": "RFC 3339格式的日期，表示加速项目的最近更新时间。"}
        self.last_update_time = last_update_time
        # {"en" : "Latest version of the property.", "zh_CN": "加速项目的最新版本。"}
        self.latest_version = latest_version
        # {"en" : "Enum: wsapro,webpro,vodpro,downloadpro 
        # Service type, one of wsapro, webpro, vodpro , downloadpro , 1523.", "zh_CN": "取值范围: wsapro,webpro,vodpro,downloadpro 
        # 服务类型，即全站加速，网页加速，点播加速及下载加速。"}
        self.legacy_type = legacy_type
        # {"en" : "Describes the version of the property deployed to staging.", "zh_CN": "描述部署到演练环境的加速项目版本。"}
        self.staging_version = staging_version
        # {"en" : "Describes the version of the property deployed to production.", "zh_CN": "描述部署到生产环境的加速项目版本。"}
        self.production_version = production_version

    def validate(self):
        if self.staging_version:
            self.staging_version.validate()
        if self.production_version:
            self.production_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.legacy_type is not None:
            result['legacyType'] = self.legacy_type
        if self.staging_version is not None:
            result['stagingVersion'] = self.staging_version.to_map()
        if self.production_version is not None:
            result['productionVersion'] = self.production_version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('legacyType') is not None:
            self.legacy_type = m.get('legacyType')
        if m.get('stagingVersion') is not None:
            temp_model = GetListOfPropertiesResponsePropertiesStagingVersion()
            self.staging_version = temp_model.from_map(m['stagingVersion'])
        if m.get('productionVersion') is not None:
            temp_model = GetListOfPropertiesResponsePropertiesProductionVersion()
            self.production_version = temp_model.from_map(m['productionVersion'])
        return self


class GetListOfPropertiesResponse(TeaModel):
    def __init__(
        self,
        properties: List[GetListOfPropertiesResponseProperties] = None,
        count: int = None,
    ):
        # {"en" : "List of properties.", "zh_CN": "加速项目列表。"}
        self.properties = properties
        # {"en" : "Range: >= 0 
        # Number of properties.
        # ", "zh_CN": "取值范围: >= 0 
        # 加速项目数量。"}
        self.count = count

    def validate(self):
        self.validate_required(self.properties, 'properties')
        if self.properties:
            for k in self.properties:
                if k:
                    k.validate()
        self.validate_required(self.count, 'count')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = []
            for k in self.properties:
                result['properties'].append(k.to_map() if k else None)
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = []
            for k in m.get('properties'):
                temp_model = GetListOfPropertiesResponseProperties()
                self.properties.append(temp_model.from_map(k))
        if m.get('count') is not None:
            self.count = m.get('count')
        return self






class CreateAPropertyVersionPaths(TeaModel):
    def __init__(
        self,
        property_id: str = None,
    ):
        # {"en" : "ID of a property", "zh_CN": "加速项目ID。"}
        self.property_id = property_id

    def validate(self):
        self.validate_required(self.property_id, 'property_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        return self


class CreateAPropertyVersionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPropertyVersionRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPropertyVersionRequestRealTimeLogHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # {"en" : "Name of an HTTP header.", "zh_CN": "HTTP标头名称"}
        self.name = name
        # {"en" : "Value of an HTTP header.", "zh_CN": "HTTP标头值"}
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateAPropertyVersionRequestRealTimeLog(TeaModel):
    def __init__(
        self,
        log_url: str = None,
        sample_rate: int = None,
        escape: str = None,
        format: str = None,
        headers: List[CreateAPropertyVersionRequestRealTimeLogHeaders] = None,
    ):
        # {"en" : "The URL that receives the notifications. It must begin with 'http' or 'https'. The server should support the POST method. This is a required field.", "zh_CN": "接收通知的服务器URL地址。必须以'http'或'https'开头。服务器须支持POST方法。这是必填字段。"}
        self.log_url = log_url
        # {"en" : "Default: 1 Range: [ 1 .. 65536 ] 
        # An integer between [1, 65536]. n means one notification for every n edge requests. 1 means every edge request will generate a notification. This is optional. Default is 1.", "zh_CN": "默认值: 1 取值范围: [ 1 .. 65536 ] 
        # 采样率。介于[1, 65536]之间的整数。n表示每n个边缘请求发送1条通知。1表示每个边缘请求都会发送。这是可选字段。默认值为1。"}
        self.sample_rate = sample_rate
        # {"en" : "Enum: json,none 
        # Specify json to enable JSON character escaping in variables or none to disable escaping.", "zh_CN": "取值范围: json,none 
        # 指定json以开启变量中的json字符转义。如果要禁用转义则指定none。"}
        self.escape = escape
        # {"en" : "This is a required field to specify the notification body to be sent to the remote server. It can be any printable text that can be sent in the body of an HTTP POST request. 
        # 
        # The following built-in variables can be used within the format field. They will be replaced with the actual values in the notifications.
        # <table><tr><th>Name</th><th>Description</th></tr><tr><td>$body_bytes_sent</td><td>Size of the response body.</td></tr><tr><td>$bytes_sent</td><td>Size of the response, including body, headers and response line.</td></tr><tr><td>$client_country_code</td><td>An ISO 3166-1 country code representing the country of the client request, for example, 'US'. 'ZZ' is returned if the country is unknown.</td></tr><tr><td>$client_real_ip</td><td>IP address of the client request.</td></tr><tr><td>$cookie_x</td><td>This lets you obtain any cookie named x.  For example, $cookie_account would retrieve the value of a cookie named 'account'.</td></tr><tr><td>$http_x</td><td>Obtain any HTTP header named x from the original request. The header name is converted to lower case with dashes replaced by underscores. For example, specify $http_user_agent to get the value of User-Agent.</td></tr><tr><td>$msec</td><td>Current unix time in seconds with millisecond precision.</td></tr><tr><td>$qtl_req_id</td><td>Unique identifier representing the request.</td></tr><tr><td>$request_uri</td><td>HTTP request URI</td></tr><tr><td>$request_method</td><td>The HTTP request method used to access the origin.</td></tr><tr><td>$request_time</td><td>Response time in milliseconds. It is the time between receiving the request's  first byte and serving the last byte of the response.</td></tr><tr><td>$sc_completed</td><td>1 to indicate the last byte of the object was served to the user, 0 otherwise.</td></tr><tr><td>$sc_initial</td><td>1 to indicate the first byte of the object was served to the user, 0 otherwise.</td></tr><tr><td>$scheme</td><td>Indicates the protocol of the user's request ('http' or https').</td></tr><tr><td>$sent_http_content_length</td><td>the original file size.</td></tr><tr><td>$sent_http_x</td><td>Obtain the value of an HTTP header named x that is returned in the response to the client. The header name should be converted to lower case with dashes replaced by underscores. For example, $sent_http_etag would give you the value of the ETag header.</td></tr><tr><td>$server_addr</td><td>IP address of the edge node serving the user's request.</td></tr><tr><td>$server_protocol</td><td>Indicates the version of HTTP used in the user's request, either 'HTTP/1.0', 'HTTP/1.1', or 'HTTP/2.0'.</td></tr><tr><td>$ssl_cipher</td><td>Indicates the cipher suite used for the TLS (SSL) connection.</td></tr><tr><td>$ssl_server_name</td><td>The hostname that a client initiating a TLS (SSL) connection is attempting to connect to. It is only sent by clients supporting SNI (Server Name Indication).</td></tr><tr><td>$ssl_protocol</td><td>Indicates the TLS version used for the TLS (SSL) connection. Example versions include 'SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2', and 'unknown'.</td></tr><tr><td>$status</td><td>An HTTP response code for the user's request.</td></tr><tr><td>$tcpinfo_rtt</td><td>The time in microseconds taken by a packet to travel to the destination and back.</td></tr></table>", "zh_CN": "该字段用来定义要发送到远程服务器的通知的格式。通知正文可以包括任何能在HTTP POST请求体中发送的可打印文本。这是必填字段。
        # 
        # 可以使用以下内置变量定义通知的格式。发送通知时，它们将被替换为实际值。
        # <table><tr><th>变量名称</th><th>描述</th></tr><tr><td>$body_bytes_sent</td><td>响应体大小。</td></tr><tr><td>$bytes_sent</td><td>响应的大小，包括响应体、响应头和响应行。</td></tr><tr><td>$client_country_code</td><td>客户端请求来源国家，以ISO 3166-1国家代码表示。例如'US'。如果国家/地区未知，则返回'ZZ'。</td></tr><tr><td>$client_real_ip</td><td>客户端请求的IP地址。</td></tr><tr><td>$cookie_x</td><td>获取某个cookie。例如，指定$cookie_account可获取名为'account'的cookie值。</td></tr><tr><td>$http_x</td><td>从原始请求中获取某个HTTP请求头。请求头名称需转换为小写，并用下划线替换连字符。例如，指定$http_user_agent来获取User-Agent的值。</td></tr><tr><td>$msec</td><td>当前unix时间，以毫秒为单位。</td></tr><tr><td>$qtl_req_id</td><td>请求的唯一标识符。</td></tr><tr><td>$request_uri</td><td>HTTP请求URI。</td></tr><tr><td>$request_method</td><td>用于访问源站的HTTP请求方法。</td></tr><tr><td>$request_time</td><td>响应时间，以毫秒为单位。这是从接收到请求的第一个字节到服务端响应最后一个字节之间的时间。</td></tr><tr><td>$sc_completed</td><td>1表示对象的最后一个字节已返回给用户，否则为0。</td></tr><tr><td>$sc_initial</td><td>1表示对象的第一个字节已返回给用户，否则为0。</td></tr><tr><td>$scheme</td><td>表示用户请求的协议（'http'或'https'）。</td></tr><tr><td>$sent_http_content_length</td><td>原始文件大小。</td></tr><tr><td>$sent_http_x</td><td>获取在对客户端响应中某个HTTP响应头的值。响应头名称需转换为小写，并用下划线替换连字符。例如，$sent_http_etag可获取ETag头的值。</td></tr><tr><td>$server_addr</td><td>为用户请求提供服务的边缘节点的IP地址。</td></tr><tr><td>$server_protocol</td><td>表示用户请求中使用的HTTP版本，可以是'HTTP/1.0'、'HTTP/1.1'或'HTTP/2.0'。</td></tr><tr><td>$ssl_cipher</td><td>表示用于TLS（SSL）连接的加密算法套件。</td></tr><tr><td>$ssl_server_name</td><td>客户端发起TLS（SSL）连接所要连接的域名。仅由支持SNI（Server Name Indication）的客户端发送。</td></tr><tr><td>$ssl_protocol</td><td>表示用于TLS（SSL）连接的TLS版本。例如，'SSLv3'、'TLSv1'、'TLSv1.1'、'TLSv1.2'和'unknown'。</td></tr><tr><td>$status</td><td>用户请求的HTTP状态码。</td></tr><tr><td>$tcpinfo_rtt</td><td>数据包往返目的地所用的时间，以微秒为单位。</td></tr></table>"}
        self.format = format
        # {"en" : "HTTP header names and values to be sent to the notification server. A header name can contain any alphanumeric character or hyphen, '-'. A header value can contain any printable characters. It can also include any of the built-in variables supported in the format field of the realTimeLog object.", "zh_CN": "需要发送到远程服务器的HTTP请求头名称和值。请求头名称可以包含任何字母，数字或连字符'-'。值可以包含任何可打印字符，也可以使用realTimeLog对象format字段中支持的任何内置变量。"}
        self.headers = headers

    def validate(self):
        self.validate_required(self.log_url, 'log_url')
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_url is not None:
            result['logUrl'] = self.log_url
        if self.sample_rate is not None:
            result['sampleRate'] = self.sample_rate
        if self.escape is not None:
            result['escape'] = self.escape
        if self.format is not None:
            result['format'] = self.format
        if self.headers is not None:
            result['headers'] = []
            for k in self.headers:
                result['headers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logUrl') is not None:
            self.log_url = m.get('logUrl')
        if m.get('sampleRate') is not None:
            self.sample_rate = m.get('sampleRate')
        if m.get('escape') is not None:
            self.escape = m.get('escape')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('headers') is not None:
            self.headers = []
            for k in m.get('headers'):
                temp_model = CreateAPropertyVersionRequestRealTimeLogHeaders()
                self.headers.append(temp_model.from_map(k))
        return self


class CreateAPropertyVersionRequestOriginsAuthentication(TeaModel):
    def __init__(
        self,
        method_name: str = None,
    ):
        # {"en" : "Authentication method.", "zh_CN": "鉴权方法。"}
        self.method_name = method_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method_name is not None:
            result['methodName'] = self.method_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        return self


class CreateAPropertyVersionRequestOrigins(TeaModel):
    def __init__(
        self,
        name: str = None,
        servers: List[str] = None,
        supported_protocol: str = None,
        direct_connection: str = None,
        host_header: str = None,
        verify_origin: bool = None,
        authentication: CreateAPropertyVersionRequestOriginsAuthentication = None,
        keep_alive_timeout: int = None,
        peer_failure_timeout: str = None,
        tls_certificate_id: str = None,
        shield: str = None,
    ):
        # {"en" : "^[a-zA-z0-9_] 
        # Name of an origin. It must be unique within this property.
        # ", "zh_CN": "^[a-zA-z0-9_] 
        # 源站名称，在此加速项目中必须唯一。"}
        self.name = name
        # {"en" : "Each entry should be a string consisting of an address optionally followed by one or more parameters, separated by space characters. The address can take one of the following three forms:
        # {hostname or IP address}
        # {hostname or IP address}:{http port}
        # {hostname or IP address}:{http port},{https port}
        # Values for the HTTP and HTTPS ports should be integers in the range [1,65535]. 
        # Even if the value of supportedProtocol is 'https', the HTTPS port has to be specified after the comma.
        # In the third form, one of the two ports can be empty.
        # 
        # Supported parameters are 'backup' and 'weight'.
        # 
        # 'backup' is used to indicate the server is a backup server. It will be used when the primary servers are unavailable.
        # 
        # 'weight' is a value in the range [1, 100]. The default value is 1. It lets you control the likelihood that one origin server will be used relative to another.
        # 
        # There should be at least one primary server defined; it does not have the 'backup' parameter.
        # 
        # Example:
        # ['www.abc.com weight=1', 'www1.abc.com:8080 weight=4', 'www2.abc.com:880,4443 backup']
        # 
        # This example specifies two primary servers which are used in a 1:4 ratio meaning one gets about 20% of the requests to origin while the other gets 80% of the requests. In addition, a backup server is specified.
        # ", "zh_CN": "源站服务器列表。每个条目为一个字符串，由一个地址与一个或多个参数组成，参数之间以空格分隔。地址可以采用以下三种形式之一：
        # {域名或IP地址}
        # {域名或IP地址}:{HTTP端口}
        # {域名或IP地址}:{HTTP端口},{HTTPS端口}
        # HTTP和HTTPS端口的值应为[1,65535]范围内的整数。
        # 即使supportedProtocol的值设为'https'，也必须在此处指定HTTPS端口。
        # 在第三种形式中，两个端口中的一个可以为空。
        # 支持ipv6 当enableIpv6Origin为true时，ipv6传入{域名或IP地址}:{HTTP端口},{HTTPS端口}时，域名或IP地址需要放入[]，如[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:80
        # 
        # 支持的参数包括'backup'和'weight'。
        # 'backup'用于标识备份服务器。它将在主服务器不可用时使用。
        # 'weight'是范围[1,100]内的值，默认值为1，用来设置服务器权重，控制一台源站服务器相对于另一台被使用的可能性。
        # 每个源站应至少定义一个主服务器（即不带'backup'参数的服务器）。
        # 
        # 示例：
        # ['www.abc.com weight=1', 'www1.abc.com:8080 weight=4', 'www2.abc.com:880,4443 backup']
        # 
        # 此示例指定了两个主服务器和一个备份服务器，其中，主服务器的权重为1:4，表示第一个服务器将获得约20%的回源请求，而另一个将获得约80%。"}
        self.servers = servers
        # {"en" : "Enum: http,https,both 
        # This optional field indicates the protocol supported by the origin server. If this property has a certificate attached to it, the value can be set to http if the allowProtocolDowngrade field is also set to true.", "zh_CN": "取值范围: http,https,both 
        # 此可选字段表示源站服务器支持的协议。如果此加速项目附加了证书，且allowProtocolDowngrade字段也设置为true，则可以将该值设置为http。"}
        self.supported_protocol = supported_protocol
        # {"en" : "Default: auto 
        # Optional. This parameter tells us how important it is to directly go to this origin without going through any intermediate cache to fetch content. The values can be 'noDirect', 'auto', 'alwaysDirect'. 
        # 
        # 'noDirect' means we always go through at least one intermediate cache. Customers who care particularly about the origin's workload can use this option. Our cache scheduler will dynamically pick the intermediate cache based on performance and resource availability.
        # 
        # 'auto' means the cache scheduler will make the choice dynamically based on performance and resource availability. This is the default behavior if not specified.
        # 
        # 'alwaysDirect' means we always directly connect to this origin.
        # ", "zh_CN": "默认值: auto 
        # 此可选字段用来指定回源方式，可以是'noDirect'、'auto'、'alwaysDirect'。
        # 
        # 'noDirect'指总是通过至少一个中间缓存节点回源。对于特别关心源站负载的客户可以使用此选项。我们的调度程序将根据性能和资源可用性动态选择中间缓存节点。
        # 'alwaysDirect'指总是直接回源。
        # 'auto'指自动选择直接回源或通过中间缓存节点回源。调度程序将根据性能和资源可用性动态做出选择。该字段未指定时，采用此默认行为。"}
        self.direct_connection = direct_connection
        # {"en" : "Optional. It should be a valid hostname. It will also be used as the SNI servername when contacting the HTTPS origin. We also allow it to be an nginx variable that begins with '$' followed by [a-z_]{3,60}. Nginx variable names are case insensitive, so we only allow lowercase characters.
        # If not specified, the value of the HOST header in the request will be used. 
        # 
        # One constraint is that if 'aswS3' is specified for origin authentication, the value of hostHeader cannot be a variable or empty. It has to be a valid Amazon S3 hostname. Refer to https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html", "zh_CN": "可选，用来指定回源HOST头部。必须是有效的域名。当连接HTTPS源站时，该值也作为SNI域名。可以用nginx变量来指定，变量以'$'开头，后跟[a-z_]{3,60}。Nginx变量名不区分大小写，因此我们只允许小写字符。
        # 如果未指定，将使用请求中的HOST请求头的值。
        # 
        # 注意：如果指定了'awsS3'作为回源鉴权参数，则hostHeader的值不能为变量或为空，而必须是有效的Amazon S3主机名。参考：https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html"}
        self.host_header = host_header
        # {"en" : "Default: False 
        # Optional. It controls whether the cache will validate the certificate of the origin.", "zh_CN": "默认值: False 
        # 可选。用来设定CDN缓存节点是否验证源站证书。"}
        self.verify_origin = verify_origin
        # {"en" : "Optional. It is a structure to specify the parameters, such as password, for authentication with the origin servers. It should have at least one field: 'methodName', which should be a string indicating one of the predefined authentication methods. The only valid value at this time is 'awsS3'. When 'awsS3' is used, the following parameters are required:
        # awsS3.region:
        # The AWS S3 region where your resources are hosted, e.g. 'us-west-1', 'ap-northeast-1', 'eu-north-1', and 'cn-north-1'.
        # awsS3.accessKey:
        # Your AWS access key that CDN Pro will use to access your resources stored on AWS S3.
        # awsS3.secretKey:
        # Your AWS secret key that CDN Pro will use to access your resources stored on AWS S3.
        # Also, the value of the hostHeader field cannot be a variable or empty. It must be a valid Amazon S3 hostname.
        # 
        # Example:
        # 
        # {'methodName':'awsS3',
        # 'awsS3':{
        # 'region':'us-west-1',
        # 'accessKey':'sdnu2932',
        # 'secretKey':'d12345678abcdefghi'
        # }}
        # ", "zh_CN": "可选。用于指定与源服务器进行身份验证（回源鉴权）的相关参数（如密码）。必须至少有'methodName'（字符串）字段，用来指定预定义的鉴权方法。目前仅支持源站为AWS S3的回源鉴权，因此唯一有效的值是'awsS3'。使用'awsS3'时，需要提供以下参数：
        # awsS3.region:
        # 您存储在S3上的资源所在的AWS区域。例如，'us-west-1'，'ap-northeast-1'，'eu-north-1'，'cn-north-1'。
        # awsS3.accessKey:
        # 您的 AWS 访问密钥（access key），CDN Pro 将使用它来访问您存储在 AWS S3 上的资源。
        # awsS3.secretKey:
        # 您的 AWS 密钥（secret key），CDN Pro 将使用它来访问您存储在 AWS S3 上的资源。
        # 此外，hostHeader字段的值不能为变量或为空，必须是有效的Amazon S3主机名。
        # 
        # 示例：
        # 
        # {'methodName':'awsS3',
        # 'awsS3':{
        # 'region':'us-west-1',
        # 'accessKey':'sdnu2932',
        # 'secretKey':'d12345678abcdefghi'
        # }}
        # "}
        self.authentication = authentication
        # {"en" : "Default: 60 Range: [ 5 .. 600 ] 
        # Timeout in seconds during which an idle keepalive connection to an upstream server will stay open. A service quota setting of maxUpstreamKeepaliveTimeOut can change the maximum permitted value.", "zh_CN": "默认值: 60 取值范围: [ 5 .. 600 ] 
        # 该字段用于指定CDN Pro服务器和源站建连的Keep-Alive超时时间，单位为秒。通过maxUpstreamKeepaliveTimeOut 该服务设置项可以更改允许的最大值。如果需要调整最大值，请联系我们的技术支持。"}
        self.keep_alive_timeout = keep_alive_timeout
        # {"en":
        # "This setting allows you to specify the number of unsuccessful attempts to reach one of the origin's IP addresses or peers before it is marked as unavailable for a period of time designated by the timeout. If all peers of all servers are unavailable, requests for content from the origin will receive an immediate 502 HTTP response. By default, six attempts to a peer are made, after which a one-second timeout applies to that peer. To disable this feature, set peerFailureTimeout to 'off'.", "zh_CN": "
        # 该字段用于设置源站故障剔除。开启此功能后，当连接某个源站服务器的失败次数达到设定阈值，该源站服务器将被标记为不可用，并保持该状态直到设定的超时时长。失败次数阈值和超时时长分别通过failureThreshold参数和timeout参数设置。CDN Pro回源时将剔除不可用的源站服务器。如果所有源站服务器都被标记为不可用，则对应的请求将立即响应502状态码。默认情况下，当连接某个源站服务器连续失败6次之后，该服务器将被标记为不可用，超时时长为1秒。如果要禁用此功能，请将peerFailureTimeout设置为'off'。开启源站故障剔除配置示例：<code>{'peerFailureTimeout':{'failureThreshold':10,'timeout':3}}</code>"}
        self.peer_failure_timeout = peer_failure_timeout
        # {"en" : "Refers to a certificate used to authenticate with the origin server. This certificate must also be deployed.", "zh_CN": "用于验证源站服务器的证书，该证书同样必须被部署。"}
        self.tls_certificate_id = tls_certificate_id
        # {"en" : "Refers to the ID of an origin shield representing a set of servers that will make requests to your origin servers rather than the CDN Pro edge servers. This can help further reduce traffic to your origin. Origin shield is allowed only when directConnection is set to noDirect. This is an advanced feature that can be enabled by contacting our support team. The origin shields API provides a list of available shields along with their IP addresses. It is best to select a shield whose region is closest to your origin servers. Use of a shield in China requires your property have 'hasBeian' set to true. If your origin servers have an access control list, add the IPs of the shield you choose to use.", "zh_CN": "指定某个源站盾（origin shield）的ID。使用源站盾功能后，所有回源请求都会通过源站盾中转回源，这可以帮助收敛回源流量。需要把directConnection设置为noDirect，才允许开启源站盾。源站盾是高级功能，如需使用请联系我们的技术支持开通。可通过调用‘获取源站盾列表’接口查询可用的源站盾及其对应的IP地址。您可根据源站的位置，选择合适的源站盾。如果您需使用中国大陆的源站盾，则该加速项目的所有域名必须已取得备案。如果您的源站开启了访问控制，请将所选择源站盾的IP地址加入白名单。"}
        self.shield = shield

    def validate(self):
        if self.authentication:
            self.authentication.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.servers is not None:
            result['servers'] = self.servers
        if self.supported_protocol is not None:
            result['supportedProtocol'] = self.supported_protocol
        if self.direct_connection is not None:
            result['directConnection'] = self.direct_connection
        if self.host_header is not None:
            result['hostHeader'] = self.host_header
        if self.verify_origin is not None:
            result['verifyOrigin'] = self.verify_origin
        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()
        if self.keep_alive_timeout is not None:
            result['keepAliveTimeout'] = self.keep_alive_timeout
        if self.peer_failure_timeout is not None:
            result['peerFailureTimeout'] = self.peer_failure_timeout
        if self.tls_certificate_id is not None:
            result['tlsCertificateId'] = self.tls_certificate_id
        if self.shield is not None:
            result['shield'] = self.shield
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('servers') is not None:
            self.servers = m.get('servers')
        if m.get('supportedProtocol') is not None:
            self.supported_protocol = m.get('supportedProtocol')
        if m.get('directConnection') is not None:
            self.direct_connection = m.get('directConnection')
        if m.get('hostHeader') is not None:
            self.host_header = m.get('hostHeader')
        if m.get('verifyOrigin') is not None:
            self.verify_origin = m.get('verifyOrigin')
        if m.get('authentication') is not None:
            temp_model = CreateAPropertyVersionRequestOriginsAuthentication()
            self.authentication = temp_model.from_map(m['authentication'])
        if m.get('keepAliveTimeout') is not None:
            self.keep_alive_timeout = m.get('keepAliveTimeout')
        if m.get('peerFailureTimeout') is not None:
            self.peer_failure_timeout = m.get('peerFailureTimeout')
        if m.get('tlsCertificateId') is not None:
            self.tls_certificate_id = m.get('tlsCertificateId')
        if m.get('shield') is not None:
            self.shield = m.get('shield')
        return self


class CreateAPropertyVersionRequestVideoSeek(TeaModel):
    def __init__(
        self,
        start_parameter: str = None,
        end_parameter: str = None,
    ):
        # {"en" : "Range: [ 1 .. 31 ] characters 
        # Name of the query parameter indicating the starting offset in bytes of the content to fetch. The parameter name should begin with a letter (a-z, A-Z) and may be followed by up to 30 letters and numbers.", "zh_CN": "取值范围: [ 1 .. 31 ] 字符 
        # 查询参数的名称，用来指定要获取的内容的起始位置（以字节计算）。参数名称应以字母（a-z，A-Z）开头，后面最多可以有30个字母和数字。"}
        self.start_parameter = start_parameter
        # {"en" : "Range: [ 0 .. 31 ] characters 
        # Name of the query parameter indicating the ending offset of the content to fetch. The parameter name should begin with a letter (a-z, A-Z) and may be followed by up to 30 letters and numbers.", "zh_CN": "取值范围: [ 0 .. 31 ] 字符 
        # 查询参数的名称，用来指定要获取的内容的结束位置（以字节计算）。参数名称应以字母（a-z，A-Z）开头，后面最多可以有30个字母和数字。"}
        self.end_parameter = end_parameter

    def validate(self):
        self.validate_required(self.start_parameter, 'start_parameter')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_parameter is not None:
            result['startParameter'] = self.start_parameter
        if self.end_parameter is not None:
            result['endParameter'] = self.end_parameter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startParameter') is not None:
            self.start_parameter = m.get('startParameter')
        if m.get('endParameter') is not None:
            self.end_parameter = m.get('endParameter')
        return self


class CreateAPropertyVersionRequestAccessControlRulesConditions(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        hostname: str = None,
        uri: str = None,
        server_regions: List[str] = None,
        client_regions: List[str] = None,
        client_ip_range: List[str] = None,
    ):
        # {"en" : "Enum: https,http 
        # Indicates whether the incoming request uses HTTP or HTTPS.", "zh_CN": "取值范围: https,http 
        # 客户端请求的协议，HTTP或HTTPS。"}
        self.scheme = scheme
        # {"en" : "Indicates the hostname requested. It must be one of the hostnames defined in the property.", "zh_CN": "请求对应的加速域名。必须是加速项目中定义的加速域名之一。"}
        self.hostname = hostname
        # {"en" : "Range: <= 500 characters 
        # The URI begins with '/' and can end with '*' for prefix matching. ", "zh_CN": "取值范围: <= 500 字符 
        # 用于前缀匹配的URI，以'/'开头，可以以'*'结尾。"}
        self.uri = uri
        # {"en" : "An array of ISO-3166-1 alpha-2 codes indicating the countries of the servers, for example, 'US' to represent 'United States of America'.", "zh_CN": "服务器所在区域，以ISO-3166-1 两位国家代码表示。例如，'US'代表'美国'。"}
        self.server_regions = server_regions
        # {"en" : "An array of ISO-3166-1 alpha-2 codes indicating one or more countries which are the source of the client requests, for example, 'CN' to represent 'China'.", "zh_CN": "客户端请求来源区域，以ISO-3166-1 两位国家代码表示。例如，'CN'代表'中国'。"}
        self.client_regions = client_regions
        # {"en" : "Indicates the starting and ending IP addresses of the client requests to match against. They must be in IPv4 or IPv6 format.", "zh_CN": "用于指定要匹配的客户端请求的开始和结束IP地址。必须是IPv4或IPv6格式。"}
        self.client_ip_range = client_ip_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.uri is not None:
            result['uri'] = self.uri
        if self.server_regions is not None:
            result['serverRegions'] = self.server_regions
        if self.client_regions is not None:
            result['clientRegions'] = self.client_regions
        if self.client_ip_range is not None:
            result['clientIpRange'] = self.client_ip_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('serverRegions') is not None:
            self.server_regions = m.get('serverRegions')
        if m.get('clientRegions') is not None:
            self.client_regions = m.get('clientRegions')
        if m.get('clientIpRange') is not None:
            self.client_ip_range = m.get('clientIpRange')
        return self


class CreateAPropertyVersionRequestAccessControlRulesAction(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        message: str = None,
    ):
        # {"en" : "Indicates the HTTP status code to respond with. It must be in the range 300-309, 400-409, or 500-509 to indicate a redirection or error.", "zh_CN": "响应的HTTP状态码，范围必须在300-309、400-409或500-509之间，分别表示重定向或错误。"}
        self.status_code = status_code
        # {"en" : "Range: <= 200 characters 
        # If the value of the status field is in the range 300-309, the message field's value will be placed in a Location HTTP header returned to the client. If the status is in the range 400-409 or 500-509, the value will be returned in the response body to the client.", "zh_CN": "取值范围: <= 200 字符 
        # 如果status字段的值在300-309范围内，message字段的值将在返回给客户端的Location响应头中。如果status字段的值在400-409或500-509范围内，则message字段的值将在返回给客户端的响应体中。"}
        self.message = message

    def validate(self):
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateAPropertyVersionRequestAccessControlRules(TeaModel):
    def __init__(
        self,
        id: str = None,
        conditions: CreateAPropertyVersionRequestAccessControlRulesConditions = None,
        action: CreateAPropertyVersionRequestAccessControlRulesAction = None,
    ):
        # {"en" : "Range: [ 0 .. 60 ] characters 
        # An optional ID for the access control rule.", "zh_CN": "取值范围: [ 0 .. 60 ] 字符 
        # 访问控制规则ID。"}
        self.id = id
        # {"en" : "Specify the conditions that the incoming request must match. At least one condition must be specified. If multiple are specified, all must match.", "zh_CN": "指定客户端请求必须匹配的条件。必须至少指定一个条件。如果指定了多个条件，则必须全部匹配。"}
        self.conditions = conditions
        # {"en" : "Indicates the action to take in response to a request that matches the conditions of the access control rule.", "zh_CN": "对于匹配到以上条件的请求所采取的相应操作。"}
        self.action = action

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.conditions is not None:
            result['conditions'] = self.conditions.to_map()
        if self.action is not None:
            result['action'] = self.action.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('conditions') is not None:
            temp_model = CreateAPropertyVersionRequestAccessControlRulesConditions()
            self.conditions = temp_model.from_map(m['conditions'])
        if m.get('action') is not None:
            temp_model = CreateAPropertyVersionRequestAccessControlRulesAction()
            self.action = temp_model.from_map(m['action'])
        return self


class CreateAPropertyVersionRequestExtraServicePorts(TeaModel):
    def __init__(
        self,
        http: List[str] = None,
        https: List[str] = None,
    ):
        # {"en" : "This is a list of ports other than 80 which are used to handle HTTP requests. The available values can be found in the systemConfigs API's response. If you need another port, please contact our support team.", "zh_CN": "指定用于处理HTTP请求的端口列表（80端口除外）。可通过调用'获取系统配置'接口来查询系统支持的端口。如果您需要开通其他端口，请联系技术支持。"}
        self.http = http
        # {"en" : "This is a list of ports other than 443 which are used to handle HTTPS requests. The available values can be found in the systemConfigs API's response. If you need another port, please contact our support team.", "zh_CN": "指定用于处理HTTPS请求的端口列表（443端口除外）。可通过调用'获取系统配置'接口来查询系统支持的端口。如果您需要开通其他端口，请联系技术支持。"}
        self.https = https

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http is not None:
            result['http'] = self.http
        if self.https is not None:
            result['https'] = self.https
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http') is not None:
            self.http = m.get('http')
        if m.get('https') is not None:
            self.https = m.get('https')
        return self


class CreateAPropertyVersionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        cache_key_hostname: str = None,
        hostnames: List[str] = None,
        real_time_log: CreateAPropertyVersionRequestRealTimeLog = None,
        edge_logic: str = None,
        has_beian: bool = None,
        redirect_http_to_https: str = None,
        origins: List[CreateAPropertyVersionRequestOrigins] = None,
        syntax_version: int = None,
        disable_http_2: bool = None,
        enable_http_3: bool = None,
        scheme_in_cache_key: bool = None,
        tls_max_version: str = None,
        load_balancer_hash_key: str = None,
        tls_certificate_id: str = None,
        tls_min_version: str = None,
        tls_ciphers: str = None,
        allow_protocol_downgrade: bool = None,
        tls_certificate_id_1: str = None,
        video_seek: CreateAPropertyVersionRequestVideoSeek = None,
        tls_session_timeout: int = None,
        enable_ocsp_stapling: bool = None,
        beian_content_type: int = None,
        enable_ipv_6origin: bool = None,
        follow_client_ip_version: str = None,
        access_control_rules: List[CreateAPropertyVersionRequestAccessControlRules] = None,
        disable_cert_automation: bool = None,
        cache_key_uri: str = None,
        extra_service_ports: CreateAPropertyVersionRequestExtraServicePorts = None,
        load_balancer_logic: str = None,
        tls_0rtt: bool = None,
    ):
        # {"en" : "A description of the version.
        # ", "zh_CN": "版本描述。"}
        self.description = description
        # {"en" : "Range: <= 80 characters ^[a-z.-_]+\
        # The cachekey hostname must be a string made of lowercase letters, digits, dot, dash, and underscore. If not specified, the incoming Host header value will be used and the cache will not be shared across different hostnames in this property.
        # ", "zh_CN": "取值范围: <= 80 字符 ^[a-z.-_]+\
        # 用于缓存键（Cache Key）的主机名必须是由小写字母、数字、点、连字符和下划线组成的字符串。如果未指定，默认将使用传入的Host请求头值，并且此加速项目中的不同加速域名之间不共享缓存。"}
        self.cache_key_hostname = cache_key_hostname
        # {"en" : "Hostnames associated with the property. A valid value is a fully qualified hostname such as www.domain.com or a wildcard hostname such as *.domain.com. Any given hostname can only be in one deployed property at a particular time. However, a wildcard hostname is permitted to overlap other hostnames you own.", "zh_CN": "与加速项目关联的加速域名。必须是FQDN完全限定域名（如 www.domain.com），或泛域名（如*.domain.com）。
        # 同一个加速域名在同一时间只能存在于一个已部署的加速项目中，但泛域名可以与关联的完全限定域名一同部署。"}
        self.hostnames = hostnames
        # {"en" : "This optional field allows you to configure notifications about client requests to be sent to a remote server. It can be used only if you have access to our realtime_log_switch directive. Please contact our support team if you require this feature.", "zh_CN": "此可选字段用来配置发送消息通知（即实时日志）到您的远程服务器。当有客户端请求访问您的加速域名时，将触发通知。这是高级功能，如果您需要此功能，请联系我们的技术支持开通。"}
        self.real_time_log = real_time_log
        # {"en" : "Range: <= 65530 characters 
        # Refer to Edge Logic Introduction.", "zh_CN": "取值范围: <= 65530 字符 
        # 自定义边缘逻辑。参考边缘逻辑介绍。"}
        self.edge_logic = edge_logic
        # {"en" : "Default: False 
        # The value indicates whether all the hostnames in this property have Beian license on file with the Chinese government. This is required to serve this property from servers in mainland China. A value of false means servers outside of mainland China will be used to distribute content to visitors in China. If set to true you must also specify the content type in the beianContentType field.", "zh_CN": "默认值: False 
        # 此加速项目中的所有加速域名是否都已获得中国政府的ICP备案。只有获取备案的域名才能使用中国大陆节点来提供服务。如果设置为true，还必须在beianContentType字段中指定内容类型。"}
        self.has_beian = has_beian
        # {"en" : "Default: False 
        # This field can be set to either a boolean value or a string. If the value is set to true, the server will redirect all HTTP requests to HTTPS using status code 301. You can also specify string values '302', '307', or '308' instead if you wish to return a different status code when a request is redirected.", "zh_CN": "默认值: False 
        # 此字段可以设置为布尔值或字符串。如果设置为true，则CDN Pro服务器会将所有HTTP请求重定向到HTTPS，并返回301状态码。如果您希望在重定向请求时返回不同的状态码，可在此处指定需要的状态码，如'302'、'307'或'308'。"}
        self.redirect_http_to_https = redirect_http_to_https
        # {"en" : "Describes the origin servers for the property's content.", "zh_CN": "描述加速项目对应的源站。"}
        self.origins = origins
        # {"en" : "Default: 1 
        # The value must be set to 1 at this time.", "zh_CN": "默认值: 1 
        # 当前仅允许值为1。"}
        self.syntax_version = syntax_version
        # {"en" : "Default: False 
        # Set to true to disable support for HTTP/2 and support only HTTP 1.1.", "zh_CN": "默认值: False 
        # 当值为true时，禁用对HTTP/2的支持，仅支持HTTP/1.1。"}
        self.disable_http_2 = disable_http_2
        # {"en" : "Default: False 
        # Set to true to enable support for HTTP/3. HTTP/3 requires TLS to work, so this field will be ignored unless you specify a certificate in the tlsCertificateId field.", "zh_CN": "默认值: False 
        # 是否开启HTTP/3，HTTP/3 需要 需要配置TLS 才生效，若您未在 tlsCertificateId 中指定证书，此字段将被忽略。"}
        self.enable_http_3 = enable_http_3
        # {"en" : "Default: False 
        # Specifies whether the scheme ('http' or 'https') should be included in the cache key. Default behavior is false. Set to true if the content is known to be different for different schemes.
        # ", "zh_CN": "默认值: False 
        # 指定缓存键（Cache Key）是否区分协议（'http'或'https'）。默认为false。如果不同协议响应的内容不同，则设置为true。"}
        self.scheme_in_cache_key = scheme_in_cache_key
        # {"en" : "Enum: 1.1,1.2,1.3 
        # Default: 1.3 
        # Maximum supported TLS version.", "zh_CN": "取值范围: 1.1,1.2,1.3 
        # 默认值: 1.3 
        # 支持的TLS最高版本。"}
        self.tls_max_version = tls_max_version
        # {"en" : "Range: <= 100 characters 
        # Multiple tiers of load balancing are used in our CDN pops to distribute the client requests to different servers. We are using consistent hashing in many of those places. By default, the URL is used as the hash key, which should be good enough in most cases. Here you can define additional variables to be added to the hash key to distribute the requests more evenly. One typical use case is when all requests carry the same URL, but use a particular header to indicate the resources. 
        # 
        # This is an optional field. The default value is an empty string. A valid value is a string meeting the following criteria:
        # 
        # Consists of alphanumeric characters, underscore _, equal sign =, dollar sign $, and ampersand sign &.
        # The variable names can only be in one of the following formats: $http_name, $cookie_name, or $arg_name.
        # At least one variable must be specified. No more than three are permitted.
        # The total length should be no more than 100 characters.
        # 
        # The validator will treat any dollar sign and the string after it (before any = or & or $) as a variable. 
        # 
        # Here are some examples of valid values:
        # <table><tr><td>$http_abc</td></tr><tr><td>abc=$http_abc&def=$http_def&c_123=$cookie_123</td></tr><tr><td>abc=$http_abc=$http_def</td></tr><tr><td>$http_abc&$http_def</td></tr><tr><td>=$http_abd&</td></tr><tr><td>&&abc==$http_abc&&&===qwer</td></tr></table>
        # ", "zh_CN": "取值范围: <= 100 字符 
        # 我们的CDN使用了多层负载均衡架构，将客户端请求分发到不同的服务器。我们在架构中多处使用到一致性哈希。默认情况下，URL被用作哈希键，这对于大多数情况都适用。您可以在这里定义要添加到哈希键的其他变量，以更均匀地分配请求。一个典型的使用场景是，所有请求都携带相同的URL，但使用特定的请求头来区分资源。
        # 
        # 这是一个可选字段，默认值为空字符串。必须满足以下条件：
        # 
        # 由字母、数字、下划线_、等号=、美元符号$和符号&组成。
        # 变量名只能采用以下格式之一：$http_name、$cookie_name、$arg_name。
        # 必须至少指定一个变量，不允许超过三个。
        # 总长度不得超过100个字符。
        # 
        # 我们的配置验证器将把任何美元符号及其后的字符串（在任何=或&或$之前）视为变量。
        # 
        # 以下是一些有效值的示例：
        # <table><tr><td>$http_abc</td></tr><tr><td>abc=$http_abc&def=$http_def&c_123=$cookie_123</td></tr><tr><td>abc=$http_abc=$http_def</td></tr><tr><td>$http_abc&$http_def</td></tr><tr><td>=$http_abd&</td></tr><tr><td>&&abc==$http_abc&&&===qwer</td></tr></table>"}
        self.load_balancer_hash_key = load_balancer_hash_key
        # {"en" : "Refers to a certificate. It is invalid to only set the tlsCertificateId1 field without setting the tlsCertificateId field. If tlsCertificateId is not set, HTTPS will not be enabled for this property. This is a feature to enable you to specify two certificates of different types, i.e. one RSA, one EC. If two certificates of the same type are specified, the one specified by tlsCertificateId will be ignored. ", "zh_CN": "该加速项目用到的证书ID。仅设置tlsCertificateId1字段而不设置tlsCertificateId字段是无效的。如果未设置tlsCertificateId，则不会为此加速项目启用HTTPS。此功能允许您指定两个不同类型的证书，即一个RSA，一个EC。如果指定了两个相同类型的证书，则将忽略tlsCertificateId指定的证书。 "}
        self.tls_certificate_id = tls_certificate_id
        # {"en" : "Enum: 1.1,1.2,1.3,1 
        # Default: 1 
        # Minimum required TLS version.", "zh_CN": "取值范围: 1.1,1.2,1.3,1 
        # 默认值: 1 
        # 所需的TLS最低版本。"}
        self.tls_min_version = tls_min_version
        # {"en" : "Range: <= 2040 characters 
        # Any cipher list supported by 'openssl ciphers'. See https://www.openssl.org/docs/manmaster/man1/ciphers.html
        # ", "zh_CN": "取值范围: <= 2040 字符 
        # 'openssl ciphers'支持的任何加密算法套件。参考：https://www.openssl.org/docs/manmaster/man1/ciphers.html"}
        self.tls_ciphers = tls_ciphers
        # {"en" : "Default: False 
        # This setting applies only if the property has an attached certificate allowing client requests to use HTTPS. If the value of allowProtocolDowngrade is false, we require all the origin servers to support HTTPS. If the value is true, we allow origins that support only HTTP, which reduces security.
        # ", "zh_CN": "默认值: False 
        # 是否允许协议降级。仅当加速项目中存在允许客户端使用HTTPS请求的证书时，此设置才适用。如果allowProtocolDowngrade的值为false，则要求所有源服务器支持HTTPS。如果值为true，则允许仅支持HTTP的源，但这会降低安全性。"}
        self.allow_protocol_downgrade = allow_protocol_downgrade
        # {"en" : "Refers to a certificate. It is invalid to only set the tlsCertificateId1 field without setting the tlsCertificateId field. If tlsCertificateId is not set, HTTPS will not be enabled for this property. This is a feature to enable you to specify two certificates of different types, i.e. one RSA, one EC. If two certificates of the same type are specified, the one specified by tlsCertificateId will be ignored. 
        # ", "zh_CN": "指该加速项目用到的证书ID。仅设置tlsCertificateId1字段而不设置tlsCertificateId字段是无效的。如果未设置tlsCertificateId，则不会为此加速项目启用HTTPS。此功能允许您指定两个不同类型的证书，即一个RSA，一个EC。如果指定了两个相同类型的证书，则将忽略tlsCertificateId指定的证书。"}
        self.tls_certificate_id_1 = tls_certificate_id_1
        # {"en" : "This object allows you to support video players requesting partial content through query string parameters. If you specify videoSeek, you must enter a value for startParameter.", "zh_CN": "此对象用来支持视频播放器通过指定查询参数来请求部分内容。当videoSeek对象存在时，必须为startParameter设置一个值。"}
        self.video_seek = video_seek
        # {"en" : "Default: 1800 Range: [ 300 .. 86400 ] 
        # Lifespan of TLS session ticket in seconds.", "zh_CN": "默认值: 1800 取值范围: [ 300 .. 86400 ] 
        # TLS会话ticket的有效期（秒）。"}
        self.tls_session_timeout = tls_session_timeout
        # {"en" : "Default: False 
        # Enables Online Certificate Status Protocol (OCSP) stapling to check the revocation status of digital certificates. (Refer to https://en.wikipedia.org/wiki/OCSP_stapling)", "zh_CN": "默认值: False 
        # 是否启用在线证书状态协议（OCSP）装订以检查数字证书的吊销状态。参考：https://en.wikipedia.org/wiki/OCSP_stapling"}
        self.enable_ocsp_stapling = enable_ocsp_stapling
        # {"en" : "Range: [ 1 .. 24 ] 
        # If you are planning to distribute content through servers in mainland China, you will need to set the hasBeian field to true and also indicate the type of content you are distributing. Enter the value that best corresponds to your content:
        # 
        # <table><tr><th>Value</th><th>Content Type</th></tr><tr><td>1</td><td>Instant Messaging</td></tr><tr><td>2</td><td>Search Engine</td></tr><tr><td>3</td><td>Web Portal</td></tr><tr><td>4</td><td>Online Postal Service</td></tr><tr><td>5</td><td>Online News</td></tr><tr><td>6</td><td>Blog</td></tr><tr><td>7</td><td>Advertisement</td></tr><tr><td>8</td><td>Organization Web Portal</td></tr><tr><td>9</td><td>Shopping</td></tr><tr><td>10</td><td>Online Payment</td></tr><tr><td>11</td><td>Online Bank</td></tr><tr><td>12</td><td>Online Stock Market</td></tr><tr><td>13</td><td>Online Gaming</td></tr><tr><td>14</td><td>Online Music</td></tr><tr><td>15</td><td>Online Movie</td></tr><tr><td>16</td><td>Online Picture</td></tr><tr><td>17</td><td>Software Download</td></tr><tr><td>18</td><td>Job Hunting</td></tr><tr><td>19</td><td>Online Dating</td></tr><tr><td>20</td><td>Online Real Property</td></tr><tr><td>21</td><td>Online Education</td></tr><tr><td>22</td><td>Web Design</td></tr><tr><td>23</td><td>WAP</td></tr><tr><td>24</td><td>Others</td></tr></table>", "zh_CN": "取值范围: [ 1 .. 24 ] 
        # 如果您的域名已获得备案，希望通过中国大陆的服务器分发内容，则需要将hasBeian字段设置为true，并说明您分发的内容类型。请选择与您的内容最匹配的值：
        # 
        # <table><tr><th>值</th><th>内容类型</th></tr><tr><td>1</td><td>即时通信</td></tr><tr><td>2</td><td>搜索引擎</td></tr><tr><td>3</td><td>综合门户</td></tr><tr><td>4</td><td>网上邮局</td></tr><tr><td>5</td><td>网络新闻</td></tr><tr><td>6</td><td>博客/个人空间</td></tr><tr><td>7</td><td>网络广告</td></tr><tr><td>8</td><td>单位门户网站</td></tr><tr><td>9</td><td>网络购物</td></tr><tr><td>10</td><td>网上支付</td></tr><tr><td>11</td><td>网上银行</td></tr><tr><td>12</td><td>网上炒股</td></tr><tr><td>13</td><td>网络游戏</td></tr><tr><td>14</td><td>网络音乐</td></tr><tr><td>15</td><td>网络影视</td></tr><tr><td>16</td><td>网络图片</td></tr><tr><td>17</td><td>软件下载</td></tr><tr><td>18</td><td>网上求职</td></tr><tr><td>19</td><td>在线交友</td></tr><tr><td>20</td><td>网上房产</td></tr><tr><td>21</td><td>网络教育</td></tr><tr><td>22</td><td>网站建设</td></tr><tr><td>23</td><td>WAP</td></tr><tr><td>24</td><td>其他</td></tr></table>"}
        self.beian_content_type = beian_content_type
        # {"en" : "Default: False 
        # Is it allowed to use IPv6 addresses as the source server for this project.", "zh_CN": "默认值: False 
        # 是否允许使用 IPv6 地址作为该项目的源站服务器"}
        self.enable_ipv_6origin = enable_ipv_6origin
        # {"en" : "Default value: off Optional values: auto, strict, off
        # When enableIpv6Origin is allowed, this setting will control whether to follow the client IP protocol version back to the source.
        # Auto: Refers to selecting the IP address for returning to the source based on the IP protocol version requested by the client. When the source server is unavailable, it automatically switches to another IP protocol address for returning to the source
        # Strict: Strictly select the IP address for returning to the source based on the IP protocol version requested by the client. When the source server is unavailable, it is not allowed to switch to another protocol address for returning to the source
        # Off: Ignore the IP protocol version requested by the client and randomly select an available IPv4 or IPv6 address to return to the source.", "zh_CN": "默认值：off 可选值：auto、strict、off 当enableIpv6Origin为允许时，该设置将控制是否跟随客户端IP协议版本回源。
        # auto：表示根据客户端请求的IP协议版本来选择回源IP地址，当源站服务器不可用时自动切换成其他IP协议地址回源
        # strict：严格根据客户端请求的IP协议版本来选择回源IP地址，当源站服务器不可用时不允许切换成其他协议地址回源
        # off：忽略客户端请求的IP协议版本，随机选择可用的IPv4或IPv6地址回源"}
        self.follow_client_ip_version = follow_client_ip_version
        # {"en" : "Specify one or more access control rules to restrict access to your content. More advanced configuration can be done using Edge Logic. These access control rules take precedence over Edge Logic if both are defined.", "zh_CN": "指定一个或多个访问控制规则以限制对内容的访问。可以使用边缘逻辑进行更高级的配置。此处定义的访问控制规则，优先级高于边缘逻辑。"}
        self.access_control_rules = access_control_rules
        # {"en" : "Default: False 
        # By default, CDN Pro takes control of the contents under the /.well-known/{acme-challenge, pki-validation} directories to support certificate auto-renew for properties. If for any reason you need to manage these two directories by yourself on the origin, for example, to implement your own certificate auto-renew mechanism, you can use this configuration option to disable the default behavior by setting its value to true. For more information about our support for certificate auto-renewal, refer to the description of the autoRenew field in the Create a certificate API.", "zh_CN": "默认值: False 
        # 默认情况下，CDN Pro控制/.well-known/{acme-challenge, pki-validation}目录下的内容，以支持加速项目的证书自动更新功能。如果您需要自己在源站管理这两个目录，例如，为了实现您自己的证书自动更新机制，您可以将此字段设置为true来禁用默认行为。关于证书自动更新的更多信息，请参考'创建证书'接口中autoRenew字段的说明。"}
        self.disable_cert_automation = disable_cert_automation
        # {"en" : "Enum: preRewrite,postRewrite 
        # Default: preRewrite 
        # This setting controls how the URI of the incoming request is incorporated into the cache key if you use a 'rewrite' directive in the property's Edge Logic. The default value, 'preRewrite', puts the unmodified URI into the cache key while 'postRewrite' uses the modified URI. If your rewrite directive converts multiple different URIs into the same value, using 'postRewrite' may result in a higher cache hit ratio.", "zh_CN": "取值范围: preRewrite,postRewrite 
        # 默认值: preRewrite 
        # 如果在加速项目的边缘逻辑中使用了'rewrite'指令，可使用该字段来控制客户端请求的URI如何合并到缓存键（Cache Key）中 。默认值'preRewrite'指将改写前的URI放入缓存键，而'postRewrite'则使用改写后的URI。如果您的'rewrite'指令将多个不同的URI改写为相同的值，则使用'postRewrite'可以提高缓存命中率。"}
        self.cache_key_uri = cache_key_uri
        # {"en" : "This field lists ports other than the default 80 used to handle HTTP requests and ports other than the default 443 used to handle HTTPS requests. ", "zh_CN": "除标准的80，443端口外，我们还支持一些扩展端口。可用该字段指定用于处理HTTP和HTTPS请求的扩展端口。"}
        self.extra_service_ports = extra_service_ports
        # {"en" : "Range: <= 65530 characters 
        # This field allows you to enter Edge Logic to customize load balancing. A subset of the  directives can be used. Refer to the basic directives listed in the baseLbDirectives field of the response to the system configuration API. Currently, these include 'if', 'else', 'elseif', 'set', 'return', 'add_header', 'deny', 'allow', 'access_log_sampling', and 'proxy_set_header.' In addition, some advanced Edge Logic directives, identified by the system configuration API's advancedLbDirectives, can be enabled for your account if needed. Please contact our support team if you require any of them. <br/> Example use: <br />
        # if ($http_user_agent = bot) { return 403;}
        # ", "zh_CN": "取值范围: <= 65530 字符 
        # 此字段可用来自定义边缘逻辑，控制负载均衡器的行为。支持使用 边缘逻辑指令中的部分指令。请参考'获取系统配置'接口中baseLbDirectives字段所列出的负载均衡基础指令。目前，这些基础指令包括'if'、'else'、'elseif'、'set'、'return'、'add_header'、'deny'、'allow'、'access_log_sampling'和'proxy_set_headers'。此外，我们还支持一些高级指令，请参考'获取系统配置'接口中advancedLbDirectives字段所列出的负载均衡高级指令。如果您需要使用这些高级指令，请联系技术支持。
        # 
        # <br/>示例：<br/>
        # 
        # if ($http_user_agent = bot) { return 403;}
        # "}
        self.load_balancer_logic = load_balancer_logic
        # {"en" : "Default: False 
        # Enable TLS zero round-trip time, a feature of TLS 1.3 that can improve performance for repeat visits to a site. If enabling it though, be sure your site is not vulnerable to the HTTP replay attack.", "zh_CN": "默认值: False 
        # 是否开启TLS 0-RTT功能。这是TLS 1.3版本支持的功能。启用该功能后，当用户频繁访问您的站点时，可提高访问响应速度。需要注意的是，启用该功能可能会加大站点遭受HTTP replay攻击的风险。"}
        self.tls_0rtt = tls_0rtt

    def validate(self):
        if self.real_time_log:
            self.real_time_log.validate()
        if self.origins:
            for k in self.origins:
                if k:
                    k.validate()
        if self.video_seek:
            self.video_seek.validate()
        if self.access_control_rules:
            for k in self.access_control_rules:
                if k:
                    k.validate()
        if self.extra_service_ports:
            self.extra_service_ports.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.cache_key_hostname is not None:
            result['cacheKeyHostname'] = self.cache_key_hostname
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.real_time_log is not None:
            result['realTimeLog'] = self.real_time_log.to_map()
        if self.edge_logic is not None:
            result['edgeLogic'] = self.edge_logic
        if self.has_beian is not None:
            result['hasBeian'] = self.has_beian
        if self.redirect_http_to_https is not None:
            result['redirectHttpToHttps'] = self.redirect_http_to_https
        if self.origins is not None:
            result['origins'] = []
            for k in self.origins:
                result['origins'].append(k.to_map() if k else None)
        if self.syntax_version is not None:
            result['syntaxVersion'] = self.syntax_version
        if self.disable_http_2 is not None:
            result['disableHttp2'] = self.disable_http_2
        if self.enable_http_3 is not None:
            result['enableHttp3'] = self.enable_http_3
        if self.scheme_in_cache_key is not None:
            result['schemeInCacheKey'] = self.scheme_in_cache_key
        if self.tls_max_version is not None:
            result['tlsMaxVersion'] = self.tls_max_version
        if self.load_balancer_hash_key is not None:
            result['loadBalancerHashKey'] = self.load_balancer_hash_key
        if self.tls_certificate_id is not None:
            result['tlsCertificateId'] = self.tls_certificate_id
        if self.tls_min_version is not None:
            result['tlsMinVersion'] = self.tls_min_version
        if self.tls_ciphers is not None:
            result['tlsCiphers'] = self.tls_ciphers
        if self.allow_protocol_downgrade is not None:
            result['allowProtocolDowngrade'] = self.allow_protocol_downgrade
        if self.tls_certificate_id_1 is not None:
            result['tlsCertificateId1'] = self.tls_certificate_id_1
        if self.video_seek is not None:
            result['videoSeek'] = self.video_seek.to_map()
        if self.tls_session_timeout is not None:
            result['tlsSessionTimeout'] = self.tls_session_timeout
        if self.enable_ocsp_stapling is not None:
            result['enableOcspStapling'] = self.enable_ocsp_stapling
        if self.beian_content_type is not None:
            result['beianContentType'] = self.beian_content_type
        if self.enable_ipv_6origin is not None:
            result['enableIpv6Origin'] = self.enable_ipv_6origin
        if self.follow_client_ip_version is not None:
            result['followClientIpVersion'] = self.follow_client_ip_version
        if self.access_control_rules is not None:
            result['accessControlRules'] = []
            for k in self.access_control_rules:
                result['accessControlRules'].append(k.to_map() if k else None)
        if self.disable_cert_automation is not None:
            result['disableCertAutomation'] = self.disable_cert_automation
        if self.cache_key_uri is not None:
            result['cacheKeyUri'] = self.cache_key_uri
        if self.extra_service_ports is not None:
            result['extraServicePorts'] = self.extra_service_ports.to_map()
        if self.load_balancer_logic is not None:
            result['loadBalancerLogic'] = self.load_balancer_logic
        if self.tls_0rtt is not None:
            result['tls0Rtt'] = self.tls_0rtt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('cacheKeyHostname') is not None:
            self.cache_key_hostname = m.get('cacheKeyHostname')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('realTimeLog') is not None:
            temp_model = CreateAPropertyVersionRequestRealTimeLog()
            self.real_time_log = temp_model.from_map(m['realTimeLog'])
        if m.get('edgeLogic') is not None:
            self.edge_logic = m.get('edgeLogic')
        if m.get('hasBeian') is not None:
            self.has_beian = m.get('hasBeian')
        if m.get('redirectHttpToHttps') is not None:
            self.redirect_http_to_https = m.get('redirectHttpToHttps')
        if m.get('origins') is not None:
            self.origins = []
            for k in m.get('origins'):
                temp_model = CreateAPropertyVersionRequestOrigins()
                self.origins.append(temp_model.from_map(k))
        if m.get('syntaxVersion') is not None:
            self.syntax_version = m.get('syntaxVersion')
        if m.get('disableHttp2') is not None:
            self.disable_http_2 = m.get('disableHttp2')
        if m.get('enableHttp3') is not None:
            self.enable_http_3 = m.get('enableHttp3')
        if m.get('schemeInCacheKey') is not None:
            self.scheme_in_cache_key = m.get('schemeInCacheKey')
        if m.get('tlsMaxVersion') is not None:
            self.tls_max_version = m.get('tlsMaxVersion')
        if m.get('loadBalancerHashKey') is not None:
            self.load_balancer_hash_key = m.get('loadBalancerHashKey')
        if m.get('tlsCertificateId') is not None:
            self.tls_certificate_id = m.get('tlsCertificateId')
        if m.get('tlsMinVersion') is not None:
            self.tls_min_version = m.get('tlsMinVersion')
        if m.get('tlsCiphers') is not None:
            self.tls_ciphers = m.get('tlsCiphers')
        if m.get('allowProtocolDowngrade') is not None:
            self.allow_protocol_downgrade = m.get('allowProtocolDowngrade')
        if m.get('tlsCertificateId1') is not None:
            self.tls_certificate_id_1 = m.get('tlsCertificateId1')
        if m.get('videoSeek') is not None:
            temp_model = CreateAPropertyVersionRequestVideoSeek()
            self.video_seek = temp_model.from_map(m['videoSeek'])
        if m.get('tlsSessionTimeout') is not None:
            self.tls_session_timeout = m.get('tlsSessionTimeout')
        if m.get('enableOcspStapling') is not None:
            self.enable_ocsp_stapling = m.get('enableOcspStapling')
        if m.get('beianContentType') is not None:
            self.beian_content_type = m.get('beianContentType')
        if m.get('enableIpv6Origin') is not None:
            self.enable_ipv_6origin = m.get('enableIpv6Origin')
        if m.get('followClientIpVersion') is not None:
            self.follow_client_ip_version = m.get('followClientIpVersion')
        if m.get('accessControlRules') is not None:
            self.access_control_rules = []
            for k in m.get('accessControlRules'):
                temp_model = CreateAPropertyVersionRequestAccessControlRules()
                self.access_control_rules.append(temp_model.from_map(k))
        if m.get('disableCertAutomation') is not None:
            self.disable_cert_automation = m.get('disableCertAutomation')
        if m.get('cacheKeyUri') is not None:
            self.cache_key_uri = m.get('cacheKeyUri')
        if m.get('extraServicePorts') is not None:
            temp_model = CreateAPropertyVersionRequestExtraServicePorts()
            self.extra_service_ports = temp_model.from_map(m['extraServicePorts'])
        if m.get('loadBalancerLogic') is not None:
            self.load_balancer_logic = m.get('loadBalancerLogic')
        if m.get('tls0Rtt') is not None:
            self.tls_0rtt = m.get('tls0Rtt')
        return self


class CreateAPropertyVersionResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPropertyVersionResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"Refers to the new version", "zh_CN":"通过Location响应头返回新建的加速项目版本的URL。URL中包含了加速项目的ID以及版本号。URL示例：<code>Location: http://open.chinanetcenter.com/cdn/properties/5dca2205f9e9cc0001df7b33/versions/2</code>"}
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






class UpdateAPropertyVersionPaths(TeaModel):
    def __init__(
        self,
        property_id: str = None,
        version: str = None,
    ):
        # {"en" : "ID of a property.", "zh_CN": "加速项目ID。"}
        self.property_id = property_id
        # {"en" : "A property version. It must be an integer value >=1. The Get a property version API also permits you to specify the word 'latest' to obtain the most recent version.", "zh_CN": "加速项目版本。必须是大于等于1的整数值。"}
        self.version = version

    def validate(self):
        self.validate_required(self.property_id, 'property_id')
        self.validate_required(self.version, 'version')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.property_id is not None:
            result['propertyId'] = self.property_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('propertyId') is not None:
            self.property_id = m.get('propertyId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpdateAPropertyVersionParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAPropertyVersionRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAPropertyVersionRequestRealTimeLogHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # {"en" : "Name of an HTTP header.", "zh_CN": "HTTP标头名称"}
        self.name = name
        # {"en" : "Value of an HTTP header.", "zh_CN": "HTTP标头值"}
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class UpdateAPropertyVersionRequestRealTimeLog(TeaModel):
    def __init__(
        self,
        log_url: str = None,
        sample_rate: int = None,
        escape: str = None,
        format: str = None,
        headers: List[UpdateAPropertyVersionRequestRealTimeLogHeaders] = None,
    ):
        # {"en" : "The URL that receives the notifications. It must begin with 'http' or 'https'. The server should support the POST method. This is a required field.", "zh_CN": "接收通知的服务器URL地址。必须以'http'或'https'开头。服务器须支持POST方法。这是必填字段。"}
        self.log_url = log_url
        # {"en" : "Default: 1 Range: [ 1 .. 65536 ] 
        # An integer between [1, 65536]. n means one notification for every n edge requests. 1 means every edge request will generate a notification. This is optional. Default is 1.", "zh_CN": "默认值: 1 取值范围: [ 1 .. 65536 ] 
        # 采样率。介于[1, 65536]之间的整数。n表示每n个边缘请求发送1条通知。1表示每个边缘请求都会发送。这是可选字段。默认值为1。"}
        self.sample_rate = sample_rate
        # {"en" : "Enum: json,none 
        # Specify json to enable JSON character escaping in variables or none to disable escaping.", "zh_CN": "取值范围: json,none 
        # 指定json以开启变量中的json字符转义。如果要禁用转义则指定none。"}
        self.escape = escape
        # {"en" : "This is a required field to specify the notification body to be sent to the remote server. It can be any printable text that can be sent in the body of an HTTP POST request. 
        # 
        # The following built-in variables can be used within the format field. They will be replaced with the actual values in the notifications.
        # <table><tr><th>Name</th><th>Description</th></tr><tr><td>$body_bytes_sent</td><td>Size of the response body.</td></tr><tr><td>$bytes_sent</td><td>Size of the response, including body, headers and response line.</td></tr><tr><td>$client_country_code</td><td>An ISO 3166-1 country code representing the country of the client request, for example, 'US'. 'ZZ' is returned if the country is unknown.</td></tr><tr><td>$client_real_ip</td><td>IP address of the client request.</td></tr><tr><td>$cookie_x</td><td>This lets you obtain any cookie named x.  For example, $cookie_account would retrieve the value of a cookie named 'account'.</td></tr><tr><td>$http_x</td><td>Obtain any HTTP header named x from the original request. The header name is converted to lower case with dashes replaced by underscores. For example, specify $http_user_agent to get the value of User-Agent.</td></tr><tr><td>$msec</td><td>Current unix time in seconds with millisecond precision.</td></tr><tr><td>$qtl_req_id</td><td>Unique identifier representing the request.</td></tr><tr><td>$request_uri</td><td>HTTP request URI</td></tr><tr><td>$request_method</td><td>The HTTP request method used to access the origin.</td></tr><tr><td>$request_time</td><td>Response time in milliseconds. It is the time between receiving the request's  first byte and serving the last byte of the response.</td></tr><tr><td>$sc_completed</td><td>1 to indicate the last byte of the object was served to the user, 0 otherwise.</td></tr><tr><td>$sc_initial</td><td>1 to indicate the first byte of the object was served to the user, 0 otherwise.</td></tr><tr><td>$scheme</td><td>Indicates the protocol of the user's request ('http' or https').</td></tr><tr><td>$sent_http_content_length</td><td>the original file size.</td></tr><tr><td>$sent_http_x</td><td>Obtain the value of an HTTP header named x that is returned in the response to the client. The header name should be converted to lower case with dashes replaced by underscores. For example, $sent_http_etag would give you the value of the ETag header.</td></tr><tr><td>$server_addr</td><td>IP address of the edge node serving the user's request.</td></tr><tr><td>$server_protocol</td><td>Indicates the version of HTTP used in the user's request, either 'HTTP/1.0', 'HTTP/1.1', or 'HTTP/2.0'.</td></tr><tr><td>$ssl_cipher</td><td>Indicates the cipher suite used for the TLS (SSL) connection.</td></tr><tr><td>$ssl_server_name</td><td>The hostname that a client initiating a TLS (SSL) connection is attempting to connect to. It is only sent by clients supporting SNI (Server Name Indication).</td></tr><tr><td>$ssl_protocol</td><td>Indicates the TLS version used for the TLS (SSL) connection. Example versions include 'SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2', and 'unknown'.</td></tr><tr><td>$status</td><td>An HTTP response code for the user's request.</td></tr><tr><td>$tcpinfo_rtt</td><td>The time in microseconds taken by a packet to travel to the destination and back.</td></tr></table>", "zh_CN": "该字段用来定义要发送到远程服务器的通知的格式。通知正文可以包括任何能在HTTP POST请求体中发送的可打印文本。这是必填字段。
        # 
        # 可以使用以下内置变量定义通知的格式。发送通知时，它们将被替换为实际值。
        # <table><tr><th>变量名称</th><th>描述</th></tr><tr><td>$body_bytes_sent</td><td>响应体大小。</td></tr><tr><td>$bytes_sent</td><td>响应的大小，包括响应体、响应头和响应行。</td></tr><tr><td>$client_country_code</td><td>客户端请求来源国家，以ISO 3166-1国家代码表示。例如'US'。如果国家/地区未知，则返回'ZZ'。</td></tr><tr><td>$client_real_ip</td><td>客户端请求的IP地址。</td></tr><tr><td>$cookie_x</td><td>获取某个cookie。例如，指定$cookie_account可获取名为'account'的cookie值。</td></tr><tr><td>$http_x</td><td>从原始请求中获取某个HTTP请求头。请求头名称需转换为小写，并用下划线替换连字符。例如，指定$http_user_agent来获取User-Agent的值。</td></tr><tr><td>$msec</td><td>当前unix时间，以毫秒为单位。</td></tr><tr><td>$qtl_req_id</td><td>请求的唯一标识符。</td></tr><tr><td>$request_uri</td><td>HTTP请求URI。</td></tr><tr><td>$request_method</td><td>用于访问源站的HTTP请求方法。</td></tr><tr><td>$request_time</td><td>响应时间，以毫秒为单位。这是从接收到请求的第一个字节到服务端响应最后一个字节之间的时间。</td></tr><tr><td>$sc_completed</td><td>1表示对象的最后一个字节已返回给用户，否则为0。</td></tr><tr><td>$sc_initial</td><td>1表示对象的第一个字节已返回给用户，否则为0。</td></tr><tr><td>$scheme</td><td>表示用户请求的协议（'http'或'https'）。</td></tr><tr><td>$sent_http_content_length</td><td>原始文件大小。</td></tr><tr><td>$sent_http_x</td><td>获取在对客户端响应中某个HTTP响应头的值。响应头名称需转换为小写，并用下划线替换连字符。例如，$sent_http_etag可获取ETag头的值。</td></tr><tr><td>$server_addr</td><td>为用户请求提供服务的边缘节点的IP地址。</td></tr><tr><td>$server_protocol</td><td>表示用户请求中使用的HTTP版本，可以是'HTTP/1.0'、'HTTP/1.1'或'HTTP/2.0'。</td></tr><tr><td>$ssl_cipher</td><td>表示用于TLS（SSL）连接的加密算法套件。</td></tr><tr><td>$ssl_server_name</td><td>客户端发起TLS（SSL）连接所要连接的域名。仅由支持SNI（Server Name Indication）的客户端发送。</td></tr><tr><td>$ssl_protocol</td><td>表示用于TLS（SSL）连接的TLS版本。例如，'SSLv3'、'TLSv1'、'TLSv1.1'、'TLSv1.2'和'unknown'。</td></tr><tr><td>$status</td><td>用户请求的HTTP状态码。</td></tr><tr><td>$tcpinfo_rtt</td><td>数据包往返目的地所用的时间，以微秒为单位。</td></tr></table>"}
        self.format = format
        # {"en" : "HTTP header names and values to be sent to the notification server. A header name can contain any alphanumeric character or hyphen, '-'. A header value can contain any printable characters. It can also include any of the built-in variables supported in the format field of the realTimeLog object.", "zh_CN": "需要发送到远程服务器的HTTP请求头名称和值。请求头名称可以包含任何字母，数字或连字符'-'。值可以包含任何可打印字符，也可以使用realTimeLog对象format字段中支持的任何内置变量。"}
        self.headers = headers

    def validate(self):
        self.validate_required(self.log_url, 'log_url')
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_url is not None:
            result['logUrl'] = self.log_url
        if self.sample_rate is not None:
            result['sampleRate'] = self.sample_rate
        if self.escape is not None:
            result['escape'] = self.escape
        if self.format is not None:
            result['format'] = self.format
        if self.headers is not None:
            result['headers'] = []
            for k in self.headers:
                result['headers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logUrl') is not None:
            self.log_url = m.get('logUrl')
        if m.get('sampleRate') is not None:
            self.sample_rate = m.get('sampleRate')
        if m.get('escape') is not None:
            self.escape = m.get('escape')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('headers') is not None:
            self.headers = []
            for k in m.get('headers'):
                temp_model = UpdateAPropertyVersionRequestRealTimeLogHeaders()
                self.headers.append(temp_model.from_map(k))
        return self


class UpdateAPropertyVersionRequestOriginsAuthentication(TeaModel):
    def __init__(
        self,
        method_name: str = None,
    ):
        # {"en" : "Authentication method.", "zh_CN": "鉴权方法。"}
        self.method_name = method_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method_name is not None:
            result['methodName'] = self.method_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        return self


class UpdateAPropertyVersionRequestOrigins(TeaModel):
    def __init__(
        self,
        name: str = None,
        servers: List[str] = None,
        supported_protocol: str = None,
        direct_connection: str = None,
        host_header: str = None,
        verify_origin: bool = None,
        authentication: UpdateAPropertyVersionRequestOriginsAuthentication = None,
        keep_alive_timeout: int = None,
        peer_failure_timeout: str = None,
        tls_certificate_id: str = None,
        shield: str = None,
    ):
        # {"en" : "^[a-zA-z0-9_] 
        # Name of an origin. It must be unique within this property.
        # ", "zh_CN": "^[a-zA-z0-9_] 
        # 源站名称，在此加速项目中必须唯一。"}
        self.name = name
        # {"en" : "Each entry should be a string consisting of an address optionally followed by one or more parameters, separated by space characters. The address can take one of the following three forms:
        # {hostname or IP address}
        # {hostname or IP address}:{http port}
        # {hostname or IP address}:{http port},{https port}
        # Values for the HTTP and HTTPS ports should be integers in the range [1,65535]. 
        # Even if the value of supportedProtocol is 'https', the HTTPS port has to be specified after the comma.
        # In the third form, one of the two ports can be empty.
        # 
        # Supported parameters are 'backup' and 'weight'.
        # 
        # 'backup' is used to indicate the server is a backup server. It will be used when the primary servers are unavailable.
        # 
        # 'weight' is a value in the range [1, 100]. The default value is 1. It lets you control the likelihood that one origin server will be used relative to another.
        # 
        # There should be at least one primary server defined; it does not have the 'backup' parameter.
        # 
        # Example:
        # ['www.abc.com weight=1', 'www1.abc.com:8080 weight=4', 'www2.abc.com:880,4443 backup']
        # 
        # This example specifies two primary servers which are used in a 1:4 ratio meaning one gets about 20% of the requests to origin while the other gets 80% of the requests. In addition, a backup server is specified.
        # ", "zh_CN": "源站服务器列表。每个条目为一个字符串，由一个地址与一个或多个参数组成，参数之间以空格分隔。地址可以采用以下三种形式之一：
        # {域名或IP地址}
        # {域名或IP地址}:{HTTP端口}
        # {域名或IP地址}:{HTTP端口},{HTTPS端口}
        # HTTP和HTTPS端口的值应为[1,65535]范围内的整数。
        # 即使supportedProtocol的值设为'https'，也必须在此处指定HTTPS端口。
        # 在第三种形式中，两个端口中的一个可以为空。
        # 支持ipv6 当enableIpv6Origin为true时，ipv6传入{域名或IP地址}:{HTTP端口},{HTTPS端口}时，域名或IP地址需要放入[]，如[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:80
        # 
        # 支持的参数包括'backup'和'weight'。
        # 'backup'用于标识备份服务器。它将在主服务器不可用时使用。
        # 'weight'是范围[1,100]内的值，默认值为1，用来设置服务器权重，控制一台源站服务器相对于另一台被使用的可能性。
        # 每个源站应至少定义一个主服务器（即不带'backup'参数的服务器）。
        # 
        # 示例：
        # ['www.abc.com weight=1', 'www1.abc.com:8080 weight=4', 'www2.abc.com:880,4443 backup']
        # 
        # 此示例指定了两个主服务器和一个备份服务器，其中，主服务器的权重为1:4，表示第一个服务器将获得约20%的回源请求，而另一个将获得约80%。"}
        self.servers = servers
        # {"en" : "Enum: http,https,both 
        # This optional field indicates the protocol supported by the origin server. If this property has a certificate attached to it, the value can be set to http if the allowProtocolDowngrade field is also set to true.", "zh_CN": "取值范围: http,https,both 
        # 此可选字段表示源站服务器支持的协议。如果此加速项目附加了证书，且allowProtocolDowngrade字段也设置为true，则可以将该值设置为http。"}
        self.supported_protocol = supported_protocol
        # {"en" : "Default: auto 
        # Optional. This parameter tells us how important it is to directly go to this origin without going through any intermediate cache to fetch content. The values can be 'noDirect', 'auto', 'alwaysDirect'. 
        # 
        # 'noDirect' means we always go through at least one intermediate cache. Customers who care particularly about the origin's workload can use this option. Our cache scheduler will dynamically pick the intermediate cache based on performance and resource availability.
        # 
        # 'auto' means the cache scheduler will make the choice dynamically based on performance and resource availability. This is the default behavior if not specified.
        # 
        # 'alwaysDirect' means we always directly connect to this origin.
        # ", "zh_CN": "默认值: auto 
        # 此可选字段用来指定回源方式，可以是'noDirect'、'auto'、'alwaysDirect'。
        # 
        # 'noDirect'指总是通过至少一个中间缓存节点回源。对于特别关心源站负载的客户可以使用此选项。我们的调度程序将根据性能和资源可用性动态选择中间缓存节点。
        # 'alwaysDirect'指总是直接回源。
        # 'auto'指自动选择直接回源或通过中间缓存节点回源。调度程序将根据性能和资源可用性动态做出选择。该字段未指定时，采用此默认行为。"}
        self.direct_connection = direct_connection
        # {"en" : "Optional. It should be a valid hostname. It will also be used as the SNI servername when contacting the HTTPS origin. We also allow it to be an nginx variable that begins with '$' followed by [a-z_]{3,60}. Nginx variable names are case insensitive, so we only allow lowercase characters.
        # If not specified, the value of the HOST header in the request will be used. 
        # 
        # One constraint is that if 'aswS3' is specified for origin authentication, the value of hostHeader cannot be a variable or empty. It has to be a valid Amazon S3 hostname. Refer to https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html", "zh_CN": "可选，用来指定回源HOST头部。必须是有效的域名。当连接HTTPS源站时，该值也作为SNI域名。可以用nginx变量来指定，变量以'$'开头，后跟[a-z_]{3,60}。Nginx变量名不区分大小写，因此我们只允许小写字符。
        # 如果未指定，将使用请求中的HOST请求头的值。
        # 
        # 注意：如果指定了'awsS3'作为回源鉴权参数，则hostHeader的值不能为变量或为空，而必须是有效的Amazon S3主机名。参考：https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html"}
        self.host_header = host_header
        # {"en" : "Default: False 
        # Optional. It controls whether the cache will validate the certificate of the origin.", "zh_CN": "默认值: False 
        # 可选。用来设定CDN缓存节点是否验证源站证书。"}
        self.verify_origin = verify_origin
        # {"en" : "Optional. It is a structure to specify the parameters, such as password, for authentication with the origin servers. It should have at least one field: 'methodName', which should be a string indicating one of the predefined authentication methods. The only valid value at this time is 'awsS3'. When 'awsS3' is used, the following parameters are required:
        # awsS3.region:
        # The AWS S3 region where your resources are hosted, e.g. 'us-west-1', 'ap-northeast-1', 'eu-north-1', and 'cn-north-1'.
        # awsS3.accessKey:
        # Your AWS access key that CDN Pro will use to access your resources stored on AWS S3.
        # awsS3.secretKey:
        # Your AWS secret key that CDN Pro will use to access your resources stored on AWS S3.
        # Also, the value of the hostHeader field cannot be a variable or empty. It must be a valid Amazon S3 hostname.
        # 
        # Example:
        # 
        # {'methodName':'awsS3',
        # 'awsS3':{
        # 'region':'us-west-1',
        # 'accessKey':'sdnu2932',
        # 'secretKey':'d12345678abcdefghi'
        # }}
        # ", "zh_CN": "可选。用于指定与源服务器进行身份验证（回源鉴权）的相关参数（如密码）。必须至少有'methodName'（字符串）字段，用来指定预定义的鉴权方法。目前仅支持源站为AWS S3的回源鉴权，因此唯一有效的值是'awsS3'。使用'awsS3'时，需要提供以下参数：
        # awsS3.region:
        # 您存储在S3上的资源所在的AWS区域。例如，'us-west-1'，'ap-northeast-1'，'eu-north-1'，'cn-north-1'。
        # awsS3.accessKey:
        # 您的 AWS 访问密钥（access key），CDN Pro 将使用它来访问您存储在 AWS S3 上的资源。
        # awsS3.secretKey:
        # 您的 AWS 密钥（secret key），CDN Pro 将使用它来访问您存储在 AWS S3 上的资源。
        # 此外，hostHeader字段的值不能为变量或为空，必须是有效的Amazon S3主机名。
        # 
        # 示例：
        # 
        # {'methodName':'awsS3',
        # 'awsS3':{
        # 'region':'us-west-1',
        # 'accessKey':'sdnu2932',
        # 'secretKey':'d12345678abcdefghi'
        # }}
        # "}
        self.authentication = authentication
        # {"en" : "Default: 60 Range: [ 5 .. 600 ] 
        # Timeout in seconds during which an idle keepalive connection to an upstream server will stay open. A service quota setting of maxUpstreamKeepaliveTimeOut can change the maximum permitted value.", "zh_CN": "默认值: 60 取值范围: [ 5 .. 600 ] 
        # 该字段用于指定CDN Pro服务器和源站建连的Keep-Alive超时时间，单位为秒。通过maxUpstreamKeepaliveTimeOut 该服务设置项可以更改允许的最大值。如果需要调整最大值，请联系我们的技术支持。"}
        self.keep_alive_timeout = keep_alive_timeout
        # {"en" : "
        # This setting allows you to specify the number of unsuccessful attempts to reach one of the origin's IP addresses or peers before it is marked as unavailable for a period of time designated by the timeout. If all peers of all servers are unavailable, requests for content from the origin will receive an immediate 502 HTTP response. By default, six attempts to a peer are made, after which a one-second timeout applies to that peer. To disable this feature, set peerFailureTimeout to 'off'.", "zh_CN": "
        # 该字段用于设置源站故障剔除。开启此功能后，当连接某个源站服务器的失败次数达到设定阈值，该源站服务器将被标记为不可用，并保持该状态直到设定的超时时长。失败次数阈值和超时时长分别通过failureThreshold参数和timeout参数设置。CDN Pro回源时将剔除不可用的源站服务器。如果所有源站服务器都被标记为不可用，则对应的请求将立即响应502状态码。默认情况下，当连接某个源站服务器连续失败6次之后，该服务器将被标记为不可用，超时时长为1秒。如果要禁用此功能，请将peerFailureTimeout设置为'off'。开启源站故障剔除配置示例：<code>{'peerFailureTimeout':{'failureThreshold':10,'timeout':3}}</code>"}
        self.peer_failure_timeout = peer_failure_timeout
        # {"en" : "Refers to a certificate used to authenticate with the origin server. This certificate must also be deployed.", "zh_CN": "用于验证源站服务器的证书，该证书同样必须被部署。"}
        self.tls_certificate_id = tls_certificate_id
        # {"en" : "Refers to the ID of an origin shield representing a set of servers that will make requests to your origin servers rather than the CDN Pro edge servers. This can help further reduce traffic to your origin. Origin shield is allowed only when directConnection is set to noDirect. This is an advanced feature that can be enabled by contacting our support team. The origin shields API provides a list of available shields along with their IP addresses. It is best to select a shield whose region is closest to your origin servers. Use of a shield in China requires your property have 'hasBeian' set to true. If your origin servers have an access control list, add the IPs of the shield you choose to use.", "zh_CN": "指定某个源站盾（origin shield）的ID。使用源站盾功能后，所有回源请求都会通过源站盾中转回源，这可以帮助收敛回源流量。需要把directConnection设置为noDirect，才允许开启源站盾。源站盾是高级功能，如需使用请联系我们的技术支持开通。可通过调用‘获取源站盾列表’接口查询可用的源站盾及其对应的IP地址。您可根据源站的位置，选择合适的源站盾。如果您需使用中国大陆的源站盾，则该加速项目的所有域名必须已取得备案。如果您的源站开启了访问控制，请将所选择源站盾的IP地址加入白名单。"}
        self.shield = shield

    def validate(self):
        if self.authentication:
            self.authentication.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.servers is not None:
            result['servers'] = self.servers
        if self.supported_protocol is not None:
            result['supportedProtocol'] = self.supported_protocol
        if self.direct_connection is not None:
            result['directConnection'] = self.direct_connection
        if self.host_header is not None:
            result['hostHeader'] = self.host_header
        if self.verify_origin is not None:
            result['verifyOrigin'] = self.verify_origin
        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()
        if self.keep_alive_timeout is not None:
            result['keepAliveTimeout'] = self.keep_alive_timeout
        if self.peer_failure_timeout is not None:
            result['peerFailureTimeout'] = self.peer_failure_timeout
        if self.tls_certificate_id is not None:
            result['tlsCertificateId'] = self.tls_certificate_id
        if self.shield is not None:
            result['shield'] = self.shield
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('servers') is not None:
            self.servers = m.get('servers')
        if m.get('supportedProtocol') is not None:
            self.supported_protocol = m.get('supportedProtocol')
        if m.get('directConnection') is not None:
            self.direct_connection = m.get('directConnection')
        if m.get('hostHeader') is not None:
            self.host_header = m.get('hostHeader')
        if m.get('verifyOrigin') is not None:
            self.verify_origin = m.get('verifyOrigin')
        if m.get('authentication') is not None:
            temp_model = UpdateAPropertyVersionRequestOriginsAuthentication()
            self.authentication = temp_model.from_map(m['authentication'])
        if m.get('keepAliveTimeout') is not None:
            self.keep_alive_timeout = m.get('keepAliveTimeout')
        if m.get('peerFailureTimeout') is not None:
            self.peer_failure_timeout = m.get('peerFailureTimeout')
        if m.get('tlsCertificateId') is not None:
            self.tls_certificate_id = m.get('tlsCertificateId')
        if m.get('shield') is not None:
            self.shield = m.get('shield')
        return self


class UpdateAPropertyVersionRequestVideoSeek(TeaModel):
    def __init__(
        self,
        start_parameter: str = None,
        end_parameter: str = None,
    ):
        # {"en" : "Range: [ 1 .. 31 ] characters 
        # Name of the query parameter indicating the starting offset in bytes of the content to fetch. The parameter name should begin with a letter (a-z, A-Z) and may be followed by up to 30 letters and numbers.", "zh_CN": "取值范围: [ 1 .. 31 ] 字符 
        # 查询参数的名称，用来指定要获取的内容的起始位置（以字节计算）。参数名称应以字母（a-z，A-Z）开头，后面最多可以有30个字母和数字。"}
        self.start_parameter = start_parameter
        # {"en" : "Range: [ 0 .. 31 ] characters 
        # Name of the query parameter indicating the ending offset of the content to fetch. The parameter name should begin with a letter (a-z, A-Z) and may be followed by up to 30 letters and numbers.", "zh_CN": "取值范围: [ 0 .. 31 ] 字符 
        # 查询参数的名称，用来指定要获取的内容的结束位置（以字节计算）。参数名称应以字母（a-z，A-Z）开头，后面最多可以有30个字母和数字。"}
        self.end_parameter = end_parameter

    def validate(self):
        self.validate_required(self.start_parameter, 'start_parameter')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_parameter is not None:
            result['startParameter'] = self.start_parameter
        if self.end_parameter is not None:
            result['endParameter'] = self.end_parameter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startParameter') is not None:
            self.start_parameter = m.get('startParameter')
        if m.get('endParameter') is not None:
            self.end_parameter = m.get('endParameter')
        return self


class UpdateAPropertyVersionRequestAccessControlRulesConditions(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        hostname: str = None,
        uri: str = None,
        server_regions: List[str] = None,
        client_regions: List[str] = None,
        client_ip_range: List[str] = None,
    ):
        # {"en" : "Enum: https,http 
        # Indicates whether the incoming request uses HTTP or HTTPS.", "zh_CN": "取值范围: https,http 
        # 客户端请求的协议，HTTP或HTTPS。"}
        self.scheme = scheme
        # {"en" : "Indicates the hostname requested. It must be one of the hostnames defined in the property.", "zh_CN": "请求对应的加速域名。必须是加速项目中定义的加速域名之一。"}
        self.hostname = hostname
        # {"en" : "Range: <= 500 characters 
        # The URI begins with '/' and can end with '*' for prefix matching. ", "zh_CN": "取值范围: <= 500 字符 
        # 用于前缀匹配的URI，以'/'开头，可以以'*'结尾。"}
        self.uri = uri
        # {"en" : "An array of ISO-3166-1 alpha-2 codes indicating the countries of the servers, for example, 'US' to represent 'United States of America'.", "zh_CN": "服务器所在区域，以ISO-3166-1 两位国家代码表示。例如，'US'代表'美国'。"}
        self.server_regions = server_regions
        # {"en" : "An array of ISO-3166-1 alpha-2 codes indicating one or more countries which are the source of the client requests, for example, 'CN' to represent 'China'.", "zh_CN": "客户端请求来源区域，以ISO-3166-1 两位国家代码表示。例如，'CN'代表'中国'。"}
        self.client_regions = client_regions
        # {"en" : "Indicates the starting and ending IP addresses of the client requests to match against. They must be in IPv4 or IPv6 format.", "zh_CN": "用于指定要匹配的客户端请求的开始和结束IP地址。必须是IPv4或IPv6格式。"}
        self.client_ip_range = client_ip_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.uri is not None:
            result['uri'] = self.uri
        if self.server_regions is not None:
            result['serverRegions'] = self.server_regions
        if self.client_regions is not None:
            result['clientRegions'] = self.client_regions
        if self.client_ip_range is not None:
            result['clientIpRange'] = self.client_ip_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('serverRegions') is not None:
            self.server_regions = m.get('serverRegions')
        if m.get('clientRegions') is not None:
            self.client_regions = m.get('clientRegions')
        if m.get('clientIpRange') is not None:
            self.client_ip_range = m.get('clientIpRange')
        return self


class UpdateAPropertyVersionRequestAccessControlRulesAction(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        message: str = None,
    ):
        # {"en" : "Indicates the HTTP status code to respond with. It must be in the range 300-309, 400-409, or 500-509 to indicate a redirection or error.", "zh_CN": "响应的HTTP状态码，范围必须在300-309、400-409或500-509之间，分别表示重定向或错误。"}
        self.status_code = status_code
        # {"en" : "Range: <= 200 characters 
        # If the value of the status field is in the range 300-309, the message field's value will be placed in a Location HTTP header returned to the client. If the status is in the range 400-409 or 500-509, the value will be returned in the response body to the client.", "zh_CN": "取值范围: <= 200 字符 
        # 如果status字段的值在300-309范围内，message字段的值将在返回给客户端的Location响应头中。如果status字段的值在400-409或500-509范围内，则message字段的值将在返回给客户端的响应体中。"}
        self.message = message

    def validate(self):
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateAPropertyVersionRequestAccessControlRules(TeaModel):
    def __init__(
        self,
        id: str = None,
        conditions: UpdateAPropertyVersionRequestAccessControlRulesConditions = None,
        action: UpdateAPropertyVersionRequestAccessControlRulesAction = None,
    ):
        # {"en" : "Range: [ 0 .. 60 ] characters 
        # An optional ID for the access control rule.", "zh_CN": "取值范围: [ 0 .. 60 ] 字符 
        # 访问控制规则ID。"}
        self.id = id
        # {"en" : "Specify the conditions that the incoming request must match. At least one condition must be specified. If multiple are specified, all must match.", "zh_CN": "指定客户端请求必须匹配的条件。必须至少指定一个条件。如果指定了多个条件，则必须全部匹配。"}
        self.conditions = conditions
        # {"en" : "Indicates the action to take in response to a request that matches the conditions of the access control rule.", "zh_CN": "对于匹配到以上条件的请求所采取的相应操作。"}
        self.action = action

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.conditions is not None:
            result['conditions'] = self.conditions.to_map()
        if self.action is not None:
            result['action'] = self.action.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('conditions') is not None:
            temp_model = UpdateAPropertyVersionRequestAccessControlRulesConditions()
            self.conditions = temp_model.from_map(m['conditions'])
        if m.get('action') is not None:
            temp_model = UpdateAPropertyVersionRequestAccessControlRulesAction()
            self.action = temp_model.from_map(m['action'])
        return self


class UpdateAPropertyVersionRequestExtraServicePorts(TeaModel):
    def __init__(
        self,
        http: List[str] = None,
        https: List[str] = None,
    ):
        # {"en" : "This is a list of ports other than 80 which are used to handle HTTP requests. The available values can be found in the systemConfigs API's response. If you need another port, please contact our support team.", "zh_CN": "指定用于处理HTTP请求的端口列表（80端口除外）。可通过调用'获取系统配置'接口来查询系统支持的端口。如果您需要开通其他端口，请联系技术支持。"}
        self.http = http
        # {"en" : "This is a list of ports other than 443 which are used to handle HTTPS requests. The available values can be found in the systemConfigs API's response. If you need another port, please contact our support team.", "zh_CN": "指定用于处理HTTPS请求的端口列表（443端口除外）。可通过调用'获取系统配置'接口来查询系统支持的端口。如果您需要开通其他端口，请联系技术支持。"}
        self.https = https

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http is not None:
            result['http'] = self.http
        if self.https is not None:
            result['https'] = self.https
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http') is not None:
            self.http = m.get('http')
        if m.get('https') is not None:
            self.https = m.get('https')
        return self


class UpdateAPropertyVersionRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        cache_key_hostname: str = None,
        hostnames: List[str] = None,
        real_time_log: UpdateAPropertyVersionRequestRealTimeLog = None,
        edge_logic: str = None,
        has_beian: bool = None,
        redirect_http_to_https: str = None,
        origins: List[UpdateAPropertyVersionRequestOrigins] = None,
        syntax_version: int = None,
        disable_http_2: bool = None,
        enable_http_3: bool = None,
        scheme_in_cache_key: bool = None,
        tls_max_version: str = None,
        load_balancer_hash_key: str = None,
        tls_certificate_id: str = None,
        tls_min_version: str = None,
        tls_ciphers: str = None,
        allow_protocol_downgrade: bool = None,
        tls_certificate_id_1: str = None,
        video_seek: UpdateAPropertyVersionRequestVideoSeek = None,
        tls_session_timeout: int = None,
        enable_ocsp_stapling: bool = None,
        beian_content_type: int = None,
        enable_ipv_6origin: bool = None,
        follow_client_ip_version: str = None,
        access_control_rules: List[UpdateAPropertyVersionRequestAccessControlRules] = None,
        disable_cert_automation: bool = None,
        cache_key_uri: str = None,
        extra_service_ports: UpdateAPropertyVersionRequestExtraServicePorts = None,
        load_balancer_logic: str = None,
        tls_0rtt: bool = None,
    ):
        # {"en" : "A description of the version.
        # ", "zh_CN": "版本描述。"}
        self.description = description
        # {"en" : "Range: <= 80 characters ^[a-z.-_]+\
        # The cachekey hostname must be a string made of lowercase letters, digits, dot, dash, and underscore. If not specified, the incoming Host header value will be used and the cache will not be shared across different hostnames in this property.
        # ", "zh_CN": "取值范围: <= 80 字符 ^[a-z.-_]+\
        # 用于缓存键（Cache Key）的主机名必须是由小写字母、数字、点、连字符和下划线组成的字符串。如果未指定，默认将使用传入的Host请求头值，并且此加速项目中的不同加速域名之间不共享缓存。"}
        self.cache_key_hostname = cache_key_hostname
        # {"en" : "Hostnames associated with the property. A valid value is a fully qualified hostname such as www.domain.com or a wildcard hostname such as *.domain.com. Any given hostname can only be in one deployed property at a particular time. However, a wildcard hostname is permitted to overlap other hostnames you own.", "zh_CN": "与加速项目关联的加速域名。必须是FQDN完全限定域名（如 www.domain.com），或泛域名（如*.domain.com）。
        # 同一个加速域名在同一时间只能存在于一个已部署的加速项目中，但泛域名可以与关联的完全限定域名一同部署。"}
        self.hostnames = hostnames
        # {"en" : "This optional field allows you to configure notifications about client requests to be sent to a remote server. It can be used only if you have access to our realtime_log_switch directive. Please contact our support team if you require this feature.", "zh_CN": "此可选字段用来配置发送消息通知（即实时日志）到您的远程服务器。当有客户端请求访问您的加速域名时，将触发通知。这是高级功能，如果您需要此功能，请联系我们的技术支持开通。"}
        self.real_time_log = real_time_log
        # {"en" : "Range: <= 65530 characters 
        # Refer to Edge Logic Introduction.", "zh_CN": "取值范围: <= 65530 字符 
        # 自定义边缘逻辑。参考边缘逻辑介绍。"}
        self.edge_logic = edge_logic
        # {"en" : "Default: False 
        # The value indicates whether all the hostnames in this property have Beian license on file with the Chinese government. This is required to serve this property from servers in mainland China. A value of false means servers outside of mainland China will be used to distribute content to visitors in China. If set to true you must also specify the content type in the beianContentType field.", "zh_CN": "默认值: False 
        # 此加速项目中的所有加速域名是否都已获得中国政府的ICP备案。只有获取备案的域名才能使用中国大陆节点来提供服务。如果设置为true，还必须在beianContentType字段中指定内容类型。"}
        self.has_beian = has_beian
        # {"en" : "Default: False 
        # This field can be set to either a boolean value or a string. If the value is set to true, the server will redirect all HTTP requests to HTTPS using status code 301. You can also specify string values '302', '307', or '308' instead if you wish to return a different status code when a request is redirected.", "zh_CN": "默认值: False 
        # 此字段可以设置为布尔值或字符串。如果设置为true，则CDN Pro服务器会将所有HTTP请求重定向到HTTPS，并返回301状态码。如果您希望在重定向请求时返回不同的状态码，可在此处指定需要的状态码，如'302'、'307'或'308'。"}
        self.redirect_http_to_https = redirect_http_to_https
        # {"en" : "Describes the origin servers for the property's content.", "zh_CN": "描述加速项目对应的源站。"}
        self.origins = origins
        # {"en" : "Default: 1 
        # The value must be set to 1 at this time.", "zh_CN": "默认值: 1 
        # 当前仅允许值为1。"}
        self.syntax_version = syntax_version
        # {"en" : "Default: False 
        # Set to true to disable support for HTTP/2 and support only HTTP 1.1.", "zh_CN": "默认值: False 
        # 当值为true时，禁用对HTTP/2的支持，仅支持HTTP/1.1。"}
        self.disable_http_2 = disable_http_2
        # {"en" : "Default: False 
        # Set to true to enable support for HTTP/3. HTTP/3 requires TLS to work, so this field will be ignored unless you specify a certificate in the tlsCertificateId field.", "zh_CN": "默认值: False 
        # 是否开启HTTP/3，HTTP/3 需要 需要配置TLS 才生效，若您未在 tlsCertificateId 中指定证书，此字段将被忽略。"}
        self.enable_http_3 = enable_http_3
        # {"en" : "Default: False 
        # Specifies whether the scheme ('http' or 'https') should be included in the cache key. Default behavior is false. Set to true if the content is known to be different for different schemes.
        # ", "zh_CN": "默认值: False 
        # 指定缓存键（Cache Key）是否区分协议（'http'或'https'）。默认为false。如果不同协议响应的内容不同，则设置为true。"}
        self.scheme_in_cache_key = scheme_in_cache_key
        # {"en" : "Enum: 1.1,1.2,1.3 
        # Default: 1.3 
        # Maximum supported TLS version.", "zh_CN": "取值范围: 1.1,1.2,1.3 
        # 默认值: 1.3 
        # 支持的TLS最高版本。"}
        self.tls_max_version = tls_max_version
        # {"en" : "Range: <= 100 characters 
        # Multiple tiers of load balancing are used in our CDN pops to distribute the client requests to different servers. We are using consistent hashing in many of those places. By default, the URL is used as the hash key, which should be good enough in most cases. Here you can define additional variables to be added to the hash key to distribute the requests more evenly. One typical use case is when all requests carry the same URL, but use a particular header to indicate the resources. 
        # 
        # This is an optional field. The default value is an empty string. A valid value is a string meeting the following criteria:
        # 
        # Consists of alphanumeric characters, underscore _, equal sign =, dollar sign $, and ampersand sign &.
        # The variable names can only be in one of the following formats: $http_name, $cookie_name, or $arg_name.
        # At least one variable must be specified. No more than three are permitted.
        # The total length should be no more than 100 characters.
        # 
        # The validator will treat any dollar sign and the string after it (before any = or & or $) as a variable. 
        # 
        # Here are some examples of valid values:
        # <table><tr><td>$http_abc</td></tr><tr><td>abc=$http_abc&def=$http_def&c_123=$cookie_123</td></tr><tr><td>abc=$http_abc=$http_def</td></tr><tr><td>$http_abc&$http_def</td></tr><tr><td>=$http_abd&</td></tr><tr><td>&&abc==$http_abc&&&===qwer</td></tr></table>
        # ", "zh_CN": "取值范围: <= 100 字符 
        # 我们的CDN使用了多层负载均衡架构，将客户端请求分发到不同的服务器。我们在架构中多处使用到一致性哈希。默认情况下，URL被用作哈希键，这对于大多数情况都适用。您可以在这里定义要添加到哈希键的其他变量，以更均匀地分配请求。一个典型的使用场景是，所有请求都携带相同的URL，但使用特定的请求头来区分资源。
        # 
        # 这是一个可选字段，默认值为空字符串。必须满足以下条件：
        # 
        # 由字母、数字、下划线_、等号=、美元符号$和符号&组成。
        # 变量名只能采用以下格式之一：$http_name、$cookie_name、$arg_name。
        # 必须至少指定一个变量，不允许超过三个。
        # 总长度不得超过100个字符。
        # 
        # 我们的配置验证器将把任何美元符号及其后的字符串（在任何=或&或$之前）视为变量。
        # 
        # 以下是一些有效值的示例：
        # <table><tr><td>$http_abc</td></tr><tr><td>abc=$http_abc&def=$http_def&c_123=$cookie_123</td></tr><tr><td>abc=$http_abc=$http_def</td></tr><tr><td>$http_abc&$http_def</td></tr><tr><td>=$http_abd&</td></tr><tr><td>&&abc==$http_abc&&&===qwer</td></tr></table>"}
        self.load_balancer_hash_key = load_balancer_hash_key
        # {"en" : "Refers to a certificate. It is invalid to only set the tlsCertificateId1 field without setting the tlsCertificateId field. If tlsCertificateId is not set, HTTPS will not be enabled for this property. This is a feature to enable you to specify two certificates of different types, i.e. one RSA, one EC. If two certificates of the same type are specified, the one specified by tlsCertificateId will be ignored. ", "zh_CN": "该加速项目用到的证书ID。仅设置tlsCertificateId1字段而不设置tlsCertificateId字段是无效的。如果未设置tlsCertificateId，则不会为此加速项目启用HTTPS。此功能允许您指定两个不同类型的证书，即一个RSA，一个EC。如果指定了两个相同类型的证书，则将忽略tlsCertificateId指定的证书。 "}
        self.tls_certificate_id = tls_certificate_id
        # {"en" : "Enum: 1.1,1.2,1.3,1 
        # Default: 1 
        # Minimum required TLS version.", "zh_CN": "取值范围: 1.1,1.2,1.3,1 
        # 默认值: 1 
        # 所需的TLS最低版本。"}
        self.tls_min_version = tls_min_version
        # {"en" : "Range: <= 2040 characters 
        # Any cipher list supported by 'openssl ciphers'. See https://www.openssl.org/docs/manmaster/man1/ciphers.html
        # ", "zh_CN": "取值范围: <= 2040 字符 
        # 'openssl ciphers'支持的任何加密算法套件。参考：https://www.openssl.org/docs/manmaster/man1/ciphers.html"}
        self.tls_ciphers = tls_ciphers
        # {"en" : "Default: False 
        # This setting applies only if the property has an attached certificate allowing client requests to use HTTPS. If the value of allowProtocolDowngrade is false, we require all the origin servers to support HTTPS. If the value is true, we allow origins that support only HTTP, which reduces security.
        # ", "zh_CN": "默认值: False 
        # 是否允许协议降级。仅当加速项目中存在允许客户端使用HTTPS请求的证书时，此设置才适用。如果allowProtocolDowngrade的值为false，则要求所有源服务器支持HTTPS。如果值为true，则允许仅支持HTTP的源，但这会降低安全性。"}
        self.allow_protocol_downgrade = allow_protocol_downgrade
        # {"en" : "Refers to a certificate. It is invalid to only set the tlsCertificateId1 field without setting the tlsCertificateId field. If tlsCertificateId is not set, HTTPS will not be enabled for this property. This is a feature to enable you to specify two certificates of different types, i.e. one RSA, one EC. If two certificates of the same type are specified, the one specified by tlsCertificateId will be ignored. 
        # ", "zh_CN": "指该加速项目用到的证书ID。仅设置tlsCertificateId1字段而不设置tlsCertificateId字段是无效的。如果未设置tlsCertificateId，则不会为此加速项目启用HTTPS。此功能允许您指定两个不同类型的证书，即一个RSA，一个EC。如果指定了两个相同类型的证书，则将忽略tlsCertificateId指定的证书。"}
        self.tls_certificate_id_1 = tls_certificate_id_1
        # {"en" : "This object allows you to support video players requesting partial content through query string parameters. If you specify videoSeek, you must enter a value for startParameter.", "zh_CN": "此对象用来支持视频播放器通过指定查询参数来请求部分内容。当videoSeek对象存在时，必须为startParameter设置一个值。"}
        self.video_seek = video_seek
        # {"en" : "Default: 1800 Range: [ 300 .. 86400 ] 
        # Lifespan of TLS session ticket in seconds.", "zh_CN": "默认值: 1800 取值范围: [ 300 .. 86400 ] 
        # TLS会话ticket的有效期（秒）。"}
        self.tls_session_timeout = tls_session_timeout
        # {"en" : "Default: False 
        # Enables Online Certificate Status Protocol (OCSP) stapling to check the revocation status of digital certificates. (Refer to https://en.wikipedia.org/wiki/OCSP_stapling)", "zh_CN": "默认值: False 
        # 是否启用在线证书状态协议（OCSP）装订以检查数字证书的吊销状态。参考：https://en.wikipedia.org/wiki/OCSP_stapling"}
        self.enable_ocsp_stapling = enable_ocsp_stapling
        # {"en" : "Range: [ 1 .. 24 ] 
        # If you are planning to distribute content through servers in mainland China, you will need to set the hasBeian field to true and also indicate the type of content you are distributing. Enter the value that best corresponds to your content:
        # 
        # <table><tr><th>Value</th><th>Content Type</th></tr><tr><td>1</td><td>Instant Messaging</td></tr><tr><td>2</td><td>Search Engine</td></tr><tr><td>3</td><td>Web Portal</td></tr><tr><td>4</td><td>Online Postal Service</td></tr><tr><td>5</td><td>Online News</td></tr><tr><td>6</td><td>Blog</td></tr><tr><td>7</td><td>Advertisement</td></tr><tr><td>8</td><td>Organization Web Portal</td></tr><tr><td>9</td><td>Shopping</td></tr><tr><td>10</td><td>Online Payment</td></tr><tr><td>11</td><td>Online Bank</td></tr><tr><td>12</td><td>Online Stock Market</td></tr><tr><td>13</td><td>Online Gaming</td></tr><tr><td>14</td><td>Online Music</td></tr><tr><td>15</td><td>Online Movie</td></tr><tr><td>16</td><td>Online Picture</td></tr><tr><td>17</td><td>Software Download</td></tr><tr><td>18</td><td>Job Hunting</td></tr><tr><td>19</td><td>Online Dating</td></tr><tr><td>20</td><td>Online Real Property</td></tr><tr><td>21</td><td>Online Education</td></tr><tr><td>22</td><td>Web Design</td></tr><tr><td>23</td><td>WAP</td></tr><tr><td>24</td><td>Others</td></tr></table>", "zh_CN": "取值范围: [ 1 .. 24 ] 
        # 如果您的域名已获得备案，希望通过中国大陆的服务器分发内容，则需要将hasBeian字段设置为true，并说明您分发的内容类型。请选择与您的内容最匹配的值：
        # 
        # <table><tr><th>值</th><th>内容类型</th></tr><tr><td>1</td><td>即时通信</td></tr><tr><td>2</td><td>搜索引擎</td></tr><tr><td>3</td><td>综合门户</td></tr><tr><td>4</td><td>网上邮局</td></tr><tr><td>5</td><td>网络新闻</td></tr><tr><td>6</td><td>博客/个人空间</td></tr><tr><td>7</td><td>网络广告</td></tr><tr><td>8</td><td>单位门户网站</td></tr><tr><td>9</td><td>网络购物</td></tr><tr><td>10</td><td>网上支付</td></tr><tr><td>11</td><td>网上银行</td></tr><tr><td>12</td><td>网上炒股</td></tr><tr><td>13</td><td>网络游戏</td></tr><tr><td>14</td><td>网络音乐</td></tr><tr><td>15</td><td>网络影视</td></tr><tr><td>16</td><td>网络图片</td></tr><tr><td>17</td><td>软件下载</td></tr><tr><td>18</td><td>网上求职</td></tr><tr><td>19</td><td>在线交友</td></tr><tr><td>20</td><td>网上房产</td></tr><tr><td>21</td><td>网络教育</td></tr><tr><td>22</td><td>网站建设</td></tr><tr><td>23</td><td>WAP</td></tr><tr><td>24</td><td>其他</td></tr></table>"}
        self.beian_content_type = beian_content_type
        # {"en" : "Default: False 
        # Is it allowed to use IPv6 addresses as the source server for this project.", "zh_CN": "默认值: False 
        # 是否允许使用 IPv6 地址作为该项目的源站服务器"}
        self.enable_ipv_6origin = enable_ipv_6origin
        # {"en" : "Default value: off Optional values: auto, strict, off
        # When enableIpv6Origin is allowed, this setting will control whether to follow the client IP protocol version back to the source.
        # Auto: Refers to selecting the IP address for returning to the source based on the IP protocol version requested by the client. When the source server is unavailable, it automatically switches to another IP protocol address for returning to the source
        # Strict: Strictly select the IP address for returning to the source based on the IP protocol version requested by the client. When the source server is unavailable, it is not allowed to switch to another protocol address for returning to the source
        # Off: Ignore the IP protocol version requested by the client and randomly select an available IPv4 or IPv6 address to return to the source.", "zh_CN": "默认值：off 可选值：auto、strict、off 当enableIpv6Origin为允许时，该设置将控制是否跟随客户端IP协议版本回源。
        # auto：表示根据客户端请求的IP协议版本来选择回源IP地址，当源站服务器不可用时自动切换成其他IP协议地址回源
        # strict：严格根据客户端请求的IP协议版本来选择回源IP地址，当源站服务器不可用时不允许切换成其他协议地址回源
        # off：忽略客户端请求的IP协议版本，随机选择可用的IPv4或IPv6地址回源"}
        self.follow_client_ip_version = follow_client_ip_version
        # {"en" : "Specify one or more access control rules to restrict access to your content. More advanced configuration can be done using Edge Logic. These access control rules take precedence over Edge Logic if both are defined.", "zh_CN": "指定一个或多个访问控制规则以限制对内容的访问。可以使用边缘逻辑进行更高级的配置。此处定义的访问控制规则，优先级高于边缘逻辑。"}
        self.access_control_rules = access_control_rules
        # {"en" : "Default: False 
        # By default, CDN Pro takes control of the contents under the /.well-known/{acme-challenge, pki-validation} directories to support certificate auto-renew for properties. If for any reason you need to manage these two directories by yourself on the origin, for example, to implement your own certificate auto-renew mechanism, you can use this configuration option to disable the default behavior by setting its value to true. For more information about our support for certificate auto-renewal, refer to the description of the autoRenew field in the Create a certificate API.", "zh_CN": "默认值: False 
        # 默认情况下，CDN Pro控制/.well-known/{acme-challenge, pki-validation}目录下的内容，以支持加速项目的证书自动更新功能。如果您需要自己在源站管理这两个目录，例如，为了实现您自己的证书自动更新机制，您可以将此字段设置为true来禁用默认行为。关于证书自动更新的更多信息，请参考'创建证书'接口中autoRenew字段的说明。"}
        self.disable_cert_automation = disable_cert_automation
        # {"en" : "Enum: preRewrite,postRewrite 
        # Default: preRewrite 
        # This setting controls how the URI of the incoming request is incorporated into the cache key if you use a 'rewrite' directive in the property's Edge Logic. The default value, 'preRewrite', puts the unmodified URI into the cache key while 'postRewrite' uses the modified URI. If your rewrite directive converts multiple different URIs into the same value, using 'postRewrite' may result in a higher cache hit ratio.", "zh_CN": "取值范围: preRewrite,postRewrite 
        # 默认值: preRewrite 
        # 如果在加速项目的边缘逻辑中使用了'rewrite'指令，可使用该字段来控制客户端请求的URI如何合并到缓存键（Cache Key）中 。默认值'preRewrite'指将改写前的URI放入缓存键，而'postRewrite'则使用改写后的URI。如果您的'rewrite'指令将多个不同的URI改写为相同的值，则使用'postRewrite'可以提高缓存命中率。"}
        self.cache_key_uri = cache_key_uri
        # {"en" : "This field lists ports other than the default 80 used to handle HTTP requests and ports other than the default 443 used to handle HTTPS requests. ", "zh_CN": "除标准的80，443端口外，我们还支持一些扩展端口。可用该字段指定用于处理HTTP和HTTPS请求的扩展端口。"}
        self.extra_service_ports = extra_service_ports
        # {"en" : "Range: <= 65530 characters 
        # This field allows you to enter Edge Logic to customize load balancing. A subset of the  directives can be used. Refer to the basic directives listed in the baseLbDirectives field of the response to the system configuration API. Currently, these include 'if', 'else', 'elseif', 'set', 'return', 'add_header', 'deny', 'allow', 'access_log_sampling', and 'proxy_set_header.' In addition, some advanced Edge Logic directives, identified by the system configuration API's advancedLbDirectives, can be enabled for your account if needed. Please contact our support team if you require any of them. <br/> Example use: <br />
        # if ($http_user_agent = bot) { return 403;}
        # ", "zh_CN": "取值范围: <= 65530 字符 
        # 此字段可用来自定义边缘逻辑，控制负载均衡器的行为。支持使用 边缘逻辑指令中的部分指令。请参考'获取系统配置'接口中baseLbDirectives字段所列出的负载均衡基础指令。目前，这些基础指令包括'if'、'else'、'elseif'、'set'、'return'、'add_header'、'deny'、'allow'、'access_log_sampling'和'proxy_set_headers'。此外，我们还支持一些高级指令，请参考'获取系统配置'接口中advancedLbDirectives字段所列出的负载均衡高级指令。如果您需要使用这些高级指令，请联系技术支持。
        # 
        # <br/>示例：<br/>
        # 
        # if ($http_user_agent = bot) { return 403;}
        # "}
        self.load_balancer_logic = load_balancer_logic
        # {"en" : "Default: False 
        # Enable TLS zero round-trip time, a feature of TLS 1.3 that can improve performance for repeat visits to a site. If enabling it though, be sure your site is not vulnerable to the HTTP replay attack.", "zh_CN": "默认值: False 
        # 是否开启TLS 0-RTT功能。这是TLS 1.3版本支持的功能。启用该功能后，当用户频繁访问您的站点时，可提高访问响应速度。需要注意的是，启用该功能可能会加大站点遭受HTTP replay攻击的风险。"}
        self.tls_0rtt = tls_0rtt

    def validate(self):
        if self.real_time_log:
            self.real_time_log.validate()
        if self.origins:
            for k in self.origins:
                if k:
                    k.validate()
        if self.video_seek:
            self.video_seek.validate()
        if self.access_control_rules:
            for k in self.access_control_rules:
                if k:
                    k.validate()
        if self.extra_service_ports:
            self.extra_service_ports.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.cache_key_hostname is not None:
            result['cacheKeyHostname'] = self.cache_key_hostname
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.real_time_log is not None:
            result['realTimeLog'] = self.real_time_log.to_map()
        if self.edge_logic is not None:
            result['edgeLogic'] = self.edge_logic
        if self.has_beian is not None:
            result['hasBeian'] = self.has_beian
        if self.redirect_http_to_https is not None:
            result['redirectHttpToHttps'] = self.redirect_http_to_https
        if self.origins is not None:
            result['origins'] = []
            for k in self.origins:
                result['origins'].append(k.to_map() if k else None)
        if self.syntax_version is not None:
            result['syntaxVersion'] = self.syntax_version
        if self.disable_http_2 is not None:
            result['disableHttp2'] = self.disable_http_2
        if self.enable_http_3 is not None:
            result['enableHttp3'] = self.enable_http_3
        if self.scheme_in_cache_key is not None:
            result['schemeInCacheKey'] = self.scheme_in_cache_key
        if self.tls_max_version is not None:
            result['tlsMaxVersion'] = self.tls_max_version
        if self.load_balancer_hash_key is not None:
            result['loadBalancerHashKey'] = self.load_balancer_hash_key
        if self.tls_certificate_id is not None:
            result['tlsCertificateId'] = self.tls_certificate_id
        if self.tls_min_version is not None:
            result['tlsMinVersion'] = self.tls_min_version
        if self.tls_ciphers is not None:
            result['tlsCiphers'] = self.tls_ciphers
        if self.allow_protocol_downgrade is not None:
            result['allowProtocolDowngrade'] = self.allow_protocol_downgrade
        if self.tls_certificate_id_1 is not None:
            result['tlsCertificateId1'] = self.tls_certificate_id_1
        if self.video_seek is not None:
            result['videoSeek'] = self.video_seek.to_map()
        if self.tls_session_timeout is not None:
            result['tlsSessionTimeout'] = self.tls_session_timeout
        if self.enable_ocsp_stapling is not None:
            result['enableOcspStapling'] = self.enable_ocsp_stapling
        if self.beian_content_type is not None:
            result['beianContentType'] = self.beian_content_type
        if self.enable_ipv_6origin is not None:
            result['enableIpv6Origin'] = self.enable_ipv_6origin
        if self.follow_client_ip_version is not None:
            result['followClientIpVersion'] = self.follow_client_ip_version
        if self.access_control_rules is not None:
            result['accessControlRules'] = []
            for k in self.access_control_rules:
                result['accessControlRules'].append(k.to_map() if k else None)
        if self.disable_cert_automation is not None:
            result['disableCertAutomation'] = self.disable_cert_automation
        if self.cache_key_uri is not None:
            result['cacheKeyUri'] = self.cache_key_uri
        if self.extra_service_ports is not None:
            result['extraServicePorts'] = self.extra_service_ports.to_map()
        if self.load_balancer_logic is not None:
            result['loadBalancerLogic'] = self.load_balancer_logic
        if self.tls_0rtt is not None:
            result['tls0Rtt'] = self.tls_0rtt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('cacheKeyHostname') is not None:
            self.cache_key_hostname = m.get('cacheKeyHostname')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('realTimeLog') is not None:
            temp_model = UpdateAPropertyVersionRequestRealTimeLog()
            self.real_time_log = temp_model.from_map(m['realTimeLog'])
        if m.get('edgeLogic') is not None:
            self.edge_logic = m.get('edgeLogic')
        if m.get('hasBeian') is not None:
            self.has_beian = m.get('hasBeian')
        if m.get('redirectHttpToHttps') is not None:
            self.redirect_http_to_https = m.get('redirectHttpToHttps')
        if m.get('origins') is not None:
            self.origins = []
            for k in m.get('origins'):
                temp_model = UpdateAPropertyVersionRequestOrigins()
                self.origins.append(temp_model.from_map(k))
        if m.get('syntaxVersion') is not None:
            self.syntax_version = m.get('syntaxVersion')
        if m.get('disableHttp2') is not None:
            self.disable_http_2 = m.get('disableHttp2')
        if m.get('enableHttp3') is not None:
            self.enable_http_3 = m.get('enableHttp3')
        if m.get('schemeInCacheKey') is not None:
            self.scheme_in_cache_key = m.get('schemeInCacheKey')
        if m.get('tlsMaxVersion') is not None:
            self.tls_max_version = m.get('tlsMaxVersion')
        if m.get('loadBalancerHashKey') is not None:
            self.load_balancer_hash_key = m.get('loadBalancerHashKey')
        if m.get('tlsCertificateId') is not None:
            self.tls_certificate_id = m.get('tlsCertificateId')
        if m.get('tlsMinVersion') is not None:
            self.tls_min_version = m.get('tlsMinVersion')
        if m.get('tlsCiphers') is not None:
            self.tls_ciphers = m.get('tlsCiphers')
        if m.get('allowProtocolDowngrade') is not None:
            self.allow_protocol_downgrade = m.get('allowProtocolDowngrade')
        if m.get('tlsCertificateId1') is not None:
            self.tls_certificate_id_1 = m.get('tlsCertificateId1')
        if m.get('videoSeek') is not None:
            temp_model = UpdateAPropertyVersionRequestVideoSeek()
            self.video_seek = temp_model.from_map(m['videoSeek'])
        if m.get('tlsSessionTimeout') is not None:
            self.tls_session_timeout = m.get('tlsSessionTimeout')
        if m.get('enableOcspStapling') is not None:
            self.enable_ocsp_stapling = m.get('enableOcspStapling')
        if m.get('beianContentType') is not None:
            self.beian_content_type = m.get('beianContentType')
        if m.get('enableIpv6Origin') is not None:
            self.enable_ipv_6origin = m.get('enableIpv6Origin')
        if m.get('followClientIpVersion') is not None:
            self.follow_client_ip_version = m.get('followClientIpVersion')
        if m.get('accessControlRules') is not None:
            self.access_control_rules = []
            for k in m.get('accessControlRules'):
                temp_model = UpdateAPropertyVersionRequestAccessControlRules()
                self.access_control_rules.append(temp_model.from_map(k))
        if m.get('disableCertAutomation') is not None:
            self.disable_cert_automation = m.get('disableCertAutomation')
        if m.get('cacheKeyUri') is not None:
            self.cache_key_uri = m.get('cacheKeyUri')
        if m.get('extraServicePorts') is not None:
            temp_model = UpdateAPropertyVersionRequestExtraServicePorts()
            self.extra_service_ports = temp_model.from_map(m['extraServicePorts'])
        if m.get('loadBalancerLogic') is not None:
            self.load_balancer_logic = m.get('loadBalancerLogic')
        if m.get('tls0Rtt') is not None:
            self.tls_0rtt = m.get('tls0Rtt')
        return self


class UpdateAPropertyVersionResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAPropertyVersionResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateAPropertyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPropertyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPropertyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPropertyRequestVersionRealTimeLogHeaders(TeaModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # {"en" : "Name of an HTTP header.", "zh_CN": "HTTP标头名称"}
        self.name = name
        # {"en" : "Value of an HTTP header.", "zh_CN": "HTTP标头值"}
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CreateAPropertyRequestVersionRealTimeLog(TeaModel):
    def __init__(
        self,
        log_url: str = None,
        sample_rate: int = None,
        escape: str = None,
        format: str = None,
        headers: List[CreateAPropertyRequestVersionRealTimeLogHeaders] = None,
    ):
        # {"en" : "The URL that receives the notifications. It must begin with 'http' or 'https'. The server should support the POST method. This is a required field.", "zh_CN": "接收通知的服务器URL地址。必须以'http'或'https'开头。服务器须支持POST方法。这是必填字段。"}
        self.log_url = log_url
        # {"en" : "Default: 1 Range: [ 1 .. 65536 ] 
        # An integer between [1, 65536]. n means one notification for every n edge requests. 1 means every edge request will generate a notification. This is optional. Default is 1.", "zh_CN": "默认值: 1 取值范围: [ 1 .. 65536 ] 
        # 采样率。介于[1, 65536]之间的整数。n表示每n个边缘请求发送1条通知。1表示每个边缘请求都会发送。这是可选字段。默认值为1。"}
        self.sample_rate = sample_rate
        # {"en" : "Enum: json,none 
        # Specify json to enable JSON character escaping in variables or none to disable escaping.", "zh_CN": "取值范围: json,none 
        # 指定json以开启变量中的json字符转义。如果要禁用转义则指定none。"}
        self.escape = escape
        # {"en" : "This is a required field to specify the notification body to be sent to the remote server. It can be any printable text that can be sent in the body of an HTTP POST request. 
        # 
        # The following built-in variables can be used within the format field. They will be replaced with the actual values in the notifications.
        # <table><tr><th>Name</th><th>Description</th></tr><tr><td>$body_bytes_sent</td><td>Size of the response body.</td></tr><tr><td>$bytes_sent</td><td>Size of the response, including body, headers and response line.</td></tr><tr><td>$client_country_code</td><td>An ISO 3166-1 country code representing the country of the client request, for example, 'US'. 'ZZ' is returned if the country is unknown.</td></tr><tr><td>$client_real_ip</td><td>IP address of the client request.</td></tr><tr><td>$cookie_x</td><td>This lets you obtain any cookie named x.  For example, $cookie_account would retrieve the value of a cookie named 'account'.</td></tr><tr><td>$http_x</td><td>Obtain any HTTP header named x from the original request. The header name is converted to lower case with dashes replaced by underscores. For example, specify $http_user_agent to get the value of User-Agent.</td></tr><tr><td>$msec</td><td>Current unix time in seconds with millisecond precision.</td></tr><tr><td>$qtl_req_id</td><td>Unique identifier representing the request.</td></tr><tr><td>$request_uri</td><td>HTTP request URI</td></tr><tr><td>$request_method</td><td>The HTTP request method used to access the origin.</td></tr><tr><td>$request_time</td><td>Response time in milliseconds. It is the time between receiving the request's  first byte and serving the last byte of the response.</td></tr><tr><td>$sc_completed</td><td>1 to indicate the last byte of the object was served to the user, 0 otherwise.</td></tr><tr><td>$sc_initial</td><td>1 to indicate the first byte of the object was served to the user, 0 otherwise.</td></tr><tr><td>$scheme</td><td>Indicates the protocol of the user's request ('http' or https').</td></tr><tr><td>$sent_http_content_length</td><td>the original file size.</td></tr><tr><td>$sent_http_x</td><td>Obtain the value of an HTTP header named x that is returned in the response to the client. The header name should be converted to lower case with dashes replaced by underscores. For example, $sent_http_etag would give you the value of the ETag header.</td></tr><tr><td>$server_addr</td><td>IP address of the edge node serving the user's request.</td></tr><tr><td>$server_protocol</td><td>Indicates the version of HTTP used in the user's request, either 'HTTP/1.0', 'HTTP/1.1', or 'HTTP/2.0'.</td></tr><tr><td>$ssl_cipher</td><td>Indicates the cipher suite used for the TLS (SSL) connection.</td></tr><tr><td>$ssl_server_name</td><td>The hostname that a client initiating a TLS (SSL) connection is attempting to connect to. It is only sent by clients supporting SNI (Server Name Indication).</td></tr><tr><td>$ssl_protocol</td><td>Indicates the TLS version used for the TLS (SSL) connection. Example versions include 'SSLv3', 'TLSv1', 'TLSv1.1', 'TLSv1.2', and 'unknown'.</td></tr><tr><td>$status</td><td>An HTTP response code for the user's request.</td></tr><tr><td>$tcpinfo_rtt</td><td>The time in microseconds taken by a packet to travel to the destination and back.</td></tr></table>", "zh_CN": "该字段用来定义要发送到远程服务器的通知的格式。通知正文可以包括任何能在HTTP POST请求体中发送的可打印文本。这是必填字段。
        # 
        # 可以使用以下内置变量定义通知的格式。发送通知时，它们将被替换为实际值。
        # <table><tr><th>变量名称</th><th>描述</th></tr><tr><td>$body_bytes_sent</td><td>响应体大小。</td></tr><tr><td>$bytes_sent</td><td>响应的大小，包括响应体、响应头和响应行。</td></tr><tr><td>$client_country_code</td><td>客户端请求来源国家，以ISO 3166-1国家代码表示。例如'US'。如果国家/地区未知，则返回'ZZ'。</td></tr><tr><td>$client_real_ip</td><td>客户端请求的IP地址。</td></tr><tr><td>$cookie_x</td><td>获取某个cookie。例如，指定$cookie_account可获取名为'account'的cookie值。</td></tr><tr><td>$http_x</td><td>从原始请求中获取某个HTTP请求头。请求头名称需转换为小写，并用下划线替换连字符。例如，指定$http_user_agent来获取User-Agent的值。</td></tr><tr><td>$msec</td><td>当前unix时间，以毫秒为单位。</td></tr><tr><td>$qtl_req_id</td><td>请求的唯一标识符。</td></tr><tr><td>$request_uri</td><td>HTTP请求URI。</td></tr><tr><td>$request_method</td><td>用于访问源站的HTTP请求方法。</td></tr><tr><td>$request_time</td><td>响应时间，以毫秒为单位。这是从接收到请求的第一个字节到服务端响应最后一个字节之间的时间。</td></tr><tr><td>$sc_completed</td><td>1表示对象的最后一个字节已返回给用户，否则为0。</td></tr><tr><td>$sc_initial</td><td>1表示对象的第一个字节已返回给用户，否则为0。</td></tr><tr><td>$scheme</td><td>表示用户请求的协议（'http'或'https'）。</td></tr><tr><td>$sent_http_content_length</td><td>原始文件大小。</td></tr><tr><td>$sent_http_x</td><td>获取在对客户端响应中某个HTTP响应头的值。响应头名称需转换为小写，并用下划线替换连字符。例如，$sent_http_etag可获取ETag头的值。</td></tr><tr><td>$server_addr</td><td>为用户请求提供服务的边缘节点的IP地址。</td></tr><tr><td>$server_protocol</td><td>表示用户请求中使用的HTTP版本，可以是'HTTP/1.0'、'HTTP/1.1'或'HTTP/2.0'。</td></tr><tr><td>$ssl_cipher</td><td>表示用于TLS（SSL）连接的加密算法套件。</td></tr><tr><td>$ssl_server_name</td><td>客户端发起TLS（SSL）连接所要连接的域名。仅由支持SNI（Server Name Indication）的客户端发送。</td></tr><tr><td>$ssl_protocol</td><td>表示用于TLS（SSL）连接的TLS版本。例如，'SSLv3'、'TLSv1'、'TLSv1.1'、'TLSv1.2'和'unknown'。</td></tr><tr><td>$status</td><td>用户请求的HTTP状态码。</td></tr><tr><td>$tcpinfo_rtt</td><td>数据包往返目的地所用的时间，以微秒为单位。</td></tr></table>"}
        self.format = format
        # {"en" : "HTTP header names and values to be sent to the notification server. A header name can contain any alphanumeric character or hyphen, '-'. A header value can contain any printable characters. It can also include any of the built-in variables supported in the format field of the realTimeLog object.", "zh_CN": "需要发送到远程服务器的HTTP请求头名称和值。请求头名称可以包含任何字母，数字或连字符'-'。值可以包含任何可打印字符，也可以使用realTimeLog对象format字段中支持的任何内置变量。"}
        self.headers = headers

    def validate(self):
        self.validate_required(self.log_url, 'log_url')
        if self.headers:
            for k in self.headers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.log_url is not None:
            result['logUrl'] = self.log_url
        if self.sample_rate is not None:
            result['sampleRate'] = self.sample_rate
        if self.escape is not None:
            result['escape'] = self.escape
        if self.format is not None:
            result['format'] = self.format
        if self.headers is not None:
            result['headers'] = []
            for k in self.headers:
                result['headers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logUrl') is not None:
            self.log_url = m.get('logUrl')
        if m.get('sampleRate') is not None:
            self.sample_rate = m.get('sampleRate')
        if m.get('escape') is not None:
            self.escape = m.get('escape')
        if m.get('format') is not None:
            self.format = m.get('format')
        if m.get('headers') is not None:
            self.headers = []
            for k in m.get('headers'):
                temp_model = CreateAPropertyRequestVersionRealTimeLogHeaders()
                self.headers.append(temp_model.from_map(k))
        return self


class CreateAPropertyRequestVersionOriginsAuthentication(TeaModel):
    def __init__(
        self,
        method_name: str = None,
    ):
        # {"en" : "Authentication method.", "zh_CN": "鉴权方法。"}
        self.method_name = method_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.method_name is not None:
            result['methodName'] = self.method_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('methodName') is not None:
            self.method_name = m.get('methodName')
        return self


class CreateAPropertyRequestVersionOrigins(TeaModel):
    def __init__(
        self,
        name: str = None,
        servers: List[str] = None,
        supported_protocol: str = None,
        direct_connection: str = None,
        host_header: str = None,
        verify_origin: bool = None,
        authentication: CreateAPropertyRequestVersionOriginsAuthentication = None,
        keep_alive_timeout: int = None,
        peer_failure_timeout: str = None,
        tls_certificate_id: str = None,
        shield: str = None,
    ):
        # {"en" : "^[a-zA-z0-9_] 
        # Name of an origin. It must be unique within this property.
        # ", "zh_CN": "^[a-zA-z0-9_] 
        # 源站名称，在此加速项目中必须唯一。"}
        self.name = name
        # {"en" : "Each entry should be a string consisting of an address optionally followed by one or more parameters, separated by space characters. The address can take one of the following three forms:
        # {hostname or IP address}
        # {hostname or IP address}:{http port}
        # {hostname or IP address}:{http port},{https port}
        # Values for the HTTP and HTTPS ports should be integers in the range [1,65535]. 
        # Even if the value of supportedProtocol is 'https', the HTTPS port has to be specified after the comma.
        # In the third form, one of the two ports can be empty.
        # 
        # Supported parameters are 'backup' and 'weight'.
        # 
        # 'backup' is used to indicate the server is a backup server. It will be used when the primary servers are unavailable.
        # 
        # 'weight' is a value in the range [1, 100]. The default value is 1. It lets you control the likelihood that one origin server will be used relative to another.
        # 
        # There should be at least one primary server defined; it does not have the 'backup' parameter.
        # 
        # Example:
        # ['www.abc.com weight=1', 'www1.abc.com:8080 weight=4', 'www2.abc.com:880,4443 backup']
        # 
        # This example specifies two primary servers which are used in a 1:4 ratio meaning one gets about 20% of the requests to origin while the other gets 80% of the requests. In addition, a backup server is specified.
        # ", "zh_CN": "源站服务器列表。每个条目为一个字符串，由一个地址与一个或多个参数组成，参数之间以空格分隔。地址可以采用以下三种形式之一：
        # {域名或IP地址}
        # {域名或IP地址}:{HTTP端口}
        # {域名或IP地址}:{HTTP端口},{HTTPS端口}
        # HTTP和HTTPS端口的值应为[1,65535]范围内的整数。
        # 即使supportedProtocol的值设为'https'，也必须在此处指定HTTPS端口。
        # 在第三种形式中，两个端口中的一个可以为空。
        # 支持ipv6 当enableIpv6Origin为true时，ipv6传入{域名或IP地址}:{HTTP端口},{HTTPS端口}时，域名或IP地址需要放入[]，如[2001:0db8:85a3:0000:0000:8a2e:0370:7334]:80
        # 
        # 支持的参数包括'backup'和'weight'。
        # 'backup'用于标识备份服务器。它将在主服务器不可用时使用。
        # 'weight'是范围[1,100]内的值，默认值为1，用来设置服务器权重，控制一台源站服务器相对于另一台被使用的可能性。
        # 每个源站应至少定义一个主服务器（即不带'backup'参数的服务器）。
        # 
        # 示例：
        # ['www.abc.com weight=1', 'www1.abc.com:8080 weight=4', 'www2.abc.com:880,4443 backup']
        # 
        # 此示例指定了两个主服务器和一个备份服务器，其中，主服务器的权重为1:4，表示第一个服务器将获得约20%的回源请求，而另一个将获得约80%。"}
        self.servers = servers
        # {"en" : "Enum: http,https,both 
        # This optional field indicates the protocol supported by the origin server. If this property has a certificate attached to it, the value can be set to http if the allowProtocolDowngrade field is also set to true.", "zh_CN": "取值范围: http,https,both 
        # 此可选字段表示源站服务器支持的协议。如果此加速项目附加了证书，且allowProtocolDowngrade字段也设置为true，则可以将该值设置为http。"}
        self.supported_protocol = supported_protocol
        # {"en" : "Default: auto 
        # Optional. This parameter tells us how important it is to directly go to this origin without going through any intermediate cache to fetch content. The values can be 'noDirect', 'auto', 'alwaysDirect'. 
        # 
        # 'noDirect' means we always go through at least one intermediate cache. Customers who care particularly about the origin's workload can use this option. Our cache scheduler will dynamically pick the intermediate cache based on performance and resource availability.
        # 
        # 'auto' means the cache scheduler will make the choice dynamically based on performance and resource availability. This is the default behavior if not specified.
        # 
        # 'alwaysDirect' means we always directly connect to this origin.
        # ", "zh_CN": "默认值: auto 
        # 此可选字段用来指定回源方式，可以是'noDirect'、'auto'、'alwaysDirect'。
        # 
        # 'noDirect'指总是通过至少一个中间缓存节点回源。对于特别关心源站负载的客户可以使用此选项。我们的调度程序将根据性能和资源可用性动态选择中间缓存节点。
        # 'alwaysDirect'指总是直接回源。
        # 'auto'指自动选择直接回源或通过中间缓存节点回源。调度程序将根据性能和资源可用性动态做出选择。该字段未指定时，采用此默认行为。"}
        self.direct_connection = direct_connection
        # {"en" : "Optional. It should be a valid hostname. It will also be used as the SNI servername when contacting the HTTPS origin. We also allow it to be an nginx variable that begins with '$' followed by [a-z_]{3,60}. Nginx variable names are case insensitive, so we only allow lowercase characters.
        # If not specified, the value of the HOST header in the request will be used. 
        # 
        # One constraint is that if 'aswS3' is specified for origin authentication, the value of hostHeader cannot be a variable or empty. It has to be a valid Amazon S3 hostname. Refer to https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html", "zh_CN": "可选，用来指定回源HOST头部。必须是有效的域名。当连接HTTPS源站时，该值也作为SNI域名。可以用nginx变量来指定，变量以'$'开头，后跟[a-z_]{3,60}。Nginx变量名不区分大小写，因此我们只允许小写字符。
        # 如果未指定，将使用请求中的HOST请求头的值。
        # 
        # 注意：如果指定了'awsS3'作为回源鉴权参数，则hostHeader的值不能为变量或为空，而必须是有效的Amazon S3主机名。参考：https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html"}
        self.host_header = host_header
        # {"en" : "Default: False 
        # Optional. It controls whether the cache will validate the certificate of the origin.", "zh_CN": "默认值: False 
        # 可选。用来设定CDN缓存节点是否验证源站证书。"}
        self.verify_origin = verify_origin
        # {"en" : "Optional. It is a structure to specify the parameters, such as password, for authentication with the origin servers. It should have at least one field: 'methodName', which should be a string indicating one of the predefined authentication methods. The only valid value at this time is 'awsS3'. When 'awsS3' is used, the following parameters are required:
        # awsS3.region:
        # The AWS S3 region where your resources are hosted, e.g. 'us-west-1', 'ap-northeast-1', 'eu-north-1', and 'cn-north-1'.
        # awsS3.accessKey:
        # Your AWS access key that CDN Pro will use to access your resources stored on AWS S3.
        # awsS3.secretKey:
        # Your AWS secret key that CDN Pro will use to access your resources stored on AWS S3.
        # Also, the value of the hostHeader field cannot be a variable or empty. It must be a valid Amazon S3 hostname.
        # 
        # Example:
        # 
        # {'methodName':'awsS3',
        # 'awsS3':{
        # 'region':'us-west-1',
        # 'accessKey':'sdnu2932',
        # 'secretKey':'d12345678abcdefghi'
        # }}
        # ", "zh_CN": "可选。用于指定与源服务器进行身份验证（回源鉴权）的相关参数（如密码）。必须至少有'methodName'（字符串）字段，用来指定预定义的鉴权方法。目前仅支持源站为AWS S3的回源鉴权，因此唯一有效的值是'awsS3'。使用'awsS3'时，需要提供以下参数：
        # awsS3.region:
        # 您存储在S3上的资源所在的AWS区域。例如，'us-west-1'，'ap-northeast-1'，'eu-north-1'，'cn-north-1'。
        # awsS3.accessKey:
        # 您的 AWS 访问密钥（access key），CDN Pro 将使用它来访问您存储在 AWS S3 上的资源。
        # awsS3.secretKey:
        # 您的 AWS 密钥（secret key），CDN Pro 将使用它来访问您存储在 AWS S3 上的资源。
        # 此外，hostHeader字段的值不能为变量或为空，必须是有效的Amazon S3主机名。
        # 
        # 示例：
        # 
        # {'methodName':'awsS3',
        # 'awsS3':{
        # 'region':'us-west-1',
        # 'accessKey':'sdnu2932',
        # 'secretKey':'d12345678abcdefghi'
        # }}
        # "}
        self.authentication = authentication
        # {"en" : "Default: 60 Range: [ 5 .. 600 ] 
        # Timeout in seconds during which an idle keepalive connection to an upstream server will stay open. A service quota setting of maxUpstreamKeepaliveTimeOut can change the maximum permitted value.", "zh_CN": "默认值: 60 取值范围: [ 5 .. 600 ] 
        # 该字段用于指定CDN Pro服务器和源站建连的Keep-Alive超时时间，单位为秒。通过maxUpstreamKeepaliveTimeOut 该服务设置项可以更改允许的最大值。如果需要调整最大值，请联系我们的技术支持。"}
        self.keep_alive_timeout = keep_alive_timeout
        # {"en" : "
        # This setting allows you to specify the number of unsuccessful attempts to reach one of the origin's IP addresses or peers before it is marked as unavailable for a period of time designated by the timeout. If all peers of all servers are unavailable, requests for content from the origin will receive an immediate 502 HTTP response. By default, six attempts to a peer are made, after which a one-second timeout applies to that peer. To disable this feature, set peerFailureTimeout to 'off'.", "zh_CN": "
        # 该字段用于设置源站故障剔除。开启此功能后，当连接某个源站服务器的失败次数达到设定阈值，该源站服务器将被标记为不可用，并保持该状态直到设定的超时时长。失败次数阈值和超时时长分别通过failureThreshold参数和timeout参数设置。CDN Pro回源时将剔除不可用的源站服务器。如果所有源站服务器都被标记为不可用，则对应的请求将立即响应502状态码。默认情况下，当连接某个源站服务器连续失败6次之后，该服务器将被标记为不可用，超时时长为1秒。如果要禁用此功能，请将peerFailureTimeout设置为'off'。开启源站故障剔除配置示例：<code>{'peerFailureTimeout':{'failureThreshold':10,'timeout':3}}</code>"}
        self.peer_failure_timeout = peer_failure_timeout
        # {"en" : "Refers to a certificate used to authenticate with the origin server. This certificate must also be deployed.", "zh_CN": "用于验证源站服务器的证书，该证书同样必须被部署。"}
        self.tls_certificate_id = tls_certificate_id
        # {"en" : "Refers to the ID of an origin shield representing a set of servers that will make requests to your origin servers rather than the CDN Pro edge servers. This can help further reduce traffic to your origin. Origin shield is allowed only when direcConnection is set to noDirect. This is an advanced feature that can be enabled by contacting our support team. The origin shields API provides a list of available shields along with their IP addresses. It is best to select a shield whose region is closest to your origin servers. Use of a shield in China requires your property have 'hasBeian' set to true. If your origin servers have an access control list, add the IPs of the shield you choose to use.", "zh_CN": "指定某个源站盾（origin shield）的ID。使用源站盾功能后，所有回源请求都会通过源站盾中转回源，这可以帮助收敛回源流量。需要把directConnection设置为noDirect，才允许开启源站盾。源站盾是高级功能，如需使用请联系我们的技术支持开通。可通过调用‘获取源站盾列表’接口查询可用的源站盾及其对应的IP地址。您可根据源站的位置，选择合适的源站盾。如果您需使用中国大陆的源站盾，则该加速项目的所有域名必须已取得备案。如果您的源站开启了访问控制，请将所选择源站盾的IP地址加入白名单。"}
        self.shield = shield

    def validate(self):
        if self.authentication:
            self.authentication.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.servers is not None:
            result['servers'] = self.servers
        if self.supported_protocol is not None:
            result['supportedProtocol'] = self.supported_protocol
        if self.direct_connection is not None:
            result['directConnection'] = self.direct_connection
        if self.host_header is not None:
            result['hostHeader'] = self.host_header
        if self.verify_origin is not None:
            result['verifyOrigin'] = self.verify_origin
        if self.authentication is not None:
            result['authentication'] = self.authentication.to_map()
        if self.keep_alive_timeout is not None:
            result['keepAliveTimeout'] = self.keep_alive_timeout
        if self.peer_failure_timeout is not None:
            result['peerFailureTimeout'] = self.peer_failure_timeout
        if self.tls_certificate_id is not None:
            result['tlsCertificateId'] = self.tls_certificate_id
        if self.shield is not None:
            result['shield'] = self.shield
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('servers') is not None:
            self.servers = m.get('servers')
        if m.get('supportedProtocol') is not None:
            self.supported_protocol = m.get('supportedProtocol')
        if m.get('directConnection') is not None:
            self.direct_connection = m.get('directConnection')
        if m.get('hostHeader') is not None:
            self.host_header = m.get('hostHeader')
        if m.get('verifyOrigin') is not None:
            self.verify_origin = m.get('verifyOrigin')
        if m.get('authentication') is not None:
            temp_model = CreateAPropertyRequestVersionOriginsAuthentication()
            self.authentication = temp_model.from_map(m['authentication'])
        if m.get('keepAliveTimeout') is not None:
            self.keep_alive_timeout = m.get('keepAliveTimeout')
        if m.get('peerFailureTimeout') is not None:
            self.peer_failure_timeout = m.get('peerFailureTimeout')
        if m.get('tlsCertificateId') is not None:
            self.tls_certificate_id = m.get('tlsCertificateId')
        if m.get('shield') is not None:
            self.shield = m.get('shield')
        return self


class CreateAPropertyRequestVersionVideoSeek(TeaModel):
    def __init__(
        self,
        start_parameter: str = None,
        end_parameter: str = None,
    ):
        # {"en" : "Range: [ 1 .. 31 ] characters 
        # Name of the query parameter indicating the starting offset in bytes of the content to fetch. The parameter name should begin with a letter (a-z, A-Z) and may be followed by up to 30 letters and numbers.", "zh_CN": "取值范围: [ 1 .. 31 ] 字符 
        # 查询参数的名称，用来指定要获取的内容的起始位置（以字节计算）。参数名称应以字母（a-z，A-Z）开头，后面最多可以有30个字母和数字。"}
        self.start_parameter = start_parameter
        # {"en" : "Range: [ 0 .. 31 ] characters 
        # Name of the query parameter indicating the ending offset of the content to fetch. The parameter name should begin with a letter (a-z, A-Z) and may be followed by up to 30 letters and numbers.", "zh_CN": "取值范围: [ 0 .. 31 ] 字符 
        # 查询参数的名称，用来指定要获取的内容的结束位置（以字节计算）。参数名称应以字母（a-z，A-Z）开头，后面最多可以有30个字母和数字。"}
        self.end_parameter = end_parameter

    def validate(self):
        self.validate_required(self.start_parameter, 'start_parameter')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_parameter is not None:
            result['startParameter'] = self.start_parameter
        if self.end_parameter is not None:
            result['endParameter'] = self.end_parameter
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startParameter') is not None:
            self.start_parameter = m.get('startParameter')
        if m.get('endParameter') is not None:
            self.end_parameter = m.get('endParameter')
        return self


class CreateAPropertyRequestVersionAccessControlRulesConditions(TeaModel):
    def __init__(
        self,
        scheme: str = None,
        hostname: str = None,
        uri: str = None,
        server_regions: List[str] = None,
        client_regions: List[str] = None,
        client_ip_range: List[str] = None,
    ):
        # {"en" : "Enum: https,http 
        # Indicates whether the incoming request uses HTTP or HTTPS.", "zh_CN": "取值范围: https,http 
        # 客户端请求的协议，HTTP或HTTPS。"}
        self.scheme = scheme
        # {"en" : "Indicates the hostname requested. It must be one of the hostnames defined in the property.", "zh_CN": "请求对应的加速域名。必须是加速项目中定义的加速域名之一。"}
        self.hostname = hostname
        # {"en" : "Range: <= 500 characters 
        # The URI begins with '/' and can end with '*' for prefix matching. ", "zh_CN": "取值范围: <= 500 字符 
        # 用于前缀匹配的URI，以'/'开头，可以以'*'结尾。"}
        self.uri = uri
        # {"en" : "An array of ISO-3166-1 alpha-2 codes indicating the countries of the servers, for example, 'US' to represent 'United States of America'.", "zh_CN": "服务器所在区域，以ISO-3166-1 两位国家代码表示。例如，'US'代表'美国'。"}
        self.server_regions = server_regions
        # {"en" : "An array of ISO-3166-1 alpha-2 codes indicating one or more countries which are the source of the client requests, for example, 'CN' to represent 'China'.", "zh_CN": "客户端请求来源区域，以ISO-3166-1 两位国家代码表示。例如，'CN'代表'中国'。"}
        self.client_regions = client_regions
        # {"en" : "Indicates the starting and ending IP addresses of the client requests to match against. They must be in IPv4 or IPv6 format.", "zh_CN": "用于指定要匹配的客户端请求的开始和结束IP地址。必须是IPv4或IPv6格式。"}
        self.client_ip_range = client_ip_range

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scheme is not None:
            result['scheme'] = self.scheme
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.uri is not None:
            result['uri'] = self.uri
        if self.server_regions is not None:
            result['serverRegions'] = self.server_regions
        if self.client_regions is not None:
            result['clientRegions'] = self.client_regions
        if self.client_ip_range is not None:
            result['clientIpRange'] = self.client_ip_range
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scheme') is not None:
            self.scheme = m.get('scheme')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('uri') is not None:
            self.uri = m.get('uri')
        if m.get('serverRegions') is not None:
            self.server_regions = m.get('serverRegions')
        if m.get('clientRegions') is not None:
            self.client_regions = m.get('clientRegions')
        if m.get('clientIpRange') is not None:
            self.client_ip_range = m.get('clientIpRange')
        return self


class CreateAPropertyRequestVersionAccessControlRulesAction(TeaModel):
    def __init__(
        self,
        status_code: str = None,
        message: str = None,
    ):
        # {"en" : "Indicates the HTTP status code to respond with. It must be in the range 300-309, 400-409, or 500-509 to indicate a redirection or error.", "zh_CN": "响应的HTTP状态码，范围必须在300-309、400-409或500-509之间，分别表示重定向或错误。"}
        self.status_code = status_code
        # {"en" : "Range: <= 200 characters 
        # If the value of the status field is in the range 300-309, the message field's value will be placed in a Location HTTP header returned to the client. If the status is in the range 400-409 or 500-509, the value will be returned in the response body to the client.", "zh_CN": "取值范围: <= 200 字符 
        # 如果status字段的值在300-309范围内，message字段的值将在返回给客户端的Location响应头中。如果status字段的值在400-409或500-509范围内，则message字段的值将在返回给客户端的响应体中。"}
        self.message = message

    def validate(self):
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateAPropertyRequestVersionAccessControlRules(TeaModel):
    def __init__(
        self,
        id: str = None,
        conditions: CreateAPropertyRequestVersionAccessControlRulesConditions = None,
        action: CreateAPropertyRequestVersionAccessControlRulesAction = None,
    ):
        # {"en" : "Range: [ 0 .. 60 ] characters 
        # An optional ID for the access control rule.", "zh_CN": "取值范围: [ 0 .. 60 ] 字符 
        # 访问控制规则ID。"}
        self.id = id
        # {"en" : "Specify the conditions that the incoming request must match. At least one condition must be specified. If multiple are specified, all must match.", "zh_CN": "指定客户端请求必须匹配的条件。必须至少指定一个条件。如果指定了多个条件，则必须全部匹配。"}
        self.conditions = conditions
        # {"en" : "Indicates the action to take in response to a request that matches the conditions of the access control rule.", "zh_CN": "对于匹配到以上条件的请求所采取的相应操作。"}
        self.action = action

    def validate(self):
        if self.conditions:
            self.conditions.validate()
        if self.action:
            self.action.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.conditions is not None:
            result['conditions'] = self.conditions.to_map()
        if self.action is not None:
            result['action'] = self.action.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('conditions') is not None:
            temp_model = CreateAPropertyRequestVersionAccessControlRulesConditions()
            self.conditions = temp_model.from_map(m['conditions'])
        if m.get('action') is not None:
            temp_model = CreateAPropertyRequestVersionAccessControlRulesAction()
            self.action = temp_model.from_map(m['action'])
        return self


class CreateAPropertyRequestVersionExtraServicePorts(TeaModel):
    def __init__(
        self,
        http: List[str] = None,
        https: List[str] = None,
    ):
        # {"en" : "This is a list of ports other than 80 which are used to handle HTTP requests. The available values can be found in the systemConfigs API's response. If you need another port, please contact our support team.", "zh_CN": "指定用于处理HTTP请求的端口列表（80端口除外）。可通过调用'获取系统配置'接口来查询系统支持的端口。如果您需要开通其他端口，请联系技术支持。"}
        self.http = http
        # {"en" : "This is a list of ports other than 443 which are used to handle HTTPS requests. The available values can be found in the systemConfigs API's response. If you need another port, please contact our support team.", "zh_CN": "指定用于处理HTTPS请求的端口列表（443端口除外）。可通过调用'获取系统配置'接口来查询系统支持的端口。如果您需要开通其他端口，请联系技术支持。"}
        self.https = https

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.http is not None:
            result['http'] = self.http
        if self.https is not None:
            result['https'] = self.https
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('http') is not None:
            self.http = m.get('http')
        if m.get('https') is not None:
            self.https = m.get('https')
        return self


class CreateAPropertyRequestVersion(TeaModel):
    def __init__(
        self,
        description: str = None,
        cache_key_hostname: str = None,
        hostnames: List[str] = None,
        real_time_log: CreateAPropertyRequestVersionRealTimeLog = None,
        edge_logic: str = None,
        has_beian: bool = None,
        redirect_http_to_https: str = None,
        origins: List[CreateAPropertyRequestVersionOrigins] = None,
        syntax_version: int = None,
        disable_http_2: bool = None,
        enable_http_3: bool = None,
        scheme_in_cache_key: bool = None,
        tls_max_version: str = None,
        load_balancer_hash_key: str = None,
        tls_certificate_id: str = None,
        tls_min_version: str = None,
        tls_ciphers: str = None,
        allow_protocol_downgrade: bool = None,
        tls_certificate_id_1: str = None,
        video_seek: CreateAPropertyRequestVersionVideoSeek = None,
        tls_session_timeout: int = None,
        enable_ocsp_stapling: bool = None,
        beian_content_type: int = None,
        enable_ipv_6origin: bool = None,
        follow_client_ip_version: str = None,
        access_control_rules: List[CreateAPropertyRequestVersionAccessControlRules] = None,
        disable_cert_automation: bool = None,
        cache_key_uri: str = None,
        extra_service_ports: CreateAPropertyRequestVersionExtraServicePorts = None,
        load_balancer_logic: str = None,
        tls_0rtt: bool = None,
    ):
        # {"en" : "A description of the version.
        # ", "zh_CN": "版本描述。"}
        self.description = description
        # {"en" : "Range: <= 80 characters ^[a-z.-_]+\
        # The cachekey hostname must be a string made of lowercase letters, digits, dot, dash, and underscore. If not specified, the incoming Host header value will be used and the cache will not be shared across different hostnames in this property.
        # ", "zh_CN": "取值范围: <= 80 字符 ^[a-z.-_]+\
        # 用于缓存键（Cache Key）的主机名必须是由小写字母、数字、点、连字符和下划线组成的字符串。如果未指定，默认将使用传入的Host请求头值，并且此加速项目中的不同加速域名之间不共享缓存。"}
        self.cache_key_hostname = cache_key_hostname
        # {"en" : "Hostnames associated with the property. A valid value is a fully qualified hostname such as www.domain.com or a wildcard hostname such as *.domain.com. Any given hostname can only be in one deployed property at a particular time. However, a wildcard hostname is permitted to overlap other hostnames you own.", "zh_CN": "与加速项目关联的加速域名。必须是FQDN完全限定域名（如 www.domain.com），或泛域名（如*.domain.com）。
        # 同一个加速域名在同一时间只能存在于一个已部署的加速项目中，但泛域名可以与关联的完全限定域名一同部署。"}
        self.hostnames = hostnames
        # {"en" : "This optional field allows you to configure notifications about client requests to be sent to a remote server. This is an advanced feature. Please contact our support team if you require this feature.", "zh_CN": "此可选字段用来配置发送消息通知（即实时日志）到您的远程服务器。当有客户端请求访问您的加速域名时，将触发通知。这是高级功能，如果您需要此功能，请联系我们的技术支持开通。"}
        self.real_time_log = real_time_log
        # {"en" : "Range: <= 65530 characters 
        # Refer to Edge Logic Introduction.", "zh_CN": "取值范围: <= 65530 字符 
        # 自定义边缘逻辑。参考边缘逻辑介绍。"}
        self.edge_logic = edge_logic
        # {"en" : "Default: False 
        # The value indicates whether all the hostnames in this property have Beian license on file with the Chinese government. This is required to serve this property from servers in mainland China. A value of false means servers outside of mainland China will be used to distribute content to visitors in China. If set to true you must also specify the content type in the beianContentType field.", "zh_CN": "默认值: False 
        # 此加速项目中的所有加速域名是否都已获得中国政府的ICP备案。只有获取备案的域名才能使用中国大陆节点来提供服务。如果设置为true，还必须在beianContentType字段中指定内容类型。"}
        self.has_beian = has_beian
        # {"en" : "Default: False 
        # This field can be set to either a boolean value or a string. If the value is set to true, the server will redirect all HTTP requests to HTTPS using status code 301. You can also specify string values '302', '307', or '308' instead if you wish to return a different status code when a request is redirected.", "zh_CN": "默认值: False 
        # 此字段可以设置为布尔值或字符串。如果设置为true，则CDN Pro服务器会将所有HTTP请求重定向到HTTPS，并返回301状态码。如果您希望在重定向请求时返回不同的状态码，可在此处指定需要的状态码，如'302'、'307'或'308'。"}
        self.redirect_http_to_https = redirect_http_to_https
        # {"en" : "Describes the origin servers for the property's content.", "zh_CN": "描述加速项目对应的源站。"}
        self.origins = origins
        # {"en" : "Default: 1 
        # The value must be set to 1 at this time.", "zh_CN": "默认值: 1 
        # 当前仅允许值为1。"}
        self.syntax_version = syntax_version
        # {"en" : "Default: False 
        # Set to true to disable support for HTTP/2 and support only HTTP 1.1.", "zh_CN": "默认值: False 
        # 当值为true时，禁用对HTTP/2的支持，仅支持HTTP/1.1。"}
        self.disable_http_2 = disable_http_2
        # {"en" : "Default: False 
        # Set to true to enable support for HTTP/3. HTTP/3 requires TLS to work, so this field will be ignored unless you specify a certificate in the tlsCertificateId field.", "zh_CN": "默认值: False 
        # 是否开启HTTP/3，HTTP/3 需要 需要配置TLS 才生效，若您未在 tlsCertificateId 中指定证书，此字段将被忽略。"}
        self.enable_http_3 = enable_http_3
        # {"en" : "Default: False 
        # Specifies whether the scheme ('http' or 'https') should be included in the cache key. Default behavior is false. Set to true if the content is known to be different for different schemes.
        # ", "zh_CN": "默认值: False 
        # 指定缓存键（Cache Key）是否区分协议（'http'或'https'）。默认为false。如果不同协议响应的内容不同，则设置为true。"}
        self.scheme_in_cache_key = scheme_in_cache_key
        # {"en" : "Enum: 1.1,1.2,1.3 
        # Default: 1.3 
        # Maximum supported TLS version.", "zh_CN": "取值范围: 1.1,1.2,1.3 
        # 默认值: 1.3 
        # 支持的TLS最高版本。"}
        self.tls_max_version = tls_max_version
        # {"en" : "Range: <= 100 characters 
        # Multiple tiers of load balancing are used in our CDN pops to distribute the client requests to different servers. We are using consistent hashing in many of those places. By default, the URL is used as the hash key, which should be good enough in most cases. Here you can define additional variables to be added to the hash key to distribute the requests more evenly. One typical use case is when all requests carry the same URL, but use a particular header to indicate the resources. 
        # 
        # This is an optional field. The default value is an empty string. A valid value is a string meeting the following criteria:
        # 
        # Consists of alphanumeric characters, underscore _, equal sign =, dollar sign $, and ampersand sign &.
        # The variable names can only be in one of the following formats: $http_name, $cookie_name, or $arg_name.
        # At least one variable must be specified. No more than three are permitted.
        # The total length should be no more than 100 characters.
        # 
        # The validator will treat any dollar sign and the string after it (before any = or & or $) as a variable. 
        # 
        # Here are some examples of valid values:
        # <table><tr><td>$http_abc</td></tr><tr><td>abc=$http_abc&def=$http_def&c_123=$cookie_123</td></tr><tr><td>abc=$http_abc=$http_def</td></tr><tr><td>$http_abc&$http_def</td></tr><tr><td>=$http_abd&</td></tr><tr><td>&&abc==$http_abc&&&===qwer</td></tr></table>
        # ", "zh_CN": "取值范围: <= 100 字符 
        # 我们的CDN使用了多层负载均衡架构，将客户端请求分发到不同的服务器。我们在架构中多处使用到一致性哈希。默认情况下，URL被用作哈希键，这对于大多数情况都适用。您可以在这里定义要添加到哈希键的其他变量，以更均匀地分配请求。一个典型的使用场景是，所有请求都携带相同的URL，但使用特定的请求头来区分资源。
        # 
        # 这是一个可选字段，默认值为空字符串。必须满足以下条件：
        # 
        # 由字母、数字、下划线_、等号=、美元符号$和符号&组成。
        # 变量名只能采用以下格式之一：$http_name、$cookie_name、$arg_name。
        # 必须至少指定一个变量，不允许超过三个。
        # 总长度不得超过100个字符。
        # 
        # 我们的配置验证器将把任何美元符号及其后的字符串（在任何=或&或$之前）视为变量。
        # 
        # 以下是一些有效值的示例：
        # <table><tr><td>$http_abc</td></tr><tr><td>abc=$http_abc&def=$http_def&c_123=$cookie_123</td></tr><tr><td>abc=$http_abc=$http_def</td></tr><tr><td>$http_abc&$http_def</td></tr><tr><td>=$http_abd&</td></tr><tr><td>&&abc==$http_abc&&&===qwer</td></tr></table>"}
        self.load_balancer_hash_key = load_balancer_hash_key
        # {"en" : "Refers to a certificate. It is invalid to only set the tlsCertificateId1 field without setting the tlsCertificateId field. If tlsCertificateId is not set, HTTPS will not be enabled for this property. This is a feature to enable you to specify two certificates of different types, i.e. one RSA, one EC. If two certificates of the same type are specified, the one specified by tlsCertificateId will be ignored. ", "zh_CN": "该加速项目用到的证书ID。仅设置tlsCertificateId1字段而不设置tlsCertificateId字段是无效的。如果未设置tlsCertificateId，则不会为此加速项目启用HTTPS。此功能允许您指定两个不同类型的证书，即一个RSA，一个EC。如果指定了两个相同类型的证书，则将忽略tlsCertificateId指定的证书。 "}
        self.tls_certificate_id = tls_certificate_id
        # {"en" : "Enum: 1.1,1.2,1.3,1 
        # Default: 1 
        # Minimum required TLS version.", "zh_CN": "取值范围: 1.1,1.2,1.3,1 
        # 默认值: 1 
        # 所需的TLS最低版本。"}
        self.tls_min_version = tls_min_version
        # {"en" : "Range: <= 2040 characters 
        # Any cipher list supported by 'openssl ciphers'. See https://www.openssl.org/docs/manmaster/man1/ciphers.html
        # ", "zh_CN": "取值范围: <= 2040 字符 
        # 'openssl ciphers'支持的任何加密算法套件。参考：https://www.openssl.org/docs/manmaster/man1/ciphers.html"}
        self.tls_ciphers = tls_ciphers
        # {"en" : "Default: False 
        # This setting applies only if the property has an attached certificate allowing client requests to use HTTPS. If the value of allowProtocolDowngrade is false, we require all the origin servers to support HTTPS. If the value is true, we allow origins that support only HTTP, which reduces security.
        # ", "zh_CN": "默认值: False 
        # 是否允许协议降级。仅当加速项目中存在允许客户端使用HTTPS请求的证书时，此设置才适用。如果allowProtocolDowngrade的值为false，则要求所有源服务器支持HTTPS。如果值为true，则允许仅支持HTTP的源，但这会降低安全性。"}
        self.allow_protocol_downgrade = allow_protocol_downgrade
        # {"en" : "Refers to a certificate. It is invalid to only set the tlsCertificateId1 field without setting the tlsCertificateId field. If tlsCertificateId is not set, HTTPS will not be enabled for this property. This is a feature to enable you to specify two certificates of different types, i.e. one RSA, one EC. If two certificates of the same type are specified, the one specified by tlsCertificateId will be ignored. 
        # ", "zh_CN": "指该加速项目用到的证书ID。仅设置tlsCertificateId1字段而不设置tlsCertificateId字段是无效的。如果未设置tlsCertificateId，则不会为此加速项目启用HTTPS。此功能允许您指定两个不同类型的证书，即一个RSA，一个EC。如果指定了两个相同类型的证书，则将忽略tlsCertificateId指定的证书。"}
        self.tls_certificate_id_1 = tls_certificate_id_1
        # {"en" : "This object allows you to support video players requesting partial content through query string parameters. If you specify videoSeek, you must enter a value for startParameter.", "zh_CN": "此对象用来支持视频播放器通过指定查询参数来请求部分内容。当videoSeek对象存在时，必须为startParameter设置一个值。"}
        self.video_seek = video_seek
        # {"en" : "Default: 1800 Range: [ 300 .. 86400 ] 
        # Lifespan of TLS session ticket in seconds.", "zh_CN": "默认值: 1800 取值范围: [ 300 .. 86400 ] 
        # TLS会话ticket的有效期（秒）。"}
        self.tls_session_timeout = tls_session_timeout
        # {"en" : "Default: False 
        # Enables Online Certificate Status Protocol (OCSP) stapling to check the revocation status of digital certificates. (Refer to https://en.wikipedia.org/wiki/OCSP_stapling)", "zh_CN": "默认值: False 
        # 是否启用在线证书状态协议（OCSP）装订以检查数字证书的吊销状态。参考：https://en.wikipedia.org/wiki/OCSP_stapling"}
        self.enable_ocsp_stapling = enable_ocsp_stapling
        # {"en" : "Range: [ 1 .. 24 ] 
        # If you are planning to distribute content through servers in mainland China, you will need to set the hasBeian field to true and also indicate the type of content you are distributing. Enter the value that best corresponds to your content:
        # 
        # <table><tr><th>Value</th><th>Content Type</th></tr><tr><td>1</td><td>Instant Messaging</td></tr><tr><td>2</td><td>Search Engine</td></tr><tr><td>3</td><td>Web Portal</td></tr><tr><td>4</td><td>Online Postal Service</td></tr><tr><td>5</td><td>Online News</td></tr><tr><td>6</td><td>Blog</td></tr><tr><td>7</td><td>Advertisement</td></tr><tr><td>8</td><td>Organization Web Portal</td></tr><tr><td>9</td><td>Shopping</td></tr><tr><td>10</td><td>Online Payment</td></tr><tr><td>11</td><td>Online Bank</td></tr><tr><td>12</td><td>Online Stock Market</td></tr><tr><td>13</td><td>Online Gaming</td></tr><tr><td>14</td><td>Online Music</td></tr><tr><td>15</td><td>Online Movie</td></tr><tr><td>16</td><td>Online Picture</td></tr><tr><td>17</td><td>Software Download</td></tr><tr><td>18</td><td>Job Hunting</td></tr><tr><td>19</td><td>Online Dating</td></tr><tr><td>20</td><td>Online Real Property</td></tr><tr><td>21</td><td>Online Education</td></tr><tr><td>22</td><td>Web Design</td></tr><tr><td>23</td><td>WAP</td></tr><tr><td>24</td><td>Others</td></tr></table>", "zh_CN": "取值范围: [ 1 .. 24 ] 
        # 如果您的域名已获得备案，希望通过中国大陆的服务器分发内容，则需要将hasBeian字段设置为true，并说明您分发的内容类型。请选择与您的内容最匹配的值：
        # 
        # <table><tr><th>值</th><th>内容类型</th></tr><tr><td>1</td><td>即时通信</td></tr><tr><td>2</td><td>搜索引擎</td></tr><tr><td>3</td><td>综合门户</td></tr><tr><td>4</td><td>网上邮局</td></tr><tr><td>5</td><td>网络新闻</td></tr><tr><td>6</td><td>博客/个人空间</td></tr><tr><td>7</td><td>网络广告</td></tr><tr><td>8</td><td>单位门户网站</td></tr><tr><td>9</td><td>网络购物</td></tr><tr><td>10</td><td>网上支付</td></tr><tr><td>11</td><td>网上银行</td></tr><tr><td>12</td><td>网上炒股</td></tr><tr><td>13</td><td>网络游戏</td></tr><tr><td>14</td><td>网络音乐</td></tr><tr><td>15</td><td>网络影视</td></tr><tr><td>16</td><td>网络图片</td></tr><tr><td>17</td><td>软件下载</td></tr><tr><td>18</td><td>网上求职</td></tr><tr><td>19</td><td>在线交友</td></tr><tr><td>20</td><td>网上房产</td></tr><tr><td>21</td><td>网络教育</td></tr><tr><td>22</td><td>网站建设</td></tr><tr><td>23</td><td>WAP</td></tr><tr><td>24</td><td>其他</td></tr></table>"}
        self.beian_content_type = beian_content_type
        # {"en" : "Default: False 
        # Is it allowed to use IPv6 addresses as the source server for this project.", "zh_CN": "默认值: False 
        # 是否允许使用 IPv6 地址作为该项目的源站服务器"}
        self.enable_ipv_6origin = enable_ipv_6origin
        # {"en" : "Default value: off Optional values: auto, strict, off
        # When enableIpv6Origin is allowed, this setting will control whether to follow the client IP protocol version back to the source.
        # Auto: Refers to selecting the IP address for returning to the source based on the IP protocol version requested by the client. When the source server is unavailable, it automatically switches to another IP protocol address for returning to the source
        # Strict: Strictly select the IP address for returning to the source based on the IP protocol version requested by the client. When the source server is unavailable, it is not allowed to switch to another protocol address for returning to the source
        # Off: Ignore the IP protocol version requested by the client and randomly select an available IPv4 or IPv6 address to return to the source.", "zh_CN": "默认值：off 可选值：auto、strict、off 当enableIpv6Origin为允许时，该设置将控制是否跟随客户端IP协议版本回源。
        # auto：表示根据客户端请求的IP协议版本来选择回源IP地址，当源站服务器不可用时自动切换成其他IP协议地址回源
        # strict：严格根据客户端请求的IP协议版本来选择回源IP地址，当源站服务器不可用时不允许切换成其他协议地址回源
        # off：忽略客户端请求的IP协议版本，随机选择可用的IPv4或IPv6地址回源"}
        self.follow_client_ip_version = follow_client_ip_version
        # {"en" : "Specify one or more access control rules to restrict access to your content. More advanced configuration can be done using Edge Logic. These access control rules take precedence over Edge Logic if both are defined.", "zh_CN": "指定一个或多个访问控制规则以限制对内容的访问。可以使用边缘逻辑进行更高级的配置。此处定义的访问控制规则，优先级高于边缘逻辑。"}
        self.access_control_rules = access_control_rules
        # {"en" : "Default: False 
        # By default, CDN Pro takes control of the contents under the /.well-known/{acme-challenge, pki-validation} directories to support certificate auto-renew for properties. If for any reason you need to manage these two directories by yourself on the origin, for example, to implement your own certificate auto-renew mechanism, you can use this configuration option to disable the default behavior by setting its value to true. For more information about our support for certificate auto-renewal, refer to the description of the autoRenew field in the Create a certificate API.", "zh_CN": "默认值: False 
        # 默认情况下，CDN Pro控制/.well-known/{acme-challenge, pki-validation}目录下的内容，以支持加速项目的证书自动更新功能。如果您需要自己在源站管理这两个目录，例如，为了实现您自己的证书自动更新机制，您可以将此字段设置为true来禁用默认行为。关于证书自动更新的更多信息，请参考'创建证书'接口中autoRenew字段的说明。"}
        self.disable_cert_automation = disable_cert_automation
        # {"en" : "Enum: preRewrite,postRewrite 
        # Default: preRewrite 
        # This setting controls how the URI of the incoming request is incorporated into the cache key if you use a 'rewrite' directive in the property's Edge Logic. The default value, 'preRewrite', puts the unmodified URI into the cache key while 'postRewrite' uses the modified URI. If your rewrite directive converts multiple different URIs into the same value, using 'postRewrite' may result in a higher cache hit ratio.", "zh_CN": "取值范围: preRewrite,postRewrite 
        # 默认值: preRewrite 
        # 如果在加速项目的边缘逻辑中使用了'rewrite'指令，可使用该字段来控制客户端请求的URI如何合并到缓存键（Cache Key）中 。默认值'preRewrite'指将改写前的URI放入缓存键，而'postRewrite'则使用改写后的URI。如果您的'rewrite'指令将多个不同的URI改写为相同的值，则使用'postRewrite'可以提高缓存命中率。"}
        self.cache_key_uri = cache_key_uri
        # {"en" : "This field lists ports other than the default 80 used to handle HTTP requests and ports other than the default 443 used to handle HTTPS requests. ", "zh_CN": "除标准的80，443端口外，我们还支持一些扩展端口。可用该字段指定用于处理HTTP和HTTPS请求的扩展端口。"}
        self.extra_service_ports = extra_service_ports
        # {"en" : "Range: <= 65530 characters 
        # This field allows you to enter Edge Logic to customize load balancing. A subset of the  directives can be used. Refer to the basic directives listed in the baseLbDirectives field of the response to the system configuration API. Currently, these include 'if', 'else', 'elseif', 'set', 'return', 'add_header', 'deny', 'allow', 'access_log_sampling', and 'proxy_set_header.' In addition, some advanced Edge Logic directives, identified by the system configuration API's advancedLbDirectives, can be enabled for your account if needed. Please contact our support team if you require any of them. <br/> Example use: <br />
        # if ($http_user_agent = bot) { return 403;}
        # ", "zh_CN": "取值范围: <= 65530 字符 
        # 此字段可用来自定义边缘逻辑，控制负载均衡器的行为。支持使用 边缘逻辑指令中的部分指令。请参考'获取系统配置'接口中baseLbDirectives字段所列出的负载均衡基础指令。目前，这些基础指令包括'if'、'else'、'elseif'、'set'、'return'、'add_header'、'deny'、'allow'、'access_log_sampling'和'proxy_set_headers'。此外，我们还支持一些高级指令，请参考'获取系统配置'接口中advancedLbDirectives字段所列出的负载均衡高级指令。如果您需要使用这些高级指令，请联系技术支持。
        # 
        # <br/>示例：<br/>
        # 
        # if ($http_user_agent = bot) { return 403;}
        # "}
        self.load_balancer_logic = load_balancer_logic
        # {"en" : "Default: False 
        # Enable TLS zero round-trip time, a feature of TLS 1.3 that can improve performance for repeat visits to a site. If enabling it though, be sure your site is not vulnerable to the HTTP replay attack.", "zh_CN": "默认值: False 
        # 是否开启TLS 0-RTT功能。这是TLS 1.3版本支持的功能。启用该功能后，当用户频繁访问您的站点时，可提高访问响应速度。需要注意的是，启用该功能可能会加大站点遭受HTTP replay攻击的风险。"}
        self.tls_0rtt = tls_0rtt

    def validate(self):
        if self.real_time_log:
            self.real_time_log.validate()
        if self.origins:
            for k in self.origins:
                if k:
                    k.validate()
        if self.video_seek:
            self.video_seek.validate()
        if self.access_control_rules:
            for k in self.access_control_rules:
                if k:
                    k.validate()
        if self.extra_service_ports:
            self.extra_service_ports.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.cache_key_hostname is not None:
            result['cacheKeyHostname'] = self.cache_key_hostname
        if self.hostnames is not None:
            result['hostnames'] = self.hostnames
        if self.real_time_log is not None:
            result['realTimeLog'] = self.real_time_log.to_map()
        if self.edge_logic is not None:
            result['edgeLogic'] = self.edge_logic
        if self.has_beian is not None:
            result['hasBeian'] = self.has_beian
        if self.redirect_http_to_https is not None:
            result['redirectHttpToHttps'] = self.redirect_http_to_https
        if self.origins is not None:
            result['origins'] = []
            for k in self.origins:
                result['origins'].append(k.to_map() if k else None)
        if self.syntax_version is not None:
            result['syntaxVersion'] = self.syntax_version
        if self.disable_http_2 is not None:
            result['disableHttp2'] = self.disable_http_2
        if self.enable_http_3 is not None:
            result['enableHttp3'] = self.enable_http_3
        if self.scheme_in_cache_key is not None:
            result['schemeInCacheKey'] = self.scheme_in_cache_key
        if self.tls_max_version is not None:
            result['tlsMaxVersion'] = self.tls_max_version
        if self.load_balancer_hash_key is not None:
            result['loadBalancerHashKey'] = self.load_balancer_hash_key
        if self.tls_certificate_id is not None:
            result['tlsCertificateId'] = self.tls_certificate_id
        if self.tls_min_version is not None:
            result['tlsMinVersion'] = self.tls_min_version
        if self.tls_ciphers is not None:
            result['tlsCiphers'] = self.tls_ciphers
        if self.allow_protocol_downgrade is not None:
            result['allowProtocolDowngrade'] = self.allow_protocol_downgrade
        if self.tls_certificate_id_1 is not None:
            result['tlsCertificateId1'] = self.tls_certificate_id_1
        if self.video_seek is not None:
            result['videoSeek'] = self.video_seek.to_map()
        if self.tls_session_timeout is not None:
            result['tlsSessionTimeout'] = self.tls_session_timeout
        if self.enable_ocsp_stapling is not None:
            result['enableOcspStapling'] = self.enable_ocsp_stapling
        if self.beian_content_type is not None:
            result['beianContentType'] = self.beian_content_type
        if self.enable_ipv_6origin is not None:
            result['enableIpv6Origin'] = self.enable_ipv_6origin
        if self.follow_client_ip_version is not None:
            result['followClientIpVersion'] = self.follow_client_ip_version
        if self.access_control_rules is not None:
            result['accessControlRules'] = []
            for k in self.access_control_rules:
                result['accessControlRules'].append(k.to_map() if k else None)
        if self.disable_cert_automation is not None:
            result['disableCertAutomation'] = self.disable_cert_automation
        if self.cache_key_uri is not None:
            result['cacheKeyUri'] = self.cache_key_uri
        if self.extra_service_ports is not None:
            result['extraServicePorts'] = self.extra_service_ports.to_map()
        if self.load_balancer_logic is not None:
            result['loadBalancerLogic'] = self.load_balancer_logic
        if self.tls_0rtt is not None:
            result['tls0Rtt'] = self.tls_0rtt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('cacheKeyHostname') is not None:
            self.cache_key_hostname = m.get('cacheKeyHostname')
        if m.get('hostnames') is not None:
            self.hostnames = m.get('hostnames')
        if m.get('realTimeLog') is not None:
            temp_model = CreateAPropertyRequestVersionRealTimeLog()
            self.real_time_log = temp_model.from_map(m['realTimeLog'])
        if m.get('edgeLogic') is not None:
            self.edge_logic = m.get('edgeLogic')
        if m.get('hasBeian') is not None:
            self.has_beian = m.get('hasBeian')
        if m.get('redirectHttpToHttps') is not None:
            self.redirect_http_to_https = m.get('redirectHttpToHttps')
        if m.get('origins') is not None:
            self.origins = []
            for k in m.get('origins'):
                temp_model = CreateAPropertyRequestVersionOrigins()
                self.origins.append(temp_model.from_map(k))
        if m.get('syntaxVersion') is not None:
            self.syntax_version = m.get('syntaxVersion')
        if m.get('disableHttp2') is not None:
            self.disable_http_2 = m.get('disableHttp2')
        if m.get('enableHttp3') is not None:
            self.enable_http_3 = m.get('enableHttp3')
        if m.get('schemeInCacheKey') is not None:
            self.scheme_in_cache_key = m.get('schemeInCacheKey')
        if m.get('tlsMaxVersion') is not None:
            self.tls_max_version = m.get('tlsMaxVersion')
        if m.get('loadBalancerHashKey') is not None:
            self.load_balancer_hash_key = m.get('loadBalancerHashKey')
        if m.get('tlsCertificateId') is not None:
            self.tls_certificate_id = m.get('tlsCertificateId')
        if m.get('tlsMinVersion') is not None:
            self.tls_min_version = m.get('tlsMinVersion')
        if m.get('tlsCiphers') is not None:
            self.tls_ciphers = m.get('tlsCiphers')
        if m.get('allowProtocolDowngrade') is not None:
            self.allow_protocol_downgrade = m.get('allowProtocolDowngrade')
        if m.get('tlsCertificateId1') is not None:
            self.tls_certificate_id_1 = m.get('tlsCertificateId1')
        if m.get('videoSeek') is not None:
            temp_model = CreateAPropertyRequestVersionVideoSeek()
            self.video_seek = temp_model.from_map(m['videoSeek'])
        if m.get('tlsSessionTimeout') is not None:
            self.tls_session_timeout = m.get('tlsSessionTimeout')
        if m.get('enableOcspStapling') is not None:
            self.enable_ocsp_stapling = m.get('enableOcspStapling')
        if m.get('beianContentType') is not None:
            self.beian_content_type = m.get('beianContentType')
        if m.get('enableIpv6Origin') is not None:
            self.enable_ipv_6origin = m.get('enableIpv6Origin')
        if m.get('followClientIpVersion') is not None:
            self.follow_client_ip_version = m.get('followClientIpVersion')
        if m.get('accessControlRules') is not None:
            self.access_control_rules = []
            for k in m.get('accessControlRules'):
                temp_model = CreateAPropertyRequestVersionAccessControlRules()
                self.access_control_rules.append(temp_model.from_map(k))
        if m.get('disableCertAutomation') is not None:
            self.disable_cert_automation = m.get('disableCertAutomation')
        if m.get('cacheKeyUri') is not None:
            self.cache_key_uri = m.get('cacheKeyUri')
        if m.get('extraServicePorts') is not None:
            temp_model = CreateAPropertyRequestVersionExtraServicePorts()
            self.extra_service_ports = temp_model.from_map(m['extraServicePorts'])
        if m.get('loadBalancerLogic') is not None:
            self.load_balancer_logic = m.get('loadBalancerLogic')
        if m.get('tls0Rtt') is not None:
            self.tls_0rtt = m.get('tls0Rtt')
        return self


class CreateAPropertyRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        legacy_type: str = None,
        description: str = None,
        version: CreateAPropertyRequestVersion = None,
    ):
        # {"en" : "Name of the property.", "zh_CN": "加速项目的名称。"}
        self.name = name
        # {"en" : " Service type, one of wsapro, webpro, vodpro , downloadpro , 1523.", "zh_CN": "取值范围: wsapro,webpro,vodpro,downloadpro 
        # 服务类型，即全站加速，网页加速，点播加速及下载加速。"}
        self.legacy_type = legacy_type
        # {"en" : "Range: <= 250 characters 
        # Description of the property.", "zh_CN": "取值范围: <= 250 字符 
        # 加速项目的描述。"}
        self.description = description
        # {"en" : "Describes a property configuration. This contains all the settings.", "zh_CN": "描述加速项目的所有配置信息。"}
        self.version = version

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.legacy_type, 'legacy_type')
        self.validate_required(self.version, 'version')
        if self.version:
            self.version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.legacy_type is not None:
            result['legacyType'] = self.legacy_type
        if self.description is not None:
            result['description'] = self.description
        if self.version is not None:
            result['version'] = self.version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('legacyType') is not None:
            self.legacy_type = m.get('legacyType')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('version') is not None:
            temp_model = CreateAPropertyRequestVersion()
            self.version = temp_model.from_map(m['version'])
        return self


class CreateAPropertyResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAPropertyResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"Refers to the new property URL.", "zh_CN":"通过Location响应头返回新建的加速项目的URL。URL中包含加速项目ID。可使用该ID调用'查询加速项目的基础信息及版本信息'接口来查看加速项目详情。URL示例：<code>Location: http://open.chinanetcenter.com/cdn/properties/5dwa2205f9e9cc0001df7b24</code>"}
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




