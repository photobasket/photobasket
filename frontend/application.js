$(document).ready(function () {
    var path = document.location.pathname;
    $.ajax({url: "/rest" + path}).done(function(data) {
        for (var i = 0; i < data.images.length; i++) {
            $('#thumbnails').append('<div class="col-xs-3 image"><img data-image-id="' +
                                    i+ '" src="' +
                                    data.images[i].thumb320 + '"></div>');
            $('#fullscreen-images').append('<div class="item"><img data-image-id="' + i + '" src="' +
                                           data.images[i].url + '"></div>');
        }
        $('.image img').click(function(evt) {
            var image_id = $(evt.target).data('image-id');
            $('#fullscreen-images .item img').each(function (index, img) {
                var $img = $(img);
                if ($img.data('image-id') == image_id) {
                    $img.parent().addClass('active');
                } else {
                    $img.parent().removeClass('active');
                }
            });
            $('#myModal').modal();
        });
    });
    var source = $('thumbnail-template').html();
    $('.carousel').carousel({interval: false});
});
