const WebSocket = require("ws");
const { spawn } = require("child_process");
const fs = require("fs"); // Added to check if file exists

const ws = new WebSocket("wss://movieplay-zvp8.onrender.com");

ws.on("open", () => {
  console.log("Connected ✅");
  ws.send(JSON.stringify({ type: "register", clientId: "PAVAN" }));
});

ws.on("message", (data) => {
  const msg = JSON.parse(data.toString());

  if (msg.type === "command") {
    const scriptPath = "pe.py";

    // Verify the file exists so we don't get a different error
    if (!fs.existsSync(scriptPath)) {
        console.error(`Error: ${scriptPath} not found in this directory!`);
        return;
    }

    console.log("Passing prompt to Python:", msg.command);

    // FIX: Changed "python" to "python3" for macOS
    const pythonProcess = spawn("python3", [scriptPath, msg.command]);

    pythonProcess.stdout.on("data", (data) => {
      console.log(`Python Output: ${data}`);
    });

    pythonProcess.stderr.on("data", (data) => {
      console.error(`Python Error: ${data}`);
    });

    // Handle process-level errors (like if python3 is still not found)
    pythonProcess.on("error", (err) => {
      console.error("Failed to start Python process:", err.message);
    });
  }
});

ws.on("close", () => console.log("Disconnected ❌"));
ws.on("error", (err) => console.error("WS error:", err.message));
