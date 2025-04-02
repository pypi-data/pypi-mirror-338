import websocket
import threading
import time
import json
from ncatbot_sync.logger import get_logger

log = get_logger("connect")


class WebSocketClient:
    def __init__(self, url, token, on_message):
        self.recive_url = url + "/event"
        self.send_url = url + "/api"
        self.token = token
        self.on_message = on_message
        self.recive_ws = None
        self.send_ws = None
        self.thread = None
        self.headers = {"Authorization": f"Bearer {self.token}"} if self.token else None
        self.last_heartbeat_time = None
        self.heartbeat_interval = None
        self.is_quit = False
        self.retcode = (None, None)

    @classmethod
    def test_connection(cls, url, token=None, timeout=3):
        """
        静态方法测试连接可用性
        :param url: 要测试的完整URL（包含/event或/api）
        :param token: 认证令牌（可选）
        :param timeout: 测试超时时间（秒）
        :return: (是否成功, 错误信息)
        """
        test_ws = None
        try:
            headers = {"Authorization": f"Bearer {token}"} if token else None
            # 创建临时测试连接
            test_ws = websocket.create_connection(
                url,
                header=headers,
                timeout=timeout
            )
            # 验证握手状态
            if test_ws.getstatus() != 101:
                return False, f"无效的握手状态码: {test_ws.getstatus()}"

            # 主动关闭测试连接
            test_ws.close()
            return True, "连接成功"
        except websocket.WebSocketTimeoutException:
            return False, "连接超时"
        except websocket.WebSocketBadStatusException as e:
            return False, f"握手失败: {str(e)}"
        except Exception as e:
            return False, f"连接失败: {str(e)}"
        finally:
            if test_ws:
                test_ws.close()

    def connect(self):
        """ 建立WebSocket连接前先执行测试 """
        # 测试接收端连接
        success, msg = self.test_connection(self.recive_url, self.token)
        if not success:
            log.error(msg)
            exit(1)

        # 测试通过后建立正式连接
        self.recive_ws = websocket.WebSocketApp(
            self.recive_url,
            header=self.headers,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close
        )

        self.thread = threading.Thread(target=self.recive_ws.run_forever)
        self.thread.daemon = True
        self.thread.start()

    def _on_open(self, ws):
        """ 连接成功回调 """
        log.info(f"连接 {self.recive_url} 成功")

    def _on_message(self, ws, message):
        """ 处理接收到的消息 """
        try:
            data = json.loads(message)
        except json.JSONDecodeError:
            log.error(f"JSON 错误: {message}")
            return
        if data.get('status', None) == 'failed':
            self.retcode = (data.get('code', None), data.get('message', None))
            self.is_quit = True
        # 处理元事件
        if data.get('post_type') == 'meta_event':
            self._handle_meta_event(data)
        else:
            self.on_message(message)

    def _handle_meta_event(self, data):
        """ 处理元事件 """
        meta_type = data.get('meta_event_type')
        if meta_type == 'lifecycle':
            sub_type = data.get('sub_type')
            if sub_type == 'connect':
                log.info("连接 机器人 成功")
            elif sub_type in ['enable', 'disable']:
                log.info(f"机器人状态已更改为: {sub_type}.")
        elif meta_type == 'heartbeat':
            self.last_heartbeat_time = time.time()
            self.heartbeat_interval = data.get('interval', 15000)
            status = data.get('status', {})
            log.debug(f"心跳 间隔: {self.heartbeat_interval}ms, 状态: {status}")

    def _on_error(self, ws, error):
        """ 错误处理 """
        log.error(f"服务错误: {error}")
        if "10054" in str(error):
            log.warning("远程主机强迫关闭了一个现有的连接")
            self.is_quit = True

    def _on_close(self, ws, status, reason):
        """ 连接关闭处理 """
        if self.is_quit:
            status, reason = self.retcode
        log.warning(f"连接已关闭 状态码: {status}, 数据: {reason}，连接断开来自于服务端")
        self.last_heartbeat_time = None
        self.heartbeat_interval = None

    def _send(self, data: dict) -> dict:
        """ 发送API请求 """
        if self.send_ws is None:
            self.send_ws = websocket.WebSocket()
            self.send_ws.connect(self.send_url, header=self.headers)

        try:
            # 发送JSON序列化后的数据
            self.send_ws.send(data)
            response = self.send_ws.recv()
            return json.loads(response)
        except Exception as e:
            log.error(f"发送消息失败: {e}")
            return {"error": str(e)}
        finally:
            # 发送后关闭API连接（根据OneBot建议，每次API调用独立连接）
            self.send_ws.close(status=1000, reason="关闭API连接")
            self.send_ws = None

    def _close(self):
        """ 关闭所有连接 """
        if self.recive_ws:
            self.recive_ws.close(status=1000, reason="关闭接收连接")
        if self.send_ws:
            self.send_ws.close(status=1000, reason="关闭发送连接")
        log.info("关闭所有连接")
