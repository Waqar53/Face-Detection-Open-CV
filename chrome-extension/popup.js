document.getElementById("loginBtn").addEventListener("click", async () => {
    chrome.tabs.create({ url: "http://localhost:3000" });
  });
