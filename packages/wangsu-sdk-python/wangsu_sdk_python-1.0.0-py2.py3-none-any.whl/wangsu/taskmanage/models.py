# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QuerysubtasklistRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QuerysubtasklistResponse(TeaModel):
    def __init__(
        self,
        subtasks: List[str] = None,
    ):
        # {"en":"list of subtasks", "zh_CN":"云手机子任务单列表"}
        self.subtasks = subtasks

    def validate(self):
        self.validate_required(self.subtasks, 'subtasks')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subtasks is not None:
            result['subtasks'] = self.subtasks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('subtasks') is not None:
            self.subtasks = m.get('subtasks')
        return self


class QuerysubtasklistPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QuerysubtasklistParameters(TeaModel):
    def __init__(
        self,
        ids: str = None,
    ):
        # {"en":"subtask ID to be queried", "zh_CN":"要查询的任务单id，多个id使用英文逗号进行分隔"}
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        return self


class QuerysubtasklistRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QuerysubtasklistResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTaskListRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTaskListTask(TeaModel):
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


class QueryTaskListResponse(TeaModel):
    def __init__(
        self,
        tasks: List[QueryTaskListTask] = None,
        status: int = None,
        result: str = None,
    ):
        # {"en":"task list", "zh_CN":"任务单列表"}
        self.tasks = tasks
        # {"en":"status", "zh_CN":"状态"}
        self.status = status
        # {"en":"message", "zh_CN":"消息"}
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
                temp_model = QueryTaskListTask()
                self.tasks.append(temp_model.from_map(k))
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class QueryTaskListPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTaskListParameters(TeaModel):
    def __init__(
        self,
        ids: str = None,
    ):
        # {"en":"task ID to be queried", "zh_CN":"要查询的任务单id，多个id使用英文逗号进行分隔"}
        self.ids = ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ids is not None:
            result['ids'] = self.ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ids') is not None:
            self.ids = m.get('ids')
        return self


class QueryTaskListRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTaskListResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




