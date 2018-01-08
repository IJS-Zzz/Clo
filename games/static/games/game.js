alert('Привет!\n\nЗдесь все просто, но тебе потребуется клавиатура!\nДвигай шарик стрелками "вверх", "вниз", "влево" и "вправо" и получай удовольствие.\n\nНо только попробуй выйти за границы....');
alert('Ах да, чуть не забыл...\n\nШарик умеет прыгать, используй "Пробел"!')


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



function jump(){
    var ball_style = getComputedStyle(ball);
    var top = parseInt(ball_style.top, 10);

    var start = Date.now();

    var g = 10;
    var V0 = -13;
    var y = 0;
    var change_color = true;

    var timer = setInterval(function() {
        if(top <= 460) {
            time = (Date.now() - start)/500;
            y = V0*time + g*time*time/2;
            top = top + y;
            ball.style.top = top + 'px';
            if (top <= -30 && change_color){
                    new_color()
                    change_color = false;
            }
            // console.log(top + "   "+ y + '    ' + time);

        }
        else{
            ball.style.top = '460px';
            clearInterval(timer); // конец через 2 секунды
            return;
        }
    }, 20);
}





function move_ball(e) {
    var ball = document.getElementById('ball');
    var ball_style = getComputedStyle(ball);

    var top = parseInt(ball_style.top, 10);
    var left = parseInt(ball_style.left, 10);

    // Стрелка вверх
    if (e.keyCode == 38) {
        if (top <= -30){
            top = 490
            new_color()
        }
        else{
            top -= 10;
        }
        ball.style.top = top + 'px';
    }
    // Стрелка вниз
    else if (e.keyCode == 40) {
        if (top >= 490){
            top = -30
            new_color()
        }
        else{
            top += 10;
        }
        ball.style.top = top + 'px';
    }
    // Стрелка налево
    if (e.keyCode == 37) {
        if (left <= -30){
            left = 490
            new_color()
        }
        else{
            left -= 10;
        }
        ball.style.left = left + 'px';
    }
    // Стрелка направо
    else if (e.keyCode == 39) {
        if (left >= 490){
            left = -30
            new_color()
        }
        else{
            left += 10;
        }
        ball.style.left = left + 'px';
    }

    // Пробел
    if(e.keyCode == 32){
        // console.log(top);
        jump();
    }

}

function reset() {
    var ball = document.getElementById('ball');
    ball.style.top = '230px';
    ball.style.left = '230px';
}

// document.onkeydown = document.onkeyup = document.onkeypress = move_box;
document.onkeydown = move_ball;