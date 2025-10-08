const apiKey = "3a6ecdfc882b05d3eae6edf8ceb1402b";

function getWeather() {
  const city = document.getElementById("city").value;
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric`;

  fetch(url)
    .then(response => {
      if (!response.ok) throw new Error("City not found");
      return response.json();
    })
    .then(data => {
      const result = `
        <h2>${data.name}, ${data.sys.country}</h2>
        <p> Temperature: ${data.main.temp}°C</p>
        <p>Condition: ${data.weather[0].description}</p>
        <p> Humidity: ${data.main.humidity}%</p>
      `;
      document.getElementById("result").innerHTML = result;
    })
    .catch(error => {
      document.getElementById("result").innerHTML = `<p style="color:red">${error.message}</p>`;
    });
}
