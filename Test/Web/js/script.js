document.addEventListener("DOMContentLoaded", function() {
    const hostData = {
        name: "主机1",
        cpu: "i5 12500h",
        kernel: "6.14.3-arch1-1",
        bootMode: "UEFI",
        logicalCores: 12,
        cpuUsage: 45,
        memoryUsage: 65,
        temperature: 55,
        power: 85,
        totalMemory: 6,
        usedMemory: 4
    };

    const vmData = [
        {
            name: "VM1",
            cpuUsage: 20,
            memoryUsage: 2,
            status: "在线",
            uptime: "5小时23分钟",
            logicalCores: 4,
            memoryCapacity: 8
        },
        {
            name: "VM2",
            cpuUsage: 35,
            memoryUsage: 3,
            status: "离线",
            uptime: "2小时10分钟",
            logicalCores: 4,
            memoryCapacity: 8
        }
    ];

    const containerData = [
        {
            name: "Container1",
            image: "nginx:latest",
            cpuUsage: 15,
            memoryUsage: 1,
            status: "在线"
        },
        {
            name: "Container2",
            image: "mysql:latest",
            cpuUsage: 30,
            memoryUsage: 2,
            status: "离线"
        }
    ];

    // Display host info
    const hostCard = document.getElementById('host-card');
    hostCard.innerHTML = `
        <div class="card-header">主机信息</div>
        <div class="card-body">
            <p><strong>CPU:</strong> ${hostData.cpu} | <strong>内核:</strong> ${hostData.kernel}</p>
            <p><strong>引导模式:</strong> ${hostData.bootMode} | <strong>逻辑核心:</strong> ${hostData.logicalCores}</p>
            <p><strong>CPU使用率:</strong> ${hostData.cpuUsage}% | <strong>内存使用率:</strong> ${hostData.memoryUsage}% (${hostData.usedMemory}GB/${hostData.totalMemory}GB)</p>
            <p><strong>温度:</strong> ${hostData.temperature}°C | <strong>功耗:</strong> ${hostData.power}W</p>
        </div>
    `;

    // Display VM info
    const vmCardsContainer = document.getElementById('vm-cards');
    vmData.forEach(vm => {
        const vmCard = document.createElement('div');
        vmCard.classList.add('card');
        vmCard.innerHTML = `
            <div class="card-header">${vm.name}</div>
            <div class="card-body">
                <p><strong>CPU占用:</strong> ${vm.cpuUsage}% | <strong>内存占用:</strong> ${vm.memoryUsage}GB</p>
                <p><strong>状态:</strong> ${vm.status} | <strong>运行时间:</strong> ${vm.uptime}</p>
                <p><strong>核心数:</strong> ${vm.logicalCores} | <strong>内存容量:</strong> ${vm.memoryCapacity}GB</p>
            </div>
        `;
        vmCardsContainer.appendChild(vmCard);
    });

    // Display container info
    const containerCardsContainer = document.getElementById('container-cards');
    containerData.forEach(container => {
        const containerCard = document.createElement('div');
        containerCard.classList.add('card');
        containerCard.innerHTML = `
            <div class="card-header">${container.name}</div>
            <div class="card-body">
                <p><strong>镜像:</strong> ${container.image} | <strong>CPU:</strong> ${container.cpuUsage}% | <strong>内存:</strong> ${container.memoryUsage}GB</p>
                <p><strong>状态:</strong> ${container.status}</p>
            </div>
        `;
        containerCardsContainer.appendChild(containerCard);
    });
});



const toggleBtn = document.getElementById('theme-toggle');

// 初始化时恢复上次主题
if (localStorage.getItem('theme') === 'dark') {
  document.body.classList.add('dark');
  toggleBtn.textContent = '🌙 暗色';
} else {
  toggleBtn.textContent = '🌞 亮色';
}

toggleBtn.addEventListener('click', function() {
  document.body.classList.toggle('dark');
  const isDark = document.body.classList.contains('dark');
  toggleBtn.textContent = isDark ? '🌙 暗色' : '🌞 亮色';
  localStorage.setItem('theme', isDark ? 'dark' : 'light');
});
