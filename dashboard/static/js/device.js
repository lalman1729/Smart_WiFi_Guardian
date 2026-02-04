let deviceChart = null;

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
      document.getElementById("deviceDetails").style.display = "block";
      document.getElementById("deviceTitle").innerText =
        `Device ${ip} Activity`;

      const ctx = document.getElementById("deviceChart");

      if (deviceChart) deviceChart.destroy();

      deviceChart = new Chart(ctx, {
        type: "doughnut",
        data: {
          labels: Object.keys(data.categories),
          datasets: [{
            data: Object.values(data.categories),
            backgroundColor: [
              "#4cc9f0", "#4895ef", "#4361ee",
              "#3f37c9", "#7209b7"
            ]
          }]
        }
      });
    });
}
