# Chat_Plugin

## 本人仅为一学生,项目仅供学习参考,本人不会对项目进行任何维护

## 简介
`Chat_Plugin` 是一个基于 NoneBot 的插件,用于获取群聊中 @ 机器人的消息,并调用本地的 Ollama 服务进行回复.

## 下载方式

### 通过 GitHub 下载
你可以通过以下步骤从 GitHub 下载本插件:
1. 克隆仓库到本地:
```bash
git clone https://github.com/Ender-Kylin/Chat_Plugin.git
```

### 通过 Gitee 下载
如果你想从 Gitee 下载本插件,可以按照以下步骤操作:
1. 克隆仓库到本地:
```bash
git clone https://gitee.com/enderkylin/chat_-plugin.git
```


## 安装
将本插件添加到你的 NoneBot 项目中,在项目的 `bot.py` 或其他入口文件中添加以下代码:
```python
nonebot.load_plugin("chat_plugin")
```

## 配置文件示例
在 `.env` 文件中,添加 Ollama 的服务地址.示例如下:
```plaintext
OLLAMA_URL=http://localhost:11434
```
你可以根据实际情况修改 `OLLAMA_URL` 的值.如果不提供 `.env` 文件,插件将使用默认的地址 `http://localhost:11434`.

## 使用方法
在群聊中,@ 机器人并发送问题,机器人将调用 Ollama 服务进行回复,并将回复内容发送到群聊中.

## 错误处理
如果在调用 Ollama 服务时出现错误,插件将记录错误日志,并向群聊发送一条提示消息,告知用户处理请求时出错,请稍后再试.

## 开源许可证
本插件采用 [MIT 许可证](LICENSE) 进行开源.

## 贡献
如果你想为这个项目做出贡献,请随时提交 issue 或 pull request.我们欢迎任何形式的贡献,包括但不限于 bug 修复、功能增强、文档改进等.

