fetch("/api/stats")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("deviceList");

    data.devices.forEach(ip => {
      const li = document.createElement("li");
      li.textContent = ip;
      li.style.cursor = "pointer";

      li.onclick = () => loadDevice(ip);
      list.appendChild(li);
    });
  });

function loadDevice(ip) {
  fetch(`/api/device/${ip}`)
    .then(res => res.json())
    .then(data => {
      const table = document.getElementById("deviceTable");
      table.innerHTML = "";

      Object.entries(data).forEach(([domain, count]) => {
        const row = document.createElement("tr");
        row.innerHTML = `<td>${domain}</td><td>${count}</td>`;
        table.appendChild(row);
      });
    });
}
