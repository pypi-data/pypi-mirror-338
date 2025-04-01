# Abundance 项目

## 项目简介
“Abundance” 是一个功能强大的 Python 框架，融合了多种优秀框架的设计理念。它以 PyQt 为基础构建 GUI 界面，借鉴了 Vue3 的目录结构与规范，以及 Spring Boot 的多模块设计思想，为开发者提供高效、灵活且易于维护的开发体验。项目启动时会自动加载配置参数，还能展示定制的 banner 信息，同时支持 Redis 缓存操作。

## 主要特性
### 启动配置加载
项目启动时会从配置文件自动加载参数，支持根据不同环境（开发、测试、生产）进行灵活配置，确保项目在各环境下稳定运行。例如，开发环境可开启调试信息，生产环境则关闭以提升性能。

### Banner 打印
启动时展示定制的 banner 信息，开发者可修改 `resources/banner.txt` 文件内容，打造独特的启动仪式感。

### Redis 缓存支持
提供了丰富的 Redis 操作工具类 `RedisUtils`，支持对字符串、哈希、集合、列表等多种数据类型的缓存操作，包括设置过期时间、批量获取和删除等功能。

### 组件注册与依赖注入
通过 `InstanceContainer` 实现组件的注册和依赖注入，方便管理项目中的组件。

## 目录结构
### 根目录
- **abundance**：框架核心代码目录。
    - **Abundance.py**：包含项目的基本信息，如名称、版本、作者等。
    - **AbundanceApplication.py**：项目的启动类，负责环境准备、组件注册、依赖注入、日志设置和 banner 打印等操作。
    - **util**：工具类目录，包含 `StopWatch.py`（用于计时）、`data_utils.py` 和 `path_utils.py` 等工具函数。
    - **pyqt**：与 PyQt 相关的代码目录，包含 `router.py`（路由管理）、`store.py`（数据存储）等。
    - **beans**：组件相关目录，包含组件工厂等。
    - **log**：日志设置目录，包含 `LoggingSetup.py` 用于配置日志。
    - **loader**：资源加载目录，包含 `PropertyLoader.py`（属性加载）、`Resource.py`（资源类）和 `ResourceLoader.py`（资源加载器）。
    - **core**：核心功能目录，包含环境配置、实例管理和属性配置等子目录。
    - **bridge**：桥接相关代码目录，包含 `bridge.py` 和 `route.py`。
    - **context**：上下文相关目录，包含属性配置相关代码。
    - **banner**：banner 相关代码目录，包含 `AbundanceApplicationBannerPrinter.py`（banner 打印器）、`AbundanceBanner.py` 和 `BannerMode.py`（banner 显示模式）。
- **resources**：资源目录，存放项目所需的各种资源文件。
    - **config**：存放配置文件，如项目的配置参数、数据库连接信息等。这些配置文件可根据不同的环境进行修改，以满足项目的不同需求。
    - **banner.txt**：启动 banner 的相关文本文件，开发者可以修改其中的内容来定制启动时的 banner 信息。
- **main.py**：项目的主启动文件，是项目的入口点。运行该文件即可启动整个项目。
- **poetry.lock**：Poetry 生成的依赖锁定文件，记录了项目所依赖的具体版本信息，可确保项目在不同环境下使用的依赖版本一致，避免因版本差异而导致的问题。
- **pyproject.toml**：Poetry 的项目配置文件，定义了项目的元数据（如项目名称、版本号、作者等）和依赖关系。开发者可以在这里添加或修改项目的依赖信息。

## 依赖管理
使用 Poetry 作为包管理器，确保项目依赖的一致性和可重复性。在项目根目录下，运行以下命令安装项目所需的依赖：
```bash
poetry install
```
该命令会根据 `pyproject.toml` 文件中的依赖信息，自动下载并安装项目所需的所有依赖。同时，它会使用 `poetry.lock` 文件来确保安装的依赖版本与开发环境一致。

## 使用说明
### 配置文件
根据项目需求，在 `resources/config` 目录下配置相关参数。可以创建不同的配置文件，如 `development.ini` 用于开发环境，`production.ini` 用于生产环境。在配置文件中，可以设置数据库连接信息、API 接口地址、调试开关等参数。

### 启动项目
在完成依赖安装和配置文件设置后，运行以下命令启动项目：
```bash
python main.py
```
项目启动时，会自动加载配置文件中的参数，并展示定制的 banner 信息。

## Redis 缓存使用示例
```python
from abundance_common.core.utils.RedisUtils import RedisUtils

# 初始化 Redis 连接
redis_utils = RedisUtils()

# 设置缓存
redis_utils.set('key', 'value', time=60)

# 获取缓存
result = redis_utils.get('key')
print(result)

# 删除缓存
redis_utils.del_key('key')
```

## 贡献与反馈
欢迎广大开发者为 “Abundance” 项目贡献代码、提出建议或反馈问题。你可以通过以下方式参与项目开发：
- **提交 Issue**：在 GitHub 上的 Issues 页面提交问题或建议，详细描述问题的现象、复现步骤和期望的结果。
- **提交 Pull Request**：如果你有代码贡献，可以提交 Pull Request。在提交之前，请确保你的代码符合项目的代码规范，并添加必要的测试用例。

希望 “Abundance” 项目能够为你的开发工作带来便利和帮助！