# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class UpdateASecretPaths(TeaModel):
    def __init__(
        self,
        secret_id: str = None,
    ):
        # {"en" : "ID of a secret.", "zh_CN": "保密信息id。"}
        self.secret_id = secret_id

    def validate(self):
        self.validate_required(self.secret_id, 'secret_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_id is not None:
            result['secretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('secretId') is not None:
            self.secret_id = m.get('secretId')
        return self


class UpdateASecretParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateASecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateASecretRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        secret: str = None,
    ):
        # {"en" : "Range: [ 1 .. 30 ] characters ^[A-Za-z0-9_.-]+\
        # Name of the secret. It can consist of letters, numbers, hyphens, underscores, and periods. Refer to this in your Edge Logic using the $SECRET(secretName) syntax. If you change the name, property versions referring to the old name will not pass future validation.", "zh_CN": "取值范围: [ 1 .. 30 ] 字符 ^[A-Za-z0-9_.-]+\
        # 保密信息的名称。可以由字母、数字、连字符、下划线和句点组成。在边缘逻辑中使用$SECRET(secretName) 语法引用。如果您修改了保密信息的名称，那么以原有名称引用保密信息的加速项目版本将无法通过验证。"}
        self.name = name
        # {"en" : "Range: <= 250 characters 
        # A description of the secret. This may be useful for recording the purpose of the secret.", "zh_CN": "取值范围: <= 250 字符 
        # 保密信息的描述。"}
        self.description = description
        # {"en" : "Range: [ 8 .. 3599 ] characters 
        # The sensitive text you want to protect. The secret can consist of printable ASCII characters along with the tab, newline, and return characters. When you deploy your property, references to $SECRET(secretName) in your Edge Logic will be replaced by this text. Once the property is deployed, it will use the value of the secret at that time. If you change the secret's value and want your property to use the new value, you must revalidate and redeploy the property.", "zh_CN": "取值范围: [ 8 .. 3599 ] 字符 
        # 保密信息存放的敏感内容。可以包含可打印的ASCII字符、制表符(0x09)、换行符(0x0a) 和回车符(0x0d)。保密信息更新后，在已部署加速项目中已引用的保密信息不会自动被更新。如果您修改了保密信息存放的内容，必须重新验证并部署，加速项目才能使用到最新的值。"}
        self.secret = secret

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.secret is not None:
            result['secret'] = self.secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        return self


class UpdateASecretResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateASecretResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetASecretPaths(TeaModel):
    def __init__(
        self,
        secret_id: str = None,
    ):
        # {"en" : "ID of a secret.", "zh_CN": "保密信息id。"}
        self.secret_id = secret_id

    def validate(self):
        self.validate_required(self.secret_id, 'secret_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_id is not None:
            result['secretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('secretId') is not None:
            self.secret_id = m.get('secretId')
        return self


class GetASecretParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASecretRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASecretResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetASecretResponseUsageInProduction(TeaModel):
    def __init__(
        self,
        property_id: str = None,
    ):
        # {"en" : "ID of a property using the secret.", "zh_CN": "引用此保密信息的加速项目ID。"}
        self.property_id = property_id

    def validate(self):
        pass

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


class GetASecretResponseUsageInStaging(TeaModel):
    def __init__(
        self,
        property_id: str = None,
    ):
        # {"en" : "ID of a property using the secret.", "zh_CN": "引用此保密信息的加速项目ID。"}
        self.property_id = property_id

    def validate(self):
        pass

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


class GetASecretResponse(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        description: str = None,
        secret: str = None,
        last_update_time: str = None,
        creation_time: str = None,
        usage_in_production: List[GetASecretResponseUsageInProduction] = None,
        usage_in_staging: List[GetASecretResponseUsageInStaging] = None,
    ):
        # {"en" : "ID of the secret.", "zh_CN": "保密信息ID。"}
        self.id = id
        # {"en" : "Range: [ 1 .. 30 ] characters ^[A-Za-z0-9_.-]+\
        # Name of the secret. It can consist of letters, numbers, hyphens, underscores, and periods. Refer to this in your Edge Logic using the $SECRET(secretName) syntax.", "zh_CN": "取值范围: [ 1 .. 30 ] 字符 ^[A-Za-z0-9_.-]+\
        # 保密信息的名称。可以由字母、数字、连字符、下划线和句点组成。在边缘逻辑中使用$SECRET(secretName) 语法引用。"}
        self.name = name
        # {"en" : "Range: <= 250 characters 
        # Description of the secret.", "zh_CN": "取值范围: <= 250 字符 
        # 保密信息的描述。"}
        self.description = description
        # {"en" : "Range: [ 8 .. 3599 ] characters 
        # The value of the secret. The secret can consist of printable ASCII characters along with the tab, newline, and return characters. For security, we will not show all the characters. The middle of the secret will be masked out by asterisk characters. References to $SECRET(secretName) in your Edge Logic will be replaced by the value.", "zh_CN": "取值范围: [ 8 .. 3599 ] 字符 
        # 保密信息存放的敏感内容。可以包含可打印的ASCII字符、制表符(0x09)、换行符(0x0a) 和回车符(0x0d)。出于安全考虑，此处不显示所有字符，部分内容将用星号标记。"}
        self.secret = secret
        # {"en" : "An RFC 3339 date indicating when the secret was last updated, for example, '2021-07-06T00:00:00Z'.", "zh_CN": "RFC 3339格式的日期，表示保密信息的最后一次更新时间。例如，'2021-07-06T00:00:00Z'。"}
        self.last_update_time = last_update_time
        # {"en" : "An RFC 3339 date indicating when the secret was created. This will be in UTC time, for example, '2021-07-06T00:00:00Z'.", "zh_CN": "RFC 3339格式的日期，表示保密信息的创建时间，使用UTC时区。例如，'2021-07-06T00:00:00Z'。"}
        self.creation_time = creation_time
        # {"en" : "Properties deployed to production that refer to the secret.", "zh_CN": "保密信息在生产环境中的使用情况。"}
        self.usage_in_production = usage_in_production
        # {"en" : "Properties deployed to staging that refer to the secret.", "zh_CN": "保密信息在演练环境中的使用情况。"}
        self.usage_in_staging = usage_in_staging

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.secret, 'secret')
        self.validate_required(self.last_update_time, 'last_update_time')
        self.validate_required(self.creation_time, 'creation_time')
        self.validate_required(self.usage_in_production, 'usage_in_production')
        if self.usage_in_production:
            for k in self.usage_in_production:
                if k:
                    k.validate()
        self.validate_required(self.usage_in_staging, 'usage_in_staging')
        if self.usage_in_staging:
            for k in self.usage_in_staging:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.secret is not None:
            result['secret'] = self.secret
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.usage_in_production is not None:
            result['usageInProduction'] = []
            for k in self.usage_in_production:
                result['usageInProduction'].append(k.to_map() if k else None)
        if self.usage_in_staging is not None:
            result['usageInStaging'] = []
            for k in self.usage_in_staging:
                result['usageInStaging'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('usageInProduction') is not None:
            self.usage_in_production = []
            for k in m.get('usageInProduction'):
                temp_model = GetASecretResponseUsageInProduction()
                self.usage_in_production.append(temp_model.from_map(k))
        if m.get('usageInStaging') is not None:
            self.usage_in_staging = []
            for k in m.get('usageInStaging'):
                temp_model = GetASecretResponseUsageInStaging()
                self.usage_in_staging.append(temp_model.from_map(k))
        return self






class DeleteASecretPaths(TeaModel):
    def __init__(
        self,
        secret_id: str = None,
    ):
        # {"en" : "ID of a secret.", "zh_CN": "保密信息id。"}
        self.secret_id = secret_id

    def validate(self):
        self.validate_required(self.secret_id, 'secret_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.secret_id is not None:
            result['secretId'] = self.secret_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('secretId') is not None:
            self.secret_id = m.get('secretId')
        return self


class DeleteASecretParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteASecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteASecretRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteASecretResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteASecretResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetAListOfSecretsPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfSecretsParameters(TeaModel):
    def __init__(
        self,
        offset: int = None,
        limit: int = None,
        search: str = None,
    ):
        # {"en" : "Default: 0 Range: >= 0 
        # Index of the first secret to return.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Default: 100 Range: [ 1 .. 200 ] 
        # Maximum number of secrets to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit
        # {"en" : "The value of the search parameter is matched on the id, name, and description fields of the secrets. Partial matches are supported.", "zh_CN": "根据搜索关键字匹配保密信息的ID，名称和描述进行查询。"}
        self.search = search

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
        if self.search is not None:
            result['search'] = self.search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('search') is not None:
            self.search = m.get('search')
        return self


class GetAListOfSecretsRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfSecretsRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfSecretsResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfSecretsResponseSecrets(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        description: str = None,
        creation_time: str = None,
        last_update_time: str = None,
    ):
        # {"en" : "ID of a secret.", "zh_CN": "保密信息ID。"}
        self.id = id
        # {"en" : "Range: [ 1 .. 30 ] characters ^[A-Za-z0-9_.-]+\
        # Name of the secret. It can consist of letters, numbers, hyphens, underscores, and periods. Refer to this in your Edge Logic as $SECRET(secretName).", "zh_CN": "取值范围: [ 1 .. 30 ] 字符 ^[A-Za-z0-9_.-]+\
        # 保密信息的名称。可以由字母、数字、连字符、下划线和句点组成。在边缘逻辑中使用$SECRET(secretName) 语法引用。"}
        self.name = name
        # {"en" : "Range: <= 250 characters 
        # A description of the secret.", "zh_CN": "取值范围: <= 250 字符 
        # 保密信息的描述。"}
        self.description = description
        # {"en" : "An RFC 3339 date indicating when the secret was created. This will be in UTC time, for example, '2021-07-06T00:00:00Z'.
        # ", "zh_CN": "RFC 3339格式的日期，表示保密信息的创建时间，使用UTC时区。例如，'2021-07-06T00:00:00Z'。"}
        self.creation_time = creation_time
        # {"en" : "An RFC 3339 date indicating when the secret was last updated, for example, '2021-07-06T00:00:00Z'.
        # ", "zh_CN": "RFC 3339格式的日期，表示保密信息的最后一次更新时间。例如，'2021-07-06T00:00:00Z'。"}
        self.last_update_time = last_update_time

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
        if self.description is not None:
            result['description'] = self.description
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.last_update_time is not None:
            result['lastUpdateTime'] = self.last_update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('lastUpdateTime') is not None:
            self.last_update_time = m.get('lastUpdateTime')
        return self


class GetAListOfSecretsResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        secrets: List[GetAListOfSecretsResponseSecrets] = None,
    ):
        # {"en" : "Range: >= 0 
        # Total number of secrets. The actual number returned in the secrets field of the response will depend on the limit and offset parameters.", "zh_CN": "取值范围: >= 0 
        # 保密信息的总数。返回的实际数量取决于查询参数。"}
        self.count = count
        # {"en" : "A list of secrets.", "zh_CN": "保密信息列表。"}
        self.secrets = secrets

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.secrets, 'secrets')
        if self.secrets:
            for k in self.secrets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.secrets is not None:
            result['secrets'] = []
            for k in self.secrets:
                result['secrets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('secrets') is not None:
            self.secrets = []
            for k in m.get('secrets'):
                temp_model = GetAListOfSecretsResponseSecrets()
                self.secrets.append(temp_model.from_map(k))
        return self






class CreateASecretPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateASecretParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateASecretRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateASecretRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        secret: str = None,
    ):
        # {"en" : "Range: [ 1 .. 30 ] characters ^[A-Za-z0-9_.-]+\
        # The name of the secret. It can consist of letters, numbers, hyphens, underscores, and periods. Refer to this in your Edge Logic using the $SECRET(secretName) syntax.", "zh_CN": "取值范围: [ 1 .. 30 ] 字符 ^[A-Za-z0-9_.-]+\
        # 保密信息的名称。可以由字母、数字、连字符、下划线和句点组成。在边缘逻辑中使用$SECRET(secretName) 语法来引用。"}
        self.name = name
        # {"en" : "Range: <= 250 characters 
        # A description of the secret. This may be useful for recording the purpose of the secret.", "zh_CN": "取值范围: <= 250 字符 
        # 保密信息的描述。"}
        self.description = description
        # {"en" : "Range: [ 8 .. 3599 ] characters 
        # The sensitive text you want to protect. When you deploy your property, references to $SECRET(secretName) in your Edge Logic will be replaced by this text. The secret can consist of printable ASCII characters along with the tab, newline, and return characters.", "zh_CN": "取值范围: [ 8 .. 3599 ] 字符 
        # 需要被保护的敏感内容。当部署加速项目时，将对边缘逻辑中的 $SECRET(secretName)进行解析，提取出敏感内容。支持可打印的ASCII字符、制表符(0x09)、换行符(0x0a) 和回车符(0x0d)。"}
        self.secret = secret

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.secret, 'secret')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.secret is not None:
            result['secret'] = self.secret
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        return self


class CreateASecretResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateASecretResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"The location header contains a reference to the new secret's ID.", "zh_CN":"通过Location响应头返回新建的保密信息的URL。URL中包含保密信息的ID，可使用该ID调用‘获取保密信息详请’接口来查看保密信息的详请。URL示例：<code>Location: https://openapi.chinanetcenter.com/cdn/secrets/60d6707cca3e387d2a28fc9e</code>。"}
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




