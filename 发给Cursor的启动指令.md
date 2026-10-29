# 发给 Cursor 的项目启动指令

> 把下面整段内容复制粘贴到 Cursor 对话框发送即可。

---

## 项目：晴雨（ClearRain）— 大学生心理健康测评系统

你是 Cursor，负责这个项目的**编码实现**。

### 你的边界（铁律）
- **只操作 `src/` 目录**，禁止修改 `docs/` 下任何文件
- 所有接口、数据结构、技术决策**必须以 `docs/` 目录下的文档为唯一事实来源**，禁止凭记忆写代码
- 开工前先 `git pull`，看完 `TASKS.md` 再动手；完成后 `git commit` 并更新 TASKS.md

### 技术栈（版本锁定，禁止变更）
- 后端：Python 3.13 + Django 5.1 + DRF 3.15 + SimpleJWT + SQLite(开发)/MySQL 8.0(生产)
- 前端：Node 24 + Vue 3.4 + Vite 5 + Vue Router 4 + Pinia + Axios + ECharts 5
- 学生端 UI：Vant 4（移动端优先 375px）
- 管理端 UI：Element Plus（PC 优先 1366px）

### 项目结构
```
项目根目录/
├── docs/          ← TRAE 写的文档，你只读不写
│   ├── 01-产品需求.md
│   ├── 02-架构设计.md
│   ├── 03-数据模型.md
│   ├── 04-API契约.md      ← 接口以这个为准
│   ├── 05-页面原型.md
│   ├── 06-开发路线.md
│   └── 07-编码规范.md
├── src/           ← 你的工作区
│   ├── backend/   ← Django 项目
│   └── frontend/  ← Vue 项目（学生端 + 管理端）
└── TASKS.md       ← 任务看板，开工前必读
```

### 后端核心规范
- 分层：Model → Serializer → Service → ViewSet → URL，ViewSet 只调 Service 不写业务
- 所有写操作加 `@transaction.atomic`
- 关联查询用 `select_related`/`prefetch_related`，禁止 N+1
- 密码用 `set_password()`，禁止明文
- 统一返回 `{code, msg, data}`，code: 200/400/401/403/404/500
- 列表接口强制分页，返回 `{results, total, page, page_size, total_pages}`
- 用 logging，禁止 print

### 前端核心规范
- 只用 Composition API + `<script setup>`，禁止 Options API / this
- 基本类型用 `ref()`，对象用 `reactive()`
- 所有请求走 `src/api/request.js` 封装的 axios 实例，禁止裸写 axios
- 路由守卫处理 401 自动跳登录
- 学生端只用 Vant，管理端只用 Element Plus，禁止混用
- 每个异步操作有 loading，请求失败必须 toast 提示

### 不过度防御（重要）
- 信任上游校验：Serializer 校验过的字段 Service 不重复校验
- 异常不吞：只在 DB 写操作/外部调用处捕获，其余向上抛由全局处理器处理
- 不写冗余判空：`get_object_or_404()` 后不重复 `if obj is None`
- 不提前实现不存在的场景（YAGNI）
- 注释克制：代码自解释，只在业务规则处加中文注释

### Skill 与 MCP
- 不确定 API 用法 → 用 Context7 MCP 查官方文档，不要凭记忆写
- 前端页面完成 → 用 impeccable skill 做 UI 审查
- 代码提交 → 用 GitHub MCP 管理

### Git 提交规范
```
<type>(<scope>): <subject>
```
- type：feat / fix / refactor / style / docs / chore
- scope：backend / frontend-student / frontend-admin / config
- 从 main/develop 建分支，禁止直接在主分支开发
- 开工前 `git pull --rebase`，完成后分段 commit（单个 ≤ 500 行），更新 TASKS.md
- 禁止 `git push --force` 到主分支

### 完整规则
以上是要点，完整规范见项目根目录的 `AGENTS.md` 和 `.cursor/rules/` 下的 6 个规则文件。

现在请先执行 `git pull`，然后读取 `TASKS.md`，告诉我当前有哪些待办任务。
