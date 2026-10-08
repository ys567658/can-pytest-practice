import can
import time


# 定义一个测试函数，pytest 会自动发现它
def test_can_communication():
    # 使用 with 语句自动管理资源
    with can.interface.Bus(interface='virtual', channel='vcan0') as bus_send, \
            can.interface.Bus(interface='virtual', channel='vcan0') as bus_recv:
        speed = 100
        msg = can.Message(
            arbitration_id=0x123,
            data=[0x00, speed],
            is_extended_id=False
        )
        bus_send.send(msg)
        time.sleep(0.1)
        received = bus_recv.recv(timeout=1.0)

        # 核心变化：用 assert 断言替代 if 打印
        assert received is not None, "错误：接收端超时，没有收到任何报文！"
        assert received.arbitration_id == 0x123, f"错误：ID 不匹配！期望 0x123，实际收到 {hex(received.arbitration_id)}"
        assert received.data == bytearray([0x00, 100]), f"错误：数据不匹配！期望 [0x00, 100]，实际收到 {received.data}"