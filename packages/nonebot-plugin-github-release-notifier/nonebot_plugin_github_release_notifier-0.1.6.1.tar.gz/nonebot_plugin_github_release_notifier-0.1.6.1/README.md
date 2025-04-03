# Nonebot_plugin_github_release_notifier

一个用于监控 GitHub 仓库发布并发送通知的插件。

## 功能
- 监控多个 GitHub 仓库。
- 通过qq bot通知用户新动态。
- 可自定义通知格式。

## 写在最前面
本插件使用aiohttp获取github api数据，但是国内目前无法稳定连接github api

如有连接问题请尝试使用代理或其他工具

## 安装

### 通过nb-cli安装
```nb-cli install nonebot-plugin-github-release-notifier```
### 通过pip安装
```pip install nonebot-plugin-github-release-notifier```

### 复制仓库安装
1. 克隆仓库：
    ```bash
    git clone https://github.com/HTony03/nonebot_plugin_github_release_notifier.git
    ```
2. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```
3. 将插件置于你的plugins文件夹

## 使用
#### pyproject.toml使用
在`pyproject.toml`文件中添加以下内容
```toml
[tool.nonebot]
plugins = ["nonebot_plugin_github_release_notifier"]
```
#### bot.py使用
```python title="bot.py"
import nonebot
from nonebot.adapters.onebot.v11 import Adapter

nonebot.init(_env_file=".env")

driver = nonebot.get_driver()
driver.register_adapter(Adapter)

nonebot.load_builtin_plugins()

# load other plugins

nonebot.load_plugin("nonebot_plugin_apscheduler")
nonebot.load_plugin("nonebot_plugin_github_release_notifier")

nonebot.run()

```
## 配置
相关`.env`配置项如下

所有配置项均为可选参数 群组可通过command添加

使用前请确保nonebot的`SUPERUSERS`配置项已配置

```dotenv
# 在获取失败时是否发送失败信息
GITHUB_SEND_FAILURE_GROUP=True
GITHUB_SEND_FAILURE_SUPERUSER=False

# 用于访问 GitHub API 的 GitHub Token
# 接受任何 Token，无论是classic Token还是full_grained access Token
GITHUB_TOKEN=""

# 群组到仓库的映射(自动添加到数据库，以数据库配置作为第一数据源)
# 格式: {group_id: [{repo: str (, commit: bool)(, issue: bool)(, pull_req: bool)(, release: bool)}]}
GITHUB_NOTIFY_GROUP={}

# 验证 GitHub Token 的最大重试次数
GITHUB_VALIDATE_RETRIES=3

# 每次验证重试之间的延迟（以秒为单位）
GITHUB_VALIDATE_DELAY=5

# 删除群组仓库(用于删除数据库配置)
# 格式: {group_id: ['repo']}
GITHUB_DEL_GROUP_REPO={}

# 在获取仓库数据失败时禁用配置
GITHUB_DISABLE_WHEN_FAIL=False

# bot发送模版
# 格式: {"commit": <your_template>, "issue": <your_template>, "pull_req": <your_template>, "release": <your_template>}
# 可用参数：
# commit: repo, message, author, url
# issue: repo, title, author, url
# pull_req: repo, title, author, url
# release: repo, name, version, details, url
# 用法: '{<parameter>}' (使用python format功能实现)
# 未设定时使用默认模版
GITHUB_SENDING_TEMPLATES={}

# repo添加入群聊时的默认设置
GITHUB_DEFAULT_CONFIG_SETTING=True
```

### 命令
(此部分中的repo名均可使用repo链接，repo的.git链接代替)
#### **1. 添加群组仓库映射**
**命令**: `/add_group_repo` 或 `/add_repo`  
**权限**: SUPERUSERS或群聊管理员/群主  
**说明**: 添加一个新的群组到仓库的映射。

- **群组消息**:
  - **格式**: `/add_group_repo <仓库名>`
  - **示例**: `/add_group_repo <user>/<repo>`
- **私聊消息**:
  - **格式**: `/add_group_repo <仓库名> <群组ID>`
  - **示例**: `/add_group_repo <user>/<repo> 123456`

---

#### **2. 删除群组仓库映射**
**命令**: `/del_group_repo` 或 `/del_repo`  
**权限**: SUPERUSERS或群聊管理员/群主  
**说明**: 删除一个群组到仓库的映射。

- **群组消息**:
  - **格式**: `/del_group_repo <仓库名>`
  - **示例**: `/del_group_repo <user>/<repo>`
- **私聊消息**:
  - **格式**: `/del_group_repo <仓库名> <群组ID>`
  - **示例**: `/del_group_repo <user>/<repo> 123456`

---

#### **3. 修改仓库配置**
**命令**: `/change_repo_config` 或 `/repo_cfg`  
**权限**: SUPERUSERS或群聊管理员/群主  
**说明**: 修改群组仓库的配置项。

- **群组消息**:
  - **格式**: `/change_repo_config <仓库名> <配置项> <值>`
  - **示例**: `/change_repo_config <user>/<repo> issue False`
- **私聊消息**:
  - **格式**: `/change_repo_config <仓库名> <群组ID> <配置项> <值>`
  - **示例**: `/change_repo_config <user>/<repo> 123456 issue False`
- **支持的配置项**:
  - `commit` (提交通知)
  - `issue` (问题通知)
  - `pull_req` (拉取请求通知)
  - `release` (发布通知)

---

#### **4. 查看群组仓库映射**
**命令**: `/show_group_repo` 或 `/group_repo`  
**权限**: SUPERUSERS或群聊管理员/群主  
**说明**: 查看当前群组或所有群组的仓库映射及其配置。

- **群组消息**:
  - **格式**: `/show_group_repo`
  - **示例**: `/show_group_repo`
- **私聊消息**:
  - **格式**: `/show_group_repo`
  - **示例**: `/show_group_repo`

---

#### **5. 刷新 GitHub 状态**
**命令**: `/refresh_github_stat`  
**权限**: SUPERUSERS或群聊管理员/群主  
**说明**: 手动刷新 GitHub 仓库的状态。

- **格式**: `/refresh_github_stat`
- **示例**: `/refresh_github_stat`

---

#### **6. 重新加载数据库**
**命令**: `/reload_database` 或 `/reload_db`  
**权限**: SUPERUSERS或群聊管理员/群主  
**说明**: 重新加载数据库中的群组和仓库映射。

- **格式**: `/reload_database`
- **示例**: `/reload_database`

---

### 示例
1. 添加仓库映射：
   ```
   /add_group_repo <user>/<repo>
   ```
2. 删除仓库映射：
   ```
   /del_group_repo <user>/<repo>
   ```
3. 修改仓库配置：
   ```
   /change_repo_config <user>/<repo> issue False
   ```
4. 查看当前群组的仓库映射：
   ```
   /show_group_repo
   ```
5. 刷新 GitHub 状态：
   ```
   /refresh_github_stat
   ```
6. 重新加载数据库：
   ```
   /reload_database
   ```

### TODOS

- [x] 自定义发送信息格式
- [ ] 添加help
- [ ] 数据库结构重置


## LICENCE
本插件按照MIT协议传播

## Releases
`V0.1.2` 修改发布信息

`V0.1.0`-`V0.1.1` 主程序完成，功能适配， 准备发布
