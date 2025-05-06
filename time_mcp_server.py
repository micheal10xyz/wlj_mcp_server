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


mcp = FastMCP('smart-hotel')

@mcp.tool()
async def get_current_datetime():
    """获取当前时间

    Returns:
        str: 当前时间，返回格式yyyy-MM-dd HH:mm:ss，示例 2025-04-23 12:00:00
    """
    logging.info('获取当前时间')
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@mcp.tool()
async def get_history_properties(did: str = None):
    """根据设备ID获取历史属性

    Returns:
        List[str]: 设备历史属性
        格式描述：
        ---time表示发生时间
        ---did表示设备ID
        ---property表示属性名称
        ---value表示属性值
        返回值示例：
        [
            "time=2025-04-28 12:00:00, did=111, property=开关，value=true",
            "time=2025-04-28 12:00:00, did=111, property=开关，value=false",
            "time=2025-04-29 12:00:00, did=111, property=开关，value=true"
        ]
    """
    logging.info('获取历史属性')
    history_properties = [
        "time=2025-04-28 12:00:00, did=111, property=开关，value=true",
        "time=2025-04-28 12:00:00, did=111, property=开关，value=false",
        "time=2025-04-29 12:00:00, did=111, property=开关，value=true",
        "time=2025-05-01 12:00:00, did=111, property=开关，value=false",
        "time=2025-05-06 12:00:00, did=111, property=开关，value=true"
    ]
    return history_properties



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
    logging.info('获取设备列表')
    device_str_list = [
        'did=111, device_name=吸顶灯, room_name=302, gateway_did=g999, online=false',
        'did=222, device_name=窗帘, room_name=302, gateway_did=g999, online=false',
        'did=333, device_name=走廊灯, room_name=302, gateway_did=g999, online=false',
        'did=g999, device_name=蓝牙网关, room_name=302, online=false'
    ]
    return '设备列表如下：' + '\n--- '.join(device_str_list)


if __name__ == "__main__":
    mcp.run(transport='sse')
