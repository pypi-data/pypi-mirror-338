# -*- coding: utf-8 -*-

from mcp.server.fastmcp import FastMCP
from pydantic import Field
import logging
from bilibili_api import hot, sync, search, rank, video  # 添加video导入
logger = logging.getLogger("mcp")


# 初始化mcp服务
mcp = FastMCP("bilibili-mcp-server-full")

# 定义工具
@mcp.tool(name="B站基础搜索",description="按照关键词搜索Bilibili视频信息")
async def search_video(keyword: str = Field(description="搜索关键词")):
    """
    搜索视频

    Args:
        keyword (str): 搜索关键词
    Returns:
        dict: 搜索结果
    """
    try:
        result = sync(search.search(keyword))

        # 只返回视频信息
        
        return result
    except Exception as e:
        logger.error(f"搜索视频失败: {e}")
        return None

@mcp.tool(name="B站全站排行",description="获取Bilibili全站排行")
async def get_all_rank():
    """
    获取Bilibili全站排行
    Returns:
        dict: 全站排行
    """
    try:
        result = sync(rank.get_rank())
        return result
    except Exception as e:
        logger.error(f"获取全站排行失败: {e}")
        return None  


# 获取热门内的综合热门
@mcp.tool(name="B站综合热门",description="获取Bilibili综合热门视频")
async def get_hot_videos():
    """
    获取Bilibili综合热门视频
    Returns:
        dict: 综合热门视频
    """
    try:
        result = sync(hot.get_hot_videos())
        return result
    except Exception as e:
        logger.error(f"获取综合热门视频失败: {e}")
        return None

@mcp.tool(name="B站热门搜索词",description="获取Bilibili热门搜索词")
async def get_hot_buzzwords():
    """
    获取Bilibili热门搜索词
    Returns:
        dict: 热门搜索词
    """
    try:
        result = sync(hot.get_hot_buzzwords())
        return result
    except Exception as e:
        logger.error(f"获取热门搜索词失败: {e}")
        return None

@mcp.tool(name="B站视频信息", description="根据BVID获取Bilibili视频详细信息")
async def get_video_info(bvid: str = Field(description="视频BVID，如BV1MbZnYoEk1")):
    """
    根据BVID获取视频详细信息
    
    Args:
        bvid (str): 视频BVID
    Returns:
        dict: 视频详细信息
    """
    try:
        v = video.Video(bvid=bvid)
        info = sync(v.get_info())
        # 获取当前在线人数
        online_count = sync(v.get_online())
        info["online_count"] = online_count
        # 获取视频标签
        tags = sync(v.get_tags())
        info["tags"] = tags
        return info
    except Exception as e:
        logger.error(f"获取视频信息失败: {e}")
        return None


def run():
    mcp.run(transport="stdio")



if __name__ == "__main__":
   run()