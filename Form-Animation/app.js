function animateForm() {
    const arrowBtn = document.querySelectorAll(".fa-arrow-right");
    console.log(arrowBtn);

    arrowBtn.forEach(arrow => {
        arrow.addEventListener('click', () => {
            const currInput = arrow.previousElementSibling;
            const currForm = arrow.parentElement;
            const nextForm = currForm.nextElementSibling;

            //Validation Check
            if (currInput.type === "text" && validateUser(currInput)){
                console.log(currInput.value);
                activateForm(currForm, nextForm);
            }

            currForm.addEventListener('animationend', () => {
                currForm.style.animation = "";
            });
        });
    });
}

function validateUser(user) {
    if (user.value.length < 6) {
        error("crimson");
        user.parentElement.style.animation = "shake 0.5s ease";
        console.log("Need more characters");
    } 
    else {
        error("rgb(87,189,130)");
        return true;
    }
}

function activateForm(current, next){
    /*
    args : 
    current --- the current form that want to be deactivated
    next -- next form that will be activated
    */
   current.classList.add("inactive");
   current.classList.remove("active");
   next.classList.remove("inactive");
   next.classList.add("active");
}

function error(color) {
    document.body.style.backgroundColor = color;
}

animateForm();