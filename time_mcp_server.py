from mcp.server.fastmcp import FastMCP
from datetime import datetime
import logging
import sys

logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.StreamHandler(sys.stdout),  # 输出到控制台
            logging.FileHandler('logs/app.log')      # 输出到文件
        ]
    )


mcp = FastMCP('time')

@mcp.tool()
async def get_current_datetime():
    """获取当前时间

    Returns:
        str: 当前时间，返回格式yyyy-MM-dd HH:mm:ss，示例 2025-04-23 12:00:00
    """
    logging.info('获取当前时间')
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@mcp.tool()
async def get_devices_by_room(room_name: str = None):
    """根据房间名称查询设备列表
    Args:
        room_name (str, optional): 房间名称，示例：302

    Returns:
        str: 房间中设备列表，
        示例：
        设备列表如下：
        --- did=111, device_name=吸顶灯, room_name=302, gateway_did=g999
        --- did=g999, device_name=蓝牙网关, room_name=302

    """
    device_str_list = [
        'did=111, device_name=吸顶灯, room_name=302, gateway_did=g999, online=false',
        'did=222, device_name=窗帘, room_name=302, gateway_did=g999, online=false',
        'did=333, device_name=走廊灯, room_name=302, gateway_did=g999, online=false',
        'did=g999, device_name=蓝牙网关, room_name=302, online=false'
    ]
    return '设备列表如下：' + '\n--- '.join(device_str_list)


if __name__ == "__main__":
    mcp.run(transport='sse')
