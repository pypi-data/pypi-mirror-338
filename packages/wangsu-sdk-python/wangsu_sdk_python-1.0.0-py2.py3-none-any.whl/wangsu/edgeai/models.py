# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class EnableDisableFileRequest(TeaModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        file_ids: List[str] = None,
        enable: bool = None,
    ):
        # {"en":"knowledgeId", "zh_CN":"知识库id"}
        self.knowledge_base_id = knowledge_base_id
        # {"en":"fileIds", "zh_CN":"文件id列表"}
        self.file_ids = file_ids
        # {"en":"isEnable", "zh_CN":"是否启用"}
        self.enable = enable

    def validate(self):
        self.validate_required(self.knowledge_base_id, 'knowledge_base_id')
        self.validate_required(self.file_ids, 'file_ids')
        self.validate_required(self.enable, 'enable')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_base_id is not None:
            result['knowledgeBaseId'] = self.knowledge_base_id
        if self.file_ids is not None:
            result['fileIds'] = self.file_ids
        if self.enable is not None:
            result['enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('knowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('knowledgeBaseId')
        if m.get('fileIds') is not None:
            self.file_ids = m.get('fileIds')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        return self


class EnableDisableFileResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        messgae: str = None,
    ):
        # {"en":"code", "zh_CN":"响应码"}
        self.code = code
        # {"en":"message", "zh_CN":"响应信息"}
        self.messgae = messgae

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.messgae, 'messgae')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.messgae is not None:
            result['messgae'] = self.messgae
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('messgae') is not None:
            self.messgae = m.get('messgae')
        return self


class EnableDisableFilePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableDisableFileParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableDisableFileRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EnableDisableFileResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RagKnowledgeBaseListServiceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # {"en":"knowledge base name","zh_CN":"知识库名称"}
        self.name = name
        # {"en":"page num","zh_CN":"页数"}
        self.page_no = page_no
        # {"en":"page size","zh_CN":"页大小"}
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class RagKnowledgeBaseListServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseListServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseListServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseListServiceResponseData(TeaModel):
    def __init__(
        self,
        last_updated: str = None,
        size: int = None,
        create_time: str = None,
        name: str = None,
        description: str = None,
        id: str = None,
    ):
        # {"en":"last update time","zh_CN":"最近更新时间"}
        self.last_updated = last_updated
        # {"en":"size","zh_CN":"知识库大小"}
        self.size = size
        # {"en":"create time","zh_CN":"创建时间"}
        self.create_time = create_time
        # {"en":"knowledge base name","zh_CN":"知识库名称"}
        self.name = name
        # {"en":"knowledge base desc","zh_CN":"知识库描述"}
        self.description = description
        # {"en":"knowledge base id","zh_CN":"知识库 id"}
        self.id = id

    def validate(self):
        self.validate_required(self.last_updated, 'last_updated')
        self.validate_required(self.size, 'size')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_updated is not None:
            result['lastUpdated'] = self.last_updated
        if self.size is not None:
            result['size'] = self.size
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('lastUpdated') is not None:
            self.last_updated = m.get('lastUpdated')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class RagKnowledgeBaseListServiceResponse(TeaModel):
    def __init__(
        self,
        total: int = None,
        code: int = None,
        data: List[RagKnowledgeBaseListServiceResponseData] = None,
        message: str = None,
    ):
        # {"en":"total","zh_CN":"总数"}
        self.total = total
        # {"en":"code","zh_CN":"响应码"}
        self.code = code
        # {"en":"array","zh_CN":"数组"}
        self.data = data
        # {"en":"message","zh_CN":"响应描述"}
        self.message = message

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            for k in self.data:
                if k:
                    k.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = RagKnowledgeBaseListServiceResponseData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class RagKnowledgeBaseListServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RagFileDeleteServiceRequest(TeaModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        file_ids: List[str] = None,
    ):
        # {"en":"knowledge base id","zh_CN":"知识库 ID"}
        self.knowledge_base_id = knowledge_base_id
        # {"en":"file id list","zh_CN":"文件 id列表"}
        self.file_ids = file_ids

    def validate(self):
        self.validate_required(self.knowledge_base_id, 'knowledge_base_id')
        self.validate_required(self.file_ids, 'file_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_base_id is not None:
            result['knowledgeBaseId'] = self.knowledge_base_id
        if self.file_ids is not None:
            result['fileIds'] = self.file_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('knowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('knowledgeBaseId')
        if m.get('fileIds') is not None:
            self.file_ids = m.get('fileIds')
        return self


class RagFileDeleteServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagFileDeleteServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagFileDeleteServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagFileDeleteServiceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"code","zh_CN":"响应码"}
        self.code = code
        # {"en":"message","zh_CN":"响应信息"}
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


class RagFileDeleteServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RagKnowledgeBaseDeleteServiceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en":"knowledge base id","zh_CN":"知识库 id"}
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


class RagKnowledgeBaseDeleteServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseDeleteServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseDeleteServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseDeleteServiceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"code","zh_CN":"响应码"}
        self.code = code
        # {"en":"message","zh_CN":"响应信息"}
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


class RagKnowledgeBaseDeleteServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class ListRagFileRequest(TeaModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        file_name: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # {"en":"knowledge id", "zh_CN":"知识库id"}
        self.knowledge_base_id = knowledge_base_id
        # {"en":"fileName", "zh_CN":"文件名"}
        self.file_name = file_name
        # {"en":"pageNo", "zh_CN":"第几页"}
        self.page_no = page_no
        # {"en":"pageSize", "zh_CN":"每页大小"}
        self.page_size = page_size

    def validate(self):
        self.validate_required(self.knowledge_base_id, 'knowledge_base_id')
        self.validate_required(self.page_no, 'page_no')
        self.validate_required(self.page_size, 'page_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_base_id is not None:
            result['knowledgeBaseId'] = self.knowledge_base_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.page_no is not None:
            result['pageNo'] = self.page_no
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('knowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('knowledgeBaseId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('pageNo') is not None:
            self.page_no = m.get('pageNo')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListRagFileResponse(TeaModel):
    def __init__(
        self,
        total: int = None,
        code: int = None,
        data: List[str] = None,
        last_updated: str = None,
        file_name: str = None,
        size: int = None,
        is_enabled: bool = None,
        file_id: str = None,
        status: int = None,
        message: str = None,
    ):
        # {"en":"total", "zh_CN":"总数"}
        self.total = total
        # {"en":"code", "zh_CN":"响应码"}
        self.code = code
        # {"en":"", "zh_CN":""}
        self.data = data
        # {"en":"update time", "zh_CN":"更新时间"}
        self.last_updated = last_updated
        # {"en":"file name", "zh_CN":"文件名"}
        self.file_name = file_name
        # {"en":"file size", "zh_CN":"文件大小"}
        self.size = size
        # {"en":"isEnabled", "zh_CN":"是否启用"}
        self.is_enabled = is_enabled
        # {"en":"fileId", "zh_CN":"文件id"}
        self.file_id = file_id
        # {"en":"status", "zh_CN":"0:失败,1:成功,2:处理中"}
        self.status = status
        # {"en":"message", "zh_CN":"响应信息"}
        self.message = message

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        self.validate_required(self.last_updated, 'last_updated')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.size, 'size')
        self.validate_required(self.is_enabled, 'is_enabled')
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.status, 'status')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.last_updated is not None:
            result['lastUpdated'] = self.last_updated
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.size is not None:
            result['size'] = self.size
        if self.is_enabled is not None:
            result['isEnabled'] = self.is_enabled
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.status is not None:
            result['status'] = self.status
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('lastUpdated') is not None:
            self.last_updated = m.get('lastUpdated')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('isEnabled') is not None:
            self.is_enabled = m.get('isEnabled')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListRagFilePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListRagFileParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListRagFileRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ListRagFileResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateRagFileRequest(TeaModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        file_name: str = None,
        content: str = None,
    ):
        # {"en":"knowledge id", "zh_CN":"知识库id"}
        self.knowledge_base_id = knowledge_base_id
        # {"en":"file name,Maximum Length 255", "zh_CN":"文件名，最大长度 255"}
        self.file_name = file_name
        # {"en":"file content after Base64 encode", "zh_CN":"文件内容Base64 encode "}
        self.content = content

    def validate(self):
        self.validate_required(self.knowledge_base_id, 'knowledge_base_id')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.content, 'content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_base_id is not None:
            result['knowledgeBaseId'] = self.knowledge_base_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('knowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('knowledgeBaseId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class CreateRagFileResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        id: str = None,
        message: str = None,
    ):
        # {"en":"code", "zh_CN":"响应码"}
        self.code = code
        # {"en":"file id", "zh_CN":"文件id"}
        self.id = id
        # {"en":"message", "zh_CN":"响应信息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.id, 'id')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class CreateRagFilePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateRagFileParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateRagFileRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateRagFileResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RagKnowledgeBaseCreateServiceRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
    ):
        # {"en":"name,Maximum Length 100","zh_CN":"知识库名称，最大长度 100"}
        self.name = name
        # {"en":"description,Maximum Length 500","zh_CN":"知识库描述，最大长度 500"}
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


class RagKnowledgeBaseCreateServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseCreateServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseCreateServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseCreateServiceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        id: str = None,
        message: str = None,
    ):
        # {"en":"code","zh_CN":"响应码"}
        self.code = code
        # {"en":"knowledge base id","zh_CN":"知识库 ID"}
        self.id = id
        # {"en":"message","zh_CN":"响应信息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.id, 'id')
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.id is not None:
            result['id'] = self.id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class RagKnowledgeBaseCreateServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class RagKnowledgeBaseUpdateServiceRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        description: str = None,
    ):
        # {"en":"knowledge base id","zh_CN":"知识库 id"}
        self.id = id
        # {"en":"knowledge base name, Maximum Length 100","zh_CN":"知识库名称，最大长度100"}
        self.name = name
        # {"en":"knowledge base description, Maximum Length 500","zh_CN":"知识库描述，最大长度 500"}
        self.description = description

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class RagKnowledgeBaseUpdateServiceRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseUpdateServicePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseUpdateServiceParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class RagKnowledgeBaseUpdateServiceResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"code","zh_CN":"响应码"}
        self.code = code
        # {"en":"message","zh_CN":"响应信息"}
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


class RagKnowledgeBaseUpdateServiceResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdatefileRequest(TeaModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        file_id: str = None,
        file_name: str = None,
        content: str = None,
    ):
        # {"en":"knowledge id", "zh_CN":"知识库id"}
        self.knowledge_base_id = knowledge_base_id
        # {"en":"file id", "zh_CN":"文件id"}
        self.file_id = file_id
        # {"en":"file name", "zh_CN":"文件名文件名，最大长度255"}
        self.file_name = file_name
        # {"en":"file content after Base64 encode", "zh_CN":"文件内容Base64 encode"}
        self.content = content

    def validate(self):
        self.validate_required(self.knowledge_base_id, 'knowledge_base_id')
        self.validate_required(self.file_id, 'file_id')
        self.validate_required(self.file_name, 'file_name')
        self.validate_required(self.content, 'content')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.knowledge_base_id is not None:
            result['knowledgeBaseId'] = self.knowledge_base_id
        if self.file_id is not None:
            result['fileId'] = self.file_id
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.content is not None:
            result['content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('knowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('knowledgeBaseId')
        if m.get('fileId') is not None:
            self.file_id = m.get('fileId')
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('content') is not None:
            self.content = m.get('content')
        return self


class UpdatefileResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"code", "zh_CN":"响应码"}
        self.code = code
        # {"en":"message", "zh_CN":"响应信息"}
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


class UpdatefilePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdatefileParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdatefileRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdatefileResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




