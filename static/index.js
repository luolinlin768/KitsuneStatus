document.getElementById("myBtn").addEventListener("click", () => {
    alert("按钮已点击！");
    fetch("/test")  // 示例API调用
        .then(res => res.json())
        .then(data => console.log(data));
});