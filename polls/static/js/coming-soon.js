jQuery(document).ready(function () {

    jQuery('body').css('overflowY','hidden');
        jQuery.waitForImages.hasImgProperties = ['background','backgroundImage'];
        jQuery('body').waitForImages(function() {
        // All descendant images have loaded, now slide up.
//                        alert("done");
        jQuery(".page-mask").fadeOut(500);
        jQuery('body').css('overflowY','auto');
    });

        

	$(function () {
		var austDay = new Date();
		austDay = new Date(austDay.getFullYear() + 1, 1 - 1, 30);
		$('#defaultCountdown').countdown({until: austDay});
		$('#year').text(austDay.getFullYear());
	});

});
