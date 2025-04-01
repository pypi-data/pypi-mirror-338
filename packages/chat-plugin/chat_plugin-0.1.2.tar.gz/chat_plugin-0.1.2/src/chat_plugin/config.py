from nonebot import get_driver
from pydantic import Extra
from pydantic_settings import BaseSettings  # 注意这里的变化

class Config(BaseSettings):
    """
    插件配置项
    会自动从 .env 文件中读取 OLLAMA_URL 配置
    """
    ollama_url: str = "http://localhost:11434"  # 默认值
    
    class Config:
        extra = Extra.ignore  # 忽略其他未定义字段
        env_file = ".env"     # 指定从 .env 文件读取
        env_file_encoding = "utf-8"

# 获取全局驱动配置
driver = get_driver()

# 合并配置
plugin_config = Config(**driver.config.dict())