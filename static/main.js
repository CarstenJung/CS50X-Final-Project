// input type file scan
document.getElementById('image').onchange = function () {
    // Show loaded image
    let loadedImg = document.getElementById('loaded_img')
    
    loadedImg.style.opacity = 1;
    loadedImg.src = URL.createObjectURL(this.files[0])

  };