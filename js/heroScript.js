function setup() {
  var largest = 0
  $('.skin').each(function() {
    if ($(this).width() > largest) {
      largest = $(this).width();
    }
  });
  $('.skin').each(function() {
    $(this).width(largest+1);
  });
}
window.addEventListener('load',setup,false);

var dlIcon = $('.download');
dlIcon.on('mouseover', function() {
  $(this).css('border-color', 'white');
  $(this).css('box-shadow', '0px 0px 25px white inset');
});
dlIcon.on('mouseout', function() {
  $(this).css('border-color', '#3D007A');
  $(this).css('box-shadow', '0px 0px 50px #3D007A inset');
});

var skinIcon = $('.skin');
skinIcon.on('mouseover', function() {
  $(this).css('border-color', 'white');
  $(this).css('box-shadow', '0px 0px 25px white inset');
});
skinIcon.on('mouseout', function() {
  $(this).css('border-color', '#3D007A');
  $(this).css('box-shadow', '0px 0px 50px #3D007A inset');
});

var menu = $('#menu');
menu.on('mouseover', function() {
  $(this).css('border-color', 'white');
  $(this).css('box-shadow', '0px 0px 25px white inset');
});
menu.on('mouseout', function() {
  $(this).css('border-color', '#3D007A');
  $(this).css('box-shadow', '0px 0px 50px #3D007A inset');
});
