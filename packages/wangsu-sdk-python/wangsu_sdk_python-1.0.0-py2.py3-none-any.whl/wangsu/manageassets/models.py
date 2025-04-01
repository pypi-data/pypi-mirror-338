# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class VideoEnableRequest(TeaModel):
    def __init__(
        self,
        video_id: str = None,
    ):
        # {"en":"The video id to enable", "zh_CN":"要启用的视频id"}
        self.video_id = video_id

    def validate(self):
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['videoId'] = self.video_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        return self


class VideoEnableResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class VideoEnablePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoEnableParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoEnableRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoEnableResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteCategoryRequest(TeaModel):
    def __init__(
        self,
        node_id: int = None,
    ):
        # {"en":"Node id", "zh_CN":"节点Id"}
        self.node_id = node_id

    def validate(self):
        self.validate_required(self.node_id, 'node_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        return self


class DeleteCategoryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
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


class DeleteCategoryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCategoryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCategoryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteCategoryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetCategoryListRequest(TeaModel):
    def __init__(
        self,
        parent_node_id: str = None,
        page_size: int = None,
        page_index: int = None,
    ):
        # {"en":"Id of the parent node. If empty, finds all first-level category tags", "zh_CN":"父节点Id。如果为空则查找所有一级分类标签"}
        self.parent_node_id = parent_node_id
        # {"en":"Number of items per page The value ranges from 1 to 100. The default value is 10", "zh_CN":"每页数量条数数，取值范围1-50，默认为10"}
        self.page_size = page_size
        # {"en":"Index of page The value starts from 1. The default value is 1", "zh_CN":"取数据第几页，从1开始取值,默认为1"}
        self.page_index = page_index

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_node_id is not None:
            result['parentNodeId'] = self.parent_node_id
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parentNodeId') is not None:
            self.parent_node_id = m.get('parentNodeId')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        return self


class GetCategoryListCategory(TeaModel):
    def __init__(
        self,
        label_name: str = None,
        parent_node_id: int = None,
        node_id: int = None,
        create_user: str = None,
    ):
        # {"en":"Label name", "zh_CN":"标签名称"}
        self.label_name = label_name
        # {"en":"ID of the upper-layer node. A Tier 1 node has no upper-level node. Only secondary nodes have parent nodes", "zh_CN":"上级节点ID。一级节点无上级节点。只有二级节点才有上级节点"}
        self.parent_node_id = parent_node_id
        # {"en":"Tag node ID", "zh_CN":"标签节点ID"}
        self.node_id = node_id
        # {"en":"Create a user", "zh_CN":"创建用户"}
        self.create_user = create_user

    def validate(self):
        self.validate_required(self.label_name, 'label_name')
        self.validate_required(self.parent_node_id, 'parent_node_id')
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.create_user, 'create_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label_name is not None:
            result['labelName'] = self.label_name
        if self.parent_node_id is not None:
            result['parentNodeId'] = self.parent_node_id
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.create_user is not None:
            result['createUser'] = self.create_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')
        if m.get('parentNodeId') is not None:
            self.parent_node_id = m.get('parentNodeId')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        return self


class GetCategoryListData(TeaModel):
    def __init__(
        self,
        total: int = None,
        page_size: int = None,
        page_index: int = None,
        category_list: List[GetCategoryListCategory] = None,
    ):
        # {"en":"Total number of data items", "zh_CN":"总数据条数"}
        self.total = total
        # {"en":"Returns the number of data bars", "zh_CN":"返回数据条数"}
        self.page_size = page_size
        # {"en":"Return to page number", "zh_CN":"返回第几页"}
        self.page_index = page_index
        # {"en":"GetCategoryListData detail list", "zh_CN":"数据明细列表"}
        self.category_list = category_list

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.page_size, 'page_size')
        self.validate_required(self.page_index, 'page_index')
        self.validate_required(self.category_list, 'category_list')
        if self.category_list:
            for k in self.category_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.category_list is not None:
            result['categoryList'] = []
            for k in self.category_list:
                result['categoryList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('categoryList') is not None:
            self.category_list = []
            for k in m.get('categoryList'):
                temp_model = GetCategoryListCategory()
                self.category_list.append(temp_model.from_map(k))
        return self


class GetCategoryListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[GetCategoryListData] = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
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
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = GetCategoryListData()
                self.data.append(temp_model.from_map(k))
        return self


class GetCategoryListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCategoryListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCategoryListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetCategoryListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteVideoByCategoryRequest(TeaModel):
    def __init__(
        self,
        node_id: int = None,
        notify_url: str = None,
    ):
        # {"en":"Node id", "zh_CN":"节点Id"}
        self.node_id = node_id
        # {"en":"Delete the result callback notification address", "zh_CN":"删除结果回调通知地址"}
        self.notify_url = notify_url

    def validate(self):
        self.validate_required(self.node_id, 'node_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        return self


class DeleteVideoByCategoryData(TeaModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        # {"en":"Delete task ID", "zh_CN":"删除任务ID"}
        self.task_id = task_id

    def validate(self):
        self.validate_required(self.task_id, 'task_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class DeleteVideoByCategoryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[DeleteVideoByCategoryData] = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
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
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = DeleteVideoByCategoryData()
                self.data.append(temp_model.from_map(k))
        return self


class DeleteVideoByCategoryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteVideoByCategoryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteVideoByCategoryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteVideoByCategoryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetMaterialListRequest(TeaModel):
    def __init__(
        self,
        material_id: str = None,
        material_name: str = None,
        suffix: str = None,
        create_user: str = None,
        publish_domain: str = None,
        upload_time_start: int = None,
        upload_time_end: int = None,
        page_index: str = None,
        page_size: str = None,
    ):
        # {"en":"GetMaterialListMaterial ID", "zh_CN":"素材ID"}
        self.material_id = material_id
        # {"en":"GetMaterialListMaterial name (fuzzy query)", "zh_CN":"素材名称（模糊查询）"}
        self.material_name = material_name
        # {"en":"GetMaterialListMaterial suffix", "zh_CN":"素材后缀"}
        self.suffix = suffix
        # {"en":"Create a user", "zh_CN":"创建用户"}
        self.create_user = create_user
        # {"en":"Publish domain name", "zh_CN":"发布域名"}
        self.publish_domain = publish_domain
        # {"en":"The query start time is based on the upload time. The query end time cannot be later than the timestamp in seconds", "zh_CN":"查询开始时间,根据上传时间查询，秒级时间戳，不得晚查询结束时间"}
        self.upload_time_start = upload_time_start
        # {"en":"The query end time is based on the upload time. The timestamp is in seconds and cannot be earlier than the query start time", "zh_CN":"查询结束时间,根据上传时间查询，秒级时间戳，不得早于查询开始时间"}
        self.upload_time_end = upload_time_end
        # {"en":"The page in the material list starts with 1. The default value is 1", "zh_CN":"取素材列表第几页，从1开始取值,默认为1"}
        self.page_index = page_index
        # {"en":"Average Number of materials per page. The value ranges from 1 to 50. The default value is 10", "zh_CN":"平均每页素材数量，取值范围1-50，默认为10"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.material_id is not None:
            result['materialId'] = self.material_id
        if self.material_name is not None:
            result['materialName'] = self.material_name
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.create_user is not None:
            result['createUser'] = self.create_user
        if self.publish_domain is not None:
            result['publishDomain'] = self.publish_domain
        if self.upload_time_start is not None:
            result['uploadTimeStart'] = self.upload_time_start
        if self.upload_time_end is not None:
            result['uploadTimeEnd'] = self.upload_time_end
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('materialId') is not None:
            self.material_id = m.get('materialId')
        if m.get('materialName') is not None:
            self.material_name = m.get('materialName')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        if m.get('publishDomain') is not None:
            self.publish_domain = m.get('publishDomain')
        if m.get('uploadTimeStart') is not None:
            self.upload_time_start = m.get('uploadTimeStart')
        if m.get('uploadTimeEnd') is not None:
            self.upload_time_end = m.get('uploadTimeEnd')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetMaterialListMaterial(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        suffix: str = None,
        file_size: int = None,
        url: str = None,
        create_user: str = None,
        create_time: int = None,
    ):
        # {"en":"GetMaterialListMaterial ID", "zh_CN":"素材ID"}
        self.id = id
        # {"en":"GetMaterialListMaterial name", "zh_CN":"素材名称"}
        self.name = name
        # {"en":"File suffix", "zh_CN":"文件后缀"}
        self.suffix = suffix
        # {"en":"File size (unit: bit)", "zh_CN":"文件大小(单位为bit)"}
        self.file_size = file_size
        # {"en":"File url", "zh_CN":"文件url"}
        self.url = url
        # {"en":"Create user", "zh_CN":"创建用户"}
        self.create_user = create_user
        # {"en":"Create time", "zh_CN":"创建时间"}
        self.create_time = create_time

    def validate(self):
        self.validate_required(self.id, 'id')
        self.validate_required(self.name, 'name')
        self.validate_required(self.suffix, 'suffix')
        self.validate_required(self.file_size, 'file_size')
        self.validate_required(self.url, 'url')
        self.validate_required(self.create_user, 'create_user')
        self.validate_required(self.create_time, 'create_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        if self.url is not None:
            result['url'] = self.url
        if self.create_user is not None:
            result['createUser'] = self.create_user
        if self.create_time is not None:
            result['createTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        return self


class GetMaterialListData(TeaModel):
    def __init__(
        self,
        total: int = None,
        material_list: List[GetMaterialListMaterial] = None,
    ):
        # {"en":"Total number of materials that match search conditions", "zh_CN":"符合查询条件的素材总个数"}
        self.total = total
        # {"en":"GetMaterialListMaterial list", "zh_CN":"素材列表"}
        self.material_list = material_list

    def validate(self):
        self.validate_required(self.total, 'total')
        self.validate_required(self.material_list, 'material_list')
        if self.material_list:
            for k in self.material_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.material_list is not None:
            result['materialList'] = []
            for k in self.material_list:
                result['materialList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('materialList') is not None:
            self.material_list = []
            for k in m.get('materialList'):
                temp_model = GetMaterialListMaterial()
                self.material_list.append(temp_model.from_map(k))
        return self


class GetMaterialListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetMaterialListData = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
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
            temp_model = GetMaterialListData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetMaterialListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetMaterialListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetMaterialListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetMaterialListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteAudioRequest(TeaModel):
    def __init__(
        self,
        audio_id: str = None,
        validate_occupy: int = None,
    ):
        # {"en":"id of the audio you want to delete", "zh_CN":"需要删除的音频的id"}
        self.audio_id = audio_id
        # {"en":"Occupancy check; 0 not check, 1 check, default check", "zh_CN":"占用校验；0 不校验，1 校验, 默认校验"}
        self.validate_occupy = validate_occupy

    def validate(self):
        self.validate_required(self.audio_id, 'audio_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_id is not None:
            result['audioId'] = self.audio_id
        if self.validate_occupy is not None:
            result['validateOccupy'] = self.validate_occupy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioId') is not None:
            self.audio_id = m.get('audioId')
        if m.get('validateOccupy') is not None:
            self.validate_occupy = m.get('validateOccupy')
        return self


class DeleteAudioResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Create the result status code. 200 indicates success", "zh_CN":"创建结果状态码，200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"操作成功"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteAudioPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAudioParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAudioRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAudioResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class EditAudioRequest(TeaModel):
    def __init__(
        self,
        audio_id: str = None,
        audio_name: str = None,
        publish_domain: str = None,
    ):
        # {"en":"Audio id to edit", "zh_CN":"需编辑的音频id"}
        self.audio_id = audio_id
        # {"en":"The value is a new audio name, with a maximum of 40 Chinese characters.", "zh_CN":"修改后的音频名称，最大40中文。"}
        self.audio_name = audio_name
        # {"en":"Adjusted published domain name.", "zh_CN":"调整后的发布域名。"}
        self.publish_domain = publish_domain

    def validate(self):
        self.validate_required(self.audio_id, 'audio_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_id is not None:
            result['audioId'] = self.audio_id
        if self.audio_name is not None:
            result['audioName'] = self.audio_name
        if self.publish_domain is not None:
            result['publishDomain'] = self.publish_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioId') is not None:
            self.audio_id = m.get('audioId')
        if m.get('audioName') is not None:
            self.audio_name = m.get('audioName')
        if m.get('publishDomain') is not None:
            self.publish_domain = m.get('publishDomain')
        return self


class EditAudioResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Status code", "zh_CN":"状态码"}
        self.code = code
        # {"en":"Operational information", "zh_CN":"操作信息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class EditAudioPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditAudioParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditAudioRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class EditAudioResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetAudioListRequest(TeaModel):
    def __init__(
        self,
        create_user: str = None,
        start_time: str = None,
        end_time: str = None,
        audio_name: str = None,
        audio_id: str = None,
        list_order: str = None,
        page_index: str = None,
        page_size: str = None,
    ):
        # {"en":"Create a user. The value is blank by default. Multiple entries are allowed. They are separated by commas (,) and cannot start or end with a comma. This parameter is restricted by permissions. Only sub-accounts or users with special permissions can be queried.", "zh_CN":"创建用户。默认为空，允许传多个，以半角逗号隔开，不能以逗号开头或结尾，两个逗号之间的内容不为能为空或空白字符。该参数受权限限制，只能查询子账户或权限特殊配置的用户。"}
        self.create_user = create_user
        # {"en":"The start time is in the format of 2016-01-01 12:00:00. It is used to query the audio according to the creation time range.", "zh_CN":"查询起始时间，时间格式为，2016-01-01 12:00:00；用于按创建时间段查询音频；"}
        self.start_time = start_time
        # {"en":"The query end time is in the format of 2016-01-01 12:00:00. This parameter is used to query audio files within the creation period, which is smaller than the current query time.", "zh_CN":"查询截止时间，时间格式为，2016-01-01 12:00:00；用于按创建时间段查询音频，小于当前查询时间；"}
        self.end_time = end_time
        # {"en":"Audio name, used to filter audio, support fuzzy matching;", "zh_CN":"音频名称，用于筛选音频，支持模糊匹配；"}
        self.audio_name = audio_name
        # {"en":"Audio ID, used to filter audio;", "zh_CN":"音频ID，用于筛选音频；"}
        self.audio_id = audio_id
        # {"en":"The value range is · 0(in descending order by creation time)· 1(in ascending order by creation time) The default value is 0", "zh_CN":"列表排列顺序，取值范围 ： · 0(按创建时间降序排列)· 1(按创建时间升序排列)默认为0"}
        self.list_order = list_order
        # {"en":"The page of the audio list starts with 1. The default value is 1. The product of pageIndex and pageSize must be less than 100000.", "zh_CN":"取音频列表第几页，从1开始取值,默认为1。入参pageIndex和pageSize的乘积必须不大于100000。"}
        self.page_index = page_index
        # {"en":"Average number of audio files per page. The value ranges from 1 to 50. The default value is 10. The product of pageIndex and pageSize must be less than 100000", "zh_CN":"平均每页音频数量，取值范围1-50，默认为10。入参pageIndex和pageSize的乘积必须不大于100000。"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_user is not None:
            result['createUser'] = self.create_user
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.audio_name is not None:
            result['audioName'] = self.audio_name
        if self.audio_id is not None:
            result['audioId'] = self.audio_id
        if self.list_order is not None:
            result['listOrder'] = self.list_order
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('audioName') is not None:
            self.audio_name = m.get('audioName')
        if m.get('audioId') is not None:
            self.audio_id = m.get('audioId')
        if m.get('listOrder') is not None:
            self.list_order = m.get('listOrder')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetAudioListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: 'GetAudioListDataList' = None,
        message: str = None,
    ):
        # {'en':"Return status code", "zh_CN":"返回状态码"}
        self.code = code
        self.data = data
        # {'en':"Return message","zh_CN":"返回消息"}
        self.message = message

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.data, 'data')
        if self.data:
            self.data.validate()
        self.validate_required(self.message, 'message')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetAudioListDataList()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetAudioListAudioGetListResponseList(TeaModel):
    def __init__(
        self,
        audio_name: str = None,
        audio_id: str = None,
        create_user: str = None,
        audio_size: int = None,
        audio_duration: int = None,
        url: str = None,
        suffix: str = None,
        create_time: int = None,
        upload_time: int = None,
    ):
        # {'en':'Audio name', 'zh_CN':'音频名称'}
        self.audio_name = audio_name
        # {'en':'Audio ID', 'zh_CN':'音频ID'}
        self.audio_id = audio_id
        # {'en':'Create user', 'zh_CN':'创建人'}
        self.create_user = create_user
        # {'en':'The space occupied by audio, and the total space used by video and video after transcoding', 'zh_CN':'音频占用空间大小，视频及其转码后视频的总空间使用量'}
        self.audio_size = audio_size
        # {'en':'Audio duration', 'zh_CN':'音频时长'}
        self.audio_duration = audio_duration
        # {'en':'File url', 'zh_CN':'文件url'}
        self.url = url
        # {'en':'File suffix', 'zh_CN':'文件后缀'}
        self.suffix = suffix
        # {'en':'Create time', 'zh_CN':'音频创建时间'}
        self.create_time = create_time
        # {'en':'Upload time', 'zh_CN':'音频上传时间'}
        self.upload_time = upload_time

    def validate(self):
        self.validate_required(self.audio_name, 'audio_name')
        self.validate_required(self.audio_id, 'audio_id')
        self.validate_required(self.create_user, 'create_user')
        self.validate_required(self.audio_size, 'audio_size')
        self.validate_required(self.audio_duration, 'audio_duration')
        self.validate_required(self.url, 'url')
        self.validate_required(self.suffix, 'suffix')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.upload_time, 'upload_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_name is not None:
            result['audioName'] = self.audio_name
        if self.audio_id is not None:
            result['audioId'] = self.audio_id
        if self.create_user is not None:
            result['createUser'] = self.create_user
        if self.audio_size is not None:
            result['audioSize'] = self.audio_size
        if self.audio_duration is not None:
            result['audioDuration'] = self.audio_duration
        if self.url is not None:
            result['url'] = self.url
        if self.suffix is not None:
            result['suffix'] = self.suffix
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioName') is not None:
            self.audio_name = m.get('audioName')
        if m.get('audioId') is not None:
            self.audio_id = m.get('audioId')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        if m.get('audioSize') is not None:
            self.audio_size = m.get('audioSize')
        if m.get('audioDuration') is not None:
            self.audio_duration = m.get('audioDuration')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('suffix') is not None:
            self.suffix = m.get('suffix')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        return self


class GetAudioListDataList(TeaModel):
    def __init__(
        self,
        audio_get_list_response_list: List[GetAudioListAudioGetListResponseList] = None,
        audio_total: int = None,
    ):
        self.audio_get_list_response_list = audio_get_list_response_list
        # {'en':'Audio upload time', 'zh_CN':'音频上传时间'}
        self.audio_total = audio_total

    def validate(self):
        self.validate_required(self.audio_get_list_response_list, 'audio_get_list_response_list')
        if self.audio_get_list_response_list:
            for k in self.audio_get_list_response_list:
                if k:
                    k.validate()
        self.validate_required(self.audio_total, 'audio_total')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_get_list_response_list is not None:
            result['audioGetListResponseList'] = []
            for k in self.audio_get_list_response_list:
                result['audioGetListResponseList'].append(k.to_map() if k else None)
        if self.audio_total is not None:
            result['audioTotal'] = self.audio_total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioGetListResponseList') is not None:
            self.audio_get_list_response_list = []
            for k in m.get('audioGetListResponseList'):
                temp_model = GetAudioListAudioGetListResponseList()
                self.audio_get_list_response_list.append(temp_model.from_map(k))
        if m.get('audioTotal') is not None:
            self.audio_total = m.get('audioTotal')
        return self


class GetAudioListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAudioListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAudioListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAudioListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class MaterialEditRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        publish_domain: str = None,
    ):
        # {"en":"id of the material to edit", "zh_CN":"需编辑的素材id"}
        self.id = id
        # {"en":"The value can contain a maximum of 40 characters.", "zh_CN":"修改后的素材名称，最大40字符。"}
        self.name = name
        # {"en":"Adjusted published domain name.", "zh_CN":"调整后的发布域名。"}
        self.publish_domain = publish_domain

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.publish_domain is not None:
            result['publishDomain'] = self.publish_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('publishDomain') is not None:
            self.publish_domain = m.get('publishDomain')
        return self


class MaterialEditResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class MaterialEditPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class MaterialEditParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class MaterialEditRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class MaterialEditResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteMaterialRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        validate_occupy: str = None,
    ):
        # {"en":"ID of the material that you want to delete", "zh_CN":"需要删除的素材ID"}
        self.id = id
        # {"en":"Occupied check, default check
        # 0 uncheck
        # 1 check", "zh_CN":"占用校验，默认校验
        # 0 不校验
        # 1 校验"}
        self.validate_occupy = validate_occupy

    def validate(self):
        self.validate_required(self.id, 'id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.validate_occupy is not None:
            result['validateOccupy'] = self.validate_occupy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('validateOccupy') is not None:
            self.validate_occupy = m.get('validateOccupy')
        return self


class DeleteMaterialResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteMaterialPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteMaterialParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteMaterialRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteMaterialResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteVideoRequest(TeaModel):
    def __init__(
        self,
        video_id: str = None,
        validate_occupy: int = None,
        notify_url: str = None,
        is_async: int = None,
        only_delete_source: int = None,
    ):
        # {"en":"id of the video you want to delete", "zh_CN":"需要删除的视频的id"}
        self.video_id = video_id
        # {"en":"Occupied check, default check
        # 0 uncheck
        # 1 check", "zh_CN":"占用校验，默认校验
        # 0 不校验
        # 1 校验"}
        self.validate_occupy = validate_occupy
        # {"en":"Delete the result callback notification address", "zh_CN":"删除结果回调通知地址"}
        self.notify_url = notify_url
        # {"en":"Whether to delete asynchronously, the default value is 1;
        # 0: delete files synchronously, 1: delete files asynchronously", "zh_CN":"是否异步删除，默认为1；
        # 0:同步删除文件，1：异步删除文件"}
        self.is_async = is_async
        # {"en":"The default value is 0; 0: delete all files (including original files and Transcoding files), 1: delete only the original file", "zh_CN":"只删除原文件
        # 默认为0；
        # 0:删除所有文件（包含原文件和转码文件），1：只删除原文件"}
        self.only_delete_source = only_delete_source

    def validate(self):
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.validate_occupy is not None:
            result['validateOccupy'] = self.validate_occupy
        if self.notify_url is not None:
            result['notifyUrl'] = self.notify_url
        if self.is_async is not None:
            result['isAsync'] = self.is_async
        if self.only_delete_source is not None:
            result['onlyDeleteSource'] = self.only_delete_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('validateOccupy') is not None:
            self.validate_occupy = m.get('validateOccupy')
        if m.get('notifyUrl') is not None:
            self.notify_url = m.get('notifyUrl')
        if m.get('isAsync') is not None:
            self.is_async = m.get('isAsync')
        if m.get('onlyDeleteSource') is not None:
            self.only_delete_source = m.get('onlyDeleteSource')
        return self


class DeleteVideoResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class DeleteVideoPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteVideoParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteVideoRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteVideoResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VideoEditRequest(TeaModel):
    def __init__(
        self,
        video_id: str = None,
        video_name: str = None,
        video_description: str = None,
        video_classification: str = None,
        category_names: str = None,
        publish_domain: str = None,
        player_id: str = None,
    ):
        # {"en":"id of the video to edit", "zh_CN":"需编辑的视频id"}
        self.video_id = video_id
        # {"en":"The modified video name contains a maximum of 40 Chinese characters", "zh_CN":"修改后的视频名称，最大40中文"}
        self.video_name = video_name
        # {"en":"Video description, a maximum of 200 Chinese characters", "zh_CN":"视频的描述信息，最大200中文"}
        self.video_description = video_description
        # {"en":"Modified video subcategories. This field is valid only when categoryNames is not entered. If there are multiple subcategories that are the same, the video sets all of them. videoClassification can only contain Chinese characters, uppercase and lowercase letters, numbers, underscores, and spaces. It cannot start with a space. Multiple characters can be separated by commas. (categoryNames is recommended). ", "zh_CN":"修改后的视频子分类。categoryNames不填时，此字段才有效。 如果有多个相同的子分类，则视频会设置所有的子分类。videoClassification只能包含中文、大小写字母、数字、下划线、空格，不能空格开头，多个支持逗号分隔。 （建议使用categoryNames）"}
        self.video_classification = video_classification
        # {"en":"After the video category is modified, you can specify parent category and child category. The format is an urlsafe base64 encoded JSON string array. Transfer an empty array, indicating that the video classification Settings are cleared.
        # The parameters are as follows:
        # 1) parentName: indicates the name of the parent class.
        # 2) childName: indicates the name of the subcategory
        # }", "zh_CN":"修改后的视频分类，可指定父分类和子分类。 格式为经过urlsafe base64编码的JSON字符串数组。传输空数组，则表示清空视频的分类设置。 
        # 参数如下：
        # 1）parentName: 父分类名称；
        # 2）childName: 子分类名称
        # 例：W3siY2hpbGROYW1lIjoi5a2Q5YiG57G7MSIsInBhcmVudE5hbWUiOiLniLbliIbnsbsxIn0seyJjaGlsZE5hbWUiOiLlrZDliIbnsbsyIiwicGFyZW50TmFtZSI6IueItuWIhuexuzIifV0= 编码前的json串格式如下：
        # [{\"childName\":\"子分类1\",\"parentName\":\"父分类1\"},{\"childName\":\"子分类2\",\"parentName\":\"父分类2\"}]"}
        self.category_names = category_names
        # {"en":"Adjusted published domain name", "zh_CN":"调整后的发布域名"}
        self.publish_domain = publish_domain
        # {"en":"The adjusted player ID", "zh_CN":"调整后的播放器ID"}
        self.player_id = player_id

    def validate(self):
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.video_name is not None:
            result['videoName'] = self.video_name
        if self.video_description is not None:
            result['videoDescription'] = self.video_description
        if self.video_classification is not None:
            result['videoClassification'] = self.video_classification
        if self.category_names is not None:
            result['categoryNames'] = self.category_names
        if self.publish_domain is not None:
            result['publishDomain'] = self.publish_domain
        if self.player_id is not None:
            result['playerId'] = self.player_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('videoName') is not None:
            self.video_name = m.get('videoName')
        if m.get('videoDescription') is not None:
            self.video_description = m.get('videoDescription')
        if m.get('videoClassification') is not None:
            self.video_classification = m.get('videoClassification')
        if m.get('categoryNames') is not None:
            self.category_names = m.get('categoryNames')
        if m.get('publishDomain') is not None:
            self.publish_domain = m.get('publishDomain')
        if m.get('playerId') is not None:
            self.player_id = m.get('playerId')
        return self


class VideoEditResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
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


class VideoEditPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoEditParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoEditRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoEditResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class VideoBlockRequest(TeaModel):
    def __init__(
        self,
        video_id: str = None,
    ):
        # {"en":"id of the video to be masked", "zh_CN":"要屏蔽的视频id"}
        self.video_id = video_id

    def validate(self):
        self.validate_required(self.video_id, 'video_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_id is not None:
            result['videoId'] = self.video_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        return self


class VideoBlockResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Return message", "zh_CN":"返回消息"}
        self.message = message
        # {"en":"Return data", "zh_CN":"返回数据"}
        self.data = data

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.data, 'data')

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
            result['data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        return self


class VideoBlockPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoBlockParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoBlockRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class VideoBlockResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateCategoryRequest(TeaModel):
    def __init__(
        self,
        parent_node_id: int = None,
        label_name: str = None,
    ):
        # {"en":"Id of the parent node. If it is empty, create the parent node", "zh_CN":"父节点Id。如果为空则创建父级节点"}
        self.parent_node_id = parent_node_id
        # {"en":"Label name (32 characters supported)", "zh_CN":"标签名称（支持32个字符）"}
        self.label_name = label_name

    def validate(self):
        self.validate_required(self.label_name, 'label_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_node_id is not None:
            result['parentNodeId'] = self.parent_node_id
        if self.label_name is not None:
            result['labelName'] = self.label_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parentNodeId') is not None:
            self.parent_node_id = m.get('parentNodeId')
        if m.get('labelName') is not None:
            self.label_name = m.get('labelName')
        return self


class CreateCategoryData(TeaModel):
    def __init__(
        self,
        node_id: int = None,
    ):
        # {"en":"Tag node ID", "zh_CN":"标签节点ID"}
        self.node_id = node_id

    def validate(self):
        self.validate_required(self.node_id, 'node_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        return self


class CreateCategoryResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[CreateCategoryData] = None,
    ):
        # {"en":"Result status code, 200 indicates success", "zh_CN":"结果状态码，200为成功"}
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
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = []
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = []
            for k in m.get('data'):
                temp_model = CreateCategoryData()
                self.data.append(temp_model.from_map(k))
        return self


class CreateCategoryPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateCategoryParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateCategoryRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateCategoryResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class GetVideoListRequest(TeaModel):
    def __init__(
        self,
        create_user: str = None,
        start_time: str = None,
        end_time: str = None,
        video_name: str = None,
        video_id: str = None,
        video_status: int = None,
        transcode_state: int = None,
        video_classification: str = None,
        list_order: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # {"en":"Create a user. The value is blank by default. Multiple entries are allowed. They are separated by commas (,) and cannot start or end with a comma. This parameter is restricted by permissions. Only sub-accounts or users with special permissions can be queried.", "zh_CN":"创建用户。默认为空，允许传多个，以半角逗号隔开，不能以逗号开头或结尾，两个逗号之间的内容不为能为空或空白字符。该参数受权限限制，只能查询子账户或权限特殊配置的用户。"}
        self.create_user = create_user
        # {"en":"The start time is in the format of 2016-01-01 12:00:00. Query videos by creation time range.", "zh_CN":"查询起始时间，时间格式为，2016-01-01 12:00:00；用于按创建时间段查询视频；"}
        self.start_time = start_time
        # {"en":"The query end time is in the format of 2016-01-01 12:00:00. This parameter is used to query videos in the creation period, which is smaller than the current query time.", "zh_CN":"查询截止时间，时间格式为，2016-01-01 12:00:00；用于按创建时间段查询视频，小于当前查询时间；"}
        self.end_time = end_time
        # {"en":"Video name, used to filter videos, support fuzzy matching;", "zh_CN":"视频名称，用于筛选视频，支持模糊匹配；"}
        self.video_name = video_name
        # {"en":"Video ID, used to filter videos;", "zh_CN":"视频ID，用于筛选视频；"}
        self.video_id = video_id
        # {"en":"Video status, used to filter videos", "zh_CN":"视频状态，用于筛选视频。取值范围 ：
        # 0(启用)
        # 1(屏蔽)"}
        self.video_status = video_status
        # {"en":"Authorized play is not enabled. Procedure", "zh_CN":"未开启授权播放，视频的转码状态的取值范围 ：
        # 1(已转码)
        # 2(未转码)
        # 3(转码中)
        # 4(转码失败)
        # 
        # 开启授权播放（视频加密）功能时的转码状态的取值范围 ：
        # 1(已加密转码)
        # 2(非加密转码)
        # 3(转码中)
        # 4(转码失败)
        # 5(未转码)"}
        self.transcode_state = transcode_state
        # {"en":"Subcategory names for video classification, supporting multiple subcategory names simultaneously, separated by',' for each subcategory name. videoClassification can only contain Chinese characters, uppercase and lowercase letters, numbers, underscores, and spaces. It cannot start with a space. Multiple characters can be separated by commas.", "zh_CN":"视频分类子分类名称，支持同时输入多个子分类名称，每个子分类名称用“,”隔开。只能包含中文、大小写字母、数字、下划线、空格，不能空格开头，多个支持逗号分隔"}
        self.video_classification = video_classification
        # {"en":"List order", "zh_CN":"列表排列顺序，取值范围 ：
        # 0(按创建时间降序排列)
        # 1(按创建时间升序排列)
        # 默认为0"}
        self.list_order = list_order
        # {"en":"Page of the video list. The value starts from 1. The default value is 1. The product of pageIndex and pageSize must be less than 100000.", "zh_CN":"取视频列表第几页，从1开始取值,默认为1。入参pageIndex和pageSize的乘积必须不大于100000。"}
        self.page_index = page_index
        # {"en":"Average number of videos per page. The value ranges from 1 to 50. The default value is 10. The product of pageIndex and pageSize must be less than 100000.", "zh_CN":"平均每页视频数量，取值范围1-50，默认为10。入参pageIndex和pageSize的乘积必须不大于100000。"}
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_user is not None:
            result['createUser'] = self.create_user
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.video_name is not None:
            result['videoName'] = self.video_name
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.video_status is not None:
            result['videoStatus'] = self.video_status
        if self.transcode_state is not None:
            result['transcodeState'] = self.transcode_state
        if self.video_classification is not None:
            result['videoClassification'] = self.video_classification
        if self.list_order is not None:
            result['listOrder'] = self.list_order
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('videoName') is not None:
            self.video_name = m.get('videoName')
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('videoStatus') is not None:
            self.video_status = m.get('videoStatus')
        if m.get('transcodeState') is not None:
            self.transcode_state = m.get('transcodeState')
        if m.get('videoClassification') is not None:
            self.video_classification = m.get('videoClassification')
        if m.get('listOrder') is not None:
            self.list_order = m.get('listOrder')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetVideoListVideoResolution(TeaModel):
    def __init__(
        self,
        clarity: int = None,
        server_type: int = None,
        height: int = None,
        width: int = None,
        file_size: int = None,
    ):
        # {"en":"Clarity. Value range:
        # 1(original painting)
        # 2(fluency)
        # 3(standard definition)
        # 4(HD)
        # 5(Super clear)
        # -99(record file)", "zh_CN":"	清晰度。取值范围 ：
        # 1(原画)
        # 2(流畅)
        # 3(标清)
        # 4(高清)
        # 5(超清)
        # -99(录制文件)"}
        self.clarity = clarity
        # {"en":"Terminal type. Value range:
        # -1(Source video)
        # 0(PC)
        # 1(mobile terminal)", "zh_CN":"终端类型。取值范围 ：
        # -1(源视频)
        # 0(PC端)
        # 1(移动端)"}
        self.server_type = server_type
        # {"en":"height", "zh_CN":"高度"}
        self.height = height
        # {"en":"width", "zh_CN":"宽度"}
        self.width = width
        # {"en":"fileSize", "zh_CN":"文件大小(单位为bit)"}
        self.file_size = file_size

    def validate(self):
        self.validate_required(self.clarity, 'clarity')
        self.validate_required(self.server_type, 'server_type')
        self.validate_required(self.height, 'height')
        self.validate_required(self.width, 'width')
        self.validate_required(self.file_size, 'file_size')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.clarity is not None:
            result['clarity'] = self.clarity
        if self.server_type is not None:
            result['serverType'] = self.server_type
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        if self.file_size is not None:
            result['fileSize'] = self.file_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clarity') is not None:
            self.clarity = m.get('clarity')
        if m.get('serverType') is not None:
            self.server_type = m.get('serverType')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')
        return self


class GetVideoListVideoInfo(TeaModel):
    def __init__(
        self,
        video_name: str = None,
        video_id: str = None,
        create_user: str = None,
        encrypt: int = None,
        video_size: str = None,
        video_duration: str = None,
        create_time: str = None,
        upload_time: str = None,
        update_time: str = None,
        video_description: str = None,
        video_classification: str = None,
        image_url: str = None,
        publish_domain: str = None,
        player_name: str = None,
        player_id: str = None,
        video_state: int = None,
        transcode_state: int = None,
        video_source_code: int = None,
        video_resolutions: List[GetVideoListVideoResolution] = None,
    ):
        # {"en":"videoName", "zh_CN":"视频名称"}
        self.video_name = video_name
        # {"en":"videoId", "zh_CN":"视频ID"}
        self.video_id = video_id
        # {"en":"createUser", "zh_CN":"创建人"}
        self.create_user = create_user
        # {"en":"Whether to encrypt transcoding files. Value range:
        # 0(unencrypted)
        # 1(encrypted)", "zh_CN":"是否加密转码文件。取值范围 ：
        # 0(不加密)
        # 1(加密)"}
        self.encrypt = encrypt
        # {"en":"The space occupied by the video, and the total space used by the video and its transcoding", "zh_CN":"视频占用空间大小，视频及其转码后视频的总空间使用量"}
        self.video_size = video_size
        # {"en":"videoDuration", "zh_CN":"视频时长"}
        self.video_duration = video_duration
        # {"en":"createTime", "zh_CN":"视频创建时间"}
        self.create_time = create_time
        # {"en":"uploadTime", "zh_CN":"视频上传时间"}
        self.upload_time = upload_time
        # {"en":"updateTime", "zh_CN":"视频修改时间"}
        self.update_time = update_time
        # {"en":"videoDescription", "zh_CN":"视频描述"}
        self.video_description = video_description
        # {"en":"videoClassification", "zh_CN":"视频分类"}
        self.video_classification = video_classification
        # {"en":"imageUrl", "zh_CN":"视频封面URL"}
        self.image_url = image_url
        # {"en":"publishDomain", "zh_CN":"视频的发布域名"}
        self.publish_domain = publish_domain
        # {"en":"playerName", "zh_CN":"视频使用的播放器名称"}
        self.player_name = player_name
        # {"en":"playerId", "zh_CN":"视频使用的播放器ID"}
        self.player_id = player_id
        # {"en":"Video state
        # Value range:
        # 0(enable)
        # 1(mask)", "zh_CN":"视频状态
        # 取值范围：
        # 0(启用)
        # 1(屏蔽)"}
        self.video_state = video_state
        # {"en":"If authorized play is not enabled, the video transcoding status ranges from:
        # 1(transcoded)
        # 2(no transcoding)
        # 3(in transcoding)
        # 4(Transcoding fails)
        # 
        # Value range of transcoding status when the Authorized Play (video encryption) function is enabled:
        # 1(encrypted transcoding)
        # 2(non-encrypted transcoding)
        # 3(in transcoding)
        # 4(Transcoding fails)
        # 5(not transcoded)", "zh_CN":"未开启授权播放，视频的转码状态的取值范围 ：
        # 1(已转码)
        # 2(未转码)
        # 3(转码中)
        # 4(转码失败)
        # 
        # 开启授权播放（视频加密）功能时的转码状态的取值范围 ：
        # 1(已加密转码)
        # 2(非加密转码)
        # 3(转码中)
        # 4(转码失败)
        # 5(未转码)"}
        self.transcode_state = transcode_state
        # {"en":"Video source
        # Value range:
        # 0(other)
        # 1(Upload)
        # 2 (Live streaming to recording)
        # 3 (Video pull)
        # 4 (Video cutting)
        # 5 (Video Stitching)
        # 6 (edge pull recording)
        # 10 (universal version of live broadcasting to recording)
        # 11 (Uploading SDK)
        # 12 (Upload tool)", "zh_CN":"	视频来源
        # 取值范围：
        # 0(其他)
        # 1(上传)
        # 2（直播转录制）
        # 3（视频拉取）
        # 4（视频剪切）
        # 5（视频拼接）
        # 6（边缘拉流录制）
        # 10（通用版直播转录制）
        # 11（上传SDK）
        # 12（上传工具）"}
        self.video_source_code = video_source_code
        # {"en":"Video resolution and other information", "zh_CN":"视频分辨率等信息"}
        self.video_resolutions = video_resolutions

    def validate(self):
        self.validate_required(self.video_name, 'video_name')
        self.validate_required(self.video_id, 'video_id')
        self.validate_required(self.create_user, 'create_user')
        self.validate_required(self.encrypt, 'encrypt')
        self.validate_required(self.video_size, 'video_size')
        self.validate_required(self.video_duration, 'video_duration')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.upload_time, 'upload_time')
        self.validate_required(self.update_time, 'update_time')
        self.validate_required(self.video_description, 'video_description')
        self.validate_required(self.video_classification, 'video_classification')
        self.validate_required(self.image_url, 'image_url')
        self.validate_required(self.publish_domain, 'publish_domain')
        self.validate_required(self.player_name, 'player_name')
        self.validate_required(self.player_id, 'player_id')
        self.validate_required(self.video_state, 'video_state')
        self.validate_required(self.transcode_state, 'transcode_state')
        self.validate_required(self.video_source_code, 'video_source_code')
        self.validate_required(self.video_resolutions, 'video_resolutions')
        if self.video_resolutions:
            for k in self.video_resolutions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_name is not None:
            result['videoName'] = self.video_name
        if self.video_id is not None:
            result['videoId'] = self.video_id
        if self.create_user is not None:
            result['createUser'] = self.create_user
        if self.encrypt is not None:
            result['encrypt'] = self.encrypt
        if self.video_size is not None:
            result['videoSize'] = self.video_size
        if self.video_duration is not None:
            result['videoDuration'] = self.video_duration
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.upload_time is not None:
            result['uploadTime'] = self.upload_time
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.video_description is not None:
            result['videoDescription'] = self.video_description
        if self.video_classification is not None:
            result['videoClassification'] = self.video_classification
        if self.image_url is not None:
            result['imageUrl'] = self.image_url
        if self.publish_domain is not None:
            result['publishDomain'] = self.publish_domain
        if self.player_name is not None:
            result['playerName'] = self.player_name
        if self.player_id is not None:
            result['playerId'] = self.player_id
        if self.video_state is not None:
            result['videoState'] = self.video_state
        if self.transcode_state is not None:
            result['transcodeState'] = self.transcode_state
        if self.video_source_code is not None:
            result['videoSourceCode'] = self.video_source_code
        if self.video_resolutions is not None:
            result['videoResolutions'] = []
            for k in self.video_resolutions:
                result['videoResolutions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoName') is not None:
            self.video_name = m.get('videoName')
        if m.get('videoId') is not None:
            self.video_id = m.get('videoId')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        if m.get('encrypt') is not None:
            self.encrypt = m.get('encrypt')
        if m.get('videoSize') is not None:
            self.video_size = m.get('videoSize')
        if m.get('videoDuration') is not None:
            self.video_duration = m.get('videoDuration')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('uploadTime') is not None:
            self.upload_time = m.get('uploadTime')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('videoDescription') is not None:
            self.video_description = m.get('videoDescription')
        if m.get('videoClassification') is not None:
            self.video_classification = m.get('videoClassification')
        if m.get('imageUrl') is not None:
            self.image_url = m.get('imageUrl')
        if m.get('publishDomain') is not None:
            self.publish_domain = m.get('publishDomain')
        if m.get('playerName') is not None:
            self.player_name = m.get('playerName')
        if m.get('playerId') is not None:
            self.player_id = m.get('playerId')
        if m.get('videoState') is not None:
            self.video_state = m.get('videoState')
        if m.get('transcodeState') is not None:
            self.transcode_state = m.get('transcodeState')
        if m.get('videoSourceCode') is not None:
            self.video_source_code = m.get('videoSourceCode')
        if m.get('videoResolutions') is not None:
            self.video_resolutions = []
            for k in m.get('videoResolutions'):
                temp_model = GetVideoListVideoResolution()
                self.video_resolutions.append(temp_model.from_map(k))
        return self


class GetVideoListData(TeaModel):
    def __init__(
        self,
        video_total: int = None,
        video_list_info: List[GetVideoListVideoInfo] = None,
    ):
        # {"en":"The number of records of the video list information currently returned. Note that the number of records returned here is only the number of records of the current page.", "zh_CN":"当前返回的视频列表信息的记录数，注意这里返回的记录数只是当前页的记录数。"}
        self.video_total = video_total
        # {"en":"videoListInfo", "zh_CN":"视频列表信息"}
        self.video_list_info = video_list_info

    def validate(self):
        self.validate_required(self.video_total, 'video_total')
        self.validate_required(self.video_list_info, 'video_list_info')
        if self.video_list_info:
            for k in self.video_list_info:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_total is not None:
            result['videoTotal'] = self.video_total
        if self.video_list_info is not None:
            result['videoListInfo'] = []
            for k in self.video_list_info:
                result['videoListInfo'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoTotal') is not None:
            self.video_total = m.get('videoTotal')
        if m.get('videoListInfo') is not None:
            self.video_list_info = []
            for k in m.get('videoListInfo'):
                temp_model = GetVideoListVideoInfo()
                self.video_list_info.append(temp_model.from_map(k))
        return self


class GetVideoListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: GetVideoListData = None,
    ):
        # {"en":"200 success", "zh_CN":"结果状态码，200为成功"}
        self.code = code
        # {"en":"Successful operation", "zh_CN":"返回消息"}
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
            temp_model = GetVideoListData()
            self.data = temp_model.from_map(m['data'])
        return self


class GetVideoListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetVideoListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetVideoListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetVideoListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




