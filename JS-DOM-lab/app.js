(function pigify() {
    document.getElementById("brand").innerHTML = "People's Meat";
    document.getElementsByTagName("h1")[0].innerHTML = "Hello, Meat Eaters!";
    document.getElementById("banner").src = "https://img1.etsystatic.com/000/0/6394783/il_570xN.256879177.jpg";

    var h2s = document.getElementsByTagName("h2");

    h2s[0].innerHTML = "Hams";
    h2s[1].innerHTML = "Ribs";
    h2s[2].innerHTML = "Bacon";

    var btns = document.querySelectorAll(".btn-default");

    btns.forEach(btn => { 
        btn.classList.remove("btn-default"); 
        btn.classList.add("btn-primary") 
    })
})();