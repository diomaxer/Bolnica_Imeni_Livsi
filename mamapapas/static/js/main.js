$(document).ready(function(){
    $('.menu-top-mobile-open').click(function(){
        $('.menu-main-mobile').removeClass('inactive');
        $('.menu-main-mobile').toggleClass('active');
        $('.menu-top-mobile-open').removeClass('active');
        $('.menu-top-mobile-open').toggleClass('inactive');
        $('.menu-top-mobile-close').removeClass('inactive');
        $('.menu-top-mobile-close').toggleClass('active');
    })
    $('.menu-top-mobile-close').click(function(){
        $('.menu-main-mobile').removeClass('active');
        $('.menu-main-mobile').toggleClass('inactive');
        $('.menu-top-mobile-close').removeClass('active');
        $('.menu-top-mobile-close').toggleClass('inactive');
        $('.menu-top-mobile-open').removeClass('inactive');
        $('.menu-top-mobile-open').toggleClass('active');
    })
});


$(document).ready(function(){
    $('.show').click(function(){
        $('.menu-mobile-wrapper').toggleClass('active');
        $('.menu-mobile-nav').toggleClass('active');
    });
    $('.close, .menu-mobile-wrapper').click(function(){
        $('.menu-mobile-wrapper').toggleClass('active');
        $('.menu-mobile-nav').toggleClass('active');
    });
});

$(document).ready(function(){
    $('.is-locked').click(function(){
        $('.is-locked').toggleClass('is-locked-style');
    })
});