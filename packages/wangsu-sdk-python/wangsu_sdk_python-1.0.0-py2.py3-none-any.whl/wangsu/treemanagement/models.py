# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class AddTreeNodesRequest(TeaModel):
    def __init__(
        self,
        parent_node_id: str = None,
        node_name: str = None,
    ):
        # {"en":"Relay node ID. When empty, it is added to the root directory by default The node type must be a directory node.", "zh_CN":"父节点ID。为空时，默认新增到根目录下 节点类型必须是目录节点"}
        self.parent_node_id = parent_node_id
        # {"en":"Node name", "zh_CN":"新增节点名称"}
        self.node_name = node_name

    def validate(self):
        self.validate_required(self.node_name, 'node_name')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_node_id is not None:
            result['parentNodeId'] = self.parent_node_id
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parentNodeId') is not None:
            self.parent_node_id = m.get('parentNodeId')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        return self


class AddTreeNodesResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: str = None,
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


class AddTreeNodesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddTreeNodesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddTreeNodesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class AddTreeNodesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class DeleteTreeNodesRequest(TeaModel):
    def __init__(
        self,
        node_id: str = None,
    ):
        # {"en":"Tree Node Id", "zh_CN":"节点Id，必须目录节点。如果节点下有设备，会删除失败"}
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


class DeleteTreeNodesResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Result status code, 0 indicates success", "zh_CN":"结果状态码，0为成功"}
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


class DeleteTreeNodesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteTreeNodesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteTreeNodesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteTreeNodesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class QueryTreeNodesRequest(TeaModel):
    def __init__(
        self,
        parent_node_id: str = None,
    ):
        # {"en":"Relay node ID. When empty, get the root directory node The node type must be a directory node.", "zh_CN":"父节点ID。为空时，获取根目录节点 节点类型必须是目录节点。"}
        self.parent_node_id = parent_node_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_node_id is not None:
            result['parentNodeId'] = self.parent_node_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('parentNodeId') is not None:
            self.parent_node_id = m.get('parentNodeId')
        return self


class QueryTreeNodesNode(TeaModel):
    def __init__(
        self,
        node_id: str = None,
        node_name: str = None,
        node_type: int = None,
    ):
        # {"en":"Tree node ID", "zh_CN":"树节点ID"}
        self.node_id = node_id
        # {"en":"Tree node name", "zh_CN":"树节点名称"}
        self.node_name = node_name
        # {"en":"QueryTreeNodesNode Type 0 Directory node", "zh_CN":"节点类型 0 目录节点"}
        self.node_type = node_type

    def validate(self):
        self.validate_required(self.node_id, 'node_id')
        self.validate_required(self.node_name, 'node_name')
        self.validate_required(self.node_type, 'node_type')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.node_name is not None:
            result['nodeName'] = self.node_name
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('nodeName') is not None:
            self.node_name = m.get('nodeName')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        return self


class QueryTreeNodesResponse(TeaModel):
    def __init__(
        self,
        rows: List[QueryTreeNodesNode] = None,
        total: int = None,
    ):
        # {"en":"QueryTreeNodesNode List", "zh_CN":"节点列表"}
        self.rows = rows
        # {"en":"Total number of devices", "zh_CN":"总设备数"}
        self.total = total

    def validate(self):
        self.validate_required(self.rows, 'rows')
        if self.rows:
            for k in self.rows:
                if k:
                    k.validate()
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
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('rows') is not None:
            self.rows = []
            for k in m.get('rows'):
                temp_model = QueryTreeNodesNode()
                self.rows.append(temp_model.from_map(k))
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class QueryTreeNodesPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTreeNodesParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTreeNodesRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryTreeNodesResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




