document.getElementById("taskForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const payload = {
        name: document.getElementById("name").value,
        description: document.getElementById("description").value,
        status: document.getElementById("status").value,
        priority: document.getElementById("priority").value,
        severity: document.getElementById("severity").value,
        time_given: parseInt(document.getElementById("time_given").value)
    };

    try {
        const response = await fetch("http://localhost:8000/tasks", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();
        document.getElementById("response").textContent =
            JSON.stringify(data, null, 2);

    } catch (err) {
        document.getElementById("response").textContent = err.toString();
    }
});
