# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel  
from typing import Dict, List



class QueryCloudMonitorRealTimeAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # {"en":"Alert rule ID", "zh_CN":"报警规则id，需要鉴权是否该调用账号下或其下子账号的规则"}
        self.rule_id = rule_id
        # {"en":"Alarm rule name, rule ID and rule name, either one, rule ID takes priority", "zh_CN":"报警规则名称，规则ID和规则名称二选一，规则ID优先"}
        self.rule_name = rule_name
        # 监控规则条件

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        return self


class QueryCloudMonitorRealTimeAlarmRuleQueryConditionRule(TeaModel):
    def __init__(
        self,
        monitor_item: str = None,
        condition: str = None,
        threshold: str = None,
    ):
        # {"en":"Monitor item (BANDWIDTH, FLOW, REQUEST, etc.)", "zh_CN":"监控项（BANDWIDTH-带宽、FLOW-流量、REQUEST-请求数等）"}
        self.monitor_item = monitor_item
        # {"en":"Condition type (MAX, MIN, UPRUSH, SLUMPED)", "zh_CN":"条件类型（MAX-大于、MIN-小于、UPRUSH-突增、SLUMPED-突降）"}
        self.condition = condition
        # {"en":"Threshold value", "zh_CN":"监控项阈值"}
        self.threshold = threshold
        # 规则项

    def validate(self):
        self.validate_required(self.monitor_item, 'monitor_item')
        self.validate_required(self.condition, 'condition')
        self.validate_required(self.threshold, 'threshold')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_item is not None:
            result['monitorItem'] = self.monitor_item
        if self.condition is not None:
            result['condition'] = self.condition
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('monitorItem') is not None:
            self.monitor_item = m.get('monitorItem')
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class QueryCloudMonitorRealTimeAlarmRuleQueryRuleItem(TeaModel):
    def __init__(
        self,
        rule_item_id: str = None,
        start_time: str = None,
        end_time: str = None,
        condition_type: str = None,
        period: int = None,
        period_times: int = None,
        condition_rules: List[QueryCloudMonitorRealTimeAlarmRuleQueryConditionRule] = None,
    ):
        # {"en":"Rule item ID", "zh_CN":"分时段子规则"}
        self.rule_item_id = rule_item_id
        # {"en":"Start time (format: HH:00)", "zh_CN":"监控时段开始时间，格式：HH:00，示例：00:00"}
        self.start_time = start_time
        # {"en":"End time (format: HH:59)", "zh_CN":"监控时段结束时间，格式：HH:59，示例：01:59"}
        self.end_time = end_time
        # {"en":"Condition type (ANY/ALL)", "zh_CN":"告警需满足任意或全部条件，可选值：ANY-任意、ALL-全部"}
        self.condition_type = condition_type
        # {"en":"Monitoring period in minutes (1/5/10)", "zh_CN":"监控周期，周期单位为分钟（1-1分钟、5-5分钟、10-10分钟）"}
        self.period = period
        # {"en":"Number of cycles (1/2/3/5/15/30)", "zh_CN":"持续几个周期满足条件告警（1/2/3/5/15/30）"}
        self.period_times = period_times
        # {"en":"Condition rules list", "zh_CN":"条件规则列表"}
        self.condition_rules = condition_rules
        # 通知方式

    def validate(self):
        self.validate_required(self.rule_item_id, 'rule_item_id')
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.condition_type, 'condition_type')
        self.validate_required(self.period, 'period')
        self.validate_required(self.period_times, 'period_times')
        self.validate_required(self.condition_rules, 'condition_rules')
        if self.condition_rules:
            for k in self.condition_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_item_id is not None:
            result['ruleItemId'] = self.rule_item_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.condition_type is not None:
            result['conditionType'] = self.condition_type
        if self.period is not None:
            result['period'] = self.period
        if self.period_times is not None:
            result['periodTimes'] = self.period_times
        if self.condition_rules is not None:
            result['conditionRules'] = []
            for k in self.condition_rules:
                result['conditionRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleItemId') is not None:
            self.rule_item_id = m.get('ruleItemId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('conditionType') is not None:
            self.condition_type = m.get('conditionType')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodTimes') is not None:
            self.period_times = m.get('periodTimes')
        if m.get('conditionRules') is not None:
            self.condition_rules = []
            for k in m.get('conditionRules'):
                temp_model = QueryCloudMonitorRealTimeAlarmRuleQueryConditionRule()
                self.condition_rules.append(temp_model.from_map(k))
        return self


class QueryCloudMonitorRealTimeAlarmRuleQueryNotice(TeaModel):
    def __init__(
        self,
        notice_method: str = None,
        notice_object: str = None,
    ):
        # {"en":"Notice method (sms/email/robot/webhook)", "zh_CN":"通知方式（sms-短信、email-邮件、robot-机器人、webhook-webhook回调）"}
        self.notice_method = notice_method
        # {"en":"Notice object", "zh_CN":"告警通知对象，短信/邮件传联系人id，机器人传机器人id，webhook传地址"}
        self.notice_object = notice_object
        # 响应数据

    def validate(self):
        self.validate_required(self.notice_method, 'notice_method')
        self.validate_required(self.notice_object, 'notice_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notice_method is not None:
            result['noticeMethod'] = self.notice_method
        if self.notice_object is not None:
            result['noticeObject'] = self.notice_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('noticeMethod') is not None:
            self.notice_method = m.get('noticeMethod')
        if m.get('noticeObject') is not None:
            self.notice_object = m.get('noticeObject')
        return self


class QueryCloudMonitorRealTimeAlarmRuleQueryMonitorRuleData(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
        monitor_product: str = None,
        resource_type: str = None,
        monitor_resources: List[str] = None,
        statistical_method: str = None,
        alert_frequency: int = None,
        restore_notice: str = None,
        rule_items: List[QueryCloudMonitorRealTimeAlarmRuleQueryRuleItem] = None,
        notices: List[QueryCloudMonitorRealTimeAlarmRuleQueryNotice] = None,
    ):
        # {"en":"Alarm rule ID", "zh_CN":"报警规则id"}
        self.rule_id = rule_id
        # {"en":"Alert rule name", "zh_CN":"报警规则名称"}
        self.rule_name = rule_name
        # {"en":"Monitor product or dimension", "zh_CN":"按指定维度或指定已开通商品监控（userDimension-主账号维度、DG-域名组、CG-服务组、domainDimension-域名维度）"}
        self.monitor_product = monitor_product
        # {"en":"Resource type", "zh_CN":"监控资源类型"}
        self.resource_type = resource_type
        # {"en":"Monitor resources list or ALL", "zh_CN":"监控的资源名称列表或ALL"}
        self.monitor_resources = monitor_resources
        # {"en":"Statistical method (CONSOLIDATED/SEPARATE)", "zh_CN":"统计方式（CONSOLIDATED-合并统计、SEPARATE-逐一统计）"}
        self.statistical_method = statistical_method
        # {"en":"Alert frequency (0/2/5/10/15/20)", "zh_CN":"告警频率，每X分钟内产生的告警仅通知一次（0-仅首次告警、2/5/10/15/20分钟）"}
        self.alert_frequency = alert_frequency
        # {"en":"Restore notice (true/false)", "zh_CN":"告警消警是否通知（true-是、false-否）"}
        self.restore_notice = restore_notice
        # {"en":"Rule items list", "zh_CN":"规则项列表"}
        self.rule_items = rule_items
        # {"en":"Notices list", "zh_CN":"通知方式列表"}
        self.notices = notices
        # 响应体

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.monitor_product, 'monitor_product')
        self.validate_required(self.resource_type, 'resource_type')
        self.validate_required(self.monitor_resources, 'monitor_resources')
        self.validate_required(self.statistical_method, 'statistical_method')
        self.validate_required(self.alert_frequency, 'alert_frequency')
        self.validate_required(self.restore_notice, 'restore_notice')
        self.validate_required(self.rule_items, 'rule_items')
        if self.rule_items:
            for k in self.rule_items:
                if k:
                    k.validate()
        self.validate_required(self.notices, 'notices')
        if self.notices:
            for k in self.notices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.monitor_product is not None:
            result['monitorProduct'] = self.monitor_product
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.monitor_resources is not None:
            result['monitorResources'] = self.monitor_resources
        if self.statistical_method is not None:
            result['statisticalMethod'] = self.statistical_method
        if self.alert_frequency is not None:
            result['alertFrequency'] = self.alert_frequency
        if self.restore_notice is not None:
            result['restoreNotice'] = self.restore_notice
        if self.rule_items is not None:
            result['ruleItems'] = []
            for k in self.rule_items:
                result['ruleItems'].append(k.to_map() if k else None)
        if self.notices is not None:
            result['notices'] = []
            for k in self.notices:
                result['notices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('monitorProduct') is not None:
            self.monitor_product = m.get('monitorProduct')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('monitorResources') is not None:
            self.monitor_resources = m.get('monitorResources')
        if m.get('statisticalMethod') is not None:
            self.statistical_method = m.get('statisticalMethod')
        if m.get('alertFrequency') is not None:
            self.alert_frequency = m.get('alertFrequency')
        if m.get('restoreNotice') is not None:
            self.restore_notice = m.get('restoreNotice')
        if m.get('ruleItems') is not None:
            self.rule_items = []
            for k in m.get('ruleItems'):
                temp_model = QueryCloudMonitorRealTimeAlarmRuleQueryRuleItem()
                self.rule_items.append(temp_model.from_map(k))
        if m.get('notices') is not None:
            self.notices = []
            for k in m.get('notices'):
                temp_model = QueryCloudMonitorRealTimeAlarmRuleQueryNotice()
                self.notices.append(temp_model.from_map(k))
        return self


class QueryCloudMonitorRealTimeAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: QueryCloudMonitorRealTimeAlarmRuleQueryMonitorRuleData = None,
    ):
        # {"en":"Response code", "zh_CN":"功能码"}
        self.code = code
        # {"en":"Response message", "zh_CN":"功能码说明"}
        self.message = message
        # {"en":"Response data", "zh_CN":"响应数据"}
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
            temp_model = QueryCloudMonitorRealTimeAlarmRuleQueryMonitorRuleData()
            self.data = temp_model.from_map(m['data'])
        return self


class QueryCloudMonitorRealTimeAlarmRulePaths(TeaModel):
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


class QueryCloudMonitorRealTimeAlarmRuleParameters(TeaModel):
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


class QueryCloudMonitorRealTimeAlarmRuleRequestHeader(TeaModel):
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


class QueryCloudMonitorRealTimeAlarmRuleResponseHeader(TeaModel):
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






class EditCloudMonitorRealTimeAlarmRuleConditionRule(TeaModel):
    def __init__(
        self,
        monitor_item: str = None,
        condition: str = None,
        threshold: str = None,
    ):
        # {"en":"Monitoring items currently only support domain-type monitoring items. Options: BANDWIDTH, FLOW, REQUEST, BTOB, FLOW_HIT_RATE, etc.", "zh_CN":"当前仅支持监控对象类型为域名的监控项。可选监控项：BANDWIDTH-带宽、FLOW-流量、REQUEST-请求数、BTOB-回源带宽、FLOW_HIT_RATE-流量命中率等"}
        self.monitor_item = monitor_item
        # {"en":"Condition type. Options: MAX-greater than, MIN-less than, UPRUSH-surge, SLUMPED-plunge", "zh_CN":"条件类型。可选值：MAX-大于、MIN-小于、UPRUSH-突增、SLUMPED-突降"}
        self.condition = condition
        # {"en":"Threshold value, please provide a positive integer", "zh_CN":"监控项阈值，请传递正整数"}
        self.threshold = threshold
        # 规则项

    def validate(self):
        self.validate_required(self.monitor_item, 'monitor_item')
        self.validate_required(self.condition, 'condition')
        self.validate_required(self.threshold, 'threshold')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_item is not None:
            result['monitorItem'] = self.monitor_item
        if self.condition is not None:
            result['condition'] = self.condition
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('monitorItem') is not None:
            self.monitor_item = m.get('monitorItem')
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class EditCloudMonitorRealTimeAlarmRuleRuleItem(TeaModel):
    def __init__(
        self,
        rule_item_id: str = None,
        start_time: str = None,
        end_time: str = None,
        condition_type: str = None,
        period: int = None,
        period_times: int = None,
        condition_rules: List[EditCloudMonitorRealTimeAlarmRuleConditionRule] = None,
    ):
        # {"en":"Time-divided sub-rules. If an id is passed in, it is considered to specify a modification of an item rule.", "zh_CN":"分时段子规则id"}
        self.rule_item_id = rule_item_id
        # {"en":"Monitoring period start time, format: HH:00, example: 00:00", "zh_CN":"监控时段开始时间，格式：HH:00，示例：00:00"}
        self.start_time = start_time
        # {"en":"Monitoring period end time, format: HH:59, example: 01:59", "zh_CN":"监控时段结束时间，格式：HH:59，示例：01:59"}
        self.end_time = end_time
        # {"en":"Alert condition type. Options: ANY-any condition, ALL-all conditions", "zh_CN":"告警需满足任意或全部条件。可选值：ANY-任意、ALL-全部"}
        self.condition_type = condition_type
        # {"en":"Monitoring cycle in minutes. Options: 1, 5, 10", "zh_CN":"监控周期，周期单位为分钟。可选值：1-1分钟、5-5分钟、10-10分钟"}
        self.period = period
        # {"en":"Number of cycles to meet conditions before alerting. Options: 1, 2, 3, 5, 15, 30", "zh_CN":"持续几个周期满足条件告警。可选值：1、2、3、5、15、30"}
        self.period_times = period_times
        # {"en":"Condition rules list", "zh_CN":"条件规则列表"}
        self.condition_rules = condition_rules
        # 通知方式

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.condition_type, 'condition_type')
        self.validate_required(self.period, 'period')
        self.validate_required(self.period_times, 'period_times')
        self.validate_required(self.condition_rules, 'condition_rules')
        if self.condition_rules:
            for k in self.condition_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_item_id is not None:
            result['ruleItemId'] = self.rule_item_id
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.condition_type is not None:
            result['conditionType'] = self.condition_type
        if self.period is not None:
            result['period'] = self.period
        if self.period_times is not None:
            result['periodTimes'] = self.period_times
        if self.condition_rules is not None:
            result['conditionRules'] = []
            for k in self.condition_rules:
                result['conditionRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleItemId') is not None:
            self.rule_item_id = m.get('ruleItemId')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('conditionType') is not None:
            self.condition_type = m.get('conditionType')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodTimes') is not None:
            self.period_times = m.get('periodTimes')
        if m.get('conditionRules') is not None:
            self.condition_rules = []
            for k in m.get('conditionRules'):
                temp_model = EditCloudMonitorRealTimeAlarmRuleConditionRule()
                self.condition_rules.append(temp_model.from_map(k))
        return self


class EditCloudMonitorRealTimeAlarmRuleNotice(TeaModel):
    def __init__(
        self,
        notice_method: str = None,
        notice_object: str = None,
    ):
        # {"en":"Notification method. Options: MOBILE, EMAIL, robot, webhook", "zh_CN":"通知方式。可选值：MOBILE-短信、EMAIL-邮件、ROBOT-机器人、WEBHOOK-webhook回调"}
        self.notice_method = notice_method
        # {"en":"Notification object. For MOBILE/EMAIL: contact IDs separated by ;. For ROBOT: robot IDs separated by ;. For WEBHOOK: webhook URL", "zh_CN":"告警通知对象。若noticeMethod为MOBILE、EMAIL：请传递联系人id，多个用;分隔。若为ROBOT：请传递机器人id，多个用;分隔。若为WEBHOOK：请直接传递webhook地址"}
        self.notice_object = notice_object
        # 请求体

    def validate(self):
        self.validate_required(self.notice_method, 'notice_method')
        self.validate_required(self.notice_object, 'notice_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notice_method is not None:
            result['noticeMethod'] = self.notice_method
        if self.notice_object is not None:
            result['noticeObject'] = self.notice_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('noticeMethod') is not None:
            self.notice_method = m.get('noticeMethod')
        if m.get('noticeObject') is not None:
            self.notice_object = m.get('noticeObject')
        return self


class EditCloudMonitorRealTimeAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
        monitor_product: str = None,
        resource_type: str = None,
        monitor_resources: List[str] = None,
        statistical_method: str = None,
        alert_frequency: int = None,
        restore_notice: str = None,
        rule_items: List[EditCloudMonitorRealTimeAlarmRuleRuleItem] = None,
        notices: List[EditCloudMonitorRealTimeAlarmRuleNotice] = None,
    ):
        # {"en":"Alarm rule ID", "zh_CN":"报警规则id"}
        self.rule_id = rule_id
        # {"en":"Alert rule name, only supports Chinese, English, numbers, underscore, hyphen, max 100 characters", "zh_CN":"报警规则名称，仅支持中英文、数字、下划线、中划线，最多100个字符"}
        self.rule_name = rule_name
        # {"en":"Monitor by dimension or product. Dimensions: userDimension, DG, CG, domainDimension. Or input product code", "zh_CN":"可选按指定维度或指定已开通商品监控。指定维度可选项：userDimension-主账号维度、DG-域名组、CG-服务组、domainDimension-域名维度。若按商品监控，请传入商品code"}
        self.monitor_product = monitor_product
        # {"en":"Resource type. Required when monitorProduct is specific product. Options: domain", "zh_CN":"监控资源类型。当monitorPorduct传入指定商品时，需要必传resourceType。可选值：domain"}
        self.resource_type = resource_type
        # {"en":"List of resource names to monitor or ALL", "zh_CN":"传入具体要监控的资源名称列表或ALL"}
        self.monitor_resources = monitor_resources
        # {"en":"Statistical method. Default: CONSOLIDATED. Options: CONSOLIDATED-consolidated statistics, SEPARATE-separate statistics", "zh_CN":"统计方式。未传默认按合并统计。可选值：CONSOLIDATED-合并统计、SEPARATE-逐一统计"}
        self.statistical_method = statistical_method
        # {"en":"Alert frequency in minutes. Default: 5. Options: 0-first alert only, 2, 5, 10, 15, 20", "zh_CN":"告警频率。避免告警风暴，每X分钟内产生的告警仅通知一次。未传默认值是5。可选值：0-仅首次告警、2、5、10、15、20"}
        self.alert_frequency = alert_frequency
        # {"en":"Whether to notify on alert recovery. Default: true", "zh_CN":"告警消警是否通知，未传默认为是。可选值：true-是、false-否"}
        self.restore_notice = restore_notice
        # {"en":"Rule items list", "zh_CN":"规则项列表"}
        self.rule_items = rule_items
        # {"en":"Notification methods list", "zh_CN":"通知方式列表"}
        self.notices = notices
        # 响应数据

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.monitor_product, 'monitor_product')
        self.validate_required(self.rule_items, 'rule_items')
        if self.rule_items:
            for k in self.rule_items:
                if k:
                    k.validate()
        self.validate_required(self.notices, 'notices')
        if self.notices:
            for k in self.notices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.monitor_product is not None:
            result['monitorProduct'] = self.monitor_product
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.monitor_resources is not None:
            result['monitorResources'] = self.monitor_resources
        if self.statistical_method is not None:
            result['statisticalMethod'] = self.statistical_method
        if self.alert_frequency is not None:
            result['alertFrequency'] = self.alert_frequency
        if self.restore_notice is not None:
            result['restoreNotice'] = self.restore_notice
        if self.rule_items is not None:
            result['ruleItems'] = []
            for k in self.rule_items:
                result['ruleItems'].append(k.to_map() if k else None)
        if self.notices is not None:
            result['notices'] = []
            for k in self.notices:
                result['notices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('monitorProduct') is not None:
            self.monitor_product = m.get('monitorProduct')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('monitorResources') is not None:
            self.monitor_resources = m.get('monitorResources')
        if m.get('statisticalMethod') is not None:
            self.statistical_method = m.get('statisticalMethod')
        if m.get('alertFrequency') is not None:
            self.alert_frequency = m.get('alertFrequency')
        if m.get('restoreNotice') is not None:
            self.restore_notice = m.get('restoreNotice')
        if m.get('ruleItems') is not None:
            self.rule_items = []
            for k in m.get('ruleItems'):
                temp_model = EditCloudMonitorRealTimeAlarmRuleRuleItem()
                self.rule_items.append(temp_model.from_map(k))
        if m.get('notices') is not None:
            self.notices = []
            for k in m.get('notices'):
                temp_model = EditCloudMonitorRealTimeAlarmRuleNotice()
                self.notices.append(temp_model.from_map(k))
        return self


class EditCloudMonitorRealTimeAlarmRuleEditMonitorRuleData(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
    ):
        # {"en":"Rule ID", "zh_CN":"规则ID"}
        self.rule_id = rule_id
        # 响应体

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class EditCloudMonitorRealTimeAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: EditCloudMonitorRealTimeAlarmRuleEditMonitorRuleData = None,
    ):
        # {"en":"Response code", "zh_CN":"响应码"}
        self.code = code
        # {"en":"Response message", "zh_CN":"响应消息"}
        self.message = message
        # {"en":"Response data", "zh_CN":"响应数据"}
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
            temp_model = EditCloudMonitorRealTimeAlarmRuleEditMonitorRuleData()
            self.data = temp_model.from_map(m['data'])
        return self


class EditCloudMonitorRealTimeAlarmRulePaths(TeaModel):
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


class EditCloudMonitorRealTimeAlarmRuleParameters(TeaModel):
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


class EditCloudMonitorRealTimeAlarmRuleRequestHeader(TeaModel):
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


class EditCloudMonitorRealTimeAlarmRuleResponseHeader(TeaModel):
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






class DeleteCloudMonitorRealTimeAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
    ):
        # {"en":"Alert rule ID", "zh_CN":"报警规则id，需要鉴权是否该调用账号下或其下子账号的规则"}
        self.rule_id = rule_id

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class DeleteCloudMonitorRealTimeAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # {"en":"Response code", "zh_CN":"功能码"}
        self.code = code
        # {"en":"Response message", "zh_CN":"功能码说明"}
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


class DeleteCloudMonitorRealTimeAlarmRulePaths(TeaModel):
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


class DeleteCloudMonitorRealTimeAlarmRuleParameters(TeaModel):
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


class DeleteCloudMonitorRealTimeAlarmRuleRequestHeader(TeaModel):
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


class DeleteCloudMonitorRealTimeAlarmRuleResponseHeader(TeaModel):
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






class CreateCloudMonitorRealTimeAlarmRuleConditionRule(TeaModel):
    def __init__(
        self,
        monitor_item: str = None,
        condition: str = None,
        threshold: str = None,
    ):
        # {"en":"Monitoring items currently only support domain-type monitoring items. Options: BANDWIDTH, FLOW, REQUEST, BTOB, FLOW_HIT_RATE, etc.", "zh_CN":"当前仅支持监控对象类型为域名的监控项。可选监控项：BANDWIDTH-带宽、FLOW-流量、REQUEST-请求数、BTOB-回源带宽、FLOW_HIT_RATE-流量命中率等"}
        self.monitor_item = monitor_item
        # {"en":"Condition type. Options: MAX-greater than, MIN-less than, UPRUSH-surge, SLUMPED-plunge", "zh_CN":"条件类型。可选值：MAX-大于、MIN-小于、UPRUSH-突增、SLUMPED-突降"}
        self.condition = condition
        # {"en":"Threshold value, please provide a positive integer", "zh_CN":"监控项阈值，请传递正整数"}
        self.threshold = threshold
        # 规则项

    def validate(self):
        self.validate_required(self.monitor_item, 'monitor_item')
        self.validate_required(self.condition, 'condition')
        self.validate_required(self.threshold, 'threshold')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.monitor_item is not None:
            result['monitorItem'] = self.monitor_item
        if self.condition is not None:
            result['condition'] = self.condition
        if self.threshold is not None:
            result['threshold'] = self.threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('monitorItem') is not None:
            self.monitor_item = m.get('monitorItem')
        if m.get('condition') is not None:
            self.condition = m.get('condition')
        if m.get('threshold') is not None:
            self.threshold = m.get('threshold')
        return self


class CreateCloudMonitorRealTimeAlarmRuleRuleItem(TeaModel):
    def __init__(
        self,
        start_time: str = None,
        end_time: str = None,
        condition_type: str = None,
        period: int = None,
        period_times: int = None,
        condition_rules: List[CreateCloudMonitorRealTimeAlarmRuleConditionRule] = None,
    ):
        # {"en":"Monitoring period start time, format: HH:00, example: 00:00", "zh_CN":"监控时段开始时间，格式：HH:00，示例：00:00"}
        self.start_time = start_time
        # {"en":"Monitoring period end time, format: HH:59, example: 01:59", "zh_CN":"监控时段结束时间，格式：HH:59，示例：01:59"}
        self.end_time = end_time
        # {"en":"Alert condition type. Options: ANY-any condition, ALL-all conditions", "zh_CN":"告警需满足任意或全部条件。可选值：ANY-任意、ALL-全部"}
        self.condition_type = condition_type
        # {"en":"Monitoring cycle in minutes. Options: 1, 5, 10", "zh_CN":"监控周期，周期单位为分钟。可选值：1-1分钟、5-5分钟、10-10分钟"}
        self.period = period
        # {"en":"Number of cycles to meet conditions before alerting. Options: 1, 2, 3, 5, 15, 30", "zh_CN":"持续几个周期满足条件告警。可选值：1、2、3、5、15、30"}
        self.period_times = period_times
        # {"en":"Condition rules list", "zh_CN":"条件规则列表"}
        self.condition_rules = condition_rules
        # 通知方式

    def validate(self):
        self.validate_required(self.start_time, 'start_time')
        self.validate_required(self.end_time, 'end_time')
        self.validate_required(self.condition_type, 'condition_type')
        self.validate_required(self.period, 'period')
        self.validate_required(self.period_times, 'period_times')
        self.validate_required(self.condition_rules, 'condition_rules')
        if self.condition_rules:
            for k in self.condition_rules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.condition_type is not None:
            result['conditionType'] = self.condition_type
        if self.period is not None:
            result['period'] = self.period
        if self.period_times is not None:
            result['periodTimes'] = self.period_times
        if self.condition_rules is not None:
            result['conditionRules'] = []
            for k in self.condition_rules:
                result['conditionRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('conditionType') is not None:
            self.condition_type = m.get('conditionType')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('periodTimes') is not None:
            self.period_times = m.get('periodTimes')
        if m.get('conditionRules') is not None:
            self.condition_rules = []
            for k in m.get('conditionRules'):
                temp_model = CreateCloudMonitorRealTimeAlarmRuleConditionRule()
                self.condition_rules.append(temp_model.from_map(k))
        return self


class CreateCloudMonitorRealTimeAlarmRuleNotice(TeaModel):
    def __init__(
        self,
        notice_method: str = None,
        notice_object: str = None,
    ):
        # {"en":"Notification method. Options: MOBILE, EMAIL, ROBOT, webhook", "zh_CN":"通知方式。可选值：MOBILE-短信、EMAIL-邮件、ROBOT-机器人、WEBHOOK-webhook回调"}
        self.notice_method = notice_method
        # {"en":"Notification object. For MOBILE/EMAIL: contact IDs separated by ;. For ROBOT: robot IDs separated by ;. For WEBHOOK: webhook URL", "zh_CN":"告警通知对象。若noticeMethod为MOBILE、EMAIL：请传递联系人id，多个用;分隔。若为ROBOT：请传递机器人id，多个用;分隔。若为WEBHOOK：请直接传递webhook地址"}
        self.notice_object = notice_object
        # 请求体

    def validate(self):
        self.validate_required(self.notice_method, 'notice_method')
        self.validate_required(self.notice_object, 'notice_object')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notice_method is not None:
            result['noticeMethod'] = self.notice_method
        if self.notice_object is not None:
            result['noticeObject'] = self.notice_object
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('noticeMethod') is not None:
            self.notice_method = m.get('noticeMethod')
        if m.get('noticeObject') is not None:
            self.notice_object = m.get('noticeObject')
        return self


class CreateCloudMonitorRealTimeAlarmRuleRequest(TeaModel):
    def __init__(
        self,
        rule_name: str = None,
        monitor_product: str = None,
        resource_type: str = None,
        monitor_resources: List[str] = None,
        statistical_method: str = None,
        alert_frequency: int = None,
        restore_notice: str = None,
        rule_items: List[CreateCloudMonitorRealTimeAlarmRuleRuleItem] = None,
        notices: List[CreateCloudMonitorRealTimeAlarmRuleNotice] = None,
    ):
        # {"en":"Alert rule name, only supports Chinese, English, numbers, underscore, hyphen, max 100 characters", "zh_CN":"报警规则名称，仅支持中英文、数字、下划线、中划线，最多100个字符"}
        self.rule_name = rule_name
        # {"en":"Monitor by dimension or product. Dimensions: userDimension, DG, CG, domainDimension. Or input product code", "zh_CN":"可选按指定维度或指定已开通商品监控。指定维度可选项：userDimension-主账号维度、DG-域名组、CG-服务组、domainDimension-域名维度。若按商品监控，请传入商品code"}
        self.monitor_product = monitor_product
        # {"en":"Resource type. Required when monitorProduct is specific product. Options: domain", "zh_CN":"监控资源类型。当monitorPorduct传入指定商品时，需要必传resourceType。可选值：domain"}
        self.resource_type = resource_type
        # {"en":"List of resource names to monitor or ALL", "zh_CN":"传入具体要监控的资源名称列表或ALL"}
        self.monitor_resources = monitor_resources
        # {"en":"Statistical method. Default: CONSOLIDATED. Options: CONSOLIDATED-consolidated statistics, SEPARATE-separate statistics", "zh_CN":"统计方式。未传默认按合并统计。可选值：CONSOLIDATED-合并统计、SEPARATE-逐一统计"}
        self.statistical_method = statistical_method
        # {"en":"Alert frequency in minutes. Default: 5. Options: 0-first alert only, 2, 5, 10, 15, 20", "zh_CN":"告警频率。避免告警风暴，每X分钟内产生的告警仅通知一次。未传默认值是5。可选值：0-仅首次告警、2、5、10、15、20"}
        self.alert_frequency = alert_frequency
        # {"en":"Whether to notify on alert recovery. Default: true", "zh_CN":"告警消警是否通知，未传默认为是。可选值：true-是、false-否"}
        self.restore_notice = restore_notice
        # {"en":"Rule items list", "zh_CN":"规则项列表"}
        self.rule_items = rule_items
        # {"en":"Notification methods list", "zh_CN":"通知方式列表"}
        self.notices = notices
        # 响应数据

    def validate(self):
        self.validate_required(self.rule_name, 'rule_name')
        self.validate_required(self.monitor_product, 'monitor_product')
        self.validate_required(self.rule_items, 'rule_items')
        if self.rule_items:
            for k in self.rule_items:
                if k:
                    k.validate()
        self.validate_required(self.notices, 'notices')
        if self.notices:
            for k in self.notices:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_name is not None:
            result['ruleName'] = self.rule_name
        if self.monitor_product is not None:
            result['monitorProduct'] = self.monitor_product
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        if self.monitor_resources is not None:
            result['monitorResources'] = self.monitor_resources
        if self.statistical_method is not None:
            result['statisticalMethod'] = self.statistical_method
        if self.alert_frequency is not None:
            result['alertFrequency'] = self.alert_frequency
        if self.restore_notice is not None:
            result['restoreNotice'] = self.restore_notice
        if self.rule_items is not None:
            result['ruleItems'] = []
            for k in self.rule_items:
                result['ruleItems'].append(k.to_map() if k else None)
        if self.notices is not None:
            result['notices'] = []
            for k in self.notices:
                result['notices'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')
        if m.get('monitorProduct') is not None:
            self.monitor_product = m.get('monitorProduct')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        if m.get('monitorResources') is not None:
            self.monitor_resources = m.get('monitorResources')
        if m.get('statisticalMethod') is not None:
            self.statistical_method = m.get('statisticalMethod')
        if m.get('alertFrequency') is not None:
            self.alert_frequency = m.get('alertFrequency')
        if m.get('restoreNotice') is not None:
            self.restore_notice = m.get('restoreNotice')
        if m.get('ruleItems') is not None:
            self.rule_items = []
            for k in m.get('ruleItems'):
                temp_model = CreateCloudMonitorRealTimeAlarmRuleRuleItem()
                self.rule_items.append(temp_model.from_map(k))
        if m.get('notices') is not None:
            self.notices = []
            for k in m.get('notices'):
                temp_model = CreateCloudMonitorRealTimeAlarmRuleNotice()
                self.notices.append(temp_model.from_map(k))
        return self


class CreateCloudMonitorRealTimeAlarmRuleCreateMonitorRuleData(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
    ):
        # {"en":"Rule ID", "zh_CN":"规则ID"}
        self.rule_id = rule_id
        # 响应体

    def validate(self):
        self.validate_required(self.rule_id, 'rule_id')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['ruleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')
        return self


class CreateCloudMonitorRealTimeAlarmRuleResponse(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        data: CreateCloudMonitorRealTimeAlarmRuleCreateMonitorRuleData = None,
    ):
        # {"en":"Response code", "zh_CN":"响应码"}
        self.code = code
        # {"en":"Response message", "zh_CN":"响应消息"}
        self.message = message
        # {"en":"Response data", "zh_CN":"响应数据"}
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
            temp_model = CreateCloudMonitorRealTimeAlarmRuleCreateMonitorRuleData()
            self.data = temp_model.from_map(m['data'])
        return self


class CreateCloudMonitorRealTimeAlarmRulePaths(TeaModel):
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


class CreateCloudMonitorRealTimeAlarmRuleParameters(TeaModel):
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


class CreateCloudMonitorRealTimeAlarmRuleRequestHeader(TeaModel):
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


class CreateCloudMonitorRealTimeAlarmRuleResponseHeader(TeaModel):
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




