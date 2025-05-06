# # 示例：增加出版年份属性
# class Book:
#     def __init__(self, title: str, author: str, price: float, year: int = 2023):  # 默认值
#         self.title = title
#         self.author = author
#         self.price = price
#         self.year = year  # 新增属性

#     def display_info(self):
#         return f"《{self.title}》（{self.year}年）by {self.author}, 价格: ¥{self.price:.2f}"

# book = Book("深度学习", "王五", 129.99, 2022)

# print(book.display_info())

# import uvicorn
# from fastapi import FastAPI, HTTPException  # 添加了 HTTPException 导入
# from pydantic import BaseModel
# from typing import List
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# # 定义数据模型
# class Book(BaseModel):
#     id: int
#     title: str
#     author: str
#     price: float
#     year: int = 2023  # 默认值

# # 模拟数据库（内存中的只读数据）
# READ_ONLY_BOOKS = [
#     Book(id=1, title="Python入门", author="张三", price=59.99, year=2022),
#     Book(id=2, title="机器学习实战", author="李四", price=99.50),
#     Book(id=3, title="深度学习", author="王五", price=129.99)
# ]

# # --- 只读API端点 ---
# @app.get("/books/", response_model=List[Book])
# async def get_all_books():
#     """获取所有书籍（只读）"""
#     return READ_ONLY_BOOKS

# @app.get("/books/{book_id}", response_model=Book)
# async def get_book(book_id: int):
#     """根据ID获取单本书（只读）"""
#     book = next((b for b in READ_ONLY_BOOKS if b.id == book_id), None)
#     if not book:
#         raise HTTPException(status_code=404, detail="Book not found")  # 现在可以正常使用
#     return book


# @app.get("/items/", response_class=HTMLResponse)
# async def read_items():
#     return """
#     <html>
#     <head>
#         <meta charset="utf-8">
#         <meta name="robots" content="noindex,nofollow" />
#         <title>恭喜，站点创建成功！</title>
#         <style>
#             .container {
#                 width: 60%;
#                 margin: 10% auto 0;
#                 background-color: #f0f0f0;
#                 padding: 2% 5%;
#                 border-radius: 10px
#             }

#             ul {
#                 padding-left: 20px;
#             }

#             ul li {
#                 line-height: 2.3
#             }

#             a {
#                 color: #20a53a
#             }
#         </style>
#     </head>
#     <body>
#     <div class="container">
#         <h1>恭喜, 站点创建成功！</h1>
#         <h3>这是默认index.html，本页面由系统自动生成</h3>
#     </div>
#     </body>
#     </html>
#     """
from back.app.schemas import User
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
import os

app = FastAPI()




# 挂载静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 返回HTML文件
@app.get("/", response_class=HTMLResponse)
async def serve_index():
    return FileResponse("index.html")

# 可选：直接返回HTML字符串
@app.get("/simple", response_class=HTMLResponse)
async def simple_html():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Direct HTML</title>
        <link href="/static/index.css" rel="stylesheet">
    </head>
    <body>
        <h1>直接返回的HTML</h1>
        <script src="/static/index.js"></script>
    </body>
    </html>
    """


@app.get("/test")
async def get_data():
    return {"message": "Hello", "value": 42}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)