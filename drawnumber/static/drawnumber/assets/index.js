
const btnClear = document.querySelector("#btnClear");
const btnGuess = document.querySelector("#btnGuess");


let mousePressed = false;
let lastY;
let lastX;
let ctx;
let photo;
function initThis() {
    photo = document.getElementById('myCanvas')
    ctx = photo.getContext("2d");

    $('#myCanvas').mousedown(function (e) {
        mousePressed = true;
        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
    });

    $('#myCanvas').mousemove(function (e) {
        if (mousePressed) {
            Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true);
        }
    });

    $('#myCanvas').mouseup(function (e) {
        mousePressed = false;
    });
        $('#myCanvas').mouseleave(function (e) {
        mousePressed = false;
    });
}
initThis();

function Draw(x, y, isDown) {
    if (isDown) {
        ctx.beginPath();
        ctx.strokeStyle = "#000000";
        ctx.lineWidth = 9;
        ctx.lineJoin = "round";
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.stroke();
    }
    lastX = x;
    lastY = y;
}

function clearArea() {
    // Use the identity matrix while clearing the canvas
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

function prepareImage(){
    let img = new Image();
    img.onload = function(){
        context.drawImage(img, 0, 0, 28, 28);
        data  = context.getImageData(0,0,28,28).data;
        var input = [];
        for (var i=0; i < data.length ; i+=4 ) {
            input.push(data[i+2]/255)
        }
        tensor = tf.tensor(input).reshape([1, 28, 28, 1]);
        return tensor
    }
//    photo = document.getElementById('myCanvas')
//    //convert to tensor
//    let tensor = tf
//        .browser.fromPixels(photo)
//        .resizeBilinear([28,28])
//        .mean(2)
//        .expandDims(2)
//        .expandDims()
//        .toFloat()
//
//     return tensor.div(255.0);
//    console.log(tensor);
}


async function submitNumber(){
    let prediction = await model.predict(prepareImage()).array();

    console.log('Previsão és ' + prediction)

    // get the model's prediction results
    let results = await tf.argMax(prediction).data();

    console.log(results);

}





btnClear.addEventListener("click", function() {
    clearArea()
});

btnGuess.addEventListener("click", function(){
    submitNumber()
})