import logging

from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler

logger = logging.getLogger(__name__)

STATUS_MSG = {
    401: "登录状态已失效，请重新登录",
    403: "没有操作权限",
    404: "资源不存在",
}


def _extract_msg(detail):
    """把 DRF 的嵌套错误 detail 压平成一条可读文案。"""
    if isinstance(detail, dict):
        for value in detail.values():
            return _extract_msg(value)
        return ""
    if isinstance(detail, (list, tuple)) and detail:
        return _extract_msg(detail[0])
    return str(detail)


def custom_exception_handler(exc, context):
    if isinstance(exc, IntegrityError):
        logger.error("数据库完整性错误: %s", exc, exc_info=True)
        return Response({"code": 400, "msg": "数据冲突，请稍后再试", "data": None}, status=400)

    response = drf_exception_handler(exc, context)
    if response is None:
        logger.error("未处理异常", exc_info=exc)
        return Response(
            {"code": 500, "msg": "服务器开小差了，请稍后再试", "data": None}, status=500
        )

    code = response.status_code
    msg = STATUS_MSG.get(code) or _extract_msg(response.data) or "请求处理失败"
    response.data = {"code": code, "msg": msg, "data": None}
    return response
