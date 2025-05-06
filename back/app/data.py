from app.schemas import SysInfo, Host, VM, Container
# from schemas import SysInfo, Host, VM, Container
# import psutil


def get_system_info() -> SysInfo:
    system_info = SysInfo()

    return system_info.model_dump()

def get_host_status() -> Host:
    host_status = Host()
    return host_status.model_dump()


def get_vm_status() -> VM:
    vm_status = VM()
    return vm_status.model_dump()


def get_container_status() -> Container:
    container_status = Container()
    return container_status.model_dump()


if __name__ == "__main__":
    print(get_system_info())
    pass