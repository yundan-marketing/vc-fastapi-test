# FastAPI Vercel 部署项目

这是一个简单的 FastAPI 项目，可以部署到 Vercel。

## 功能

- `/` - Hello World 接口
- `/hello` - Hello 接口

## 本地开发

1. 安装依赖：
```bash
pip install -r requirements.txt
```

2. 运行应用：
```bash
uvicorn main:app --reload
```

3. 访问：
- http://localhost:8000
- http://localhost:8000/docs (API 文档)

## 部署到 Vercel

1. 安装 Vercel CLI：
```bash
npm i -g vercel
```

2. 部署：
```bash
vercel
```

或者通过 GitHub 连接 Vercel 进行自动部署。

## GitHub 提交

```bash
git init
git add .
git commit -m "Initial commit: FastAPI hello project"
git remote add origin <your-github-repo-url>
git push -u origin main
```

