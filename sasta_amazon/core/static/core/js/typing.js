const text_arr = ["Let's make your shopping experience amazing.","Welcome to your new shopping destination","Thanks for choosing us!"];
let index=0;
let charIndex=0;
let isDeleting=false;

const speed=50;
const eraseSpeed=50;

const textElement = document.getElementById("text");

function typeEffect(){
    let currentText=text_arr[index];

    if(!isDeleting){
        textElement.textContent=currentText.substring(0,charIndex++);

        if(charIndex> currentText.length){
            isDeleting=true;
            setTimeout(typeEffect,1500);
            return
        }
    }
    else{
        textElement.textContent=currentText.substring(0,charIndex--);

        if(charIndex < 0){
            isDeleting=false;
            index=(index+1)%text_arr.length;
            setTimeout(typeEffect,1500);
            return
        }
    }
    setTimeout(typeEffect, isDeleting ? eraseSpeed : speed)
}

typeEffect()