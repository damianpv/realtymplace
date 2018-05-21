var status_url = api_url+"/api/v1.0/status/";
var country_url = api_url+"/api/v1.0/country/";
var state_url = api_url+"/api/v1.0/state/";
var type_url = api_url+"/api/v1.0/type/";
var basic_url = api_url+"/api/v1.0/property-basic/";

$(document).ready(function($) {

	/* Status */
    $.getJSON(status_url, function(data){
        $select_status = '';
        $.each(data, function (dt, status){
            $select_status = '<option value="' + status.id + '">' + status.title + '</option>';
            $('#property_status').append($select_status);
        });
    });
    /* Country */
    $.getJSON(country_url, function(data){
        $select_country = '';
        $.each(data, function (dt, country){
            $select_country = '<option value="' + country.id_country + '">' + country.country + '</option>';
            $('#property_country').append($select_country);
        });
    });
    /* State */
    $.getJSON(state_url, function(data){
        $select_state = '';
        $.each(data, function (dt, state){
            $select_state = '<option value="' + state.id_state + '">' + state.state + '</option>';
            $('#property_state').append($select_state);
        });
    });
    /* Type */
    $.getJSON(type_url, function(data){
        $select_type = '';
        $.each(data, function (dt, type){
            $select_type = '<option value="' + type.id + '">' + type.title + '</option>';
            $('#property_type').append($select_type);
        });
    });
    /* Basic */
    $.getJSON(basic_url, function(data){
        $select_type = '';
        $.each(data, function (dt, basic){
            thumbnailsPerRow = 10;

            $('.footer-thumbnails').append("<div class='property-thumbnail'><a href='" + basic.title + "'><img src="  + basic.title + "></a></div>");
            var $thumbnail = $('.footer-thumbnails .property-thumbnail');
            $thumbnail.css('width', 100/thumbnailsPerRow + '%');
        });
    });


});
