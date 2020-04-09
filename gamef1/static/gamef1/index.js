const btnGuess = document.querySelector("#btnGuess");

btnGuess.addEventListener("click", function(){
   console.log('Oie')
   fillImage();

})

function fillImage(){
    field = document.getElementById('image')
    field.value = 'Sera que vai dar certo'
}

