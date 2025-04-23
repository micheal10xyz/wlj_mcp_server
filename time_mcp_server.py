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
        str: 当前时间，返回格式yyyy-MM-dd HH:mm:ss，如2025-04-23 12:00:00
    """
    logging.info('获取当前时间')
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@mcp.tool()
async def get_weather(datetime: str = None):
    """查询天气

    Args:
        datetime (str, optional): 日期时间，格式yyyy-MM-dd HH:mm:ss，如2025-04-23 12:00:00

    Returns:
        str: 内容包含天气，风速风向，空气质量
    """
    return '天气晴，北风4级，空气质量优'


if __name__ == "__main__":
    mcp.run(transport='sse')
