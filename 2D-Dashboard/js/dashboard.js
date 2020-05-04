var rooms = [
    {name: "bad",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 20,
        currentHum: 60
    }},
    {name: "arbeits",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 19,
        currentHum: 51
    }},
    {name: "schlaf",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 17,
        currentHum: 61
    }},
    {name: "wasch",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 16,
        currentHum: 72
    }},
    {name: "buegel",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 17,
        currentHum: 69
    }},
    {name: "kinder",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 19,
        currentHum: 63
    }},
    {name: "kueche",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 20,
        currentHum: 62
    }},
    {name: "wohn",
     data: {
        maxTemp: 30,
        minTemp: 10,
        currentTemp: 22,
        currentHum: 55
    }},
];

function updateValues() {
    for(let room of rooms) {
        console.log(room.name);
        var ps = $("." + room.name + ' p');
        var filled = $('.' + room.name + ' .filled-' + room.name);
        ps[0].innerHTML = room.data.currentTemp + "°";
        ps[1].innerHTML = room.data.currentHum + "%";
        var perc = (((room.data.currentTemp-room.data.minTemp)/(room.data.maxTemp-room.data.minTemp))*100).toFixed(0);
        filled.css("height", perc + "%");
    }
}

updateValues();