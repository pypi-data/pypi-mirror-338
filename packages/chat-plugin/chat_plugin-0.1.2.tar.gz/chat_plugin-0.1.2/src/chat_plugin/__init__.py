from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata

from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot import on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message
from nonebot.log import logger  # 添加日志


from ollama import Client

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="Chat_Plugin",
    description="获取@机器人的消息,并且调用本地的ollama服务进行回复",
    usage="机器人将发送模型的回复内容",
    config=Config,
)

config = get_plugin_config(Config)


#获取ollama的地址
ollama_url = config.ollama_url


repeater = on_message(priority=1)

@repeater.handle()
async def handle_at_repeater(event: GroupMessageEvent):
    # 调试:打印完整事件
    logger.debug(f"原始消息: {event.original_message}")

    # 检查是否@机器人
    is_at_bot = any(
        seg.type == "at" and seg.data["qq"] == str(event.self_id)
        for seg in event.original_message
    )
    if not is_at_bot:
        logger.debug("未@机器人,忽略")
        return

    # 提取纯文本
    user_msg = "".join(
        seg.data["text"] for seg in event.original_message 
        if seg.type == "text"
    ).strip()
    logger.debug(f"提取内容:'{user_msg}'")

    if not user_msg:
        await repeater.send("请发送问题")
    else:
        try:
            client = Client(host=ollama_url)
            response = client.chat(
                model='qwen2.5:latest',
                messages=[{
                    'role': 'user',
                    'content': user_msg,
                }]
            )
            await repeater.send(f"{response['message']['content']}")
        except Exception as e:
            logger.error(f"调用Ollama失败: {e}")
            await repeater.send("处理请求时出错,请稍后再试")