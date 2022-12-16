// input type file scan
document.getElementById('image').onchange = function () {
    // Show loaded image
    let loadedImg = document.getElementById('loaded_img')

    loadedImg.style.opacity = 1;
    loadedImg.src = URL.createObjectURL(this.files[0])
  };



/* $(document).on('submit','#form_test',function(e) {
  console.log('hello');
  e.preventDefault();
  $.ajax({
    type:'POST',
    url:'/console',
    data:{
      todo:$("#todo").val()
  },
  success:function() {
    alert('saved');
  }
  })
}); */



