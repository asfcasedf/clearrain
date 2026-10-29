# 04 — API 契约

> 项目：晴雨（ClearRain）
> 版本：v1.0
> 前缀：`/api/v1`
> 说明：所有接口返回 `{code, msg, data}`。分页返回 `data: {results, total, page, page_size, total_pages}`。

---

## 一、通用约定

### 1.1 响应格式

```json
{ "code": 200, "msg": "操作成功", "data": {} }
```

### 1.2 错误码

| code | HTTP | 含义 |
|------|------|------|
| 200 | 200 | 成功 |
| 400 | 400 | 参数错误 |
| 401 | 401 | 未登录 / Token 失效 |
| 403 | 403 | 权限不足 |
| 404 | 404 | 资源不存在 |
| 500 | 500 | 服务器异常 |

### 1.3 认证头

```
Authorization: Bearer <access_token>
```

### 1.4 分页参数

```
GET /xxx/?page=1&page_size=10
```

---

## 二、认证模块 `/auth`

### 2.1 注册

**POST** `/auth/register/` — 权限：公开

**请求体**：
```json
{
  "username": "2023001",
  "password": "abc12345",
  "nickname": "小明",
  "gender": "male",
  "grade": "2023级",
  "major": "计算机科学"
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| username | string | 是 | 学号，唯一，4-20 位 |
| password | string | 是 | 密码，6-20 位 |
| nickname | string | 是 | 昵称，1-50 字 |
| gender | string | 是 | male / female / unknown |
| grade | string | 否 | 年级 |
| major | string | 否 | 专业 |

**成功响应**：
```json
{
  "code": 200,
  "msg": "注册成功",
  "data": {
    "id": 1,
    "username": "2023001",
    "nickname": "小明"
  }
}
```

**错误**：400 学号已存在 / 参数校验失败

---

### 2.2 登录

**POST** `/auth/login/` — 权限：公开

**请求体**：
```json
{ "username": "2023001", "password": "abc12345" }
```

**成功响应**：
```json
{
  "code": 200,
  "msg": "登录成功",
  "data": {
    "access": "<jwt_access_token>",
    "refresh": "<jwt_refresh_token>",
    "user": {
      "id": 1,
      "username": "2023001",
      "nickname": "小明",
      "is_staff": false
    }
  }
}
```

**错误**：400 学号或密码错误 / 403 账号已被禁用

---

### 2.3 刷新 Token

**POST** `/auth/refresh/` — 权限：公开

**请求体**：
```json
{ "refresh": "<jwt_refresh_token>" }
```

**成功响应**：
```json
{
  "code": 200,
  "msg": "刷新成功",
  "data": { "access": "<new_access_token>" }
}
```

**错误**：401 refresh 无效或过期

---

### 2.4 获取个人信息

**GET** `/auth/me/` — 权限：已登录

**成功响应**：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "id": 1,
    "username": "2023001",
    "nickname": "小明",
    "gender": "male",
    "grade": "2023级",
    "major": "计算机科学",
    "is_staff": false,
    "date_joined": "2026-01-01 10:00:00"
  }
}
```

---

### 2.5 修改个人信息

**PUT** `/auth/me/` — 权限：已登录

**请求体**：
```json
{
  "nickname": "新昵称",
  "gender": "female",
  "grade": "2023级",
  "major": "软件工程"
}
```

**成功响应**：同 2.4

---

### 2.6 修改密码

**PUT** `/auth/password/` — 权限：已登录

**请求体**：
```json
{ "old_password": "abc12345", "new_password": "newpass678" }
```

**成功响应**：
```json
{ "code": 200, "msg": "密码已更新", "data": null }
```

**错误**：400 旧密码错误

---

## 三、量表模块 `/scales`

### 3.1 获取量表列表

**GET** `/scales/` — 权限：已登录

**成功响应**：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "results": [
      {
        "id": 1,
        "name": "PSS-10 压力感知量表",
        "code": "PSS-10",
        "description": "感知压力量表...",
        "total_questions": 10,
        "max_score": 40
      }
    ],
    "total": 1,
    "page": 1,
    "page_size": 10,
    "total_pages": 1
  }
}
```

---

### 3.2 获取量表详情（含题目与选项）

**GET** `/scales/{scale_id}/` — 权限：已登录

**成功响应**：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "id": 1,
    "name": "PSS-10 压力感知量表",
    "code": "PSS-10",
    "description": "...",
    "total_questions": 10,
    "max_score": 40,
    "questions": [
      {
        "id": 1,
        "order": 1,
        "content": "你多久因为意外发生的事情而感到心烦？",
        "is_reverse": false,
        "answers": [
          { "id": 1, "score": 0, "label": "从不" },
          { "id": 2, "score": 1, "label": "几乎从不" },
          { "id": 3, "score": 2, "label": "有时" },
          { "id": 4, "score": 3, "label": "经常" },
          { "id": 5, "score": 4, "label": "非常频繁" }
        ]
      }
    ]
  }
}
```

> 说明：`is_reverse` 字段仅管理端返回时使用，学生端测评接口不返回此字段（防止作弊）。学生端通过 `GET /scales/{id}/questions/` 获取不含 is_reverse 的题目。

---

### 3.3 学生端获取题目（不含反向标记）

**GET** `/scales/{scale_id}/questions/` — 权限：已登录

**成功响应**：题目数组，每题含 `id, order, content, answers[]`，**不含 is_reverse**。

---

## 四、测评模块 `/assessment`

### 4.1 提交测评

**POST** `/assessment/submit/` — 权限：已登录

**请求体**：
```json
{
  "scale_id": 1,
  "answers": [
    { "question_id": 1, "answer_id": 3 },
    { "question_id": 2, "answer_id": 2 }
  ],
  "duration_seconds": 120
}
```

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| scale_id | int | 是 | 量表 ID |
| answers | array | 是 | 作答列表，必须包含该量表所有题目 |
| duration_seconds | int | 否 | 作答耗时 |

**校验规则**：
- answers 数量必须等于量表题目总数
- 每个 question_id 必须属于该量表
- 每个 answer_id 必须属于对应题目

**成功响应**：
```json
{
  "code": 200,
  "msg": "已经记录下来啦 ✨",
  "data": {
    "record_id": 5,
    "total_score": 22,
    "standard_score": 55,
    "level": "medium",
    "level_text": "中压",
    "suggestion": "这在大学生中很常见，你不是一个人。试试每天给自己留 10 分钟什么都不做。"
  }
}
```

---

### 4.2 获取测评结果

**GET** `/assessment/records/{record_id}/` — 权限：已登录（仅本人，管理员可查所有）

**成功响应**：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "id": 5,
    "scale_name": "PSS-10 压力感知量表",
    "total_score": 22,
    "standard_score": 55,
    "level": "medium",
    "level_text": "中压",
    "suggestion": "这在大学生中很常见...",
    "duration_seconds": 120,
    "created_at": "2026-01-15 14:30:00"
  }
}
```

---

### 4.3 我的测评记录列表

**GET** `/assessment/records/` — 权限：已登录（仅本人）

**查询参数**：`page`, `page_size`

**成功响应**：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "results": [
      {
        "id": 5,
        "standard_score": 55,
        "level": "medium",
        "level_text": "中压",
        "created_at": "2026-01-15 14:30:00"
      }
    ],
    "total": 8,
    "page": 1,
    "page_size": 10,
    "total_pages": 1
  }
}
```

---

### 4.4 我的趋势数据

**GET** `/assessment/trend/` — 权限：已登录（仅本人）

**查询参数**：`limit`（默认 10，最多 50）

**成功响应**：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "points": [
      { "date": "2026-01-10", "standard_score": 60, "level": "medium" },
      { "date": "2026-01-15", "standard_score": 55, "level": "medium" }
    ]
  }
}
```

> 说明：按时间正序返回，供 ECharts 折线图渲染。

---

## 五、管理端模块 `/admin`

> 所有 `/admin/*` 接口要求 `is_staff=True`。

### 5.1 概览统计

**GET** `/admin/overview/` — 权限：管理员

**成功响应**：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "total_users": 150,
    "active_users": 148,
    "total_records": 320,
    "high_stress_count": 25,
    "medium_stress_count": 120,
    "low_stress_count": 175
  }
}
```

---

### 5.2 用户列表

**GET** `/admin/users/` — 权限：管理员

**查询参数**：`page`, `page_size`, `search`（学号或昵称模糊匹配）

**成功响应**：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "results": [
      {
        "id": 1,
        "username": "2023001",
        "nickname": "小明",
        "gender": "male",
        "grade": "2023级",
        "major": "计算机",
        "is_active": true,
        "is_staff": false,
        "date_joined": "2026-01-01 10:00:00"
      }
    ],
    "total": 150,
    "page": 1,
    "page_size": 10,
    "total_pages": 15
  }
}
```

---

### 5.3 启用/禁用用户

**PATCH** `/admin/users/{user_id}/` — 权限：管理员

**请求体**：
```json
{ "is_active": false }
```

**成功响应**：同 5.2 单条用户对象

> 说明：禁用后该用户登录返回 403。

---

### 5.4 量表列表（管理端）

**GET** `/admin/scales/` — 权限：管理员

返回同 3.1，但不分页（量表数量少），返回 `data: [...]` 数组。

---

### 5.5 题目管理

**GET** `/admin/scales/{scale_id}/questions/` — 权限：管理员
**POST** `/admin/scales/{scale_id}/questions/` — 权限：管理员
**PUT** `/admin/questions/{question_id}/` — 权限：管理员
**DELETE** `/admin/questions/{question_id}/` — 权限：管理员

**题目对象**：
```json
{
  "id": 1,
  "order": 1,
  "content": "题目内容",
  "is_reverse": false,
  "answers": [
    { "id": 1, "score": 0, "label": "从不", "order": 1 }
  ]
}
```

**POST 请求体**：
```json
{
  "order": 11,
  "content": "新题目",
  "is_reverse": false,
  "answers": [
    { "score": 0, "label": "从不", "order": 1 },
    { "score": 1, "label": "几乎从不", "order": 2 },
    { "score": 2, "label": "有时", "order": 3 },
    { "score": 3, "label": "经常", "order": 4 },
    { "score": 4, "label": "非常频繁", "order": 5 }
  ]
}
```

---

### 5.6 记录检索

**GET** `/admin/records/` — 权限：管理员

**查询参数**：

| 参数 | 类型 | 说明 |
|------|------|------|
| page | int | 页码 |
| page_size | int | 每页条数 |
| user_id | int | 按用户筛选 |
| level | string | low / medium / high |
| start_date | string | 起始日期 YYYY-MM-DD |
| end_date | string | 结束日期 YYYY-MM-DD |

**成功响应**：
```json
{
  "code": 200,
  "msg": "success",
  "data": {
    "results": [
      {
        "id": 5,
        "user_id": 1,
        "username": "2023001",
        "nickname": "小明",
        "scale_name": "PSS-10",
        "total_score": 22,
        "standard_score": 55,
        "level": "medium",
        "level_text": "中压",
        "created_at": "2026-01-15 14:30:00"
      }
    ],
    "total": 320,
    "page": 1,
    "page_size": 10,
    "total_pages": 32
  }
}
```

---

## 六、接口汇总

| 模块 | 方法 | 路径 | 权限 |
|------|------|------|------|
| 认证 | POST | `/auth/register/` | 公开 |
| 认证 | POST | `/auth/login/` | 公开 |
| 认证 | POST | `/auth/refresh/` | 公开 |
| 认证 | GET | `/auth/me/` | 已登录 |
| 认证 | PUT | `/auth/me/` | 已登录 |
| 认证 | PUT | `/auth/password/` | 已登录 |
| 量表 | GET | `/scales/` | 已登录 |
| 量表 | GET | `/scales/{id}/` | 已登录 |
| 量表 | GET | `/scales/{id}/questions/` | 已登录 |
| 测评 | POST | `/assessment/submit/` | 已登录 |
| 测评 | GET | `/assessment/records/` | 已登录 |
| 测评 | GET | `/assessment/records/{id}/` | 已登录 |
| 测评 | GET | `/assessment/trend/` | 已登录 |
| 管理 | GET | `/admin/overview/` | 管理员 |
| 管理 | GET | `/admin/users/` | 管理员 |
| 管理 | PATCH | `/admin/users/{id}/` | 管理员 |
| 管理 | GET | `/admin/scales/` | 管理员 |
| 管理 | GET | `/admin/scales/{id}/questions/` | 管理员 |
| 管理 | POST | `/admin/scales/{id}/questions/` | 管理员 |
| 管理 | PUT | `/admin/questions/{id}/` | 管理员 |
| 管理 | DELETE | `/admin/questions/{id}/` | 管理员 |
| 管理 | GET | `/admin/records/` | 管理员 |

---

## 七、等级文案与建议（后端返回）

| level | level_text | suggestion |
|-------|-----------|------------|
| low | 低压 | 最近状态不错，像春天的微风。继续保持规律作息和适度运动吧。 |
| medium | 中压 | 这在大学生中很常见，你不是一个人。试试每天给自己留 10 分钟什么都不做，或者找朋友聊聊天。 |
| high | 高压 | 你最近承受了不少，是时候给自己多一点关怀了。如果这种状态持续，建议联系学校心理中心寻求支持。 |

> 所有结果必须附免责声明（前端展示）：「本测评不构成临床诊断，仅供自我了解参考。」
