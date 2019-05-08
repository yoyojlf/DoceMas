//Gallaxy v1.3.0
jQuery(document).ready(function () {

    jQuery('body').css('overflowY','hidden');
        jQuery.waitForImages.hasImgProperties = ['background','backgroundImage'];
        jQuery('body').waitForImages(function() {
        // All descendant images have loaded, now slide up.
//                        alert("done");
        jQuery(".page-mask").fadeOut(500);
        jQuery('body').css('overflowY','auto');
    });


/*-------------------------------------------------*/
/* =  Animated content
/*-------------------------------------------------*/

    wow = new WOW(
        {
            animateClass: 'animated',
            offset:       100
        }
    );

    wow.init();

/* ==============================================
    Fit Videos
=============================================== */
    jQuery(window).load(function(){
        'use strict';
         jQuery(".fit-vids").fitVids();
    });




/*----------------------------------------------------*/
/*  Animated Knob
/*----------------------------------------------------*/

    jQuery('.circular-knob').each(function () {
        jQuery(this).fappear(function() {
            $('.knob').knob();
            $({
              value: 0
            }).animate({
              value: 75
            }, {
              duration: 2000,
              easing: 'swing',
              step: function() {
                return $('.knob').val(Math.ceil(this.value)).trigger('change');
              }
            });
            return setTimeout(function() {
              return $('.knob').attr('data-fgColor', 'red').trigger('change');
            }, 1000);
        }); 
    });


/*----------------------------------------------------*/
/*  Animated Progress Bars
/*----------------------------------------------------*/

    jQuery('.skillbar').each(function(){
        jQuery(this).fappear(function() {
            jQuery(this).find('.skillbar-bar').animate({
                width:jQuery(this).attr('data-percent')
            },5000);
        });
    });


/*----------------------------------------------------*/
/*  Animated Count To
/*----------------------------------------------------*/

    jQuery('#random-facts .random-box').each(function () {
        jQuery(this).fappear(function() {
            jQuery('.facts').countTo();
        }); 
    });



/*----------------------------------------------------*/
/*	Keyframe animations enable
/*----------------------------------------------------*/

jQuery().waypoint && jQuery("body").imagesLoaded(function () {
        jQuery(".animate_afc, .animate_afl, .animate_afr, .animate_aft, .animate_afb, .animate_wfc, .animate_hfc, .animate_rfc, .animate_rfl, .animate_rfr").waypoint(function () {
            if (!jQuery(this).hasClass("animate_start")) {
                var e = jQuery(this);
                setTimeout(function () {
                    e.addClass("animate_start")
                }, 20)
            }
        }, {
            offset: "85%",
            triggerOnce: !0
        })
    });



/*----------------------------------------------------*/
/*	Flickr Feed
/*----------------------------------------------------*/

$('ul#flickrfeed').jflickrfeed({
		limit: 6,
		qstrings: {
			id: '71865026@N00'
		},
		itemTemplate: '<li>'+
						'<a rel="prettyPhoto[pp_gal]" href="{{image}}">' +
							'<img src="{{image_s}}" alt="{{title}}" />' +
						'</a>' +
					  '</li>'
	}, function(data) {
		$('a[rel^="prettyPhoto"]').prettyPhoto();
	});


	
/*----------------------------------------------------*/
/*	Superfish Mainmenu Section
/*----------------------------------------------------*/
	
    jQuery(function () {
        jQuery('ul.sf-menu').stop().superfish();
    });
	


/*----------------------------------------------------*/
/*	Revolution Slider Nav Arrow Show Hide
/*----------------------------------------------------*/

    jQuery('.fullwidthbanner-container').hover(function () {
        jQuery('.tp-leftarrow').stop().animate({
            "opacity": 1
        }, 'easeIn');
        jQuery('.tp-rightarrow').stop().animate({
            "opacity": 1
        }, 'easeIn');
    }, function () {
        jQuery('.tp-leftarrow').stop().animate({
            "opacity": 0
        }, 'easeIn');
        jQuery('.tp-rightarrow').stop().animate({
            "opacity": 0
        }, 'easeIn');
    }

    );
	




/*----------------------------------------------------*/
/*	Accordion Section
/*----------------------------------------------------*/

    jQuery('.accordionMod').each(function (index) {
        var thisBox = jQuery(this).children(),
            thisMainIndex = index + 1;
        jQuery(this).attr('id', 'accordion' + thisMainIndex);
        thisBox.each(function (i) {
            var thisIndex = i + 1,
                thisParentIndex = thisMainIndex,
                thisMain = jQuery(this).parent().attr('id'),
                thisTriggers = jQuery(this).find('.accordion-toggle'),
                thisBoxes = jQuery(this).find('.accordion-inner');
            jQuery(this).addClass('panel');
            thisBoxes.wrap('<div id=\"collapseBox' + thisParentIndex + '_' + thisIndex + '\" class=\"panel-collapse collapse\" />');
            thisTriggers.wrap('<div class=\"panel-heading\" />');
            thisTriggers.attr('data-toggle', 'collapse').attr('data-parent', '#' + thisMain).attr('data-target', '#collapseBox' + thisParentIndex + '_' + thisIndex);
        });
        jQuery('.accordion-toggle').prepend('<span class=\"icon\" />');
		jQuery("div.accordion-item:first-child .accordion-toggle").addClass("current");
		jQuery("div.accordion-item:first-child .icon").addClass("iconActive");
		jQuery("div.accordion-item:first-child .panel-collapse").addClass("in");
        jQuery('.accordionMod .accordion-toggle').click(function () {
            if (jQuery(this).parent().parent().find('.panel-collapse').is('.in')) {
                jQuery(this).removeClass('current');
                jQuery(this).find('.icon').removeClass('iconActive');
            } else {
                jQuery(this).addClass('current');
                jQuery(this).find('.icon').addClass('iconActive');
            }
            jQuery(this).parent().parent().siblings().find('.accordion-toggle').removeClass('current');
            jQuery(this).parent().parent().siblings().find('.accordion-toggle > .icon').removeClass('iconActive');
        });
    });


 

});

$('.bxslider').bxSlider({
  pagerCustom: '#bx-pager',
  control: true,
  nextText: '<i class="fa fa-angle-right"></i>',
  prevText: '<i class="fa fa-angle-left"></i>'
});

/*----------------------------------------------------*/
/*	Revolution Slider Triggering
/*----------------------------------------------------*/

jQuery(document).ready(function() {
                
                    
                                
                    jQuery('.fullwidthbanner').show().revolution(
                    {
                        dottedOverlay:"none",
                        delay: 9000,
                        startwidth: 1170,
                        startheight: 470,
                        hideThumbs:200,
                        
                        thumbWidth:100,
                        thumbHeight:50,
                        thumbAmount:5,
                        
                        navigationType:"bullet",
                        navigationArrows:"solo",
                        navigationStyle:"preview2",
                        
                        touchenabled:"on",
                        onHoverStop:"on",
                        
                        swipe_velocity: 0.7,
                        swipe_min_touches: 1,
                        swipe_max_touches: 1,
                        drag_block_vertical: false,
                                                
                        parallax:"mouse",
                        parallaxBgFreeze:"on",
                        parallaxLevels:[7,4,3,2,5,4,3,2,1,0],
                                                
                        keyboardNavigation:"off",
                        
                        navigationHAlign:"center",
                        navigationVAlign:"bottom",
                        navigationHOffset:0,
                        navigationVOffset:20,

                        soloArrowLeftHalign:"left",
                        soloArrowLeftValign:"center",
                        soloArrowLeftHOffset:20,
                        soloArrowLeftVOffset:0,

                        soloArrowRightHalign:"right",
                        soloArrowRightValign:"center",
                        soloArrowRightHOffset:20,
                        soloArrowRightVOffset:0,
                                
                        shadow:0,
                        fullWidth:"on",
                        fullScreen:"off",

                        spinner:"spinner4",
                        
                        stopLoop:"off",
                        stopAfterLoops:-1,
                        stopAtSlide:-1,

                        shuffle:"off",
                        
                        autoHeight:"off",                       
                        forceFullWidth:"off",                       
                                                
                                                
                                                
                        hideThumbsOnMobile:"off",
                        hideNavDelayOnMobile:1500,                      
                        hideBulletsOnMobile:"off",
                        hideArrowsOnMobile:"off",
                        hideThumbsUnderResolution:0,
                        
                        hideSliderAtLimit:0,
                        hideCaptionAtLimit:0,
                        hideAllCaptionAtLilmit:0,
                        startWithSlide:0,
                        videoJsPath:"js/revolution-slider/videojs/",
                        fullScreenOffsetContainer: ""   
                    });
                    
                    
                    
                                    
                }); //ready
                







/*----------------------------------------------------*/
/*	Carousel Section
/*----------------------------------------------------*/

	// jQuery('.portfolio-carousel').carousel({interval: false, wrap: false});
	// jQuery('.product-carousel').carousel({interval: false, wrap: false});
    // jQuery('.product-zoom-carousel').carousel({interval: false, wrap: false});  
	// jQuery('.client-carousel').carousel({interval: false, wrap: false});
	// jQuery('.testimonials-carousel').carousel({interval: 5000, pause: "hover"});



$(document).ready(function(){
		$("a[rel^='prettyPhoto']").prettyPhoto({
			animation_speed: 'fast', /* fast/slow/normal */
			slideshow: 5000, /* false OR interval time in ms */
			autoplay_slideshow: false, /* true/false */
			opacity: 0.80, /* Value between 0 and 1 */
			show_title: true, /* true/false */
			allow_resize: true, /* Resize the photos bigger than viewport. true/false */
			default_width: 500,
			default_height: 344,
			counter_separator_label: '/', /* The separator for the gallery counter 1 "of" 2 */
			theme: 'pp_default', /* light_rounded / dark_rounded / light_square / dark_square / facebook */
			horizontal_padding: 20, /* The padding on each side of the picture */
			hideflash: false, /* Hides all the flash object on a page, set to TRUE if flash appears over prettyPhoto */
			wmode: 'opaque', /* Set the flash wmode attribute */
			autoplay: true, /* Automatically start videos: True/False */
			modal: false, /* If set to true, only the close button will close the window */
			deeplinking: true, /* Allow prettyPhoto to update the url to enable deeplinking. */
			overlay_gallery: true, /* If set to true, a gallery will overlay the fullscreen image on mouse over */
			keyboard_shortcuts: true, /* Set to false if you open forms inside prettyPhoto */
			changepicturecallback: function(){}, /* Called everytime an item is shown/changed */
			callback: function(){}, /* Called when prettyPhoto is closed */
			ie6_fallback: true,
			markup: '<div class="pp_pic_holder"> \
						<div class="ppt">&nbsp;</div> \
						<div class="pp_top"> \
							<div class="pp_left"></div> \
							<div class="pp_middle"></div> \
							<div class="pp_right"></div> \
						</div> \
						<div class="pp_content_container"> \
							<div class="pp_left"> \
							<div class="pp_right"> \
								<div class="pp_content"> \
									<div class="pp_loaderIcon"></div> \
									<div class="pp_fade"> \
										<a href="#" class="pp_expand" title="Expand the image">Expand</a> \
										<div class="pp_hoverContainer"> \
											<a class="pp_next" href="#">next</a> \
											<a class="pp_previous" href="#">previous</a> \
										</div> \
										<div id="pp_full_res"></div> \
										<div class="pp_details"> \
											<div class="pp_nav"> \
												<a href="#" class="pp_arrow_previous">Previous</a> \
												<p class="currentTextHolder">0/0</p> \
												<a href="#" class="pp_arrow_next">Next</a> \
											</div> \
											<p class="pp_description"></p> \
											{pp_social} \
											<a class="pp_close" href="#">Close</a> \
										</div> \
									</div> \
								</div> \
							</div> \
							</div> \
						</div> \
						<div class="pp_bottom"> \
							<div class="pp_left"></div> \
							<div class="pp_middle"></div> \
							<div class="pp_right"></div> \
						</div> \
					</div> \
					<div class="pp_overlay"></div>',
			gallery_markup: '<div class="pp_gallery"> \
								<a href="#" class="pp_arrow_previous">Previous</a> \
								<div> \
									<ul> \
										{gallery} \
									</ul> \
								</div> \
								<a href="#" class="pp_arrow_next">Next</a> \
							</div>',
			image_markup: '<img id="fullResImage" src="{path}" />',
			flash_markup: '<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" width="{width}" height="{height}"><param name="wmode" value="{wmode}" /><param name="allowfullscreen" value="true" /><param name="allowscriptaccess" value="always" /><param name="movie" value="{path}" /><embed src="{path}" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="{width}" height="{height}" wmode="{wmode}"></embed></object>',
			quicktime_markup: '<object classid="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B" codebase="http://www.apple.com/qtactivex/qtplugin.cab" height="{height}" width="{width}"><param name="src" value="{path}"><param name="autoplay" value="{autoplay}"><param name="type" value="video/quicktime"><embed src="{path}" height="{height}" width="{width}" autoplay="{autoplay}" type="video/quicktime" pluginspage="http://www.apple.com/quicktime/download/"></embed></object>',
			iframe_markup: '<iframe src ="{path}" width="{width}" height="{height}" frameborder="no"></iframe>',
			inline_markup: '<div class="pp_inline">{content}</div>',
			custom_markup: '',
			social_tools: '<div class="pp_social"><div class="twitter"><a href="http://twitter.com/share" class="twitter-share-button" data-count="none">Tweet</a><script type="text/javascript" src="http://platform.twitter.com/widgets.js"></script></div><div class="facebook"><iframe src="http://www.facebook.com/plugins/like.php?locale=en_US&href='+location.href+'&amp;layout=button_count&amp;show_faces=true&amp;width=500&amp;action=like&amp;font&amp;colorscheme=light&amp;height=23" scrolling="no" frameborder="0" style="border:none; overflow:hidden; width:500px; height:23px;" allowTransparency="true"></iframe></div></div>' /* html or false to disable */
		});
	});





/*----------------------------------------------------*/
/*	Hover Overlay
/*----------------------------------------------------*/

jQuery(document).ready(function () {
	
	


	jQuery('.portfolio-item').hover(function () {
			jQuery(this).find( '.portfolio-item-hover' ).animate({
				"opacity": 0.8
			}, 100, 'easeInOutCubic');
			
			
		}, function () {
			jQuery(this).find( '.portfolio-item-hover' ).animate({
				"opacity": 0
			}, 100, 'easeInOutCubic');
			
	});
	
	
	jQuery('.portfolio-item').hover(function () {
       jQuery(this).find(".fullscreen").stop().animate({'top' : '60%', 'opacity' : 1}, 250, 'easeOutBack');
        
    }, function () {
        jQuery(this).find(".fullscreen").stop().animate({'top' : '65%', 'opacity' : 0}, 150, 'easeOutBack');
        
    });
	
	
	jQuery('.blog-showcase ul li').each(function () {
		jQuery(this).on('hover', function () {
			jQuery(this).siblings('li').removeClass('blog-first-el').end().addClass('blog-first-el');
		});
	});
	
	
	jQuery('.blog-showcase-thumb').hover(function () {
        jQuery(this).find( '.post-item-hover' ).animate({
            "opacity": 0.8
        }, 100, 'easeInOutCubic');
        
    }, function () {
        jQuery(this).find( '.post-item-hover' ).animate({
            "opacity": 0
        }, 100, 'easeInOutCubic');
        
    });
	

	
	jQuery('.blog-showcase-thumb').hover(function () {
       jQuery(this).find(".fullscreen").stop().animate({'top' : '57%', 'opacity' : 1}, 250, 'easeOutBack');
        
    }, function () {
        jQuery(this).find(".fullscreen").stop().animate({'top' : '65%', 'opacity' : 0}, 150, 'easeOutBack');
        
    });



/* Post Image overlay */	
	
	jQuery('.post-image').hover(function () {
        jQuery(this).find( '.img-hover' ).animate({
            "opacity": 0.8
        }, 100, 'easeInOutCubic');
		
        
    }, function () {
        jQuery(this).find( '.img-hover' ).animate({
            "opacity": 0
        }, 100, 'easeInOutCubic');
        
    });
	
	
	jQuery('.post-image').hover(function () {
       jQuery(this).find(".fullscreen").stop().animate({'top' : '55%', 'opacity' : 1}, 250, 'easeOutBack');
        
    }, function () {
        jQuery(this).find(".fullscreen").stop().animate({'top' : '65%', 'opacity' : 0}, 150, 'easeOutBack');
        
    });
	

/*Mobile device topnav opener*/
	
	jQuery( ".down-button" ).click(function() {
    jQuery( ".down-button .icon-current" ).toggleClass("fa fa-angle-up fa fa-angle-down");
});



/*----------------------------------------------------*/
/*	Parallax section
/*----------------------------------------------------*/
    jQuery('.product-lead').parallax("50%", 0.1);
    jQuery('#services').parallax("50%", 0.1);
	jQuery('.our-clients').parallax("50%", 0.1);
	jQuery('.service-reasons').parallax("50%", 0.1);

	jQuery("a[data-rel^='prettyPhoto']").prettyPhoto({overlay_gallery: false});
	
	

/*----------------------------------------------------*/
/*	Tootltip Initialize
/*----------------------------------------------------*/



    jQuery("[data-toggle='tooltip']").tooltip();

});




/*----------------------------------------------------*/
/*	Sticky Menu
/*----------------------------------------------------*/

	jQuery(document).ready(function(){
		jQuery(".main-header").sticky({topSpacing:0});
	});



/*----------------------------------------------------*/
/*	Scroll To Top Section
/*----------------------------------------------------*/
	jQuery(document).ready(function () {
	
		jQuery(window).scroll(function () {
			if (jQuery(this).scrollTop() > 100) {
				jQuery('.scrollup').fadeIn();
			} else {
				jQuery('.scrollup').fadeOut();
			}
		});
	
		jQuery('.scrollup').click(function () {
			jQuery("html, body").animate({
				scrollTop: 0
			}, 600);
			return false;
		});
	
	});



/*----------------------------------------------------*/
/*	Twitter Section
/*----------------------------------------------------*/

	jQuery('#tweets').tweetMachine('', {
		backendScript:  'http://demo.fifothemes.com/pixma/ajax/getFromTwitter.php',
		endpoint: 'statuses/user_timeline',
		user_name: 'FIFOThemes',
		include_retweets: true,
		exclude_replies: false,
		limit: 1,
		autoRefresh: false
	});





/*----------------------------------------------------*/
/*	Tabs Control Section
/*----------------------------------------------------*/


	jQuery("#horizontal-tabs").tytabs({
		tabinit: "1",
		fadespeed: "fast"
	});
	jQuery("#horizontal-tabs.two").tytabs({
		tabinit: "1",
		prefixtabs: "tab_two",
		prefixcontent: "content_two",
		fadespeed: "fast"
	});
	jQuery("#horizontal-tabs.three").tytabs({
		tabinit: "1",
		prefixtabs: "tab_three",
		prefixcontent: "content_three",
		fadespeed: "fast"
	});
	jQuery("#horizontal-tabs.four").tytabs({
		tabinit: "1",
		prefixtabs: "tab_four",
		prefixcontent: "content_four",
		fadespeed: "fast"
	});
	jQuery("#horizontal-tabs.five").tytabs({
		tabinit: "1",
		prefixtabs: "tab_five",
		prefixcontent: "content_five",
		fadespeed: "fast"
	});
	jQuery("#vertical-tabs").tytabs({
		tabinit: "1",
		prefixtabs: "tab_v",
		prefixcontent: "content_v",
		fadespeed: "fast"
	});
	jQuery("#vertical-tabs.two").tytabs({
		tabinit: "1",
		prefixtabs: "tab_v_two",
		prefixcontent: "content_v_two",
		fadespeed: "fast"
	});
	jQuery("#vertical-tabs.three").tytabs({
		tabinit: "1",
		prefixtabs: "tab_v_three",
		prefixcontent: "content_v_three",
		fadespeed: "fast"
	});
	jQuery("#vertical-tabs.four").tytabs({
		tabinit: "1",
		prefixtabs: "tab_v_four",
		prefixcontent: "content_v_four",
		fadespeed: "fast"
	});
	jQuery("#vertical-tabs.five").tytabs({
		tabinit: "1",
		prefixtabs: "tab_v_five",
		prefixcontent: "content_v_five",
		fadespeed: "fast"
	});
	jQuery(".hideit").click(function () {
		e(this).fadeOut(600)
	});
	jQuery("#toggle-view li h4").click(function () {
		var t = e(this).siblings("div.panel");
		if (t.is(":hidden")) {
			t.slideDown("200");
			e(this).siblings("span").html("-")
		} else {
			t.slideUp("200");
			e(this).siblings("span").html("+")
		}
	});
	
	jQuery(function (jQuery) {
		jQuery("#example").popover();
		jQuery("#example_left").popover({
			placement: 'left'
		});
		jQuery("#example_top").popover({
			placement: 'top'
		});
		jQuery("#example_bottom").popover({
			placement: 'bottom'
		});
	}); 



	/*----------------------------------------------------*/
	/*	Jquery Google map Section
	/*----------------------------------------------------*/

	//Google map
	jQuery('#maps').gMap({
		address: "221 Baker Street, London, United Kingdom",
		zoom: 16,
		markers: [{
			latitude: 51.523254,
			longitude: -0.158026,
			html: "<h4>FIFO Themes</h4>Wordpress, HTML5/CSS Themes",
			popup: true
		}]
	});



	/*----------------------------------------------------*/
	/*	Contact Form Section
	/*----------------------------------------------------*/
$("#contact").submit(function (e) {
    e.preventDefault();
    var name = $("#name").val();
    var email = $("#email").val();
	var subject = $("#subject").val();
    var text = $("#text").val();
    var dataString = 'name=' + name + '&email=' + email + '&subject=' + subject + '&text=' + text;
	

    function isValidEmail(emailAddress) {
        var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
        return pattern.test(emailAddress);
    };

    if (isValidEmail(email) && (text.length > 100) && (name.length > 1)) {
        $.ajax({
            type: "POST",
            url: "ajax/process.php",
            data: dataString,
            success: function () {
                $('.success').fadeIn(1000).delay(3000).fadeOut(1000);
                $('#contact')[0].reset();
            }
        });
    } else {
        $('.error').fadeIn(1000).delay(5000).fadeOut(1000);

    }

    return false;
});
