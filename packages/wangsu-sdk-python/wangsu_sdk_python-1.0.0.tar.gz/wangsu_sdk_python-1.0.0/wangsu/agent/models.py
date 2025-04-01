# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class AgencyQuerySaleOrderDetailRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        offer_codes: List[str] = None,
        resource_ids: List[str] = None,
    ):
        # {"en":"account", "zh_CN":"账号"}
        self.account = account
        # {"en":"Item code list. If it is blank, it means all, and multiple means that any one condition is satisfied.", "zh_CN":"商品编码列表。为空表示全部，多个表示满足任意一个条件即可。"}
        self.offer_codes = offer_codes
        # {"en":"List of resource IDs. If it is blank, it means all, and multiple means that any one condition is satisfied.", "zh_CN":"资源ID列表。为空表示全部，多个表示满足任意一个条件即可。"}
        self.resource_ids = resource_ids

    def validate(self):
        self.validate_required(self.account, 'account')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account
        if self.offer_codes is not None:
            result['offerCodes'] = self.offer_codes
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('offerCodes') is not None:
            self.offer_codes = m.get('offerCodes')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        return self


class AgencyQuerySaleOrderDetailServiceOrderDto(TeaModel):
    def __init__(
        self,
        service_order_id: str = None,
        product_code: str = None,
        pay_area: str = None,
    ):
        # {"en":"Service order ID", "zh_CN":"服务订单ID"}
        self.service_order_id = service_order_id
        # {"en":"Product code", "zh_CN":"产品编码"}
        self.product_code = product_code
        # {"en":"Billing area", "zh_CN":"计费区域"}
        self.pay_area = pay_area

    def validate(self):
        self.validate_required(self.service_order_id, 'service_order_id')
        self.validate_required(self.product_code, 'product_code')
        self.validate_required(self.pay_area, 'pay_area')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_order_id is not None:
            result['serviceOrderId'] = self.service_order_id
        if self.product_code is not None:
            result['productCode'] = self.product_code
        if self.pay_area is not None:
            result['payArea'] = self.pay_area
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceOrderId') is not None:
            self.service_order_id = m.get('serviceOrderId')
        if m.get('productCode') is not None:
            self.product_code = m.get('productCode')
        if m.get('payArea') is not None:
            self.pay_area = m.get('payArea')
        return self


class AgencyQuerySaleOrderDetailQueryOrderSpecDto(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
        unit_code: str = None,
    ):
        # {"en":"Attribute code", "zh_CN":"属性编码"}
        self.code = code
        # {"en":"Attribute value", "zh_CN":"属性值"}
        self.value = value
        # {"en":"Attribute unit code", "zh_CN":"属性单位编码"}
        self.unit_code = unit_code

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.value, 'value')
        self.validate_required(self.unit_code, 'unit_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.value is not None:
            result['value'] = self.value
        if self.unit_code is not None:
            result['unitCode'] = self.unit_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('unitCode') is not None:
            self.unit_code = m.get('unitCode')
        return self


class AgencyQuerySaleOrderDetailOrderDetailInfo(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        resource_id: str = None,
        service_orders: List[AgencyQuerySaleOrderDetailServiceOrderDto] = None,
        eff_date: str = None,
        exp_date: str = None,
        order_state: str = None,
        offer_code: str = None,
        product_code_list: List[str] = None,
        datacenter_code: str = None,
        specifications: List[AgencyQuerySaleOrderDetailQueryOrderSpecDto] = None,
    ):
        # {"en":"order ID", "zh_CN":"订单ID"}
        self.order_id = order_id
        # {"en":"resource ID", "zh_CN":"资源ID"}
        self.resource_id = resource_id
        # {"en":"service order list", "zh_CN":"服务订单列表"}
        self.service_orders = service_orders
        # {"en":"Effective time (timestamp, millisecond)", "zh_CN":"生效时间（时间戳，毫秒）"}
        self.eff_date = eff_date
        # {"en":"Expiration time: (timestamp, millisecond) time of expiration or destruction. May be empty. After the resource configuration is changed, the last order will be set with an expiration time equal to the effective time of the new order minus one second", "zh_CN":"失效时间：（时间戳，毫秒）失效或销毁时间。可能为空。资源变更配置后，上一个订单会被设置失效时间，并等于新订单的生效时间减一秒"}
        self.exp_date = exp_date
        # {"en":"Order status. (after changing the configuration, the status of the previous order will automatically change to destroyed.)
        #     OSA pretreatment
        #     OSC pending
        #     OSD destroy
        #     OSH in process
        #     OSN OK", 
        #     "zh_CN":"订单状态。（变更配置后，前一个订单状态也会自动变成销毁）
        #     OSA-预处理
        #     OSC-挂起
        #     OSD-销毁 
        #     OSH-处理中
        #     OSN正常"}
        self.order_state = order_state
        # {"en":"Offer code, corresponding to the offers->name transmitted when generating resources", "zh_CN":"商品编码，对应生成资源时传过来的offers->name"}
        self.offer_code = offer_code
        # {"en":"List of product codes. Solution offers will one offer corresponds to multiple products", "zh_CN":"产品编码列表。解决方案一个商品会对应多个产品"}
        self.product_code_list = product_code_list
        # {"en":"Data center code", "zh_CN":"数据中心编码"}
        self.datacenter_code = datacenter_code
        # {"en":"Commodity specifications Show only CBSs internal interface_ Specification attribute of display='T' ",   "zh_CN":"商品规格.只展示CBSS内部interface_display= 'T' 的规格属性"}
        self.specifications = specifications

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.service_orders, 'service_orders')
        if self.service_orders:
            for k in self.service_orders:
                if k:
                    k.validate()
        self.validate_required(self.eff_date, 'eff_date')
        self.validate_required(self.exp_date, 'exp_date')
        self.validate_required(self.order_state, 'order_state')
        self.validate_required(self.offer_code, 'offer_code')
        self.validate_required(self.product_code_list, 'product_code_list')
        self.validate_required(self.datacenter_code, 'datacenter_code')
        self.validate_required(self.specifications, 'specifications')
        if self.specifications:
            for k in self.specifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.service_orders is not None:
            result['serviceOrders'] = []
            for k in self.service_orders:
                result['serviceOrders'].append(k.to_map() if k else None)
        if self.eff_date is not None:
            result['effDate'] = self.eff_date
        if self.exp_date is not None:
            result['expDate'] = self.exp_date
        if self.order_state is not None:
            result['orderState'] = self.order_state
        if self.offer_code is not None:
            result['offerCode'] = self.offer_code
        if self.product_code_list is not None:
            result['productCodeList'] = self.product_code_list
        if self.datacenter_code is not None:
            result['datacenterCode'] = self.datacenter_code
        if self.specifications is not None:
            result['specifications'] = []
            for k in self.specifications:
                result['specifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('serviceOrders') is not None:
            self.service_orders = []
            for k in m.get('serviceOrders'):
                temp_model = AgencyQuerySaleOrderDetailServiceOrderDto()
                self.service_orders.append(temp_model.from_map(k))
        if m.get('effDate') is not None:
            self.eff_date = m.get('effDate')
        if m.get('expDate') is not None:
            self.exp_date = m.get('expDate')
        if m.get('orderState') is not None:
            self.order_state = m.get('orderState')
        if m.get('offerCode') is not None:
            self.offer_code = m.get('offerCode')
        if m.get('productCodeList') is not None:
            self.product_code_list = m.get('productCodeList')
        if m.get('datacenterCode') is not None:
            self.datacenter_code = m.get('datacenterCode')
        if m.get('specifications') is not None:
            self.specifications = []
            for k in m.get('specifications'):
                temp_model = AgencyQuerySaleOrderDetailQueryOrderSpecDto()
                self.specifications.append(temp_model.from_map(k))
        return self


class AgencyQuerySaleOrderDetailResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: List[AgencyQuerySaleOrderDetailOrderDetailInfo] = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message
        # {"en":"Response data array.", "zh_CN":"接口响应数据"}
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
                temp_model = AgencyQuerySaleOrderDetailOrderDetailInfo()
                self.data.append(temp_model.from_map(k))
        return self


class AgencyQuerySaleOrderDetailPaths(TeaModel):
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


class AgencyQuerySaleOrderDetailParameters(TeaModel):
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


class AgencyQuerySaleOrderDetailRequestHeader(TeaModel):
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


class AgencyQuerySaleOrderDetailResponseHeader(TeaModel):
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






class AgencyCreateResourceSpecification(TeaModel):
    def __init__(
        self,
        code: str = None,
        value: str = None,
    ):
        # {"en":"product specification code", "zh_CN":"产品规格编码"}
        self.code = code
        # {"en":"product specification value", "zh_CN":"产品规格值"}
        self.value = value

    def validate(self):
        self.validate_required(self.code, 'code')
        self.validate_required(self.value, 'value')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AgencyCreateResourceOffer(TeaModel):
    def __init__(
        self,
        offer_code: str = None,
        quantity: str = None,
        resource_ids: List[str] = None,
        due_time: str = None,
        specifications: List[AgencyCreateResourceSpecification] = None,
    ):
        # {"en":"offer code", "zh_CN":"商品编码"}
        self.offer_code = offer_code
        # {"en":"The number of resources to be activated in batches (1 by default). Each resource will return an orderId",
        #    "zh_CN":"批量开通资源数量（默认为1）。每个资源会返回一个orderId"}
        self.quantity = quantity
        # {"en":"List of resource IDs. Each quantity needs to be assigned a resource ID. If empty, CBSS generates UUID by itself. If non-null, the number of resource IDs must be the same as quantity", 
        #    "zh_CN":"资源ID列表。每个quantity需要配一个资源ID。如果为空，CBSS自行生成UUID。如果非空，资源ID个数必须和quantity一样"}
        self.resource_ids = resource_ids
        # {"en":"Expiration timestamp. The expiration time of this order. If it is empty, cbss interprets it as 2099",
        #    "zh_CN":"到期时间戳。此次订单的到期时间。为空的话，cbss解释为2099年"}
        self.due_time = due_time
        # {"en":"list of configuration items", "zh_CN":"配置项列表"}
        self.specifications = specifications

    def validate(self):
        self.validate_required(self.offer_code, 'offer_code')
        if self.specifications:
            for k in self.specifications:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.offer_code is not None:
            result['offerCode'] = self.offer_code
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.due_time is not None:
            result['dueTime'] = self.due_time
        if self.specifications is not None:
            result['specifications'] = []
            for k in self.specifications:
                result['specifications'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('offerCode') is not None:
            self.offer_code = m.get('offerCode')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('dueTime') is not None:
            self.due_time = m.get('dueTime')
        if m.get('specifications') is not None:
            self.specifications = []
            for k in m.get('specifications'):
                temp_model = AgencyCreateResourceSpecification()
                self.specifications.append(temp_model.from_map(k))
        return self


class AgencyCreateResourceRequest(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        account: str = None,
        operator: str = None,
        operate_time: str = None,
        offer: List[AgencyCreateResourceOffer] = None,
    ):
        # {"en":"requestId", "zh_CN":"请求Id，同一个请求的唯一标志，可用于查询该请求"}
        self.request_id = request_id
        # {"en":"account", "zh_CN":"用户主账号"}
        self.account = account
        # {"en":"operator", "zh_CN":"操作员"}
        self.operator = operator
        # {"en":"Operation timestamp (order opening time), accurate to milliseconds,Suggested vacancies, cbss will fill in the system time", 
        # 	"zh_CN":"操作时间戳（订单开通时间），精确到毫秒，建议空缺，cbss会以系统时间填入"}
        self.operate_time = operate_time
        # {"en":"offer", "zh_CN":"商品"}
        self.offer = offer

    def validate(self):
        self.validate_required(self.request_id, 'request_id')
        self.validate_required(self.account, 'account')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.offer, 'offer')
        if self.offer:
            for k in self.offer:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.account is not None:
            result['account'] = self.account
        if self.operator is not None:
            result['operator'] = self.operator
        if self.operate_time is not None:
            result['operateTime'] = self.operate_time
        if self.offer is not None:
            result['offer'] = []
            for k in self.offer:
                result['offer'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')
        if m.get('offer') is not None:
            self.offer = []
            for k in m.get('offer'):
                temp_model = AgencyCreateResourceOffer()
                self.offer.append(temp_model.from_map(k))
        return self


class AgencyCreateResourceOrder(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        resource_id: str = None,
        service_order_ids: List[str] = None,
    ):
        # {"en":"AgencyCreateResourceOrder ID. Each business operation generates an orderId", "zh_CN":"订单ID。每次业务操作产生一个orderId"}
        self.order_id = order_id
        # {"en":"Resource ID. The same resource, the resourceId is always the same", "zh_CN":"资源ID。同一个资源，resourceId总是不变"}
        self.resource_id = resource_id
        # {"en":"List of service order IDs", "zh_CN":"服务订单ID列表"}
        self.service_order_ids = service_order_ids

    def validate(self):
        self.validate_required(self.order_id, 'order_id')
        self.validate_required(self.resource_id, 'resource_id')
        self.validate_required(self.service_order_ids, 'service_order_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.service_order_ids is not None:
            result['serviceOrderIds'] = self.service_order_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('serviceOrderIds') is not None:
            self.service_order_ids = m.get('serviceOrderIds')
        return self


class AgencyCreateResourceResponseData(TeaModel):
    def __init__(
        self,
        eff_date: str = None,
        orders: List[AgencyCreateResourceOrder] = None,
    ):
        # {"en":"Effective time (timestamp, milliseconds)", "zh_CN":"生效时间（时间戳，毫秒）"}
        self.eff_date = eff_date
        # {"en":"AgencyCreateResourceOrder List. Usually 1, when the input parameter qunatity>1, each resource returns 1 order", 
        # 	  "zh_CN":"订单列表。一般是1个，当入参qunatity>1时，每个资源返回1个订单"}
        self.orders = orders

    def validate(self):
        self.validate_required(self.eff_date, 'eff_date')
        self.validate_required(self.orders, 'orders')
        if self.orders:
            for k in self.orders:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.eff_date is not None:
            result['effDate'] = self.eff_date
        if self.orders is not None:
            result['orders'] = []
            for k in self.orders:
                result['orders'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effDate') is not None:
            self.eff_date = m.get('effDate')
        if m.get('orders') is not None:
            self.orders = []
            for k in m.get('orders'):
                temp_model = AgencyCreateResourceOrder()
                self.orders.append(temp_model.from_map(k))
        return self


class AgencyCreateResourceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        data: AgencyCreateResourceResponseData = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
        self.message = message
        # {"en":"data", "zh_CN":"数据"}
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
            temp_model = AgencyCreateResourceResponseData()
            self.data = temp_model.from_map(m['data'])
        return self


class AgencyCreateResourcePaths(TeaModel):
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


class AgencyCreateResourceParameters(TeaModel):
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


class AgencyCreateResourceRequestHeader(TeaModel):
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


class AgencyCreateResourceResponseHeader(TeaModel):
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






class AgencyDestroyResourceRequest(TeaModel):
    def __init__(
        self,
        account: str = None,
        operator: str = None,
        operate_time: str = None,
        resource_ids: List[str] = None,
    ):
        # {"en":"account", "zh_CN":"账号"}
        self.account = account
        # {"en":"operator", "zh_CN":"操作员"}
        self.operator = operator
        # {"en":"Destruction time (timestamp, accurate to milliseconds)Suggested vacancies, cbss will fill in the system time", "zh_CN":"销毁时间(时间戳，精确到毫秒)，建议空缺，cbss会以系统时间填入"}
        self.operate_time = operate_time
        # {"en":"resource id list", "zh_CN":"资源id列表"}
        self.resource_ids = resource_ids

    def validate(self):
        self.validate_required(self.account, 'account')
        self.validate_required(self.operator, 'operator')
        self.validate_required(self.resource_ids, 'resource_ids')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['account'] = self.account
        if self.operator is not None:
            result['operator'] = self.operator
        if self.operate_time is not None:
            result['operateTime'] = self.operate_time
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('account') is not None:
            self.account = m.get('account')
        if m.get('operator') is not None:
            self.operator = m.get('operator')
        if m.get('operateTime') is not None:
            self.operate_time = m.get('operateTime')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        return self


class AgencyDestroyResourceResponse(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
    ):
        # {"en":"Response code, 0 means successful.", "zh_CN":"接口响应code，0代表成功。"}
        self.code = code
        # {"en":"Response error message if failed.", "zh_CN":"接口响应信息，success代表成功，失败则提供失败信息。"}
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


class AgencyDestroyResourcePaths(TeaModel):
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


class AgencyDestroyResourceParameters(TeaModel):
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


class AgencyDestroyResourceRequestHeader(TeaModel):
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


class AgencyDestroyResourceResponseHeader(TeaModel):
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




