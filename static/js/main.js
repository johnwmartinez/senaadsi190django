/*  ---------------------------------------------------
    Template Name: Ogani
    Description:  Ogani eCommerce  HTML Template
    Author: Colorlib
    Author URI: https://colorlib.com
    Version: 1.0
    Created: Colorlib
---------------------------------------------------------  */
function number_format (number, decimals, dec_point, thousands_sep) {
    // Strip all characters but numerical ones.
    number = (number + '').replace(/[^0-9+\-Ee.]/g, '');
    var n = !isFinite(+number) ? 0 : +number,
        prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
        sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
        dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
        s = '',
        toFixedFix = function (n, prec) {
            var k = Math.pow(10, prec);
            return '' + Math.round(n * k) / k;
        };
    // Fix for IE parseFloat(0.55).toFixed(0) = 0;
    s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
    if (s[0].length > 3) {
        s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
    }
    if ((s[1] || '').length < prec) {
        s[1] = s[1] || '';
        s[1] += new Array(prec - s[1].length + 1).join('0');
    }
    return s.join(dec);
}

function convertir_EnMoneda($numero)
{
	return "$" + number_format($numero, 0, ',', '.');
}

'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");

        /*------------------
            Gallery filter
        --------------------*/
        $('.featured__controls li').on('click', function () {
            $('.featured__controls li').removeClass('active');
            $(this).addClass('active');
        });
        if ($('.featured__filter').length > 0) {
            var containerEl = document.querySelector('.featured__filter');
            var mixer = mixitup(containerEl);
        }
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    //Humberger Menu
    $(".humberger__open").on('click', function () {
        $(".humberger__menu__wrapper").addClass("show__humberger__menu__wrapper");
        $(".humberger__menu__overlay").addClass("active");
        $("body").addClass("over_hid");
    });

    $(".humberger__menu__overlay").on('click', function () {
        $(".humberger__menu__wrapper").removeClass("show__humberger__menu__wrapper");
        $(".humberger__menu__overlay").removeClass("active");
        $("body").removeClass("over_hid");
    });

    /*------------------
        Navigation
    --------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*-----------------------
        Categories Slider
    ------------------------*/
    $(".categories__slider").owlCarousel({
        loop: true,
        margin: 10,
        items: 4,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-left'><span/>", "<span class='fa fa-angle-right'><span/>"],
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {

            0: {
                items: 1,
            },

            480: {
                items: 2,
            },

            768: {
                items: 3,
            },

            992: {
                items: 4,
            }
        }
    });


    $('.hero__categories__all').on('click', function () {
        $('.hero__categories ul').slideToggle(400);
    });

    /*--------------------------
        Latest Product Slider
    ----------------------------*/
    $(".latest-product__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-left'><span/>", "<span class='fa fa-angle-right'><span/>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true
    });

    /*-----------------------------
        Product Discount Slider
    -------------------------------*/
    $(".product__discount__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 3,
        dots: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {

            320: {
                items: 1,
            },

            480: {
                items: 2,
            },

            768: {
                items: 2,
            },

            992: {
                items: 3,
            }
        }
    });

    /*---------------------------------
        Product Details Pic Slider
    ----------------------------------*/
    $(".product__details__pic__slider").owlCarousel({
        loop: true,
        margin: 20,
        items: 4,
        dots: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true
    });

    /*-----------------------
        Price Range Slider
    ------------------------ */
    var rangeSlider = $(".price-range"),
        minamount = $("#minamount"),
        maxamount = $("#maxamount"),
        minPrice = rangeSlider.data('min'),
        maxPrice = rangeSlider.data('max');
    rangeSlider.slider({
        range: true,
        min: minPrice,
        max: maxPrice,
        values: [minPrice, maxPrice],
        slide: function (event, ui) {
            minamount.val('$' + ui.values[0]);
            maxamount.val('$' + ui.values[1]);
        }
    });
    minamount.val('$' + rangeSlider.slider("values", 0));
    maxamount.val('$' + rangeSlider.slider("values", 1));

    /*--------------------------
        Select
    ----------------------------*/
    $("select").niceSelect();

    /*------------------
        Single Product
    --------------------*/
    $('.product__details__pic__slider img').on('click', function () {

        var imgurl = $(this).data('imgbigurl');
        var bigImg = $('.product__details__pic__item--large').attr('src');
        if (imgurl != bigImg) {
            $('.product__details__pic__item--large').attr({
                src: imgurl
            });
        }
    });

    /*-------------------
        Quantity change
    --------------------- */
    var proQty = $('.pro-qty');
    proQty.prepend('<span class="dec qtybtn">-</span>');
    proQty.append('<span class="inc qtybtn">+</span>');
    proQty.on('click', '.qtybtn', function () {
        var $button = $(this);
        var oldValue = $button.parent().find('input').val();
        if ($button.hasClass('inc')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below zero
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        $button.parent().find('input').val(newVal);
    });

    /* Funcióna agregar al carrito  */
    // add_carrito_btn
    $(document).on('click', '#add_carrito_btn', function (event) {
        event.preventDefault()
        var _vm = $(this)
        var _qty = $("#product-qty").val()
        var _productId = $(".product-id").val()
        var _productTitle = $(".product-title").val()
        var _productPrice = $(".product-price").val()
        //console.log(_qty, _productId, _productTitle, _productPrice)
        // AJAX
        $.ajax({
            url: '/agregarAcarrito',
            data: {
                'id': _productId,
                'qty': _qty,
                'title': _productTitle,
                'price': _productPrice,
            },
            dataType: 'json',
            beforeSend: function () {
                _vm.attr('disabled', true)
            },
            success: function (res) {
                var unidades = 'unidad'
                if (_qty > 1) {
                    unidades = 'unidades'
                }

                console.log(res)
                $(".cart-qty").text(res.totalitems)
                $(".total_superior").text(convertir_EnMoneda(res.cart_total))

                _vm.attr('disabled', false)

                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: `Has agregado ${_qty} ${unidades} del producto ${_productTitle} al carrito.`,
                    showConfirmButton: false,
                    timer: 2500
                })

            }
        });
        // Termina AJAX
    })

    $(document).on('click', '.add_car_indv', function (event) {
        event.preventDefault()
        var _vm = $(this)
        var _qty = 1
        var _productId = _vm.attr("data-id")
        var _productTitle = $(this).parent().parent().parent().parent().find(".product__item__text h6 a").text()
        var _productPrice = $(this).parent().parent().parent().parent().find(".product__item__text .indv_precio").val()
        
        //console.log(_qty, _productId, _productTitle, _productPrice)
        // AJAX
        $.ajax({
            url: '/agregarAcarrito',
            data: {
                'id': _productId,
                'qty': _qty,
                'title': _productTitle,
                'price': _productPrice,
            },
            dataType: 'json',
            beforeSend: function () {
                _vm.attr('disabled', true)
            },
            success: function (res) {
                var unidades = 'unidad'
                if (_qty > 1) {
                    unidades = 'unidades'
                }

                console.log(res)
                $(".cart-qty").text(res.totalitems)
                $(".total_superior").text(convertir_EnMoneda(res.cart_total))

                _vm.attr('disabled', false)

                Swal.fire({
                    position: 'top-end',
                    icon: 'success',
                    title: `Producto agregado al carrito de forma satisfactoria`,
                    showConfirmButton: false,
                    timer: 2500
                })

            }
        });
        /*
        */
        // Termina AJAX
    })

    $(document).on('click', '.eliminarIndvCarrito', function (event) {
        event.preventDefault()
        var _vm = $(this).parent().parent()
        var _productoId = _vm.attr('data-id')

        Swal.fire({
            title: '¿Estás seguro que deseas eliminar este producto?',
            showDenyButton: true,
            confirmButtonText: 'Eliminar',
            denyButtonText: `Cancelar`,
        }).then((result) => {
            /* Read more about isConfirmed, isDenied below */
            if (result.isConfirmed) {

                // AJAX
                $.ajax({
                    url:'/eliminarCarritoIndv',
                    data:{
                        'id':_productoId,
                    },
                    dataType:'json',
                    beforeSend:function(){
                        _vm.attr('disabled', true)
                    },
                    success:function(res){
                        console.log(res)
                        $(".cart-qty").text(res.totalitems)
                        $(".total_superior").text(convertir_EnMoneda(res.cart_total))
                        $(".carrito_total").text(convertir_EnMoneda(res.cart_total))
                        _vm.remove() // Eliminamos la fila del carrito
                        Swal.fire('El producto ha sido eliminaro del carrito', '', 'info')

                    }
                });

                // Termina AJAX
            } else if (result.isDenied) {
                //Swal.fire('Changes are not saved', '', 'info')
            }
        })
        
    })

    $(document).on('click', '.actualizar_carrito', function( event ){
        event.preventDefault()
        var data = {}
        var _vm = $('.carrito_global tbody tr')
        
        $.each( _vm, function( key, value ) {
            var ObjIndv = $(value)
            // AJAX por cada uno
            
            $.ajax({
                url: '/actualizarElCarrito',
                method: "POST",
                data: {
                    'qty' : ObjIndv.find('.pro-qty input').val(),
                    'productId' : ObjIndv.attr("data-id"),
                    'nombre' : ObjIndv.find('.shoping__cart__item h5').text(),
                    'precio' : ObjIndv.find('.shoping__cart__price .precio').val(),
                },
                dataType: 'json',
                beforeSend: function () {
                    // _vm.attr('disabled', true)
                },
                success: function (res) {
                    console.log(res)
                    // $(".cart-qty").text(res.totalitems)
                    // $(".total_superior").text(convertir_EnMoneda(res.cart_total))
    
                    // _vm.attr('disabled', false)
    
                    // Swal.fire({
                    //     position: 'top-end',
                    //     icon: 'success',
                    //     title: `El carrito se ha actualizado de forma correcta`,
                    //     showConfirmButton: false,
                    //     timer: 2500
                    // })
    
                }
            });

        });

        
    })


    // var _qty = 1
    // var _productId = _vm.attr("data-id")
    // var _productTitle = $(this).parent().parent().parent().parent().find(".product__item__text h6 a").text()
    // var _productPrice = $(this).parent().parent().parent().parent().find(".product__item__text .indv_precio").val()



})(jQuery);