# TRAE 工具安装状态清单

> 生成时间：2026-10-30
> 项目：晴雨（ClearRain）

---

## ✅ 已安装且可用（无需操作）

### Skills（核心需求全部覆盖）

| Skill | 来源 | 用途 |
|-------|------|------|
| frontend-design | 插件 | 前端设计原则，配合 Design 模式出原型 |
| brainstorming | 内置 | 需求梳理 |
| rapid-prototype-craft | 插件 | 高保真交互原型生成 |
| uicraft | 插件 | 网页界面设计与打磨 |
| canvas | 内置 | 数据可视化（图表） |
| html-report | 插件 | HTML 报告 + ECharts 图表 |
| impeccable | 内置 | UI/UX 审查 |
| verification-before-completion | 内置 | 测试验收 |
| systematic-debugging | 内置 | 调试 |
| test-driven-development | 内置 | TDD |
| review-bugbot / review-security | 内置 | 代码审查 |
| code-review-report | 插件 | 代码审查报告 |
| django-tdd | 内置 | Django 测试 |
| vue-best-practices | 内置 | Vue 3 规范 |
| prd-authoring | 插件 | PRD 撰写 |
| github | 插件 | GitHub 操作 |
| **git-commit** | **本次新建** | **本项目提交规范** |

> 注：`chart-visualization` 和 `webapp-testing` 未单独安装，但已由 `canvas`+`html-report`（ECharts）和 `verification-before-completion` 覆盖，无需额外安装。
> 注：`frontend-skill` 已安装但与 `frontend-design` 功能重叠，可忽略或卸载。

### MCP Servers

| MCP | 来源 | 状态 |
|-----|------|------|
| integrated_code_mode (Exec) | 内置 | ✅ 可用 |
| integrated_default (生成图片/视频等) | 内置 | ✅ 可用 |
| code-review-report | 插件 | ✅ 可用 |
| deployment | 插件 | ✅ 可用 |
| mysql | 插件 | ✅ 可用（需配置连接） |
| Memory | 内置 | ✅ 可用（TRAE 原生记忆） |

---

## 🔧 我已创建（需你补全配置）

### 1. git-commit Skill
路径：`~/.trae-cn/skills/git-commit/SKILL.md`
状态：✅ 已创建，重启 TRAE 后生效

### 2. Context7 MCP 配置
路径：`D:\my_project3\.trae\mcp.json`
状态：⚠️ 需你完成两步：
1. 去 https://context7.com 注册获取 API Key
2. 打开 `D:\my_project3\.trae\mcp.json`，把 `YOUR_CONTEXT7_API_KEY` 替换为真实 Key

---

## 🖱️ 需要你在 TRAE 界面手动操作

### 操作 1：连接 GitHub（OAuth，必须）
GitHub MCP 需要登录授权才能管理仓库/Issue/PR。

**步骤：**
1. TRAE 左下角 → 账户/插件 → 找到 `github` 插件
2. 点击「连接」/「Connect」，用 GitHub 账号授权
3. 授权成功后，GitHub MCP 即可在对话中使用

### 操作 2：启用项目级 MCP（让 Context7 生效）
**步骤：**
1. TRAE 设置 → MCP
2. 打开「项目级 MCP」开关（弹窗点确认）
3. 确认 `D:\my_project3` 已在 TRAE 中打开（作为工作区）
4. 重启 TRAE，Context7 MCP 会自动加载

### 操作 3（可选）：从市场安装额外 MCP
如需更多能力，可在 设置 → MCP → 添加 → 从市场添加 中搜索：
- `context7`（如不用项目级配置，可市场安装）
- `github`（如插件连接器不可用）
- `memory`（如需独立知识图谱记忆，TRAE 内置记忆已够用）

---

## 验证方法

重启 TRAE 后，在对话中输入 `/` 或查看可用工具列表，确认：
- [ ] git-commit skill 出现
- [ ] context7 MCP 出现（且 resolve-library-id / query-docs 可用）
- [ ] github MCP 出现（且 create_repository / list_issues 等可用）
