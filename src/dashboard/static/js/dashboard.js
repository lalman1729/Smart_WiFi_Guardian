console.log("Dashboard JS loaded");

let categoryChart = null;

async function refreshStats() {
    try {
        const res = await fetch("/api/stats");
        const data = await res.json();

        // Update counters
        document.getElementById("totalRequests").innerText = data.total_requests;
        document.getElementById("blockedDomains").innerText = data.blocked_domains;
        document.getElementById("activeDevices").innerText = data.devices.length;
        document.getElementById("threatLevel").innerText =
            data.blocked_domains > 5 ? "HIGH" :
            data.blocked_domains > 0 ? "MEDIUM" : "LOW";

                   loadDevices(data.devices);

            // Update connected devices
const deviceList = document.getElementById("deviceList");
if (deviceList) {
    deviceList.innerHTML = "";
    data.devices.forEach(ip => {
        const li = document.createElement("li");
        li.innerText = ip;
        deviceList.appendChild(li);
    });
}

        // Update domain table
        const table = document.getElementById("topDomainsTable");
        if (!table) return;

        table.innerHTML = "";
        Object.entries(data.domains).forEach(([domain, hits]) => {
            const row = document.createElement("tr");
            row.innerHTML = `<td>${domain}</td><td>${hits}</td>`;
            table.appendChild(row);
        });

        // Update chart
        const labels = Object.keys(data.categories);
        const values = Object.values(data.categories);

        const ctx = document.getElementById("categoryChart").getContext("2d");

        if (categoryChart) {
            categoryChart.data.labels = labels;
            categoryChart.data.datasets[0].data = values;
            categoryChart.update();
        } else {
            categoryChart = new Chart(ctx, {
                type: "pie",
                data: {
                    labels: labels,
                    datasets: [{
                        data: values,
                        backgroundColor: [
                            "#4caf50",
                            "#2196f3",
                            "#ff9800",
                            "#9c27b0"
                        ]
                    }]
                }
            });
        }

        console.log("Dashboard refreshed");

    } catch (err) {
        console.error("Dashboard refresh failed:", err);
    }
}

// Auto refresh every 5 seconds
setInterval(refreshStats, 5000);

// First load
refreshStats();






function loadDevices(devices) {
    const list = document.getElementById("deviceList");
    if (!list) return;

    list.innerHTML = "";

    devices.forEach(ip => {
    const li = document.createElement("li");

        li.innerText = ip;
        li.style.cursor = "pointer";
        li.onclick = () => loadDeviceDetails(ip);
        list.appendChild(li);

    });


}



function loadDeviceDetails(ip) {
    fetch(`/api/device/${ip}`)
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById("deviceTable");
            if (!table) return;

            table.innerHTML = "";

            Object.entries(data).forEach(([domain, hits]) => {
                const row = document.createElement("tr");
                row.innerHTML = `<td>${domain}</td><td>${hits}</td>`;
                table.appendChild(row);
            });
        });
}









function scanRouter() {
    const routerIp = document.getElementById("routerIp").value;
    if (!routerIp) {
        alert("Please enter router IP");
        return;
    }

    fetch("/api/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ router_ip: routerIp })
    })
    .then(res => res.json())
    .then(data => {
        if (data.devices) {
            loadDevices(data.devices);
        }
    })
    .catch(err => console.error("Scan failed", err));
}






async function scanNetwork() {
    const routerIP = document.getElementById("router-ip").value;

    const res = await fetch("/api/scan", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ router_ip: routerIP })
    });

    const data = await res.json();

    const list = document.getElementById("device-list");
    list.innerHTML = "";

    if (data.devices) {
        data.devices.forEach(ip => {
            const li = document.createElement("li");
            li.textContent = ip;
            li.onclick = () => loadDeviceActivity(ip);
            list.appendChild(li);
        });
    }
}






fetch("/api/scan", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ router_ip: routerIp })
})



/*
123

function refreshStats() {
    fetch("/api/stats")
        .then(res => res.json())
        .then(data => {
            document.getElementById("total_requests").innerText = data.total_requests;
            document.getElementById("blocked_domains").innerText = data.blocked_domains;
            document.getElementById("active_devices").innerText = data.devices.length;

            loadDevices(data.devices);
            updateCharts(data);
        });
}

function loadDevices(devices) {
    const list = document.getElementById("deviceList");
    if (!list) return;

    list.innerHTML = "";

    devices.forEach(ip => {
        const li = document.createElement("li");
        li.textContent = ip;
        li.style.cursor = "pointer";
        li.onclick = () => loadDeviceDetails(ip);
        list.appendChild(li);
    });
}


function loadDeviceDetails(ip) {
    fetch(`/api/device/${ip}`)
        .then(res => res.json())
        .then(data => {
            const table = document.getElementById("deviceTable");
            if (!table) return;

            table.innerHTML = "";

            Object.entries(data).forEach(([domain, hits]) => {
                const row = document.createElement("tr");
                row.innerHTML = `<td>${domain}</td><td>${hits}</td>`;
                table.appendChild(row);
            });
        });
}




*/








/*
fetch("/api/stats")
  .then(res => res.json())
  .then(data => {
    // Top cards
    document.getElementById("total_requests").innerText =
      data.total_requests || 0;

    document.getElementById("blocked_domains").innerText =
      data.blocked_domains || 0;

    document.getElementById("active_devices").innerText =
      data.devices.length;

    document.getElementById("threat_level").innerText =
      data.devices.length ;



    // Category chart
    const labels = Object.keys(data.categories);
    const values = Object.values(data.categories);

    new Chart(document.getElementById("category_chart"), {
      type: "pie",
      data: {
        labels: labels,
        datasets: [{
          data: values,
          backgroundColor: [
            "#4caf50", "#2196f3", "#ff9800", "#9c27b0", "#f44336"
          ]
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    });

    // Top domains table
    const table = document.getElementById("top-domains");
    table.innerHTML = "";

    Object.entries(data.domains).forEach(([domain, count]) => {
      const row = document.createElement("tr");
      row.innerHTML = `<td>${domain}</td><td>${count}</td>`;
      table.appendChild(row);
    });
  });







// Load devices
fetch("/api/stats")
  .then(res => res.json())
  .then(data => {
    const list = document.getElementById("deviceList");
    list.innerHTML = "";

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



*/

/*
let categoryChart = null;

async function refreshStats() {
  try {
    console.log("Refreshing dashboard data...");

    const res = await fetch("/api/stats");
    if (!res.ok) throw new Error("API failed");

    const data = await res.json();

    // ---- SAFE ELEMENT UPDATES ----
    const tr = document.getElementById("total_requests");
    const bd = document.getElementById("blocked_domains");
    const ad = document.getElementById("active_devices");

    if (tr) tr.textContent = data.total_requests || 0;
    if (bd) bd.textContent = data.blocked_domains || 0;
    if (ad) ad.textContent = data.devices.length || 0;

    // ---- TOP DOMAINS TABLE ----
    const table = document.getElementById("top-domains");
    if (table) {
      table.innerHTML = "";
      Object.entries(data.domains || {}).forEach(([d, h]) => {
        table.innerHTML += `<tr><td>${d}</td><td>${h}</td></tr>`;
      });
    }

    // ---- CATEGORY CHART (SAFE RESET) ----
    const canvas = document.getElementById("category_chart");
    if (canvas) {
      const ctx = canvas.getContext("2d");

      if (categoryChart) {
        categoryChart.destroy();
      }

      categoryChart = new Chart(ctx, {
        type: "doughnut",
        data: {
          labels: Object.keys(data.categories || {}),
          datasets: [{
            data: Object.values(data.categories || {}),
            backgroundColor: ["#4ade80", "#60a5fa", "#f59e0b", "#c084fc"]
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: true
        }
      });
    }

  } catch (err) {
    console.error("Dashboard refresh failed:", err);
  }
}

*/


/*
fetch('/api/stats')
.then(res => res.json())
.then(data => {

    document.getElementById("totalRequests").innerText = data.total;
    document.getElementById("blockedCount").innerText = data.blocked;
    document.getElementById("deviceCount").innerText = data.devices;

    new Chart(document.getElementById('categoryChart'), {
        type: 'doughnut',
        data: {
            labels: Object.keys(data.categories),
            datasets: [{
                data: Object.values(data.categories),
                backgroundColor: [
                    '#4cc9f0',
                    '#4895ef',
                    '#4361ee',
                    '#3f37c9',
                    '#7209b7'
                ]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    new Chart(document.getElementById('domainChart'), {
        type: 'bar',
        data: {
            labels: Object.keys(data.domains),
            datasets: [{
                data: Object.values(data.domains),
                backgroundColor: '#4cc9f0'
            }]
        }
    });
});

// Auto refresh every 5 seconds
setInterval(() => location.reload(), 5000);
*/
