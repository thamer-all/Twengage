jQuery(document).ready(function() {
jQuery('.faq-acc .btn-info').addClass('collapsed');
  jQuery('.faq-acc .btn-info').click(function(){
    jQuery(this).parent().toggleClass('shadow-acc');
  });
  jQuery('.tg-ul div').click(function(){
    jQuery('.tg-ul div').removeClass('active');
    jQuery(this).addClass('active');
  });
});

