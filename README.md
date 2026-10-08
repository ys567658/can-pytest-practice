# 虚拟 CAN 总线自动化测试脚本 (Virtual CAN Bus Pytest Script)

## 📌 项目背景
本项目是基于 Python `python-can` 与 `pytest` 框架编写的虚拟 CAN 总线通信自动化测试脚本。用于模拟车载电子控制单元（ECU）在 CAN 总线上的报文广播、接收以及断言验证流程。该项目旨在为汽车电子硬件在环（HIL）测试提供基础的工程化测试模板。

## 🛠️ 技术栈
*   编程语言：Python
*   核心库：python-can, pytest
*   通信协议：CAN 2.0 (标准帧)
*   版本管理：Git / GitHub

## 📂 核心功能
*   使用虚拟 CAN 通道 (`vcan0`) 模拟多节点总线通信。
*   发送指定 ID (`0x123`) 和车速数据 (`0x64`) 的 CAN 报文。
*   接收端监听总线并捕获报文。
*   使用 `assert` 断言验证报文的 ID 和数据载荷是否匹配预期，实现无人值守的自动化判断。

## 🚀 如何运行
1. 安装依赖：
   ```bash
   pip install python-can pytest
