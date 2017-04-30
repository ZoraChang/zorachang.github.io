var tooltip = document.querySelector('.map-tooltip');

// iterate throw all `path` tags
[].forEach.call(document.querySelectorAll('path'), function(item) {
	// attach click event, you can read the URL from a attribute for example.
//  item.addEventListener('click', function(){
 //   window.open('http://google.co.il')
 // });

  // attach mouseenter event
  item.addEventListener('mouseenter', function() {
    tooltip.innerHTML = item.getAttribute('id');
    tooltip.style.display = 'block';
  });

  item.addEventListener('mousemove', function(e) {
  	tooltip.style.top = e.clientY + 'px';
    tooltip.style.left = e.clientX + 'px';
  });

  // when mouse leave hide the tooltip
  item.addEventListener('mouseleave', function(){
  	tooltip.style.display = 'none';
  });
});
