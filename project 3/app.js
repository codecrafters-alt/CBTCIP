const API_KEY = `96d5a9518270def523e40d91c413cf77`;
let form=document.querySelector("form")
let search=document.querySelector("#search")
let weather=document.querySelector("#weather")

const getWeather=async (city)=>{
   weather.innerHTML=`<h3> searching.... </h3>`
   
   const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`;
   const response=await fetch(url)
   console.log(response)
   const data=await response.json()
   return showWeather(data)
}

const showWeather=(data)=>{
    if(data.cod==="404"){
        weather.innerHTML=`<h2>
        city not found </h2>`
        return;
    }
    weather.innerHTML=`
    <div>
      <img src="https://openweathermap.org/img/wn/${data.weather[0].icon}@2x.png">
     </div>
     <div>
       <h2>${data.main.temp}°C</h2>
       <h4>${data.weather[0].main}</h4>
     </div>
    `
}

form.addEventListener("submit",(evt)=>{
    
    getWeather(search.value)
    evt.preventDefault(); //after submit the form ka reload prevent kar deta hain
    
})