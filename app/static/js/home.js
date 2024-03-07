const body = document.getElementById("body");
const user_navigation_bar = document.getElementsByClassName("user-navigation-bar");
const worskpace = document.getElementsByClassName("workspace-container");

const button_home = document.getElementsByClassName("button-home");
button_home.addEvenListener(function button_click(){
    const status = await fetch("/home_click", ()=> {
        type: "POST",
        headers: "application-json",
        body: {{request}},
    });

});