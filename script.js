let myText = document.getElementById("my-input");

myText.addEventListener("input", ()=> {
    let count = (myText.value).length;
    console.log(myText.value, count);
    document.getElementById("count-result").
    textContent = `${count}/32`;
})




