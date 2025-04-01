# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class DeletePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # {"en":"Policy ID. Only supports deleting custom permission policies.", "zh_CN":"策略ID。仅支持删除自定义权限策略"}
        self.policy_id = policy_id

    def validate(self):
        self.validate_required(self.policy_id, 'policy_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self


class DeletePolicyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DeletePolicyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeletePolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EditPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        policy_name: str = None,
        description: str = None,
        policy_document: str = None,
    ):
        # {"en":"The ID of the policy to be modified.", "zh_CN":"要修改的策略id"}
        self.policy_id = policy_id
        # {"en":"The name of the policy to be modified..Not passing means no modification.", "zh_CN":"要修改的策略名称。不传代表不修改。"}
        self.policy_name = policy_name
        # {"en":"Policy description. You may describe the strategy here, including permission details, limited to a maximum of 250 characters.Not passing means no modification.", "zh_CN":"修改后策略描述。可在此用文字简单描述策略包含权限内容，限制最多250字符。不传代表不修改。"}
        self.description = description
        # {"en":"Permission policy content, not passing means no modification. please fill in the permission policy script as follows:
        # 
        # 
        # [{
        #         \"effect\": \"allow\",
        #         \"action\": [
        #            \"productCode:actionCode\"
        #         ],
        #        \"resource\": [
        #            \"*\"
        #         ]
        #     }]
        # 
        # 
        # A single permission policy can include permissions for multiple products, but CDN and non-CDN product permissions cannot be added to the same policy simultaneously.
        # 
        # Field descriptions:
        # 
        # -effect: The authorization effect includes two types: allow and deny.
        # 
        # -action: Describes the specific operations allowed or denied,  format: productCode:actionCode.
        # 
        # -resource: The specific resources authorized. For all resources use *, for specific resources refer to the format: wsc:&lt;service-name&gt;:&lt;region&gt;:&lt;account&gt;:&lt;relatice-id&gt;. Note: CDN products do not support specifying resources.", "zh_CN":"	
        # 修改后权限策略内容，不传代表不修改。请填写权限策略脚本，示例如下：
        # 
        # [{
        #         \"effect\": \"allow\",
        #         \"action\": [
        #            \"productCode:actionCode\"
        #         ],
        #        \"resource\": [
        #            \"*\"
        #         ]
        #     }]
        # 
        # 一个权限策略内可以包含多个产品的权限策略，但CDN和非CDN类产品权限不能同时添加到同一个策略里。
        # 
        # 各字段说明：
        # 
        # -effect：授权效果包括两种允许（allow）和拒绝（deny）
        # 
        # -action：描述允许或拒绝的特定操作，格式：productCode:actionCode
        # 
        # -resource：授权的具体资源对象。若是全部资源用*表示，若是指定资源参考格式：wsc:&lt;service-name&gt;:&lt;region&gt;:&lt;account&gt;:&lt;relatice-id&gt;。注意：CDN类产品不支持指定资源"}
        self.policy_document = policy_document

    def validate(self):
        self.validate_required(self.policy_id, 'policy_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.description is not None:
            result['description'] = self.description
        if self.policy_document is not None:
            result['policyDocument'] = self.policy_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('policyDocument') is not None:
            self.policy_document = m.get('policyDocument')
        return self


class EditPolicyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class EditPolicyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetPolicyRequest(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # {"en":"Policy ID", "zh_CN":"策略ID"}
        self.policy_id = policy_id

    def validate(self):
        self.validate_required(self.policy_id, 'policy_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self


class GetPolicyResponseData(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
        policy_name: str = None,
        description: str = None,
        type: str = None,
        policy_document: str = None,
    ):
        # {"en":"Policy ID", "zh_CN":"策略ID"}
        self.policy_id = policy_id
        # {"en":"Policy name", "zh_CN":"策略名称"}
        self.policy_name = policy_name
        # {"en":"Policy description", "zh_CN":"策略描述"}
        self.description = description
        # {"en":"Policy type: custom represents a custom Policy , system represents a system global Policy", "zh_CN":"策略类型：custom代表自定义策略  system代表系统策略"}
        self.type = type
        # {"en":"Permission policy content, as follows:
        # 
        # [{
        #         \"effect\": \"allow\",
        #         \"action\": [
        #            \"productCode:actionCode\"
        #         ],
        #        \"resource\": [
        #            \"*\"
        #         ]
        #     }]
        # 
        # Field descriptions:
        # 
        # -effect: The authorization effect includes two types: allow and deny.
        # 
        # -action: Describes the specific operations allowed or denied,  format: productCode:actionCode.
        # 
        # -resource: The specific resources authorized. For all resources use *, for specific resources refer to the format: wsc:&lt;service-name&gt;:&lt;region&gt;:&lt;account&gt;:&lt;relatice-id&gt;. Note: CDN products do not support specifying resources.", "zh_CN":"策略权限描述，示例如下：
        # 
        # [{
        #         \"effect\": \"allow\",
        #         \"action\": [
        #            \"productCode:actionCode\"
        #         ],
        #        \"resource\": [
        #            \"*\"
        #         ]
        #     }]
        # 
        # 各字段说明：
        # 
        # -effect：授权效果包括两种允许（allow）和拒绝（deny）
        # 
        # -action：描述允许或拒绝的特定操作，格式：productCode:actionCode
        # 
        # -resource：授权的具体资源对象。若是全部资源用*表示，若是指定资源参考格式：wsc:&lt;service-name&gt;:&lt;region&gt;:&lt;account&gt;:&lt;relatice-id&gt;。注意：CDN类产品不支持指定资源"}
        self.policy_document = policy_document

    def validate(self):
        self.validate_required(self.policy_id, 'policy_id')
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.type, 'type')
        self.validate_required(self.policy_document, 'policy_document')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.description is not None:
            result['description'] = self.description
        if self.type is not None:
            result['type'] = self.type
        if self.policy_document is not None:
            result['policyDocument'] = self.policy_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('policyDocument') is not None:
            self.policy_document = m.get('policyDocument')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: GetPolicyResponseData = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.message = message
        # {"en":"Detailed data on the results of the request", "zh_CN":"请求结果的详细数据"}
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
            temp_model = GetPolicyResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetPolicyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetPolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreatePolicyRequest(TeaModel):
    def __init__(
        self,
        policy_name: str = None,
        description: str = None,
        policy_document: str = None,
    ):
        # {"en":"Policy Name. Supports Chinese, English, and underline, with no more than 150 characters", "zh_CN":"策略名称，支持中文、英文和下划线，不超过150字符"}
        self.policy_name = policy_name
        # {"en":"Policy description. You may describe the strategy here, including permission details, limited to a maximum of 250 characters.", "zh_CN":"策略描述。可在此用文字简单描述策略包含权限内容，限制最多250字符"}
        self.description = description
        # {"en":"Permission policy content, please fill in the permission policy script as follows:
        # 
        # 
        # [{
        #         \"effect\": \"allow\",
        #         \"action\": [
        #            \"productCode:actionCode\"
        #         ],
        #        \"resource\": [
        #            \"*\"
        #         ]
        #     }]
        # 
        # 
        # A single permission policy can include permissions for multiple products, but CDN and non-CDN product permissions cannot be added to the same policy simultaneously.
        # 
        # Field descriptions:
        # 
        # -effect: The authorization effect includes two types: allow and deny.
        # 
        # -action: Describes the specific operations allowed or denied,  format: productCode:actionCode.
        # 
        # -resource: The specific resources authorized. For all resources use *, for specific resources refer to the format: wsc:&lt;service-name&gt;:&lt;region&gt;:&lt;account&gt;:&lt;relatice-id&gt;. Note: CDN products do not support specifying resources.", "zh_CN":"权限策略内容，请填写权限策略脚本，示例如下：
        # 
        # [{
        #         \"effect\": \"allow\",
        #         \"action\": [
        #            \"productCode:actionCode\"
        #         ],
        #        \"resource\": [
        #            \"*\"
        #         ]
        #     }]
        # 
        # 一个权限策略内可以包含多个产品的权限策略，但CDN和非CDN类产品权限不能同时添加到同一个策略里。
        # 
        # 各字段说明：
        # 
        # -effect：授权效果包括两种允许（allow）和拒绝（deny）
        # 
        # -action：描述允许或拒绝的特定操作，格式：productCode:actionCode
        # 
        # -resource：授权的具体资源对象。若是全部资源用*表示，若是指定资源参考格式：wsc:&lt;service-name&gt;:&lt;region&gt;:&lt;account&gt;:&lt;relatice-id&gt;。注意：CDN类产品不支持指定资源"}
        self.policy_document = policy_document

    def validate(self):
        self.validate_required(self.policy_name, 'policy_name')
        self.validate_required(self.policy_document, 'policy_document')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.description is not None:
            result['description'] = self.description
        if self.policy_document is not None:
            result['policyDocument'] = self.policy_document
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('policyDocument') is not None:
            self.policy_document = m.get('policyDocument')
        return self


class CreatePolicyResponseData(TeaModel):
    def __init__(
        self,
        policy_id: str = None,
    ):
        # {"en":"Policy ID", "zh_CN":"策略ID"}
        self.policy_id = policy_id

    def validate(self):
        self.validate_required(self.policy_id, 'policy_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_id is not None:
            result['policyId'] = self.policy_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyId') is not None:
            self.policy_id = m.get('policyId')
        return self


class CreatePolicyResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        data: CreatePolicyResponseData = None,
    ):
        # {"en":"request result status code", "zh_CN":"请求结果状态码"}
        self.code = code
        # {"en":"Request result information", "zh_CN":"请求结果信息"}
        self.msg = msg
        # {"en":"Detailed data on the results of the request", "zh_CN":"请求结果的详细数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.msg, 'msg')
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
        if self.data is not None:
            result['data'] = self.data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('data') is not None:
            temp_model = CreatePolicyResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class CreatePolicyPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePolicyParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePolicyRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreatePolicyResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




