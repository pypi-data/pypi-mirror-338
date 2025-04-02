# ====================== 通用工具函数 ======================
import json
import re


def assert_invalid_arguments(response, case_info):
    """参数异常通用断言, 第一阶段错误校验"""
    raw_log = response.get("raw", "")
    assert case_info["expected"]["patterns"]["value"] in raw_log, f"未匹配到错误模式: {raw_log}"


def assert_check_file_code(response, case_info):
    """参数异常通用断言, 第二阶段错误校验"""
    error_code = response.get("code", "")
    raw_log = response.get("raw_log", "").lower()

    assert error_code == case_info["expected"]["patterns"]["code"], f"未匹配到错误模式: {error_code}"
    assert case_info["expected"]["patterns"]["value"] in raw_log, f"未匹配到错误模式: {raw_log}"


def assert_deliver_fail(client, response, case_info):
    """权限校验通用断言, 第三阶段上链失败校验"""
    assert response["code"] == 0, "交易应成功提交,加入内存池"
    tx_receipt = client.wait_for_tx_confirmation(response["txhash"])
    error_code = tx_receipt.get("code", "")
    raw_log = tx_receipt.get("raw_log", "").lower()

    assert error_code == case_info["expected"]["patterns"]["code"], f"未匹配到错误模式: {error_code}"
    assert case_info["expected"]["patterns"]["value"] in raw_log, f"未匹配到错误模式: {raw_log}"


def assert_tx_success(client, response):
    """通用交易成功断言"""
    assert response["code"] == 0, f"交易提交失败: {response}"
    tx_receipt = client.wait_for_tx_confirmation(response["txhash"])
    assert tx_receipt["code"] == 0, f"交易执行失败: {tx_receipt}"
    return tx_receipt


# 解析response中的格式输出
def parse_tx_hash(response):
    if isinstance(response["raw"], str):
        return json.loads(response["raw"].split("\n")[1])


def common_assert(client, response, case_info):
    """通用断言"""
    if case_info["expected"]["error"]:
        assert_invalid_arguments(response, case_info)
    if case_info["expected"]["check_fail"]:
        assert_check_file_code(response, case_info)
    if case_info["expected"]["deliver_fail"]:
        # 开发代码不规范，添加兼容场景处理
        if response.get("raw"):
            response = parse_tx_hash(response)
        assert_deliver_fail(client, response, case_info)
    if case_info["expected"]["success"]:
        if response.get("raw"):
            response = parse_tx_hash(response)
        return assert_tx_success(client, response)


def assert_query_match(response, query_type, *args, **kwargs):
    """查询通用断言"""
    if query_type == "allocate-rate":
        expected_data: dict = args[0]
        expected_treasury, expected_dev = expected_data.get("fee_treasury_rate"), expected_data.get("dev_operator_rate")
        rates = response.get("allocate_rate", {})
        assert rates.get("dev_operator_rate") == expected_dev, "开发者费率不匹配"
        assert rates.get("fee_treasury_rate") == expected_treasury, "金库费率不匹配"


def assert_values_equal(actual, expected, message=None):
    """
    断言两个值相等，支持字符串转整数比较
    
    Args:
        actual: 实际值，可以是字符串或整数
        expected: 期望值，可以是字符串或整数
        message: 可选的错误消息
    """
    actual_int = int(actual) if actual is not None else 0
    expected_int = int(expected) if expected is not None else 0

    error_msg = f"断言失败: 期望 {expected_int}，但得到 {actual_int}"
    if message:
        error_msg = f"{message}: {error_msg}"

    assert actual_int == expected_int, error_msg
