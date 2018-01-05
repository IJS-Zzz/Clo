
var images = [
    "/static/mainApp/images/main_image.jpg",
    "/static/mainApp/images/main_image_2.jpg",
    "/static/mainApp/images/main_image_3.jpg",
];

var num = 0;

function next() {
    var slider = document.getElementById('slider');
    num++;
    if(num >= images.length){
        num = 0;
    }
    slider.src = images[num];
    loading_persent = 0;
}

function prev(){
    var slider = document.getElementById('slider');
    num--;
    if(num < 0){
        num = images.length - 1;
    }
    slider.src = images[num];
    loading_persent = 0;
}

var loading_persent = 0;
function loading() {
    var load = document.getElementById('loading');
    loading_persent += 0.1;
    if(loading_persent > 100){
        next();
    }
    load.style.width = loading_persent + '%';
}

var l = setInterval(loading, 3);