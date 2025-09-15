# MyFastAPI

这是一个基于 FastAPI + SQLAlchemy + MySQL 的企业级后端管理系统项目模板，采用 src 目录布局，适合用于中后台管理系统、B2B/B2C平台、SaaS 项目等。

## 技术栈
- Python 3.11+
- FastAPI
- SQLAlchemy 2.x
- MySQL 8+
- Pydantic 2.x
- Uvicorn

## 目录结构

```
src/
  my_project/
    main.py       # FastAPI 入口
    config.py     # 配置管理
    models/       # ORM 数据模型
    services/     # 业务逻辑
    utils/        # 工具函数
    api/          # API 路由
```

## 快速开始

1. 安装依赖

```bash
pip install -r requirements.txt
```

2. 配置数据库

修改 `src/my_project/config.py`，填入你的 MySQL 配置信息。

3. 启动服务

```bash
uvicorn src.my_project.main:app --reload
```

4. 访问接口文档

http://127.0.0.1:8000/docs

---

如需帮助或业务定制，请联系维护者.