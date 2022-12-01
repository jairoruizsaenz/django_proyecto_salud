// https://www.youtube.com/watch?v=xerlQ3tE8Ew

// :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // ::: Variables y funciones generales mapas

    // function getColor(d) {
    //     var d = parseFloat(d);
    //     return d > 90 ? '#a50026' :
    //            d > 80 ? '#d73027' :
    //            d > 70 ? '#f46d43' :
    //            d > 60 ? '#fdae61' :
    //            d > 50 ? '#fee090' :
    //            d > 40 ? '#e0f3f8' :
    //            d > 30 ? '#abd9e9' :
    //            d > 20 ? '#74add1' :
    //            d > 10 ? '#4575b4' :
    //            d > 0.0 ? '#313695' :
    //            d == 0.0 ? '#575756' :
    //                       '#000000';
    // }
    function polystyle(feature) {
        return {
            // fillColor: getColor(feature.properties.MPIO_CCDGO),
            // fillColor: getColor(feature.valor_indicador),
            fillColor: feature.color,
            weight: 0.8,
            opacity: 1,
            color: 'white',
            fillOpacity: 0.7
        };
    }

    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // ::: Mapa 1

    var map1 = L.map('map1').setView([4.683709901063048, -74.05116825770746], 4);
    // https://leaflet-extras.github.io/leaflet-providers/preview/
    // https://leafletjs.com/reference.html#tilelayer
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', { minZoom:5, maxZoom: 10 }).addTo(map1);

    var layerGroup_1 = L.featureGroup()
    map1.addLayer(layerGroup_1);

    var shape_data_1;

    function highlightFeature_1(e) {
        var layer = e.target;

        layer.setStyle({
            weight: 5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.7
        });

        if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
            layer.bringToFront();
        }
        // console.log('layer.feature:', layer.feature)
        info_1.update(layer.feature);
    }

    function resetHighlight_1(e) {
        shape_data_1.resetStyle(e.target);
        info_1.update();
    }

    // function zoomToFeature(e) {
    //     console.log(e);
    // }

    function onEachFeature_1(feature, layer) {
        layer.on({
            mouseover: highlightFeature_1,
            mouseout: resetHighlight_1,
            // click: zoomToFeature
        });
    }

    // ::::::::::::::::::::::::::::::::
    // Leyenda
    var legend_1 = L.control({position: 'bottomright'});
    legend_1.onAdd = function (map) {
        var div = L.DomUtil.create('div', 'info legend');
        // var grades = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90];
        // var labels = [];

        // loop through our density intervals and generate a label with a colored square for each interval
        // for (var i = 0; i < grades.length; i++) {
        //     div.innerHTML += 
        //         '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' + grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        // }
        div.innerHTML = '';
        return div;
    };
    legend_1.addTo(map1);

    legend_1.setContent = function(colors, values) {
        this.getContainer().innerHTML = '';
        for (var i = 0; i < colors.length; i++) {
            this.getContainer().innerHTML +=
                '<i style="background:' + colors[i] + '"></i>' + values[i] + '<br>';
        }
    };

    // ::::::::::::::::::::::::::::::::
    // Update Map

    function updateMap_1(dep_value, dim_value, ind_value) {
        // console.log("-- updateMap_1");
        layerGroup_1.clearLayers();

        if (dep_value == '00') {
            $.getJSON(shapes_departamentales, function (data) {
                var filtered_data_1 = data                
                filtered_data_1 = filtered_data_1.features;
                // TODO: deb implementar una función para extraer los datos departamentales
                data_temp = get_indicadores_data_municipal_map(filtered_data_1, dep_value, dim_value, ind_value);
                shape_data_1 = L.geoJson(data_temp[0], { style: polystyle, onEachFeature: onEachFeature_1 });
                shape_data_1.addTo(layerGroup_1)
                map1.flyToBounds(shape_data_1.getBounds());
                legend_1.setContent(data_temp[1], data_temp[2]);
            });
        }
        else {
            $.getJSON(shapes_municipales, function (data) {
                var filtered_data_1 = data
                filtered_data_1 = data['features'].filter(filtroDepartamental({selection: 1}));
                data_temp = get_indicadores_data_municipal_map(filtered_data_1, dep_value, dim_value, ind_value);
                shape_data_1 = L.geoJson(data_temp[0], { style: polystyle, onEachFeature: onEachFeature_1 });
                shape_data_1.addTo(layerGroup_1)
                map1.flyToBounds(shape_data_1.getBounds());
                legend_1.setContent(data_temp[1], data_temp[2]);
            });        
        }
    }

    // ::::::::::::::::::::::::::::::::
    // Etiqueta de datos

    var info_1 = L.control();
    info_1.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
        this.update();
        return this._div;
    };

    info_1.update = function (props) {
        var ind1 = document.getElementById("selection_indicador_1");
        var ind1_value = ind1.value;
        var ind1_text = ind1.options[ind1.selectedIndex].text;

        this._div.innerHTML = '' +  (props ? '<b>' 
            + props.properties.MPIO_CNMBR + '</b><br>' 
            + ind1_text + '<br>'
            + parseFloat(props.valor_indicador).toFixed(2) + '' + '<br>'
            : 'Pase el cursor por el mapa');
    };
    info_1.addTo(map1);


    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // ::: Mapa 2

    var map2 = L.map('map2').setView([4.683709901063048, -74.05116825770746], 4);
    // https://leaflet-extras.github.io/leaflet-providers/preview/
    // https://leafletjs.com/reference.html#tilelayer
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', { minZoom:5, maxZoom: 10 }).addTo(map2);

    var layerGroup_2 = L.featureGroup()
    map2.addLayer(layerGroup_2);

    var shape_data_2;

    function highlightFeature_2(e) {
        var layer = e.target;

        layer.setStyle({
            weight: 5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.7
        });

        if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
            layer.bringToFront();
        }
        // console.log('layer.feature:', layer.feature)
        info_2.update(layer.feature);
    }

    function resetHighlight_2(e) {
        shape_data_2.resetStyle(e.target);
        info_2.update();
    }

    // function zoomToFeature(e) {
    //     console.log(e);
    // }

    function onEachFeature_2(feature, layer) {
        layer.on({
            mouseover: highlightFeature_2,
            mouseout: resetHighlight_2,
            // click: zoomToFeature
        });
    }

    // ::::::::::::::::::::::::::::::::
    // Leyenda
    var legend_2 = L.control({position: 'bottomright'});
    legend_2.onAdd = function (map) {
        var div = L.DomUtil.create('div', 'info legend');
        // var grades = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90];
        // var labels = [];

        // loop through our density intervals and generate a label with a colored square for each interval
        // for (var i = 0; i < grades.length; i++) {
        //     div.innerHTML += 
        //         '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' + grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        // }
        div.innerHTML = '';
        return div;
    };
    legend_2.addTo(map2);

    legend_2.setContent = function(colors, values) {
        this.getContainer().innerHTML = '';
        for (var i = 0; i < colors.length; i++) {
            this.getContainer().innerHTML +=
                '<i style="background:' + colors[i] + '"></i>' + values[i] + '<br>';
        }
    };

    // ::::::::::::::::::::::::::::::::
    // Update Map

    function updateMap_2(dep_value, dim_value, ind_value) {
        // console.log("-- updateMap_2");
        layerGroup_2.clearLayers();

        if (dep_value == '00') {
            $.getJSON(shapes_departamentales, function (data) {
                var filtered_data_2 = data                
                filtered_data_2 = filtered_data_2.features;
                // TODO: deb implementar una función para extraer los datos departamentales
                data_temp = get_indicadores_data_municipal_map(filtered_data_2, dep_value, dim_value, ind_value);
                shape_data_2 = L.geoJson(data_temp[0], { style: polystyle, onEachFeature: onEachFeature_2 });
                shape_data_2.addTo(layerGroup_2)
                map2.flyToBounds(shape_data_2.getBounds());
                legend_2.setContent(data_temp[1], data_temp[2]);
            });
        }
        else {
            $.getJSON(shapes_municipales, function (data) {
                var filtered_data_2 = data
                filtered_data_2 = data['features'].filter(filtroDepartamental({selection: 2}));
                data_temp = get_indicadores_data_municipal_map(filtered_data_2, dep_value, dim_value, ind_value);
                shape_data_2 = L.geoJson(data_temp[0], { style: polystyle, onEachFeature: onEachFeature_2 });
                shape_data_2.addTo(layerGroup_2)
                map2.flyToBounds(shape_data_2.getBounds());
                legend_2.setContent(data_temp[1], data_temp[2]);
            });        
        }
    }

    // ::::::::::::::::::::::::::::::::
    // Etiqueta de datos

    var info_2 = L.control();
    info_2.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
        this.update();
        return this._div;
    };

    info_2.update = function (props) {
        var ind1 = document.getElementById("selection_indicador_2");
        var ind1_value = ind1.value;
        var ind1_text = ind1.options[ind1.selectedIndex].text;

        this._div.innerHTML = '' +  (props ? '<b>' 
            + props.properties.MPIO_CNMBR + '</b><br>' 
            + ind1_text + '<br>'
            + parseFloat(props.valor_indicador).toFixed(2) + '' + '<br>'
            : 'Pase el cursor por el mapa');
    };
    info_2.addTo(map2);

    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // ::: Mapa 3

    var map3 = L.map('map3').setView([4.683709901063048, -74.05116825770746], 4);
    // https://leaflet-extras.github.io/leaflet-providers/preview/
    // https://leafletjs.com/reference.html#tilelayer
    L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', { minZoom:5, maxZoom: 10 }).addTo(map3);

    var layerGroup_3 = L.featureGroup()
    map3.addLayer(layerGroup_3);

    var shape_data_3;

    function highlightFeature_3(e) {
        var layer = e.target;

        layer.setStyle({
            weight: 5,
            color: '#666',
            dashArray: '',
            fillOpacity: 0.7
        });

        if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
            layer.bringToFront();
        }
        // console.log('layer.feature:', layer.feature)
        info_3.update(layer.feature);
    }

    function resetHighlight_3(e) {
        shape_data_3.resetStyle(e.target);
        info_3.update();
    }

    // function zoomToFeature(e) {
    //     console.log(e);
    // }

    function onEachFeature_3(feature, layer) {
        layer.on({
            mouseover: highlightFeature_3,
            mouseout: resetHighlight_3,
            // click: zoomToFeature
        });
    }

    // ::::::::::::::::::::::::::::::::
    // Leyenda
    var legend_3 = L.control({position: 'bottomright'});
    legend_3.onAdd = function (map) {
        var div = L.DomUtil.create('div', 'info legend');
        // var grades = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90];
        // var labels = [];

        // loop through our density intervals and generate a label with a colored square for each interval
        // for (var i = 0; i < grades.length; i++) {
        //     div.innerHTML += 
        //         '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' + grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        // }
        div.innerHTML = '';
        return div;
    };
    legend_3.addTo(map3);

    legend_3.setContent = function(colors, values) {
        this.getContainer().innerHTML = '';
        for (var i = 0; i < colors.length; i++) {
            this.getContainer().innerHTML +=
                '<i style="background:' + colors[i] + '"></i>' + values[i] + '<br>';
        }
    };

    // ::::::::::::::::::::::::::::::::
    // Update Map

    function updateMap_3(dep_value, dim_value, ind_value) {
        // console.log("-- updateMap_2");
        layerGroup_3.clearLayers();

        if (dep_value == '00') {
            $.getJSON(shapes_departamentales, function (data) {
                var filtered_data_3 = data                
                filtered_data_3 = filtered_data_3.features;
                // TODO: deb implementar una función para extraer los datos departamentales
                data_temp = get_indicadores_data_municipal_map(filtered_data_3, dep_value, dim_value, ind_value);
                shape_data_3 = L.geoJson(data_temp[0], { style: polystyle, onEachFeature: onEachFeature_3 });
                shape_data_3.addTo(layerGroup_3)
                map3.flyToBounds(shape_data_3.getBounds());
                legend_3.setContent(data_temp[1], data_temp[2]);
            });
        }
        else {
            $.getJSON(shapes_municipales, function (data) {
                var filtered_data_3 = data
                filtered_data_3 = data['features'].filter(filtroDepartamental({selection: 3}));
                data_temp = get_indicadores_data_municipal_map(filtered_data_3, dep_value, dim_value, ind_value);
                shape_data_3 = L.geoJson(data_temp[0], { style: polystyle, onEachFeature: onEachFeature_3 });
                shape_data_3.addTo(layerGroup_3)
                map3.flyToBounds(shape_data_3.getBounds());
                legend_3.setContent(data_temp[1], data_temp[2]);
            });        
        }
    }

    // ::::::::::::::::::::::::::::::::
    // Etiqueta de datos

    var info_3 = L.control();
    info_3.onAdd = function (map) {
        this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
        this.update();
        return this._div;
    };

    info_3.update = function (props) {
        var ind1 = document.getElementById("selection_indicador_3");
        var ind1_value = ind1.value;
        var ind1_text = ind1.options[ind1.selectedIndex].text;

        this._div.innerHTML = '' +  (props ? '<b>' 
            + props.properties.MPIO_CNMBR + '</b><br>' 
            + ind1_text + '<br>'
            + parseFloat(props.valor_indicador).toFixed(2) + '' + '<br>'
            : 'Pase el cursor por el mapa');
    };
    info_3.addTo(map3);
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

