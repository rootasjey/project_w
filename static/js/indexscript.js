// WEBBAPPP - FICHIER JAVASCRIPT


// HORLOGE
function happyHour() {
       setInterval(TicTac, 1000);
}

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