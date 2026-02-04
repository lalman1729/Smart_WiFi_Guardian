fetch("/api/stats")
  .then(res => res.json())
  .then(data => {
    const ctx = document.getElementById("categoryChart");

    new Chart(ctx, {
      type: "pie",
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
