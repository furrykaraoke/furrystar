
  function incrementPlayCount(songId) {
    var csrfToken = getCookie('csrftoken'); // Pobierz token CSRF z ciasteczka

    $.ajax({
      type: "POST",
      url: "{% url 'increment_play_count' 0 %}".replace('0', songId),
      data: {
        csrfmiddlewaretoken: csrfToken // Dodaj token CSRF jako część danych
      },
      success: function(data) {
        if (data.message) {
          location.reload();
        }
      }
    });
  }

  // Funkcja do pobierania wartości tokenu CSRF z ciasteczka
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === name + '=') {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
