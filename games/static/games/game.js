var color_num = 0;
var color = [
    ['#1F2D31', '#F66663'],
    ['#F8F6ED', '#0050A7'],
    ['#789D8D', '#FCD25C'],
    ['#E39855', '#3491D6']
];


function new_color() {
    // var box = document.getElementById('box');
    // var ball = document.getElementById('ball');
    color_num++;
    if (color_num >= color.length) {
        color_num = 0;
    }
    box.style.background = color[color_num][0];
    ball.style.background = color[color_num][1];
}







function move_ball(e) {
    var ball = document.getElementById('ball');
    var ball_style = getComputedStyle(ball);

    var top = parseInt(ball_style.top, 10);
    var left = parseInt(ball_style.left, 10);


    if (e.keyCode == 38) {
        // вверх
        if (top <= -30){
            top = 490
            new_color()
        }
        else{
            top -= 10;
        }
        ball.style.top = top + 'px';
    }
    else if (e.keyCode == 40) {
        //вниз
        if (top >= 490){
            top = -30
            new_color()
        }
        else{
            top += 10;
        }
        ball.style.top = top + 'px';
    }
    if (e.keyCode == 37) {
        //налево
        if (left <= -30){
            left = 490
            new_color()
        }
        else{
            left -= 10;
        }
        ball.style.left = left + 'px';
    }
    else if (e.keyCode == 39) {
        //направо
        if (left >= 490){
            left = -30
            new_color()
        }
        else{
            left += 10;
        }
        ball.style.left = left + 'px';
    }
}

function reset() {
    var ball = document.getElementById('ball');
    ball.style.top = '230px';
    ball.style.left = '230px';
}

// document.onkeydown = document.onkeyup = document.onkeypress = move_box;
document.onkeydown = move_ball;