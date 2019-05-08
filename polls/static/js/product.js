
$(document).ready(function(){
    $('#demo-simpleLens-gallery .simpleLens-thumbnails-container img').simpleGallery({
        loading_image: 'img/loader.gif'
    });
    $('#demo-simpleLens-gallery .simpleLens-big-image').simpleLens({
        loading_image: 'img/loader.gif'
    });

    //Add your review
    function addReview() {
      var $ = jQuery;
      
      $('a[href="#reviews"].add-review').click(function(){
        $('.tabs #tab3').trigger('click');
        $('html, body').animate({
          scrollTop: $("#tab3").offset().top - 186
        }, 1000);
      });
    }

    addReview();

});

//Removing # tag
( function( $ ) {
   $( 'a[href="#reviews"]' ).click( function(e) {
      e.preventDefault();
   } );
} )( jQuery );


//Product Display
<!--
function display(view) {
    if (view == 'list') {
        $('.product-grid').attr('class', 'product-list');
        $('.products-block  .product-block').each(function(index, element) {
            $(element).parent().addClass("col-fullwidth");
        });     
        $('.display').html('<span><b>Display:</b></span><a class="btn-small btn-pad" onclick="display(\'grid\');"><i class="fa fa-th"></i></a><a class="list btn-small btn-color btn-pad active"><i class="fa fa-th-list"></i></a>');
        $.totalStorage('display', 'list'); 
    } else {
        $('.product-list').attr('class', 'product-grid');
        $('.products-block  .product-block').each(function(index, element) {
            $(element).parent().removeClass("col-fullwidth");  
        }); 
        $('.display').html('<span><b>Display:</b></span><a class="btn-small btn-color btn-pad active"><i class="fa fa-th"></i></a><a class="list btn-small btn-pad" onclick="display(\'list\');"><i class="fa fa-th-list"></i></a>');
        $.totalStorage('display', 'grid');
    }
}

view = $.totalStorage('display');
if (view) {
    display(view);
} else {
    display('grid');
}
//-->