// WEBBAPPP - FICHIER JAVASCRIPT
// -----------------------------
var connexionButton = null;

// Load things
// -----------
function load_things() {
       var hangon = document.querySelector('#hangon');
       if(hangon)
              hangon.addEventListener('click', info_message, false);

       connexionButton = document.querySelector('.connexionButton');
       if(connexionButton)
              connexionButton.addEventListener('click', extend_userpanel, false);


       // If we're on the exercice's content page
       if(document.querySelector('.solutionButton'))
              document.querySelector('.solutionButton').addEventListener('click', ShowSolution, false);


       // If we're on Report Page
       if(document.querySelector('.report_body')){
              refresh_button_to_iframe();
       }
}



// Show/Hide Exercice's solution
// -----------------------------
function ShowSolution(event){
       var solution = document.querySelector('.solutionArea');
       if (getComputedStyle(solution, null).display != "inline-block") { solution.style.display = "inline-block";}
       else solution.style.display = "none"; 
}

// Show/Hide messages
// ------------------
function info_message () {
       var box_to_show = document.querySelector('.box_content');
       if(box_to_show) {
              // si le message est masqué
              var firstChild = box_to_show.firstElementChild;
              firstChild.style.color = 'white';
              firstChild.style.marginTop = '10px';
              box_to_show.className = 'box_content_show';
       }
       else if (document.querySelector('.box_content_hide')) {
              // si le message est masqué
              box_to_show = document.querySelector('.box_content_hide');
              box_to_show.className = 'box_content_show';
       }
       else {
              // si le message est visble
              box_to_show = document.querySelector('.box_content_show');
              box_to_show.className = 'box_content_hide';

              // masquera le message dans 1s (syle par défaut)
              window.setTimeout(set_default_message_style, 1000);
       }
}

// Set default style on information messages
// ------------------------------------
function set_default_message_style () {
       if(document.querySelector('.box_content_hide')){
              document.querySelector('.box_content_hide').className = 'box_content';
       }
       else if(document.querySelector('.box_content_minimized')){
             document.querySelector('.box_content_minimized').className = 'box_content'; 
       }
}

// Extend panel where user can see its stats
// --------------------------
function extend_userpanel() {
       if(document.querySelector('.box_content')){
              var box_to_extend = document.querySelector('.box_content');
              box_to_extend.className = 'box_content_extended';
              connexionButton.innerHTML = "Minimize";
       }
       else if(document.querySelector('.box_content_show')){
              var box_to_extend = document.querySelector('.box_content_show');
              box_to_extend.className = 'box_content_extended';
              connexionButton.innerHTML = "Minimize";
       }
       else{
              // so the user panel is already extended
              // and we need to minimize it
              var box_to_extend = document.querySelector('.box_content_extended');
              box_to_extend.className = 'box_content_minimized';
              connexionButton.innerHTML = "Connexion";

              window.setTimeout(set_default_message_style, 1000);
       }
}



// -------------
// ---HORLOGE---
// -------------
// -------------
var _clock = null;
(function happyHour() {
       _clock = setInterval(TicTac, 1000);
})();

       function TicTac() {
              // Obtient l'heure actuelle (heures:minutes:secondes)
              var clock = new Date();

              var hours = clock.getHours();
              var minutes = clock.getMinutes();
              var seconds = clock.getSeconds();

              // trick pour toujours avoir des nombres à deux chiffres
              if (minutes < 10)
                     minutes = '0' + minutes;
              if (seconds < 10)
                     seconds = '0' + seconds;

              var currentClock = hours + ':' + minutes +':' + seconds;

              if (document.getElementById("clock"))
                     document.getElementById("clock").innerHTML = currentClock;
              else
                     clearInterval(_clock);
       }


// Add Refresh Button to iframe(s)
// if we are on Report Page
// -----------------------------
function refresh_button_to_iframe () {
       var frames = document.querySelectorAll('.iframe_control');
       for (var i = frames.length - 1; i >= 0; i--) {
              
              var img = document.createElement('img');
              img.src = "/static/img/refresh_icon.png";
              img.className = "iframe_button";
              img.addEventListener('click', reload_iframe, false);
              frames[i].appendChild(img);
       };
}


// -----------------
// ON REDACTION PAGE
// -----------------
// Clicked on a practice type
// --------------------------
function practice_type_create (event) {
       if(event.target){
              var practice = event.target;
              if(getComputedStyle(practice, null).fontWeight == '400'){
                     practice.style.fontWeight = '700';
                     var brother = practice.nextElementSibling;
                     var sister = practice.previousElementSibling;

                     if(brother) brother.style.fontWeight = '400';
                     else if(sister) sister.style.fontWeight = '400';
              }
              else if (getComputedStyle(practice, null).fontWeight == '700'){
                     // do nothing // already selected
              }
       }
}


function subject_changed (event) {
       //ajax
}