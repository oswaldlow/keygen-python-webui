# GoEdge 激活码生成工具

## 事情起因

由于 GoEdge 官方在 1.4.0 和 1.4.1 版本中添加了有毒的 .js 文件（域名：cdn.jsdelivr.vip），这些文件会自动跳转至不良网站（如黄网和博彩网站），因此被社区大佬破解了。详情请参考 [此页面](https://www.nodeseek.com/post-138216-1)。

市面上的注册机大多数都需要下载和配置环境。网上的通用的万能钥匙，无法自定义“公司/组织名”来整活。因此本项目诞生了！

## 这个是 Demo 页面
你可以通过访问 [api.demonsword.top/goedge](http://api.demonsword.top/goedge) 来体验生成激活码的功能。

## 项目功能

- **简化激活码生成**：不需要手动下载和配置环境。
- **一键生成激活码**：只需一行命令，即可完成激活码生成。
- **支持自定义**：“公司/组织名”可以根据需要自定义。

# 此激活码生成工具理论上适用于以下版本的 GoEdge：

- v1.3.2
- v1.3.9
- v1.4.0
 - v1.4.1

其他版本的 GoEdge 激活码可能也适用，请自行测试以确认兼容性。

## 使用激活码的教程

### 中文版

1. 登录 GoEdge 后台。
2. 点开 **系统设置**
3. 点击 **商业版本**
4. 点击顶部的 **激活**
5. 将生成出来的激活码填入，然后点击 **激活**，完成！

### 英文版

1. 登录 GoEdge 后台
2. 点开 **Settings**.
3. 点击 **Commercial Authority**.
4. 点击顶部的 “激活”。
5. 将生成出来的激活码填入，然后点击 “激活”，完成！

# 本项目依赖以下技术：

- **Python**：作为主编程语言。
- **Cryptography**：用于加密和解密操作。
- **Flask**：用于构建 Web 服务。
- **Base64**：用于数据编码和解码。

## 使用方法

1. **安装依赖**：确保你的环境中已安装 Python 和必要的库。可以通过以下命令安装：
    ```bash
    pip install cryptography flask base64
    ```

2. **启动服务**：运行以下命令启动 Flask 服务：
    ```bash
    python back-end.py
    ```

## 贡献

本项目是从 [GoEdge233/keygen-python](https://github.com/GoEdge233/keygen-python) fork ，特别感谢 goedge233 的原始工作和贡献。欢迎提交问题报告和功能请求，或者直接贡献代码。

如需讨论或交流，请加入 Telegram 频道 [GoEdge233](https://t.me/goedge233) 进行吹水。

## 许可证

本项目使用 [Apache 2.0 许可证](LICENSE) 进行授权。
