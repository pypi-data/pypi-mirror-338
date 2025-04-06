import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nonebot_plugin_baisuwen",  # 替换为你的包名（PyPI唯一标识）
    version="1.1.0",          # 初始版本号
    author="LongYue",       # 你的名字/用户名
    author_email="2279303156@qq.com",
    description="基于DeepSeek的智能聊天机器人，打造属于你的赛博群友",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Longxuanyue/nonebot_plugin_baisuwen",  # 项目主页
    packages=setuptools.find_packages(),  # 自动发现包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 选择许可证
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Python版本要求
    install_requires=[
        "nonebot2>=2.0.0",                 # 核心框架
        "nonebot-adapter-onebot-v11",      # OneBot协议适配器
        "httpx>=0.23.0",                   # HTTP客户端（用于DeepSeek API请求）
        "tenacity>=8.2.2",                 # 重试机制
        "redis>=4.5.1",                    # Redis客户端（含异步支持）
        "python-dotenv>=0.21.0",           # 环境变量加载（NoneBot标准配置方式）
        "msgpack>=1.0.5"                   # Redis数据序列化
    ],
    # 可选额外依赖
    extras_require={
        "dev": [
            "pytest>=7.0",                # 测试框架
            "pytest-asyncio>=0.21.0",      # 异步测试支持
            "black>=23.3.0",               # 代码格式化
            "mypy>=1.3.0"                  # 类型检查
        ]
    }
)