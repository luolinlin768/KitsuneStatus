from pydantic import BaseModel
# from pydantic import BaseModel, Field, validator
# from typing import Optional

# 数据模型
# 数据有 Host VM Container
# 2025/4/27

# Info

class SysInfo(BaseModel):
    os: str = "Unknown"
    kernel: str = "Unknown"
    cpu_model: str = "Unknown"
    logical_cores: int = 0
    vm_count: int = 0
    container_count: int = 0

# 主机数据
class Host(BaseModel):
    # CPU使用率%
    cpu_usage: float = 0.0
    # 处理器温度(℃)
    cpu_temp: float = 0.0
    # 总内存(GB)
    mem_total: float = 0.0
    # 已用内存(GB)
    mem_used: float = 0.0
    # 功耗(W)
    power: float = 0.0

# 虚拟机数据
class VM(BaseModel):
    # 虚拟机名称
    name: str = "Unknown"
    # CPU使用率%
    cpu_usage: float = 0.0
    # 内存使用量(GB)
    mem_used: float = 0.0
    # online/offline
    status: str = "offline"
    # 虚拟CPU数量
    vcpus: int = 0
    # 总内存(GB)
    mem_total: float = 0.0

# 容器数据
class Container(BaseModel):
    # 容器名称
    name: str = "Unknown"
    # 镜像名称
    image: str = "Unknown"
    # CPU使用率%
    cpu_usage: float = 0.0
    # 内存使用量(MB)
    mem_used: float = 0.0
    # running/exited
    status: str = "exited"

if __name__ == "__main__":
    host = Host()
    print(host.model_dump_json())


#####################

# class SysInfo(BaseModel):
#     """
#     系统基础信息 (静态信息)
#     """
#     os: str = Field("Unknown", description="操作系统类型")
#     kernel: str = Field("Unknown", description="内核版本")
#     cpu_model: str = Field("Unknown", description="CPU型号")
#     logical_cores: Optional[int] = Field(None, description="逻辑核心数", ge=0)
#     vm_count: Optional[int] = Field(None, description="虚拟机总数", ge=0)
#     container_count: Optional[int] = Field(None, description="容器总数", ge=0)

# class Host(BaseModel):
#     """
#     主机实时状态数据
#     """
#     cpu_usage: Optional[float] = Field(
#         None, 
#         description="CPU使用率百分比", 
#         ge=0, 
#         le=100
#     )
#     cpu_temp: Optional[float] = Field(
#         None,
#         description="处理器温度(℃)",
#         ge=0
#     )
#     mem_total: Optional[float] = Field(
#         None,
#         description="总内存(GB)",
#         gt=0
#     )
#     mem_used: Optional[float] = Field(
#         None,
#         description="已用内存(GB)",
#         ge=0
#     )
#     power: Optional[float] = Field(
#         None,
#         description="功耗(W)",
#         ge=0
#     )

# class VM(BaseModel):
#     """
#     虚拟机数据
#     """
#     name: str = Field("Unknown", description="虚拟机名称")
#     cpu_usage: Optional[float] = Field(
#         None,
#         description="CPU使用率百分比",
#         ge=0,
#         le=100
#     )
#     mem_used: Optional[float] = Field(
#         None,
#         description="内存使用量(GB)",
#         ge=0
#     )
#     status: Optional[str] = Field(
#         None,
#         description="运行状态",
#         pattern="^(online|offline)$"  # 修改这里：regex → pattern
#     )
#     vcpus: Optional[int] = Field(
#         None,
#         description="虚拟CPU数量",
#         gt=0
#     )
#     mem_total: Optional[float] = Field(
#         None,
#         description="总内存(GB)",
#         gt=0
#     )

# class Container(BaseModel):
#     """
#     容器数据
#     """
#     name: str = Field("Unknown", description="容器名称")
#     image: str = Field("Unknown", description="镜像名称")
#     cpu_usage: float = Field(
#         None,
#         description="CPU使用率百分比",
#         ge=0,
#         le=100
#     )
#     mem_used: float = Field(
#         None,
#         description="内存使用量(MB)",
#         ge=0
#     )
#     status: str = Field(
#         "exited",
#         description="运行状态",
#         pattern="^(running|exited)$"  # 修改这里：regex → pattern
#     )

#####################
