# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class DeleteAWebhookPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en" : "ID of a webhook", "zh_CN": "webhook接口id。"}
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


class DeleteAWebhookParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAWebhookRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAWebhookRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAWebhookResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class DeleteAWebhookResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class UpdateAWebhookPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en" : "ID of a webhook", "zh_CN": "webhook接口id。"}
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


class UpdateAWebhookParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAWebhookRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAWebhookRequestCredentials(TeaModel):
    def __init__(
        self,
        user: str = None,
        secret_key: str = None,
    ):
        # {"en" : "The username passed to the URL on your server.", "zh_CN": "用于鉴权的用户名。"}
        self.user = user
        # {"en" : "A string that is encoded with the date and passed in the Authorization header to your server.", "zh_CN": "用于鉴权的密钥。CDN Pro将用当期日期对密钥进行加密生成密码(password)，然后通过Authorization请求头传给你方服务器。"}
        self.secret_key = secret_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['user'] = self.user
        if self.secret_key is not None:
            result['secretKey'] = self.secret_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')
        return self


class UpdateAWebhookRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        url: str = None,
        credentials: UpdateAWebhookRequestCredentials = None,
    ):
        # {"en" : "Range: <= 250 characters 
        # Name of the webhook.", "zh_CN": "取值范围: <= 250 字符 
        # webhook接口名称。"}
        self.name = name
        # {"en" : "Range: <= 500 characters 
        # An optional description of the webhook.", "zh_CN": "取值范围: <= 500 字符 
        # webhook接口描述。"}
        self.description = description
        # {"en" : "Range: <= 250 characters 
        # That URL that will be called when the asynchronous task has completed. The HTTP POST method will be used. The body will in JSON format:
        # 
        # { 'subject': '{some text}',
        #   'taskType': '{task type}',
        #   'taskList': [
        #     { 'taskId': '{task id 1}',
        #       ...
        #     },
        #     { 'taskId': '{task id 2}',
        #       ...
        #     }
        #   ]
        # }
        # ", "zh_CN": "取值范围: <= 250 字符 
        # 当关联的异步任务执行完成时，需触发的webhook接口的地址。CDN Pro将使用HTTP POST方法调webhook接口，请求体为JSON格式。请求体示例：
        # 
        # { 'subject': '{some text}',
        #   'taskType': '{task type}',
        #   'taskList': [
        #     { 'taskId': '{task id 1}',
        #       ...
        #     },
        #     { 'taskId': '{task id 2}',
        #       ...
        #     }
        #   ]
        # }
        # "}
        self.url = url
        # {"en" : "Optional credentials passed to the URL. If requiring credentials your server should support HTTP Basic authentication the same way we do. Refer to Authentication summary. In particular, the password will be the secretKey encoded with the current date.", "zh_CN": "用于鉴权的账号信息。当您的服务器有鉴权要求时，需支持HTTP Basic鉴权方式。CDN Pro将用当前日期对secretKey进行加密，生成密码(password)。"}
        self.credentials = credentials

    def validate(self):
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.url is not None:
            result['url'] = self.url
        if self.credentials is not None:
            result['credentials'] = self.credentials.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('credentials') is not None:
            temp_model = UpdateAWebhookRequestCredentials()
            self.credentials = temp_model.from_map(m['credentials'])
        return self


class UpdateAWebhookResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class UpdateAWebhookResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class CreateAWebhookPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAWebhookParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAWebhookRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAWebhookRequestCredentials(TeaModel):
    def __init__(
        self,
        user: str = None,
        secret_key: str = None,
    ):
        # {"en" : "The username passed to the URL on your server.", "zh_CN": "用于鉴权的用户名。"}
        self.user = user
        # {"en" : "A string that is encoded with the date and passed in the Authorization header to your server.", "zh_CN": "用于鉴权的密钥。CDN Pro将用当期日期对密钥进行加密生成密码(password)，然后通过Authorization请求头传给你方服务器。"}
        self.secret_key = secret_key

    def validate(self):
        self.validate_required(self.user, 'user')
        self.validate_required(self.secret_key, 'secret_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['user'] = self.user
        if self.secret_key is not None:
            result['secretKey'] = self.secret_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')
        return self


class CreateAWebhookRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        url: str = None,
        credentials: CreateAWebhookRequestCredentials = None,
    ):
        # {"en" : "Range: <= 250 characters 
        # Name of the webhook.", "zh_CN": "取值范围: <= 250 字符 
        # webhook接口名称。"}
        self.name = name
        # {"en" : "Range: <= 500 characters 
        # Optional description of the webhook.", "zh_CN": "取值范围: <= 500 字符 
        # webhook接口描述。"}
        self.description = description
        # {"en" : "Range: <= 250 characters 
        # That URL that will be called when the asynchronous task has completed. The HTTP POST method will be used. The body will in JSON format:
        # 
        # { 'subject': '{some text}',
        #   'taskType': '{task type}',
        #   'taskList': [
        #     { 'taskId': '{task id 1}',
        #       ...
        #     },
        #     { 'taskId': '{task id 2}',
        #       ...
        #     }
        #   ]
        # }
        # ", "zh_CN": "取值范围: <= 250 字符 
        # 当关联的异步任务执行完成时，需触发的webhook接口的地址。CDN Pro将使用HTTP POST方法调用webhook接口，请求体为JSON格式。请求体示例：
        # 
        # { 'subject': '{some text}',
        #   'taskType': '{task type}',
        #   'taskList': [
        #     { 'taskId': '{task id 1}',
        #       ...
        #     },
        #     { 'taskId': '{task id 2}',
        #       ...
        #     }
        #   ]
        # }
        # "}
        self.url = url
        # {"en" : "Optional credentials passed to the URL. If requiring credentials your server should support HTTP Basic authentication the same way we do. Refer to Authentication summary. In particular, the password will be the secretKey encoded with the current date.", "zh_CN": "用于鉴权的账号信息。当您的服务器有鉴权要求时，需支持HTTP Basic鉴权方式。CDN Pro将用当前日期对secretKey进行加密，生成密码(password)。以下是一个secretKey加密和webhook接口调用的示例：
        # 
        # <pre>
        # #!/bin/bash
        # 
        # # 鉴权账号
        # USER=YourUser
        # SECRET_KEY=YourSecretKey
        # 
        # DATE=`date '+%a, %d %b %Y %H:%M:%S %Z'`
        # echo $DATE
        # 
        # # 生成密码
        # password=$(echo -n '$DATE' | openssl dgst -sha1 -hmac '$SECRET_KEY' -binary | base64)
        # echo ' '
        # 
        # # 调用webhook接口
        # apiCall='curl -i --url
        #  'https://a.webhook.com'
        # 	-X POST \n	-u $USER:$password \n	-H 'Date: $DATE' \n        -H 'Content-Type: application/json' \n        -d '{
        #                 ...
        #             }' \n        '
        # eval $apiCall
        # </pre>"}
        self.credentials = credentials

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.url, 'url')
        if self.credentials:
            self.credentials.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.url is not None:
            result['url'] = self.url
        if self.credentials is not None:
            result['credentials'] = self.credentials.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('credentials') is not None:
            temp_model = CreateAWebhookRequestCredentials()
            self.credentials = temp_model.from_map(m['credentials'])
        return self


class CreateAWebhookResponse(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class CreateAWebhookResponseHeader(TeaModel):
    def __init__(
        self,
        location: str = None,
    ):
        # {"en":"Refers to the new webhook. Example: <code>Location: https://{domain}/cdn/webhooks/60a2e69806d5583a81ad9500</code>
        # ", "zh_CN":"通过Location响应头返回新建的wehbook的地址。地址中包含webhook的ID，可使用该ID调用获取‘webhook详细信息’接口来查看webhook的详细信息。URL示例：<code>Location: https://{domain}/cdn/webhooks/60a2e69806d5583a81ad9500</code>"}
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






class GetAWebhookPaths(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # {"en" : "ID of a webhook", "zh_CN": "webhook接口id。"}
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


class GetAWebhookParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAWebhookRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAWebhookRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAWebhookResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAWebhookResponseCredentials(TeaModel):
    def __init__(
        self,
        user: str = None,
        secret_key: str = None,
    ):
        # {"en" : "The username passed to the URL on your server.", "zh_CN": "用于鉴权的用户名。"}
        self.user = user
        # {"en" : "A string that is encoded with the date and passed in the Authorization header to your server.", "zh_CN": "用于鉴权的密钥。CDN Pro将用当期日期对密钥进行加密生成密码(password)，然后通过Authorization请求头传给你方服务器。"}
        self.secret_key = secret_key

    def validate(self):
        self.validate_required(self.user, 'user')
        self.validate_required(self.secret_key, 'secret_key')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['user'] = self.user
        if self.secret_key is not None:
            result['secretKey'] = self.secret_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user') is not None:
            self.user = m.get('user')
        if m.get('secretKey') is not None:
            self.secret_key = m.get('secretKey')
        return self


class GetAWebhookResponseMetaData(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        last_updatetime: str = None,
        last_call_time: str = None,
        total_calls: int = None,
    ):
        # {"en" : "RFC 3339 date indicating when the webhook was created.", "zh_CN": "webhook接口创建时间，以RFC 3339日期格式展示。"}
        self.creation_time = creation_time
        # {"en" : "RFC 3339 date indicating when the webhook was last updated.", "zh_CN": "webhook接口最近一次更新的时间，以RFC 3339日期格式展示。"}
        self.last_updatetime = last_updatetime
        # {"en" : "RFC 3339 date indicating when the webhook was last called", "zh_CN": "webhook接口最近一次调用的时间，以RFC 3339日期格式展示。"}
        self.last_call_time = last_call_time
        # {"en" : "Range: >= 0 
        # Number of times the webhook has been called.", "zh_CN": "取值范围: >= 0 
        # webhook接口累计被调用的次数。"}
        self.total_calls = total_calls

    def validate(self):
        self.validate_required(self.creation_time, 'creation_time')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creation_time is not None:
            result['creationTime'] = self.creation_time
        if self.last_updatetime is not None:
            result['lastUpdatetime'] = self.last_updatetime
        if self.last_call_time is not None:
            result['lastCallTime'] = self.last_call_time
        if self.total_calls is not None:
            result['totalCalls'] = self.total_calls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')
        if m.get('lastUpdatetime') is not None:
            self.last_updatetime = m.get('lastUpdatetime')
        if m.get('lastCallTime') is not None:
            self.last_call_time = m.get('lastCallTime')
        if m.get('totalCalls') is not None:
            self.total_calls = m.get('totalCalls')
        return self


class GetAWebhookResponse(TeaModel):
    def __init__(
        self,
        name: str = None,
        description: str = None,
        url: str = None,
        credentials: GetAWebhookResponseCredentials = None,
        meta_data: GetAWebhookResponseMetaData = None,
    ):
        # {"en" : "Range: <= 250 characters 
        # Name of the webhook.", "zh_CN": "取值范围: <= 250 字符 
        # webhook接口名称。"}
        self.name = name
        # {"en" : "Range: <= 500 characters 
        # An optional description of the webhook.", "zh_CN": "取值范围: <= 500 字符 
        # webhook接口描述。"}
        self.description = description
        # {"en" : "Range: <= 250 characters 
        # That URL that will be called when the asynchronous task has completed. The HTTP POST method will be used. The body will in JSON format:
        # 
        # { 'subject': '{some text}',
        #   'taskType': '{task type}',
        #   'taskList': [
        #     { 'taskId': '{task id 1}',
        #       ...
        #     },
        #     { 'taskId': '{task id 2}',
        #       ...
        #     }
        #   ]
        # }
        # 
        # ", "zh_CN": "取值范围: <= 250 字符 
        # 当关联的异步任务执行完成时，需触发的webhook接口的地址。CDN Pro将使用HTTP POST方法调webhook接口，请求体为JSON格式。请求体示例：
        # 
        # { 'subject': '{some text}',
        #   'taskType': '{task type}',
        #   'taskList': [
        #     { 'taskId': '{task id 1}',
        #       ...
        #     },
        #     { 'taskId': '{task id 2}',
        #       ...
        #     }
        #   ]
        # }
        # 
        # "}
        self.url = url
        # {"en" : "Optional credentials passed to the URL. If requiring credentials your server should support HTTP Basic authentication the same way we do. Refer to Authentication summary. In particular, the password will be the secretKey encoded with the current date.", "zh_CN": "用于鉴权的账号信息。当您的服务器有鉴权要求时，需支持HTTP Basic鉴权方式。CDN Pro将用当前日期对secretKey进行加密，生成密码(password)。"}
        self.credentials = credentials
        # {"en" : "", "zh_CN": ""}
        self.meta_data = meta_data

    def validate(self):
        self.validate_required(self.name, 'name')
        self.validate_required(self.description, 'description')
        self.validate_required(self.url, 'url')
        self.validate_required(self.credentials, 'credentials')
        if self.credentials:
            self.credentials.validate()
        self.validate_required(self.meta_data, 'meta_data')
        if self.meta_data:
            self.meta_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.description is not None:
            result['description'] = self.description
        if self.url is not None:
            result['url'] = self.url
        if self.credentials is not None:
            result['credentials'] = self.credentials.to_map()
        if self.meta_data is not None:
            result['metaData'] = self.meta_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('url') is not None:
            self.url = m.get('url')
        if m.get('credentials') is not None:
            temp_model = GetAWebhookResponseCredentials()
            self.credentials = temp_model.from_map(m['credentials'])
        if m.get('metaData') is not None:
            temp_model = GetAWebhookResponseMetaData()
            self.meta_data = temp_model.from_map(m['metaData'])
        return self






class GetAListOfWebhooksPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfWebhooksParameters(TeaModel):
    def __init__(
        self,
        offset: int = None,
        limit: int = None,
    ):
        # {"en" : "Range: >= 0 
        # Index of the first webhook to return.", "zh_CN": "默认值: 0 取值范围: >= 0 
        # 查询起始位置。"}
        self.offset = offset
        # {"en" : "Default: 100 Range: [ 1 .. 200 ] 
        # Maximum number of webhooks to return.", "zh_CN": "默认值: 100 取值范围: <= 200 
        # 每次查询的最大条数。"}
        self.limit = limit

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class GetAListOfWebhooksRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfWebhooksRequest(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfWebhooksResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetAListOfWebhooksResponseWebooks(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        description: str = None,
        creation_time: str = None,
        last_update_time: str = None,
        last_call_time: str = None,
        total_calls: int = None,
        has_credentials: bool = None,
    ):
        # {"en" : "ID of the webhook.", "zh_CN": "webhook接口ID。"}
        self.id = id
        # {"en" : "Range: <= 250 characters 
        # Name of the webhook.", "zh_CN": "取值范围: <= 250 字符 
        # webhook接口名称。"}
        self.name = name
        # {"en" : "Range: <= 500 characters 
        # An optional description of the webhook.", "zh_CN": "取值范围: <= 500 字符 
        # webhook接口描述。"}
        self.description = description
        # {"en" : "RFC 3339 date indicating when the webhook was created.", "zh_CN": "webhook接口创建时间，以RFC 3339日期格式展示。"}
        self.creation_time = creation_time
        # {"en" : "RFC 3339 date indicating when the webhook was last updated.", "zh_CN": "webhook接口最近一次更新时间，以RFC 3339日期格式展示。"}
        self.last_update_time = last_update_time
        # {"en" : "RFC 3339 date indicating when the webhook was last called.", "zh_CN": "webhook接口最近一次调用时间，以RFC 3339日期格式展示。"}
        self.last_call_time = last_call_time
        # {"en" : "Range: >= 0 
        # Total number of times the webhook has been called.", "zh_CN": "取值范围: >= 0 
        # webhook接口累计被调用的次数。"}
        self.total_calls = total_calls
        # {"en" : "Whether the webhook requires credentials to access.", "zh_CN": "是否要求鉴权。"}
        self.has_credentials = has_credentials

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
        if self.last_call_time is not None:
            result['lastCallTime'] = self.last_call_time
        if self.total_calls is not None:
            result['totalCalls'] = self.total_calls
        if self.has_credentials is not None:
            result['hasCredentials'] = self.has_credentials
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
        if m.get('lastCallTime') is not None:
            self.last_call_time = m.get('lastCallTime')
        if m.get('totalCalls') is not None:
            self.total_calls = m.get('totalCalls')
        if m.get('hasCredentials') is not None:
            self.has_credentials = m.get('hasCredentials')
        return self


class GetAListOfWebhooksResponse(TeaModel):
    def __init__(
        self,
        count: int = None,
        webooks: List[GetAListOfWebhooksResponseWebooks] = None,
    ):
        # {"en" : "Range: >= 0 
        # Total number of webhooks. The number returned in the webhooks array may be fewer depending on your query parameters.", "zh_CN": "取值范围: >= 0 
        # webhook接口数量，该数量与查询参数直接相关。"}
        self.count = count
        # {"en" : "", "zh_CN": ""}
        self.webooks = webooks

    def validate(self):
        self.validate_required(self.count, 'count')
        self.validate_required(self.webooks, 'webooks')
        if self.webooks:
            for k in self.webooks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.webooks is not None:
            result['webooks'] = []
            for k in self.webooks:
                result['webooks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('webooks') is not None:
            self.webooks = []
            for k in m.get('webooks'):
                temp_model = GetAListOfWebhooksResponseWebooks()
                self.webooks.append(temp_model.from_map(k))
        return self




