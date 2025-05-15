export async function sendImageForAuth(image) {
    const response = await fetch("http://localhost:5000/authenticate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image }),
    });
    return await response.json();
  }
  