var select = document.getElementById("artykuly")
var artText = document.getElementById('artText')
select.addEventListener('change', function() {
    fetch('http://localhost:8000/konstytucja/' + select.value.toString().replace("Art.", ''))
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log('Otrzymane dane:', data);
    artText.innerHTML = data;



  })
  .catch(error => {
    console.error('Wystąpił błąd:', error);
  });
})

const randomNumber = Math.floor(Math.random() * 243);


select.value = "Art."+randomNumber.toString()


 fetch('http://localhost:8000/konstytucja/' + select.value.toString().replace("Art.", ''))
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    console.log('Otrzymane dane:', data);
    artText.innerHTML = data;



  })
  .catch(error => {
    console.error('Wystąpił błąd:', error);
  });