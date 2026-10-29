# TASKS.md — 晴雨（ClearRain）任务看板

> 状态：⬜ 待办 | 🔄 进行中 | ✅ 完成 | ⛔ 阻塞
> 规则：开工前读本文档，改完更新状态。TRAE 只管 docs/，Cursor 只管 src/。

---

## M0 准备（用户）

| 任务 | 状态 | 负责人 | 说明 |
|------|------|-------|------|
| 安装 Python 3.13 / Node 24 / MySQL 8.0 | ⬜ | 用户 | 本地开发环境 |
| 创建 GitHub 仓库并配置 remote | ⬜ | 用户 | 当前仅本地 git |
| 选定配色方案（暖橘/钴蓝/柔绿） | ⬜ | 用户 | 影响 05 原型 + 02-ui-design.mdc |
| 配置 GitHub Token（Cursor MCP） | ⬜ | 用户 | 见 Cursor工具配置清单.md |
| 配置 Context7 API Key | ⬜ | 用户 | 见 TRAE工具安装状态.md |

---

## M1 文档（TRAE）

| 任务 | 状态 | 说明 |
|------|------|------|
| docs/01-产品需求.md | ✅ | 待用户确认 |
| docs/02-架构设计.md | ✅ | 待用户确认 |
| docs/03-数据模型.md | ✅ | 待用户确认 |
| docs/04-API契约.md | ✅ | 待用户确认 |
| docs/05-页面原型.md | ✅(占位) | 配色+原型待用户分析后由 TRAE Design 生成 |
| docs/06-开发路线.md | ✅ | 待用户确认 |
| docs/07-编码规范.md | ✅ | 汇总 cursor rules |
| Git 仓库初始化 | ✅ | 本地已 init，待用户配 remote |

---

## M2 后端（Cursor，仅操作 src/backend/）

### M2.1 骨架

| 任务 | 状态 | 依赖 |
|------|------|------|
| Django 项目结构 + 配置分环境（dev/prod） | ⬜ | M1 文档确认 |
| requirements.txt | ⬜ | 同上 |
| 统一响应 {code,msg,data} + 全局异常处理 | ⬜ | 同上 |
| CORS + JWT 配置 | ⬜ | 同上 |
| StandardPagination 分页 | ⬜ | 同上 |

### M2.2 认证（accounts app）

| 任务 | 状态 |
|------|------|
| User 模型（AbstractUser + 扩展字段） | ⬜ |
| POST /auth/register/ | ⬜ |
| POST /auth/login/ | ⬜ |
| POST /auth/refresh/ | ⬜ |
| GET/PUT /auth/me/ | ⬜ |
| PUT /auth/password/ | ⬜ |

### M2.3 量表（scales app）

| 任务 | 状态 |
|------|------|
| Scale / Question / Answer 模型 | ⬜ |
| PSS-10 数据迁移（自动导入） | ⬜ |
| GET /scales/ | ⬜ |
| GET /scales/{id}/ | ⬜ |
| GET /scales/{id}/questions/ | ⬜ |

### M2.4 测评（assessment app）

| 任务 | 状态 |
|------|------|
| AssessmentRecord / AssessmentAnswer 模型 | ⬜ |
| POST /assessment/submit/（含反向计分） | ⬜ |
| GET /assessment/records/{id}/ | ⬜ |
| GET /assessment/records/ | ⬜ |
| GET /assessment/trend/ | ⬜ |

### M2.5 管理接口

| 任务 | 状态 |
|------|------|
| GET /admin/overview/ | ⬜ |
| GET /admin/users/ | ⬜ |
| PATCH /admin/users/{id}/ | ⬜ |
| GET /admin/scales/ | ⬜ |
| 题目 CRUD（/admin/scales/{id}/questions/ 等） | ⬜ |
| GET /admin/records/ | ⬜ |

---

## M3 前端（Cursor，仅操作 src/frontend/）

### M3.1 学生端（Vue 3 + Vant 4）

| 页面 | 状态 |
|------|------|
| 项目初始化 + Vant + 路由 + Pinia + axios 封装 | ⬜ |
| 登录页 | ⬜ |
| 注册页 | ⬜ |
| 首页 | ⬜ |
| 测评页 | ⬜ |
| 结果页 | ⬜ |
| 历史页 | ⬜ |
| 我的 | ⬜ |

### M3.2 管理端（Vue 3 + Element Plus）

| 页面 | 状态 |
|------|------|
| 项目初始化 + Element Plus + 路由 + axios 封装 | ⬜ |
| 登录页 | ⬜ |
| 概览 | ⬜ |
| 用户管理 | ⬜ |
| 题库管理 | ⬜ |
| 记录检索 | ⬜ |

---

## M4 联调 & M5 验收

| 任务 | 状态 | 负责人 |
|------|------|-------|
| 学生端全流程联调 | ⬜ | 双方 |
| 管理端全流程联调 | ⬜ | 双方 |
| 反向计分正确性验证 | ⬜ | 双方 |
| 全流程走通验收 | ⬜ | 用户 |

---

## 当前阻塞项

1. **配色方案未选定** — 阻塞 05 页面原型细化 + 02-ui-design.mdc 更新
2. **GitHub remote 未配置** — 阻塞 git push / 协作
3. **M1 文档待用户确认** — 确认后 Cursor 可进入 M2

## 下一步

1. 用户确认 docs/01~07 文档（05 除外，需先做配色+原型）
2. 用户选定配色方案
3. TRAE 用 Design 模式生成 12 页原型，回填 05
4. 用户确认后，通知 Cursor 开始 M2.1 骨架
