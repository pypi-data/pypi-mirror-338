class WebSocketApplication:
    """WebSocket应用基类（用户继承实现业务逻辑）"""
    def __init__(self, connection):
        self.connection = connection
        self.path_params = None

    def on_open(self):
        """连接建立时触发"""
        pass

    def on_message(self, message):
        """收到文本消息时触发"""
        pass

    def on_binary(self, data):
        """收到二进制消息时触发"""
        pass

    def on_close(self):
        """连接关闭时触发"""
        pass