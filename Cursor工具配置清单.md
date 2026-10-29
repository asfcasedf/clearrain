# Cursor 工具配置清单

> 项目：晴雨（ClearRain）
> Cursor 职责：仅操作 `src/` 目录，按 docs/ 文档编码

---

## ✅ 已就绪

### Cursor Rules（项目级，放 `D:\my_project3\.cursor\rules\`）

| 文件 | 内容 | 状态 |
|------|------|------|
| 00-ai-coding-workflow.mdc | 小步快跑、分层开发、精准修改、回滚策略 | ✅ 已复制 |
| 01-coding-standard.mdc | 全栈编码规范（接口格式/路由/权限/部署） | ✅ 已复制 |
| 02-ui-design.mdc | 温暖治愈 UI 设计系统（配色/字体/动效/文案） | ✅ 已复制 |
| 03-git-workflow.mdc | Git 分支/commit/回滚规范 | ✅ 已复制 |
| 04-django-practices.mdc | Django 5.1 + DRF 最佳实践（Service层/事务/N+1） | ✅ 本次新建 |
| 05-vue3-practices.mdc | Vue 3.4 + Vant/Element Plus 规范 | ✅ 本次新建 |

### Cursor Skills（全局，`~/.cursor/skills/`）

| Skill | 状态 |
|-------|------|
| impeccable | ✅ 已安装 |

### MCP 配置文件

| 文件 | 内容 |
|------|------|
| `~/.cursor/mcp.json` | GitHub + Context7（需填 Token） |

---

## ⚠️ 需你补全的配置

### 1. GitHub Token
打开 `~/.cursor/mcp.json`，把 `YOUR_GITHUB_TOKEN` 替换为真实 Token。

**获取方式：**
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token，勾选 `repo`、`workflow` 权限
3. 复制 token 填入

### 2. Context7 API Key
同一个文件里把 `YOUR_CONTEXT7_API_KEY` 替换。

**获取方式：** https://context7.com 注册

---

## 🔧 需你在 Cursor 界面操作

### 启用 MCP
1. 打开 Cursor
2. Settings → MCP
3. 确认 `github` 和 `context7` 出现在列表中并已启用（绿灯）
4. 如未出现，点「Add MCP Server」手动添加

### 确认 Rules 生效
1. 在 Cursor 中打开 `D:\my_project3`
2. 右下角或 Settings → Rules 确认 6 个 .mdc 文件已加载
3. `alwaysApply: true` 的规则会自动应用

---

## ⚠️ 已知版本冲突（需确认）

现有 `01-coding-standard.mdc` 写的是：
- Python 3.10、Django 4.2.8

但项目文档《开发准备清单》要求：
- Python 3.13、Django 5.1

**建议**：以项目文档为准，将 01 规则里的版本号改为 Python 3.13 / Django 5.1。
需要我帮你改吗？

---

## 验证方法

重启 Cursor 后：
- [ ] 6 个 Rules 全部加载
- [ ] GitHub MCP 可用（能调用 create_repository 等）
- [ ] Context7 MCP 可用（能调用 resolve-library-id）
- [ ] impeccable skill 可调用
