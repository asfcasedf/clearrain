# AGENTS.md — Cursor 项目指令

> 本文件由 Cursor 自动加载，作为项目的持久上下文。所有编码任务必须遵守。

## 项目：晴雨（ClearRain）

大学生心理健康测评系统（前后端分离）。包含学生端（移动端 H5）和管理端（PC 后台）。

## 你的角色与边界

你是 **Cursor**，负责**编码实现**。

- ✅ 只操作 `src/` 目录
- ❌ 禁止修改 `docs/` 目录下的任何文件
- 📖 所有接口、数据结构、技术决策**必须以 `docs/` 目录下的文档为唯一事实来源**，禁止凭记忆或猜测实现
- 开工前先 `git pull`，读 `TASKS.md`；完成后 `git commit` 并更新 TASKS.md

## MVP 优先原则

当前阶段先实现最小可用版本，跑通核心链路。
- 只做 MVP 必做功能（见 docs/01-产品需求.md 第三节），不为未来需求提前写代码（YAGNI）
- 数据模型和架构已预留扩展点，但当前不实现
- 后续迭代在现有结构上平滑扩展
- 不确定某个功能是否属于 MVP 时，先查 docs/01，仍有疑问则在 TASKS.md 标记 ⛔ 阻塞并说明，不要自行假设

## 技术栈（版本锁定）

| 层 | 技术 | 版本 |
|----|------|------|
| 后端语言 | Python | 3.13 |
| 后端框架 | Django | 5.1 |
| API | djangorestframework | 3.15 |
| 认证 | djangorestframework-simplejwt | — |
| 跨域 | django-cors-headers | — |
| API 文档 | drf-spectacular | — |
| 数据库 | SQLite(开发) / MySQL | 8.0(生产) |
| 前端运行时 | Node | 24 |
| 前端框架 | Vue | 3.4 |
| 构建工具 | Vite | 5 |
| 路由 | Vue Router | 4 |
| 状态管理 | Pinia | — |
| HTTP | Axios | — |
| 图表 | ECharts | 5 |
| 学生端 UI | Vant | 4 |
| 管理端 UI | Element Plus | — |

## 项目结构

```
项目根/
├── docs/              ← TRAE 维护，你只读不写
│   ├── 01-产品需求.md
│   ├── 02-架构设计.md
│   ├── 03-数据模型.md
│   ├── 04-API契约.md      ← 接口实现以此为准
│   ├── 05-页面原型.md
│   ├── 06-开发路线.md
│   └── 07-编码规范.md
├── src/               ← 你的工作区
│   ├── backend/       ← Django 项目
│   └── frontend/      ← Vue 项目（学生端 + 管理端）
├── .cursor/rules/     ← 6 个编码规则文件（已自动加载）
├── TASKS.md           ← 任务看板，开工前必读
└── AGENTS.md          ← 本文件
```

## 后端规范

- **分层**：Model → Serializer → Service → ViewSet → URL
  - ViewSet 只做参数校验 + 调 Service + 返回响应，不写业务逻辑
  - Service 层放所有业务计算（评分、状态变更等）
- **写操作**必须加 `@transaction.atomic`
- **关联查询**用 `select_related` / `prefetch_related`，禁止 N+1
- **密码**用 `set_password()`，禁止明文
- **统一响应**：`{code: 200, msg: "中文", data: {}}`
  - code: 200成功 / 400参数错误 / 401未登录 / 403权限不足 / 404不存在 / 500异常
- **分页**：列表接口强制分页，返回 `{results, total, page, page_size, total_pages}`
- **日志**：用 `logging`，禁止 `print`
- **禁止**：函数视图(FBV)、裸 SQL、`.objects.all()` 全表、硬编码密钥

## 前端规范

- **只用 Composition API + `<script setup>`**，禁止 Options API / `this`
- `ref()` 用于基本类型，`reactive()` 用于对象/数组
- **所有请求**走 `src/api/request.js` 封装的 axios 实例，禁止裸写 `axios.get`
- 路由守卫处理 401，自动跳转登录页
- **学生端只用 Vant，管理端只用 Element Plus**，禁止混用
- 每个异步操作有 loading 状态，请求失败必须 toast 提示，禁止静默失败
- 单文件组件 ≤ 300 行，超过拆分子组件

## 不过度防御性编程

规则里的"必须校验/必须捕获"是底线，不是让你写满屏防御代码。保持简洁：

- **信任上游**：Serializer 已校验的字段，Service 里不重复校验；ViewSet 已鉴权的，Service 不重复检查权限
- **异常不吞**：只在真正可能失败的地方捕获（DB 写操作、外部 API 调用），其余异常向上抛，由全局异常处理器统一返回
- **不写无意义判空**：`get_object_or_404()` 返回的对象不重复 `if obj is None`；`filter().first()` 明确可能为空时才判断
- **不提前实现不存在的场景**：只写当前需求需要的逻辑，不为"以后可能用到"加分支（YAGNI）
- **注释克制**：代码能自解释的不加注释，只在业务规则（如 PSS-10 反向计分）、非显而易见的算法处加中文注释
- **不堆 if-else**：能用 early return 就不嵌套，能用 dict 映射就不写 switch

## Git 工作流

### 分支策略
- 从 `main`/`develop` 创建功能分支，禁止直接在主分支开发
- 分支命名：`feature/xxx`、`fix/xxx`、`refactor/xxx`

### 提交格式
```
<type>(<scope>): <subject>
```
- type：`feat` 新功能 / `fix` 修复 / `refactor` 重构 / `style` 样式 / `chore` 工具
- scope：`backend` / `frontend-student` / `frontend-admin` / `config`
- subject ≤ 50 字，祈使句，不加句号

### 流程
1. `git pull` 拉取最新（rebase 模式优先）
2. 读 `TASKS.md`，将目标任务标记为 🔄 进行中
3. 读对应 `docs/` 文档
4. 小步实现（每次一个原子单元 ≤50 行），自测通过
5. `git diff` 确认范围，分段 commit（单个 ≤500 行）
6. 更新 `TASKS.md` 状态为 ✅
7. `git push`

### 冲突与回滚
- pull 冲突时优先 `git pull --rebase`，解决冲突后 `git rebase --continue`
- 同一错误修 3 次未解决 → `git checkout .` 回滚，换方案重来
- **禁止** `git push --force` 到主分支

## Skill 与 MCP 使用

### 可用 Skill
- **impeccable**：用于前端 UI 审查与打磨。完成页面后调用，检查配色/层级/动效/文案是否符合 02-ui-design 规范

### 可用 MCP
- **GitHub MCP**：仓库管理、Issue/PR 创建、代码搜索。提交 PR 时使用
- **Context7 MCP**：查 Django/DRF/Vue/Vant/Element Plus 官方文档。不确定 API 用法时先查，不要猜

### 使用原则
- 写代码前不确定的 API → 用 Context7 查官方文档，不要凭记忆写
- 前端页面完成 → 用 impeccable 做 UI 审查
- 提交代码 → 用 GitHub MCP 创建 PR（如项目要求 PR 流程）

## 与 TRAE 协作

- TRAE 负责 `docs/`，你负责 `src/`，双方不修改对方目录
- 接口/需求/架构变更时，TRAE 会先更新 docs，你再按新文档改代码
- 如发现 docs 有问题或缺失，在 TASKS.md 里标记 ⛔ 阻塞并说明，不要自行假设

## 编码前自检

```
□ 已读 docs/ 对应文档？
□ 本次实现 ≤ 50 行（一个原子单元）？
□ 后端：有 @transaction.atomic（写操作）？异常向上抛而非吞？
□ 前端：走封装的 request？有 loading/error 处理？
□ 没有过度防御（信任上游校验、不写冗余判空）？
□ 不确定的 API 已用 Context7 查过文档？
□ 提交前 git diff 确认范围？
□ TASKS.md 状态已更新？
```
