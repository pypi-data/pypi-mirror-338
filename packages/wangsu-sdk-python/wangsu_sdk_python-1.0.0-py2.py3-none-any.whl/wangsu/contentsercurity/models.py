# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class ImageAuditImgDto(TeaModel):
    def __init__(
        self,
        content: str = None,
        bt_id: str = None,
    ):
        # {"en":"content", "zh_CN":"上传要检测的图片，支持两种方式：
        # 1、上传图片，图片必须是base64格式编码；
        # 2、上传图片的URL；
        # 上传的图片只支持如下格式：jpg，jpeg，png，webp，gif，tiff，tif, hief，建议图片像素不小于256*256，目前最低支持20*20分辨率的图片。"}
        self.content = content
        # {"en":"btId", "zh_CN":"图⽚唯⼀标识,同⼀次请求中不可重复，btId⻓度 在30以内"}
        self.bt_id = bt_id

    def validate(self):
        self.validate_required(self.content, 'content')
        self.validate_required(self.bt_id, 'bt_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.bt_id is not None:
            result['btId'] = self.bt_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('btId') is not None:
            self.bt_id = m.get('btId')
        return self


class ImageAuditRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        audit_type: str = None,
        app_type: str = None,
        precision: str = None,
        images: List[ImageAuditImgDto] = None,
    ):
        # {"en":"userName", "zh_CN":"客户登陆账号"}
        self.user_name = user_name
        # {"en":"Non-mandatory field. If left blank, all categories are assumed. This field pertains to image audit category and supports multiple configurations. The categories include POLITY: political identification; VIOLENT: violent, terrorist, and prohibited identification; EROTIC: pornography identification; ADVERT: advertising identification; IMGTEXTRISK: image and text OCR identification. Multiple underscores are used to separate them. For example, all: POLITY_VIOLENT_EROTIC_ADVERT_IMGTEXTRISK", "zh_CN":"非必填项，为空默认是全部。图片审计类别，支持配置多个。POLITY：涉政识别； VIOLENT：暴恐违禁识别；EROTIC：色情识别；ADVERT：广告识别；IMGTEXTRISK：图文OCR识别；多个下划线分隔。例如全部：POLITY_VIOLENT_EROTIC_ADVERT_IMGTEXTRISK"}
        self.audit_type = audit_type
        # {"en":"This field is optional, and the default value is set to 'default'. If the customer has specific requirements for detection rules, Wangsu will need to provide them separately.", "zh_CN":"非必填项，默认值为“default”。若客户有特殊的检测规则要求，则需要网宿单独分配提供。"}
        self.app_type = app_type
        # {"en":"Optional, precision requirement, default value is 'balance'. Optional values are: balance (balanced recall), recall (high recall), precise (high accuracy)", "zh_CN":"非必填项，精度要求，默认值为“balance”。可选值为：balance（准召平衡）、recall（高召回）、precise（高准确）"}
        self.precision = precision
        # {"en":"The picture array contains picture content and picture IDs. Each picture ID cannot be repeated in a single request. A maximum of 12 pictures can be uploaded in one request.", "zh_CN":"图片数组：里面含图片内容，图片Id。图片Id一次请求内不能重复，一次请求最多可上传12张图片。"}
        self.images = images

    def validate(self):
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.images, 'images')
        if self.images:
            for k in self.images:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.audit_type is not None:
            result['auditType'] = self.audit_type
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.precision is not None:
            result['precision'] = self.precision
        if self.images is not None:
            result['images'] = []
            for k in self.images:
                result['images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('auditType') is not None:
            self.audit_type = m.get('auditType')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('precision') is not None:
            self.precision = m.get('precision')
        if m.get('images') is not None:
            self.images = []
            for k in m.get('images'):
                temp_model = ImageAuditImgDto()
                self.images.append(temp_model.from_map(k))
        return self


class ImageAuditImgQueryResp(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        bt_id: str = None,
        code: str = None,
        message: str = None,
        risk_level: str = None,
        risk_label: str = None,
        risk_description: str = None,
        ocr_text: str = None,
    ):
        # {"en":"requestId", "zh_CN":"网宿返回的请求id"}
        self.request_id = request_id
        # {"en":"btId", "zh_CN":"图⽚唯⼀标识,同⼀次请求中不可重复"}
        self.bt_id = bt_id
        # {"en":"code", "zh_CN":"此图片审计结果的返回码"}
        self.code = code
        # {"en":"message", "zh_CN":"此图片审计结果的返回信息，和code对应"}
        self.message = message
        # {"en":"riskLevel", "zh_CN":"审计结果，PASS ：正常，建议直接放行；REVIEW ：可疑，建议人工审核； REJECT ：违规，建议直接拦截"}
        self.risk_level = risk_level
        # {"en":"riskLabel", "zh_CN":"风险标签 涉政：politics,暴恐:violence,色情:porn,违禁:ban,辱骂:abuse,广告法:ad_law,广告:ad,黑名单:blacklist,无意义:meaningless,隐私:privacy,网络诈骗:fraud,未成年人:minor"}
        self.risk_label = risk_label
        # {"en":"riskDescription", "zh_CN":"风险原因"}
        self.risk_description = risk_description
        # {"en":"ocrText", "zh_CN":"返回图⽚中违规⽂字相关信息，当请求参数type字段包含OCR时存在"}
        self.ocr_text = ocr_text

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.bt_id, 'bt_id')
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.risk_level, 'risk_level')
        self.validate_required(self.risk_label, 'risk_label')
        self.validate_required(self.risk_description, 'risk_description')
        self.validate_required(self.ocr_text, 'ocr_text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.bt_id is not None:
            result['btId'] = self.bt_id
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.risk_label is not None:
            result['riskLabel'] = self.risk_label
        if self.risk_description is not None:
            result['riskDescription'] = self.risk_description
        if self.ocr_text is not None:
            result['ocrText'] = self.ocr_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('btId') is not None:
            self.bt_id = m.get('btId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('riskLabel') is not None:
            self.risk_label = m.get('riskLabel')
        if m.get('riskDescription') is not None:
            self.risk_description = m.get('riskDescription')
        if m.get('ocrText') is not None:
            self.ocr_text = m.get('ocrText')
        return self


class ImageAuditResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        imgs: List[ImageAuditImgQueryResp] = None,
    ):
        # {"en":"code", "zh_CN":"请求返回码，1100成功，其他是8位失败码"}
        self.code = code
        # {"en":"message", "zh_CN":"错误码具体信息描述"}
        self.message = message
        # {"en":"requestId", "zh_CN":"网宿生成的请求唯一id"}
        self.request_id = request_id
        # {"en":"imgs", "zh_CN":"查询结果"}
        self.imgs = imgs

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.imgs, 'imgs')
        if self.imgs:
            for k in self.imgs:
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.imgs is not None:
            result['imgs'] = []
            for k in self.imgs:
                result['imgs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('imgs') is not None:
            self.imgs = []
            for k in m.get('imgs'):
                temp_model = ImageAuditImgQueryResp()
                self.imgs.append(temp_model.from_map(k))
        return self


class ImageAuditPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ImageAuditParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ImageAuditRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class ImageAuditResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self






class TextAuditRequest(TeaModel):
    def __init__(
        self,
        user_name: str = None,
        lang: str = None,
        text: str = None,
        business_type: str = None,
        app_type: str = None,
    ):
        # {"en":"userName", "zh_CN":"客户登陆账号"}
        self.user_name = user_name
        # {"en":"lang", "zh_CN":"业务类别，当前支持： zh-中文文本审计；en-英文文本审计；ar-阿语文本审计；传值zh或en或ar"}
        self.lang = lang
        # {"en":"text", "zh_CN":"要审计的文本内容"}
        self.text = text
        # {"en":"businessType", "zh_CN":"非必填项，配置是否针对“未成年人”进行审计,若需要 则填写固定值为：MINOR"}
        self.business_type = business_type
        # {"en":"appType", "zh_CN":"应用类型：非必填项，默认值为“default”。
        # 若客户有特殊的检测规则要求，则需要网宿单独分配提供。"}
        self.app_type = app_type

    def validate(self):
        self.validate_required(self.user_name, 'user_name')
        self.validate_required(self.lang, 'lang')
        self.validate_required(self.text, 'text')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_name is not None:
            result['userName'] = self.user_name
        if self.lang is not None:
            result['lang'] = self.lang
        if self.text is not None:
            result['text'] = self.text
        if self.business_type is not None:
            result['businessType'] = self.business_type
        if self.app_type is not None:
            result['appType'] = self.app_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userName') is not None:
            self.user_name = m.get('userName')
        if m.get('lang') is not None:
            self.lang = m.get('lang')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('businessType') is not None:
            self.business_type = m.get('businessType')
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        return self


class TextAuditResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        risk_level: str = None,
        risk_label: str = None,
        risk_description: str = None,
    ):
        # {"en":"code", "zh_CN":"请求返回码，1100成功，其他是8位失败码"}
        self.code = code
        # {"en":"message", "zh_CN":"错误码具体信息描述"}
        self.message = message
        # {"en":"requestId", "zh_CN":"ws生成的请求唯一id"}
        self.request_id = request_id
        # {"en":"riskLevel", "zh_CN":"审计结果，PASS ：正常，建议直接放行；REVIEW ：可疑，建议人工审核； REJECT ：违规，建议直接拦截"}
        self.risk_level = risk_level
        # {"en":"riskLabel", "zh_CN":"一级风险标签：涉政:politics,暴恐:violence,色情:porn,违禁:ban,辱骂:abuse,广告法:ad_law,广告:ad,黑名单:blacklist,无意义:meaningless,隐私:privacy,网络诈骗:fraud,未成年人:minor"}
        self.risk_label = risk_label
        # {"en":"riskDescription", "zh_CN":"风险原因"}
        self.risk_description = risk_description

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.message, 'message')
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.risk_level, 'risk_level')
        self.validate_required(self.risk_label, 'risk_label')
        self.validate_required(self.risk_description, 'risk_description')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level
        if self.risk_label is not None:
            result['riskLabel'] = self.risk_label
        if self.risk_description is not None:
            result['riskDescription'] = self.risk_description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')
        if m.get('riskLabel') is not None:
            self.risk_label = m.get('riskLabel')
        if m.get('riskDescription') is not None:
            self.risk_description = m.get('riskDescription')
        return self


class TextAuditPaths(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class TextAuditParameters(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class TextAuditRequestHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class TextAuditResponseHeader(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self




