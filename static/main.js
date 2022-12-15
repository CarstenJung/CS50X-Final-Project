// input type file scan
document.getElementById('image').onchange = function () {
    // Show loaded image
    let loadedImg = document.getElementById('loaded_img')
    
    loadedImg.style.opacity = 1;
    loadedImg.src = URL.createObjectURL(this.files[0])
  };

/* let saveColors = document.getElementById('saveColor')

function preventLoading(event) {
  event.preventDefault()
}

saveColors.addEventListener('click', preventLoading, false) */
