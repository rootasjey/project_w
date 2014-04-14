// WEBBAPPP - FICHIER JAVASCRIPT
// -----------------------------

// HORLOGE
// (function happyHour() {
//        setInterval(TicTac, 1000);
// })();

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

              if (document.getElementById)
                     document.getElementById("clock").innerHTML = currentClock;
              else
                     document.write(currentClock)
       }

// Charge divers éléments
function load_things() {
       var hangon = document.querySelector('#hangon');
       hangon.addEventListener('click', info_message, false);
}

// Affiche ou Masque les messages d'information
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

// Remet le style par défaut des messages d'information
function set_default_message_style () {
       document.querySelector('.box_content_hide').className = 'box_content';
}

// Ajoute des évènements
// (function add_events() {
//        window.setTimeout(load_click_on_chapters, 1000);
// })();

function load_click_on_chapters () {
       if(document.querySelector('.chapitre')){
              var chapters = document.querySelectorAll('.chapitre');
              for (var i = chapters.length - 1; i >= 0; i--) {
                     chapters[i].addEventListener('click', open_chapter, false);
              };
       }
}

// Lorsqu'on clic sur un chapitre
function open_chapter (event) {
       var parent = event.target.parentNode;
       var chap_num = parent.id;
       chap_num = chap_num - 1;

       var xhr = new XMLHttpRequest();
       xhr.open('GET', "/domaine/informatique/chapitre?id=" + chap_num);
       xhr.send(null);
       // console.log(xhr.responseText);
}