# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class GetSceneListRequest(TeaModel):
    def __init__(
        self,
        create_user: str = None,
        start_time: str = None,
        end_time: str = None,
        list_order: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # {"en":"Create a user. The value is blank by default. Multiple entries are allowed. They are separated by commas (,) and cannot start or end with a comma. This parameter is restricted by permissions. Only sub-accounts or users with special permissions can be queried.", "zh_CN":"创建用户。默认为空，允许传多个，以半角逗号隔开，不能以逗号开头或结尾，两个逗号之间的内容不为能为空或空白字符。该参数受权限限制，只能查询子账户或权限特殊配置的用户。"}
        self.create_user = create_user
        # {"en":"The start time is in the format of 2016-01-01 12:00:00. Query by creation time range.", "zh_CN":"查询起始时间，时间格式为，2016-01-01 12:00:00；用于按创建时间段查询；"}
        self.start_time = start_time
        # {"en":"The query end time is in the format of 2016-01-01 12:00:00. This parameter is used for query by creation time range, which is smaller than the current query time.", "zh_CN":"查询截止时间，时间格式为，2016-01-01 12:00:00；用于按创建时间段查询，小于当前查询时间；"}
        self.end_time = end_time
        # {"en":"List order, value range: <br>
        # 0(in descending order by creation time)<br>
        # 1(in ascending order of creation time) The default value is 0", "zh_CN":"列表排列顺序，取值范围 ：<br>
        # 0(按创建时间降序排列)<br>
        # 1(按创建时间升序排列)默认为0"}
        self.list_order = list_order
        # {"en":"On the page of the scenario list, the value starts from 1. The default value is 1. The product of pageIndex and pageSize must be less than 100000.", "zh_CN":"取场景列表第几页，从1开始取值,默认为1。入参pageIndex和pageSize的乘积必须不大于100000。"}
        self.page_index = page_index
        # {"en":"Average Number of scenarios per page. The value ranges from 1 to 50. The default value is 10. The product of pageIndex and pageSize must be less than 100000.", "zh_CN":"平均每页场景数量，取值范围1-50，默认为10。入参pageIndex和pageSize的乘积必须不大于100000。"}
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
        if m.get('listOrder') is not None:
            self.list_order = m.get('listOrder')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetSceneListScene(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        scene_name: str = None,
        create_time: str = None,
        create_user: str = None,
    ):
        # {"en":"GetSceneListScene Id", "zh_CN":"场景Id"}
        self.scene_id = scene_id
        # {"en":"GetSceneListScene name", "zh_CN":"场景名称"}
        self.scene_name = scene_name
        # {"en":"Create time", "zh_CN":"场景创建时间"}
        self.create_time = create_time
        # {"en":"Create user", "zh_CN":"场景创建的用户"}
        self.create_user = create_user

    def validate(self):
        self.validate_required(self.scene_id, 'scene_id')
        self.validate_required(self.scene_name, 'scene_name')
        self.validate_required(self.create_time, 'create_time')
        self.validate_required(self.create_user, 'create_user')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        if self.scene_name is not None:
            result['sceneName'] = self.scene_name
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.create_user is not None:
            result['createUser'] = self.create_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        if m.get('sceneName') is not None:
            self.scene_name = m.get('sceneName')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('createUser') is not None:
            self.create_user = m.get('createUser')
        return self


class GetSceneListResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[GetSceneListScene] = None,
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
                temp_model = GetSceneListScene()
                self.data.append(temp_model.from_map(k))
        return self


class GetSceneListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSceneListParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSceneListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetSceneListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class SceneEditRequest(TeaModel):
    def __init__(
        self,
        scene_name: str = None,
        scene_id: str = None,
    ):
        # {"en":"Scene name", "zh_CN":"场景名称"}
        self.scene_name = scene_name
        # {"en":"The scene Id to edit", "zh_CN":"需要编辑的场景Id"}
        self.scene_id = scene_id

    def validate(self):
        self.validate_required(self.scene_name, 'scene_name')
        self.validate_required(self.scene_id, 'scene_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_name is not None:
            result['sceneName'] = self.scene_name
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneName') is not None:
            self.scene_name = m.get('sceneName')
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class SceneEditResponse(TeaModel):
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


class SceneEditPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SceneEditParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SceneEditRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class SceneEditResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateSceneRequest(TeaModel):
    def __init__(
        self,
        scene_name: str = None,
    ):
        # {"en":"Scene name", "zh_CN":"场景名称"}
        self.scene_name = scene_name

    def validate(self):
        self.validate_required(self.scene_name, 'scene_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_name is not None:
            result['sceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneName') is not None:
            self.scene_name = m.get('sceneName')
        return self


class CreateSceneData(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # {"en":"Scene ID", "zh_CN":"场景ID"}
        self.scene_id = scene_id

    def validate(self):
        self.validate_required(self.scene_id, 'scene_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['sceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')
        return self


class CreateSceneResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: CreateSceneData = None,
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
            temp_model = CreateSceneData()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateScenePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSceneParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSceneRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateSceneResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteSceneRequest(TeaModel):
    def __init__(
        self,
        scene_ids: List[str] = None,
    ):
        # {"en":"id of the scene you want to delete. Multiple users can be deleted at the same time", "zh_CN":"需要删除的场景的id;支持同时删除多个"}
        self.scene_ids = scene_ids

    def validate(self):
        self.validate_required(self.scene_ids, 'scene_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_ids is not None:
            result['sceneIds'] = self.scene_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sceneIds') is not None:
            self.scene_ids = m.get('sceneIds')
        return self


class DeleteSceneResponse(TeaModel):
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


class DeleteScenePaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSceneParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSceneRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteSceneResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




