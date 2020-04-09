
const btnClear = document.querySelector("#btnClear");
const btnGuess = document.querySelector("#btnGuess");

let img;
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

    // get image as DataUrl
    img = photo.toDataURL('image/png');
    console.log(img);
//    fillImage();
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
    resized_canvas.width = 250;
    resized_canvas.height = 250;
    resized_canvas.getContext('2d').scale(1, 1);
    resized_canvas.getContext('2d').drawImage(new_canvas, 0, 0);

    // uncomment to view the drawn characters
    // document.body.appendChild(resized_canvas);


    let image_data = resized_canvas.getContext('2d').getImageData(0, 0, 250, 250);



//     change to monochrome
    let monodata = [];
    for (let i = 0; i < image_data.data.length; i += 4) {
        monodata.push(image_data.data[i+3]/255);
//        monodata.push(0);
//        monodata.push(0);
//        monodata.push(0);
    }

    // create imagedata for tfjs
//    let imagedata = new ImageData(new Uint8ClampedArray(monodata), 250, 250);

//    resized_canvas.getContext('2d').putImageData(imagedata, 0, 0);


        // get image as DataUrl
//    img = resized_canvas.toDataURL('image/png');
//    console.log(img);

    // get image from pixels of monochromatic image
//    let input = tf.browser.fromPixels(imagedata);
    console.log('Este ó tensor');
    let input = tf.tensor4d(monodata,[1,250,250,1]);
    console.log(input);
//    .reshape([1, 250, 250, 4]).cast('float32').div(tf.scalar(255));

    // prediction
    console.log('Prediction started.'); // message
    let predictions = model.predict(input).dataSync(); // prediction
    console.log('Prediction completed.');// message
    console.log(predictions);

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
function fillImage(){
//    let field = document.getElementById('drawing')
    let fieldcode = document.getElementById('drawingcode')
//    field.value = 'Oxe'
    fieldcode.value = img
    console.log(img)
}

