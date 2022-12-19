// Save image from scan page
if (document.querySelector('.scan')) {
  document.getElementById('image').onchange = function () {
    // Show loaded image
    let loadedImg = document.getElementById('loaded_img')

    loadedImg.style.opacity = 1;
    loadedImg.src = URL.createObjectURL(this.files[0])
  }
}

// Copy Color RGB from mycolors
if (document.querySelector('.mycolors')) {
  var savedColor = document.querySelectorAll('.saveColor_btn');

  savedColor.forEach((btn) => {
    btn.addEventListener('click', saveColor)
  });

  function saveColor() {
    const color_rgb = document.querySelector('.mycolors_rgb');
    navigator.clipboard.writeText(color_rgb.innerText);
    console.log(color_rgb.innerHTML)
  }
}