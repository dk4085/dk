# Auth 服务 - Python JWT 认证服务

这是一个基于 FastAPI 的认证和授权服务，使用 JWT 令牌进行用户身份验证。

## 功能特性

- 用户注册（邮箱和密码）
- 用户登录（返回 JWT access 和 refresh 令牌）
- 使用 refresh 令牌更新 access 令牌
- 更新用户信息（邮箱和密码）
- 查看登录历史记录
- 用户登出（令牌加入黑名单）

## 技术栈

- **Python** 3.9
- **FastAPI** - Web 框架
- **PostgreSQL** - 数据库
- **Redis** - 黑名单令牌存储
- **Docker** & **Docker Compose** - 容器化部署
- **JWT** (JSON Web Tokens) - 身份验证

## API 端点

### 1. 用户注册
- **方法**: POST
- **端点**: `/register`
- **描述**: 创建新用户
- **请求体**:
  ```json
  {
    "email": "example@example.com",
    "password": "securepassword"
  }