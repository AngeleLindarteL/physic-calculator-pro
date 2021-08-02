const checkBox = document.querySelector("#check-box");
let formGroup = document.querySelector(".form-group")


if(checkBox.children[1].checked == false){
    for(let i = 4; i < formGroup.children.length-1; i++){
        formGroup.children[i].style.display = "none";
        formGroup.children[i].style.opacity = "0";
    }
}

checkBox.children[1].addEventListener('change',() => {
    formGroup.children[7].style.marginTop = `${formGroup.children[7].clientHeight*6}px`;
    if(checkBox.children[1].checked == false){
        setTimeout(() => {
        for(let i = 4; i < formGroup.children.length-1; i++){
            formGroup.children[i].style.display = "none";
            formGroup.children[i].style.opacity = "0";}
            formGroup.children[7].style.marginTop = `2%`
        }, 180);

    }else{
        formGroup.children[7].style.marginTop = `${formGroup.children[7].clientHeight*6}px`;
        setTimeout(() => {
            for(let i = 4; i < formGroup.children.length-1; i++){
                formGroup.children[i].style.display = "block";
                formGroup.children[i].style.opacity = "100%";
            }
            formGroup.children[7].style.marginTop = `2%`
        }, 180);
    }
})