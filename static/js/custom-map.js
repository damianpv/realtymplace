var mapStyles = [{featureType:'water',elementType:'all',stylers:[{hue:'#d7ebef'},{saturation:-5},{lightness:54},{visibility:'on'}]},{featureType:'landscape',elementType:'all',stylers:[{hue:'#eceae6'},{saturation:-49},{lightness:22},{visibility:'on'}]},{featureType:'poi.park',elementType:'all',stylers:[{hue:'#dddbd7'},{saturation:-81},{lightness:34},{visibility:'on'}]},{featureType:'poi.medical',elementType:'all',stylers:[{hue:'#dddbd7'},{saturation:-80},{lightness:-2},{visibility:'on'}]},{featureType:'poi.school',elementType:'all',stylers:[{hue:'#c8c6c3'},{saturation:-91},{lightness:-7},{visibility:'on'}]},{featureType:'landscape.natural',elementType:'all',stylers:[{hue:'#c8c6c3'},{saturation:-71},{lightness:-18},{visibility:'on'}]},{featureType:'road.highway',elementType:'all',stylers:[{hue:'#dddbd7'},{saturation:-92},{lightness:60},{visibility:'on'}]},{featureType:'poi',elementType:'all',stylers:[{hue:'#dddbd7'},{saturation:-81},{lightness:34},{visibility:'on'}]},{featureType:'road.arterial',elementType:'all',stylers:[{hue:'#dddbd7'},{saturation:-92},{lightness:37},{visibility:'on'}]},{featureType:'transit',elementType:'geometry',stylers:[{hue:'#c8c6c3'},{saturation:4},{lightness:10},{visibility:'on'}]}];

$.ajaxSetup({
    cache: true
});

$(document).ready(function($) {
    /*setTimeout(function(){
        //$('#property_country option[value=4]').attr("selected",true);
        //$('#property_country option[value="' + country_id + '"]').attr("selected",true);
        //$('#property_state option[value="' + state_id + '"]').attr("selected",true);
    }, 500);*/

    $('#btn-search-map').click(function(){
        status = $('#property_status option:selected').val();
        type = $('#property_type option:selected').val();
        country = $('#property_country option:selected').val();
        state = $('#property_state option:selected').val();
        /*price = $('#price-input').val();*/

        query = 'status=' + status + '&country=' + country + '&state=' + state + '&type=' + type //+ '&price=' + price
        zoom = 14;

        createHomepageGoogleMap(_latitude,_longitude,static_url,api_url,query,zoom,country,state,1);
        return false;
    });
});

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Google Map - Homepage
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function createHomepageGoogleMap(_latitude,_longitude,static_url,api_url,query,zoom,country,state,option){
    setMapHeight();
    if( document.getElementById('map') != null ){
        $.ajax({
            type: "GET",
            url: api_url + '/api/v1.0/property-basic/?' + query,
            /*'beforeSend': function(xhr, settings) {
                $.ajaxSettings.beforeSend(xhr, settings);
            },*/
            success: function(data, textStatus, jqXHR)
            {
                if(option == 1) {
                    _latitude = data[0]['latitude'];
                    _longitude = data[0]['longitude'];
                }
                if ((country == '') && (state == '')) { zoom = 2; /*_latitude = 0; _longitude = 0;*/ }
                var map = new google.maps.Map(document.getElementById('map'), {
                    zoom: zoom,
                    scrollwheel: false,
                    center: new google.maps.LatLng(_latitude, _longitude),
                    mapTypeId: google.maps.MapTypeId.ROADMAP,
                    styles: mapStyles
                });
                var i=0;
                var newMarkers = [];

                $.each(data, function(index, rows) {

                //for (i = 0; i < locations.length; i++) {
                    var pictureLabel = document.createElement("img");
                    pictureLabel.src = ''; //static_url+'images/property-types/' + rows.type_name + '.png';
                    var boxText = document.createElement("div");
                    infoboxOptions = {
                        content: boxText,
                        disableAutoPan: false,
                        //maxWidth: 150,
                        pixelOffset: new google.maps.Size(-100, 0),
                        zIndex: null,
                        alignBottom: true,
                        boxClass: "infobox-wrapper",
                        enableEventPropagation: true,
                        closeBoxMargin: "0px 0px -8px 0px",
                        closeBoxURL: static_url+"img/close-btn.png",
                        infoBoxClearance: new google.maps.Size(1, 1)
                    };
                    var marker = new MarkerWithLabel({
                        title: rows.title,
                        position: new google.maps.LatLng(rows.latitude, rows.longitude),
                        map: map,
                        icon: static_url+'img/marker.png',
                        labelContent: pictureLabel,
                        labelAnchor: new google.maps.Point(50, 0),
                        labelClass: "marker-style"
                    });
                    newMarkers.push(marker);
                    boxText.innerHTML =
                        '<div class="infobox-inner">' +
                            '<a href="/property/' + rows.slug + '/">' +
                            '<div class="infobox-image" style="position: relative">' +
                            '<img src="' + get_image(static_url, rows.id) + '">' + '<div><span class="infobox-price">' + rows.price + '</span></div>' +
                            '</div>' +
                            '</a>' +
                            '<div class="infobox-description">' +
                            '<div class="infobox-title"><a href="/property/' + rows.slug + '/">' + rows.title + '</a></div>' +
                            '<div class="infobox-location">' + rows.zip_code + '</div>' +
                            '</div>' +
                            '</div>';
                    //Define the infobox
                    newMarkers[i].infobox = new InfoBox(infoboxOptions);
                    google.maps.event.addListener(marker, 'click', (function(marker, i) {
                        return function() {
                            for (h = 0; h < newMarkers.length; h++) {
                                newMarkers[h].infobox.close();
                            }
                            newMarkers[i].infobox.open(map, this);
                        }
                    })(marker, i));

                //}
                    i=i+1;
                });

                var clusterStyles = [
                    {
                        url: static_url + 'img/cluster.png',
                        height: 37,
                        width: 37
                    }
                ];
                var markerCluster = new MarkerClusterer(map, newMarkers, {styles: clusterStyles, maxZoom: 15});
                $('body').addClass('loaded');
                setTimeout(function() {
                    $('body').removeClass('has-fullscreen-map');
                }, 1000);
                $('#map').removeClass('fade-map');

                //  Dynamically show/hide markers --------------------------------------------------------------

                /*google.maps.event.addListener(map, 'idle', function() {

                    for (var i=0; i < locations.length; i++) {
                        if ( map.getBounds().contains(newMarkers[i].getPosition()) ){
                            // newMarkers[i].setVisible(true); // <- Uncomment this line to use dynamic displaying of markers

                            //newMarkers[i].setMap(map);
                            //markerCluster.setMap(map);
                        } else {
                            // newMarkers[i].setVisible(false); // <- Uncomment this line to use dynamic displaying of markers

                            //newMarkers[i].setMap(null);
                            //markerCluster.setMap(null);
                        }
                    }
                });*/

                // Function which set marker to the user position
                function success(position) {
                    var center = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
                    map.panTo(center);
                    $('#map').removeClass('fade-map');
                }

            },
            error: function (jqXHR, textStatus, errorThrown)
            {
                console.log('error');
            }
        });

        // Enable Geo Location on button click
        $('.geo-location').on("click", function() {
            if (navigator.geolocation) {
                $('#map').addClass('fade-map');
                navigator.geolocation.getCurrentPosition(success);
            } else {
                error('Geo Location is not supported');
            }
        });
    }
}

function get_image(static_url, basic_pk) {
    var result = '';
    $.ajax({
        type: "GET",
        url: api_url + '/api/v1.0/property-basic-images/?basic=' + basic_pk,
        async: false,
        success: function (data, textStatus, jqXHR) {
            if (data.length > 0) {
                result = data[0]['image'];
            } else {
                result = static_url + 'img/img_default.jpg';
            }
        }
    });
    return result;
}

// Function which set marker to the user position
function success(position) {
    createHomepageGoogleMap(position.coords.latitude, position.coords.longitude);
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Google Map - Property Detail
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function initMap(latitude, longitude, image_path, static_url) {
    var subtractPosition = 0;
    var mapWrapper = $('#property-detail-map.float');

    if (document.documentElement.clientWidth > 1200) {
        subtractPosition = 0.013;
    }
    if (document.documentElement.clientWidth < 1199) {
        subtractPosition = 0.006;
    }
    if (document.documentElement.clientWidth < 979) {
        subtractPosition = 0.001;
    }
    if (document.documentElement.clientWidth < 767) {
        subtractPosition = 0;
    }

    var mapCenter = new google.maps.LatLng(latitude,longitude);

    if ( $("#property-detail-map").hasClass("float") ) {
        mapCenter = new google.maps.LatLng(latitude,longitude - subtractPosition);
        mapWrapper.css('width', mapWrapper.width() + mapWrapper.offset().left )
    }

    var mapOptions = {
        zoom: 15,
        center: mapCenter,
        disableDefaultUI: false,
        scrollwheel: false,
        styles: mapStyles
    };
    var mapElement = document.getElementById('property-detail-map');
    var map = new google.maps.Map(mapElement, mapOptions);

    var pictureLabel = document.createElement("img");
    pictureLabel.src = static_url + 'images/property-types/' + image_path;
    var markerPosition = new google.maps.LatLng(latitude,longitude);
    var marker = new MarkerWithLabel({
        position: markerPosition,
        map: map,
        icon: static_url + 'img/marker.png',
        labelContent: pictureLabel,
        labelAnchor: new google.maps.Point(50, 0),
        labelClass: "marker-style"
    });
}

/*function initMap(propertyId) {
    $.getScript("/static/js/locations.js", function(){
        var subtractPosition = 0;
        var mapWrapper = $('#property-detail-map.float');

        if (document.documentElement.clientWidth > 1200) {
            subtractPosition = 0.013;
        }
        if (document.documentElement.clientWidth < 1199) {
            subtractPosition = 0.006;
        }
        if (document.documentElement.clientWidth < 979) {
            subtractPosition = 0.001;
        }
        if (document.documentElement.clientWidth < 767) {
            subtractPosition = 0;
        }

        var mapCenter = new google.maps.LatLng(locations[propertyId][3],locations[propertyId][4]);

        if ( $("#property-detail-map").hasClass("float") ) {
            mapCenter = new google.maps.LatLng(locations[propertyId][3],locations[propertyId][4] - subtractPosition);
            mapWrapper.css('width', mapWrapper.width() + mapWrapper.offset().left )
        }

        var mapOptions = {
            zoom: 15,
            center: mapCenter,
            disableDefaultUI: false,
            scrollwheel: false,
            styles: mapStyles
        };
        var mapElement = document.getElementById('property-detail-map');
        var map = new google.maps.Map(mapElement, mapOptions);

        var pictureLabel = document.createElement("img");
        pictureLabel.src = locations[propertyId][7];
        var markerPosition = new google.maps.LatLng(locations[propertyId][3],locations[propertyId][4]);
        var marker = new MarkerWithLabel({
            position: markerPosition,
            map: map,
            icon: '/static/img/marker.png',
            labelContent: pictureLabel,
            labelAnchor: new google.maps.Point(50, 0),
            labelClass: "marker-style"
        });
    });
}*/

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Google Map - Contact
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

function contactUsMap(){
    var mapCenter = new google.maps.LatLng(_latitude,_longitude);
    var mapOptions = {
        zoom: 15,
        center: mapCenter,
        disableDefaultUI: false,
        scrollwheel: false,
        styles: mapStyles
    };
    var mapElement = document.getElementById('contact-map');
    var map = new google.maps.Map(mapElement, mapOptions);

    var marker = new MarkerWithLabel({
        position: mapCenter,
        map: map,
        icon: '/static/img/marker.png',
        //labelContent: pictureLabel,
        labelAnchor: new google.maps.Point(50, 0),
        labelClass: "marker-style"
    });
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// OpenStreetMap - Homepage
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
/*
function createHomepageOSM(_latitude,_longitude){
    setMapHeight();
    if( document.getElementById('map') != null ){
        $.getScript("/static/js/locations.js", function(){
            var map = L.map('map', {
                center: [_latitude,_longitude],
                zoom: 14,
                scrollWheelZoom: false
            });
            L.tileLayer('http://openmapsurfer.uni-hd.de/tiles/roadsg/x={x}&y={y}&z={z}', {
                //L.tileLayer('http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png', {
                //subdomains: '0123',
                attribution: 'Imagery from <a href="http://giscience.uni-hd.de/">GIScience Research Group @ University of Heidelberg</a> &mdash; Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'
            }).addTo(map);
            var markers = L.markerClusterGroup({
                showCoverageOnHover: false
            });
            for (var i = 0; i < locations.length; i++) {
                var _icon = L.divIcon({
                    html: '<img src="' + locations[i][7] +'">',
                    iconSize:     [40, 48],
                    iconAnchor:   [20, 48],
                    popupAnchor:  [0, -48]
                });
                var title = locations[i][0];
                var marker = L.marker(new L.LatLng(locations[i][3],locations[i][4]), {
                    title: title,
                    icon: _icon
                });
                marker.bindPopup(
                    '<div class="property">' +
                        '<a href="' + locations[i][5] + '">' +
                            '<div class="property-image">' +
                                '<img src="' + locations[i][6] + '">' +
                            '</div>' +
                            '<div class="overlay">' +
                                '<div class="info">' +
                                    '<div class="tag price"> ' + locations[i][2] + '</div>' +
                                    '<h3>' + locations[i][0] + '</h3>' +
                                    '<figure>' + locations[i][1] + '</figure>' +
                                '</div>' +
                            '</div>' +
                        '</a>' +
                    '</div>'
                );
                markers.addLayer(marker);
            }

            map.addLayer(markers);
            map.on('locationfound', onLocationFound);

            function locateUser() {
                $('#map').addClass('fade-map');
                map.locate({setView : true})
            }

            function onLocationFound(){
                $('#map').removeClass('fade-map');
            }

            $('.geo-location').on("click", function() {
                locateUser();
            });

            $('body').addClass('loaded');
            setTimeout(function() {
                $('body').removeClass('has-fullscreen-map');
            }, 1000);
            $('#map').removeClass('fade-map');
        });

    }
}*/

