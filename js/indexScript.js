var heroIcon = $('.icon');
heroIcon.on('mouseover', function() {
  $(this).css({
    'border': '2px solid white',
    'box-shadow': 'white 0px 0px 20px'
  });
});
heroIcon.on('mouseout', function() {
  $(this).css({
    'border': '2px solid #3D007A',
    'box-shadow': '#4215AD 0px 0px 20px'
  });
});

var bgIcon = $('.bg_icon');
bgIcon.on('mouseover', function() {
  $(this).css({
    'border': '2px solid white',
    'box-shadow': 'white 0px 0px 20px'
  });
});
bgIcon.on('mouseout', function() {
  $(this).css({
    'border': '2px solid #FF6600',
    'box-shadow': '0 0 15px 5px rgba(204,39,11,.75)'
  });
});

var miscIcon = $('.misc_icon');
miscIcon.on('mouseover', function() {
  $(this).css({
    'border': '2px solid white',
    'box-shadow': 'white 0px 0px 20px'
  });
});
miscIcon.on('mouseout', function() {
  $(this).css({
    'border': '2px solid #0000CC',
    'box-shadow': '0 0 15px 5px rgba(0, 0, 255,.75)'
  });
});

/*var dlButton = $('.download');
dlButton.on('mouseover', function() {
  $(this).css({
    'background-color': '#26004d',
    'border': '2px solid #d9d9d9'
  });
});
dlButton.on('mouseout', function() {
  $(this).css({
    'background-color': '#3D007A',
    'border': '2px solid white'
  });
});

var dlText = $('h4');
dlText.on('mouseover', function() {
  $(this).css('color', '#d9d9d9');
});
dlText.on('mouseout', function() {
  $(this).css('color', 'white');
});*/

var dlButton = $('.download');
dlButton.on('mouseover', function() {
  $(this).css({
    'box-shadow': '0px 0px 50px white',
  });
});
dlButton.on('mouseout', function() {
  $(this).css({
    'box-shadow': 'None',
  });
});
