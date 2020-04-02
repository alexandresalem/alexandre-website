var draw,
    context;

function dragStart() {
    console.log('dragStart');


}

function drag() {
    console.log('drag');
}

function init() {
    canvas = document.getElementById("draw");
    context = canvas.getContext('2d');
    context.strokeStyle = 'black';
    context.lineWidht = 6;
    context.lineCap = 'round';

    canvas.addEventListener('mousedown', dragStart, false);
    canvas.addEventListener('mousemove', drag, false);

}

import * as tf from '@tensorflow/tfjs';

function loadModelDigit() {
  return tf.loadModel({% static 'drawnumber/.keras_model/model.json'});
}

window.addEventListener('load', init, false);


