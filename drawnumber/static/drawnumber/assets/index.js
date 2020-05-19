
const btnClear = document.querySelector("#btnClear");
const btnGuess = document.querySelector("#btnGuess");

//let img;
//let mousePressed = false;
//let lastY;
//let lastX;
//let ctx;
//let photo;

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
ctx.strokeStyle = "#000000";
ctx.lineWidth = 9;
ctx.lineJoin = "round";

// Set up mouse events for drawing
var drawing = false;
var mousePos = { x:0, y:0 };
var lastPos = mousePos;
canvas.addEventListener("mousedown", function (e) {
    drawing = true;
    lastPos = getMousePos(canvas, e);
    }, false);
canvas.addEventListener("mouseup", function (e) {
    drawing = false;
    }, false);
canvas.addEventListener("mousemove", function (e) {
    mousePos = getMousePos(canvas, e);
    renderCanvas();
    }, false);

// Get the position of the mouse relative to the canvas
function getMousePos(canvasDom, mouseEvent) {
  var rect = canvasDom.getBoundingClientRect();
  return {
    x: mouseEvent.clientX - rect.left,
    y: mouseEvent.clientY - rect.top
  };
}

// Set up touch events for mobile, etc
canvas.addEventListener("touchstart", function (e) {
        mousePos = getTouchPos(canvas, e);
  var touch = e.touches[0];
  var mouseEvent = new MouseEvent("mousedown", {
    clientX: touch.clientX,
    clientY: touch.clientY
  });
  canvas.dispatchEvent(mouseEvent);
}, false);
canvas.addEventListener("touchend", function (e) {
  var mouseEvent = new MouseEvent("mouseup", {});
  canvas.dispatchEvent(mouseEvent);
}, false);
canvas.addEventListener("touchmove", function (e) {
  var touch = e.touches[0];
  var mouseEvent = new MouseEvent("mousemove", {
    clientX: touch.clientX,
    clientY: touch.clientY
  });
  canvas.dispatchEvent(mouseEvent);
}, false);

// Get the position of a touch relative to the canvas
function getTouchPos(canvasDom, touchEvent) {
  var rect = canvasDom.getBoundingClientRect();
  return {
    x: touchEvent.touches[0].clientX - rect.left,
    y: touchEvent.touches[0].clientY - rect.top
  };
}


// Draw to the canvas
function renderCanvas() {
  if (drawing) {
    ctx.moveTo(lastPos.x, lastPos.y);
    ctx.lineTo(mousePos.x, mousePos.y);
    ctx.stroke();
    lastPos = mousePos;
  }
}

// Prevent scrolling when touching the canvas
document.body.addEventListener("touchstart", function (e) {
  if (e.target == photo) {
    e.preventDefault();
  }
}, false);
document.body.addEventListener("touchend", function (e) {
  if (e.target == photo) {
    e.preventDefault();
  }
}, false);
document.body.addEventListener("touchmove", function (e) {
  if (e.target == photo) {
    e.preventDefault();
  }
}, false);
//    photo = document.getElementById('myCanvas')
//    ctx = photo.getContext("2d");
//
//    photo.addEventListener
//    $('#myCanvas').touchstart(function (e) {
//        e.preventDefault();
//        mousePressed = true;
//        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
//    });
//    $('#myCanvas').touchmove(function (e) {
//        e.preventDefault();
//        if (mousePressed) {
//            Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true);
//        }
//    });
//    $('#myCanvas').touchend(function (e) {
//        e.preventDefault();
//        mousePressed = false;
//    });
//
//
//    $('#myCanvas').mousedown(function (e) {
//        mousePressed = true;
//        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
//    });
//    $('#myCanvas').mousemove(function (e) {
//        if (mousePressed) {
//            Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true);
//        }
//    });
//    $('#myCanvas').mouseup(function (e) {
//        mousePressed = false;
//    });
//    $('#myCanvas').mouseleave(function (e) {
//        mousePressed = false;
//    });
//
//}

//
//function Draw(x, y, isDown) {
//    if (isDown) {
//ctx.beginPath();
//ctx.strokeStyle = "#000000";
//ctx.lineWidth = 9;
//ctx.lineJoin = "round";
//ctx.moveTo(lastX, lastY);
//ctx.lineTo(x, y);
//ctx.closePath();
//ctx.stroke();
//    }
//    lastX = x;
//    lastY = y;
//}

function clearArea() {
    // Use the identity matrix while clearing the canvas
    canvas.width = canvas.width;
    var ctx = canvas.getContext("2d");
    ctx.strokeStyle = "#000000";
    ctx.lineWidth = 9;
    ctx.lineJoin = "round";
//    ctx.setTransform(1, 0, 0, 1, 0, 0);
//    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
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
});


// prediction function
function predict() {

    // get image as DataUrl
    img = canvas.toDataURL('image/png');
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
    resized_canvas.width = 28;
    resized_canvas.height = 28;
    resized_canvas.getContext('2d').scale(0.112, 0.112);
    resized_canvas.getContext('2d').drawImage(new_canvas, 0, 0);

    // uncomment to view the drawn characters
    // document.body.appendChild(resized_canvas);


    let image_data = resized_canvas.getContext('2d').getImageData(0, 0, 28, 28);



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
    let input = tf.tensor4d(monodata,[1,28,28,1]);
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

    fieldcode.value = img
    console.log(img)
}



