import psutil, platform, subprocess, docker

def get_docker_info(docker_base_url):
    try:
        client = docker.DockerClient(base_url=docker_base_url, timeout=5)
        if not client.ping():
            return None  # 返回空值而不是抛出异常
        return client
    except Exception as e:  # 捕获所有异常
        return None  # 返回空值保证程序继续执行

def get_container_status(docker_base_url) -> dict:
    client = get_docker_info(docker_base_url)
    if client:
        containers = client.containers.list(all=True)
        result = []
        i = 0
        for container in containers:
            status = {
                "index" : i,
                "id": container.short_id,
                "name": container.name,
                "status": container.status,
                "image": container.image.tags[0] if container.image.tags else "",
                "ports": container.attrs["NetworkSettings"]["Ports"]
            }
            i += 1
            result.append(status)
        return result
    else:
        return {
            "docker" : "我们无法连接到你的docker"
        }

def get_system_info(docker_base_url) -> dict:
    client = get_docker_info(docker_base_url)
    if client:
        containers = client.containers.list(all=True)
        result = {
        "os" : platform.freedesktop_os_release().get('PRETTY_NAME', 'Unknown'),
        "kernel" : platform.release(),
        "cpu_model" : subprocess.run(
            "lscpu | grep 'Model name'", 
            shell=True, 
            capture_output=True, 
            text=True).stdout.strip().split(":", 1)[1].strip(),
        "logical_cores" : psutil.cpu_count(),
        "container_count" : len(containers)
        }
        return result
    else:
        result = {
        "os" : platform.freedesktop_os_release().get('PRETTY_NAME', 'Unknown'),
        "kernel" : platform.release(),
        "cpu_model" : subprocess.run(
            "lscpu | grep 'Model name'", 
            shell=True, 
            capture_output=True, 
            text=True).stdout.strip().split(":", 1)[1].strip(),
        "logical_cores" : psutil.cpu_count(),
        "container_count" : "None"
        }
        return result

def get_host_status() -> dict:
    result = {
        "cpu_usage" : psutil.cpu_percent(interval=1),
        "mem_total" : round(psutil.virtual_memory().total / (1024 ** 2), 1),
        "mem_used" : round(psutil.virtual_memory().used / (1024 ** 2), 1)
        }
    return result