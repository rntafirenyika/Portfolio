document.addEventListener('DOMContentLoaded', function() {

    var tiles = document.getElementsByClassName('tile');
    for (var i = 0; i < tiles.length; i++) {
    tiles[i].addEventListener('mouseover', function() {
        this.style.backgroundColor = '#666666';
        this.style.color = '#fff';
    });

    tiles[i].addEventListener('mouseout', function() {
        this.style.backgroundColor = '#29DEDA';
        this.style.color = '#333';
    });
    }

});


$(document).ready(function() {
  $('.custom-select').select2({
    placeholder: 'Choose...',
    allowClear: true,
  });
});

function handleSelectChange(selectElement) {
    const selectedValue = $(selectElement).val();
    if (selectedValue) {
      // Option selected
      console.log(`Selected: ${selectedValue}`);
    } else {
      // Clear selection
      console.log('No option selected');
    }
  }