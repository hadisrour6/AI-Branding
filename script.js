const myText = document.getElementById("my-input");
const slogan = document.getElementById('sloganSpan');
const keywords = document.getElementById('keywordsSpan');
const inputEl = document.getElementById('my-input');
const generate = document.getElementById('generate');


myText.addEventListener("input", () => {
    let count = (myText.value).length;
    document.getElementById("count-result").
        textContent = `${count}/24`;
})


async function generateAI() {
    input = inputEl.value;
    let KeywordURL = "https://bambooai-ec571d30a6c2.herokuapp.com/generate_keywords?prompt=" + input;
    let sloganURL = "https://bambooai-ec571d30a6c2.herokuapp.com/generate_snippet?prompt=" + input;

    const responseKey = await fetch(KeywordURL);
    const dataKey = await responseKey.json();

    const responseSlogan = await fetch(sloganURL);
    const dataSlogan = await responseSlogan.json();


    slogan.innerText = dataSlogan.snippet;
    keywords.innerText = dataKey.keywords;
}




generate.addEventListener("click", generateAI);






