
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
//    let img = new Image();
//    img.onload = function(){
//        context.drawImage(img, 0, 0, 28, 28);
//        data  = context.getImageData(0,0,28,28).data;
//        var input = [];
//        for (var i=0; i < data.length ; i+=4 ) {
//            input.push(data[i+2]/255)
//        }
//        tensor = tf.tensor(input).reshape([1, 28, 28, 1]);
//        return tensor
//    }
    photo = document.getElementById('myCanvas')
    //convert to tensor
    let tensor = tf
        .browser.fromPixels(photo)
        .resizeBilinear([28,28])
        .mean(2)
        .expandDims(2)
        .expandDims()
        .toFloat()

     return tensor.div(255.0);
    console.log(tensor);
}


async function submitNumber(){
    let prediction = await model.predict(prepareImage()).array();

    console.log('Previsão é ' + prediction)

    // get the model's prediction results
    let results = await tf.argMax(prediction).data();

    console.log(results);

}





btnClear.addEventListener("click", function() {
    clearArea()
});

btnGuess.addEventListener("click", function(){
   let prediction = predict()
   buildchart(prediction);
})


// prediction function
function predict() {

    // get image from canvas
    let image = ctx.getImageData(0, 0, 250, 250);

    // create a new canvas and copy the image from drawing canvas
    let new_canvas = document.createElement('canvas');

    // canvas dimensions
    new_canvas.height = 250;
    new_canvas.width = 250;
    new_canvas.getContext('2d').putImageData(image, 0, 0);

    // new resized canvas 28x28
    let resized_canvas = document.createElement('canvas');
    resized_canvas.width = 28;
    resized_canvas.height = 28;
    resized_canvas.getContext('2d').scale(0.14, 0.14);
    resized_canvas.getContext('2d').drawImage(new_canvas, 0, 0);

    // uncomment to view the drawn characters
    // document.body.appendChild(resized_canvas);


    let image_data = resized_canvas.getContext('2d').getImageData(0, 0, 28, 28);

    // change to monochrome
    let monodata = [];
    for (let i = 0, len = image_data.data.length/4; i < len; i += 1) {
        monodata.push(image_data.data[i * 4 + 3]);
        monodata.push(0);
        monodata.push(0);
        monodata.push(0);
    }

    // create imagedata for tfjs
    let monoimgdata = new ImageData(new Uint8ClampedArray(monodata), 28, 28);

    // get image from pixels of monochromatic image
    let input = tf.browser.fromPixels(monoimgdata, 1).reshape([1, 28, 28, 1]).cast('float32').div(tf.scalar(255));

    // prediction
    console.log('Prediction started.'); // message
    let predictions = model.predict(input).dataSync(); // prediction
    console.log('Prediction completed.');// message
    console.log(predictions)
    return predictions;

}

function buildchart(predictions) {

    var predictions_arr = [];
    for (var i=0; i<=9; i++) {
        predictions_arr[i] = predictions[i].toFixed(8) * 100;
    }

    let ctx2 = document.getElementById("prediction_chart").getContext('2d');
    var prediction_chart = new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            datasets: [{
                label: '% confidence',
                data: predictions,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255,99,132,1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });
}
