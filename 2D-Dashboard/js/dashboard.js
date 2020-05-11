$(".more_info").click(function () {
    var $title = $(this).find(".title");
    if (!$title.length) {
        $(this).append('<span class="title">' + $(this).attr("title") + '</span>');
    } else {
        $title.remove();
    }
});


var rooms = [
    {name: "bad",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 15,
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
        currentTemp: 11,
        currentHum: 61
    }},
    {name: "wasch",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 11,
        currentHum: 72
    }},
    {name: "buegel",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 16,
        currentHum: 69
    }},
    {name: "kinder",
     data: {
        maxTemp: 30,
         minTemp: 10,
        currentTemp: 28,
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

var hueStart = [187, 1, 0.48];
var hueEnd = [360, 1, 0.37];

function updateValues() {
    for(let room of rooms) {
        console.log(room.name);
        var ps = $("." + room.name + ' p');
        var filled = $('#' + room.name + '-fill');
        ps[0].innerHTML = room.data.currentTemp + "<i class='mdi mdi-temperature-celsius kreis-icon'>";
        ps[1].innerHTML = room.data.currentHum + "<i class='mdi mdi-water-percent kreis-icon'>";
        var perc = (((room.data.currentTemp-room.data.minTemp)/(room.data.maxTemp-room.data.minTemp))*100).toFixed(0);
        var color = calcHSV(perc);
        filled.css('background-color', 'hsl('+color[0]+', '+color[1]+'%, '+color[2]+'%)')
        filled.css("height", perc + "%");
    }
}

function map_range(value, low1, high1, low2, high2) {
    return low2 + (high2 - low2) * (value - low1) / (high1 - low1);
}

function calcHSV(e) {
    h = map_range(e, 0, 100, hueStart[0], hueEnd[0]);
    s = map_range(e, 0, 100, hueStart[1], hueEnd[1]);
    v = map_range(e, 0, 100, hueStart[2], hueEnd[2]);
    return [h,  s*100, v*100];
}

updateValues();