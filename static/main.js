// Save image from scan page
if (document.querySelector('.scan')) {
  document.getElementById('image').onchange = function () {
    // Show loaded image
    let loadedImg = document.getElementById('loaded_img')

    loadedImg.style.opacity = 1;
    loadedImg.src = URL.createObjectURL(this.files[0])
  }
}

// Copy IMG colors
// Copy Color RGB from mycolors
if (document.querySelector('.mycolors')) {
  // Variable for Scheme and Image colors
  var savedColor = document.querySelectorAll('.saveColor_btn');
  var saved_img_color = document.querySelectorAll('.saveColor_img');

  // Loop for Scheme colors
  savedColor.forEach((btn) => {
    btn.addEventListener('click', () => {
      const color_rgb = btn.parentElement.querySelector('.mycolors_rgb');
      navigator.clipboard.writeText(color_rgb.innerText);
      console.log(color_rgb.innerHTML)
    })
  });

  // Loop for Image colors
  saved_img_color.forEach((btn_img) => {
    btn_img.addEventListener('click', () => {
      const color_img = btn_img.parentElement.querySelector('.mycolors_img');
      navigator.clipboard.writeText(color_img.innerText);
      console.log(color_img.innerHTML)
    })
  });
}

/**********
 * GSAP
 ********** */
if (document.querySelector('.index')) {
  let hero_split = new SplitText('.gsap_hero h1', {
    type: 'words,chars'
  });

  gsap.fromTo(hero_split.chars, {
    x: 0,
    y: 10,
    autoAlpha: 0,
  }, {
    x: 0,
    y: 0,
    ease: Elastic.easeOut,
    duration: 3,
    stagger: .2,
    autoAlpha: 1,
  });

  gsap.fromTo('.gsap_hero h2', {
    autoAlpha: 0,
  }, {
    autoAlpha: 1,
    duration: 3,
    delay: 2.5,
  });
}