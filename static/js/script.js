$(document).ready(function(){

    // typing text animation script
   var typed = new Typed("#searchInput", {
        strings: ["Letni, Chamski Podryw - Pomidorowa", "Rick Astley - Never gonna give you up","Against The Current - Legends Never Die", "Alstroemeria Records - Bad Apple!"],
        typeSpeed: 30,
        backSpeed: 30,
        attr:'placeholder', 
bindInputFocusEvent: true,
        loop: true
    });
    var typed = new Typed("#welcome", {
      strings: ["HEJ! FUTRAZKU","ZNAJDZ SWOJĄ PIOSENKĘ ","I ...", "ZAŚPIEWAJ","ZARYCZ","ZAWYJ", "Z NAMI"],
      typeSpeed: 50,
      showCursor: false,
      fadeOut: true,
      backSpeed: 20,
      loop: true
  });
  
  
});

function debounce(func, timeout = 300){
  let timer;

  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => { func.apply(this, args); }, timeout);
  };
}

function search() {
      var query = searchInput.value.trim();
      if (query.length === 0) {
        searchResults.innerHTML = ''; // Wyczyść wyniki, jeśli pole jest puste
        return;
      }

      fetch(`/dynamic_search_songs/?query=${query}`)
        .then(response => response.json())
        .then(data => {
          searchResults.innerHTML = ''; // Wyczyść wyniki
          data.results.forEach(song => {
            var li = document.createElement('li');
            li.classList.add("list-group-item");
            li.textContent = song.title;
            li.addEventListener('click', function() {
              // Tutaj możesz obsłużyć kliknięcie na wynik wyszukiwania
              // np. przenieść do strony szczegółów piosenki
              window.location.href = `/piosenka/${song.id}/`;
            });
            searchResults.appendChild(li);
          });
        })
        .catch(error => {
          console.error('Błąd:', error);
        });
    }
 var searchInput = document.getElementById('searchInput');
    var searchResults = document.getElementById('searchResults');

    searchInput.addEventListener('input',  debounce(()=>search()));
function akcja(value, row, index) {
  return [
      '<a class="btn btn-sm btn-secondary" href="/piosenka/'+row.id+'" >',
      'Przejdz do piosenki',
      '</a>'
    ].join('')
}
