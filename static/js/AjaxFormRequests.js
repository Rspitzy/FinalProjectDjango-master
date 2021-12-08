
$(document).ready(function () {
    console.log('hello');
});

// $('.submit').on("click", function () {
//     alert('working')
//     var form = $(this).closest('form');
//     console.log('hello')
//     $.ajax({
//         type: 'POST',
//         url: '/add/',
//         data: {
//             product_name: $(this).closest('#product_name')
//         },
//         success: function () {
//
//         }
//     });
// });

// $.each($('.post-form'))
// $(".button_test").click( function() {
//     //alert("triggered by " + $(this).prop("id"));
//     //classList
//     alert("triggered by " + $(this).parent(".product").prop("classList"));
//     $(this).parent(".product").css("background","yellow");
// })

$(".button_test").click( function(e) {
    e.preventDefault();
    index = $(this).prop("id");
    // console.log($('#product_name_'+ index).text())
    // console.log($('#product_price_' + index).text())
    // console.log($('#product_url_' + index).prop("href"))
    // console.log($('#product_img_' + index).prop("src"))
    // console.log($('#product_price_point_' + index).val())
    // console.log($('#product_alert_' + index).prop("checked"))

    $.ajax({
        type: 'POST',
        url: '/add/',
        data: {
            product_name: $('#product_name_'+ index).text(),
            price: $('#product_price_' + index).text(),
            price_point:$('#product_price_point_' + index).val(),
            alert:$('#product_alert_' + index).prop("checked"),
            product_url:$('#product_url_' + index).prop("href"),
            product_img:$('#product_img_' + index).prop("src"),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (){

        }
    });
});


//$(document).on('submit','#post-form', function(e){
   //e.preventDefault();
   // $.ajax({
   //     type: 'POST',
   //     url:'add/',
   //     data: {
   //        product_name: $(this).closest('#name').value
   //     }
   // })
//});