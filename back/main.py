import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.data import get_system_info, get_host_status, get_container_status

app = FastAPI(title="只读API服务", docs_url=None)  # 关闭文档页

# docker_base_url如需要可以手动指定docker套接字
docker_base_url = 'unix:///var/run/docker.sock'
# docker_base_url = 'tcp://192.168.3.249:2375'
# docker_base_url = None

# 允许跨域（按需调整）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],  # 仅允许 GET
)

@app.get("/system_info", summary="获取system系统信息")
def read_system_info():
    return get_system_info(docker_base_url)

@app.get("/status/host", summary="获取host状态")
def read_host_status():
    return get_host_status()

@app.get("/status/container", summary="读取container状态")
def read_container_status():
    return get_container_status(docker_base_url)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)