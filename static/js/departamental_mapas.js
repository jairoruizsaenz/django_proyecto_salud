
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // ::: Variables y funciones generales mapas

    function getColor(d) {
        var d = parseInt(d);
        return d > 90 ? '#a50026' :
               d > 80 ? '#d73027' :
               d > 70 ? '#f46d43' :
               d > 60 ? '#fdae61' :
               d > 50 ? '#fee08b' :
               d > 40 ? '#d9ef8b' :
               d > 30 ? '#a6d96a' :
               d > 20 ? '#66bd63' :
               d > 10 ? '#1a9850' :
               d > 0 ? '#006837' :
                          '#575756';
    }
    function polystyle(feature) {
        return {
            // fillColor: getColor(feature.properties.MPIO_CCDGO),
            fillColor: getColor(feature.valor_indicador),
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
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map1);

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

    function updateMap_1(dep_value, dim_value, ind_value) {
        // console.log("-- updateMap_1");
        layerGroup_1.clearLayers();
        $.getJSON(polyData, function (data) {
            var filtered_data_1 = data
            if (selection_departamento_1.value != 'todos') {
                filtered_data_1 = data['features'].filter(filtroDepartamental({selection: 1}));
            }
            else {
                filtered_data_1 = filtered_data_1.features;
            }
            filtered_data_1 = get_indicadores_data_municipal_map(filtered_data_1, dep_value, dim_value, ind_value);
            shape_data_1 = L.geoJson(filtered_data_1, { style: polystyle, onEachFeature: onEachFeature_1 });
            shape_data_1.addTo(layerGroup_1)
            map1.flyToBounds(shape_data_1.getBounds());
        });
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
            + props.valor_indicador + '' + '<br>'
            : 'Pase el cursor por el mapa');
    };
    info_1.addTo(map1);

    // ::::::::::::::::::::::::::::::::
    // Leyenda
    var legend_1 = L.control({position: 'bottomright'});
    legend_1.onAdd = function (map) {
        var div = L.DomUtil.create('div', 'info legend'),
            grades = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
            labels = [];

        // loop through our density intervals and generate a label with a colored square for each interval
        for (var i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }

        return div;
    };
    legend_1.addTo(map1);

    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // ::: Mapa 2

    var map2 = L.map('map2').setView([4.683709901063048, -74.05116825770746], 4);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map2);

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

    function updateMap_2(dep_value, dim_value, ind_value) {
        // console.log("-- updateMap_1");
        layerGroup_2.clearLayers();
        $.getJSON(polyData, function (data) {
            var filtered_data_2 = data
            if (selection_departamento_2.value != 'todos') {
                filtered_data_2 = data['features'].filter(filtroDepartamental({selection: 2}));
            }
            else {
                filtered_data_2 = filtered_data_2.features;
            }
            filtered_data_2 = get_indicadores_data_municipal_map(filtered_data_2, dep_value, dim_value, ind_value);
            shape_data_2 = L.geoJson(filtered_data_2, { style: polystyle, onEachFeature: onEachFeature_2 });
            shape_data_2.addTo(layerGroup_2)
            map2.flyToBounds(shape_data_2.getBounds());
        });
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
        var ind2 = document.getElementById("selection_indicador_2");
        var ind2_value = ind2.value;
        var ind2_text = ind2.options[ind2.selectedIndex].text;

        this._div.innerHTML = '' +  (props ? '<b>' 
            + props.properties.MPIO_CNMBR + '</b><br>' 
            + ind2_text + '<br>'
            + props.valor_indicador + '' + '<br>'
            : 'Pase el cursor por el mapa');
    };
    info_2.addTo(map2);

    // ::::::::::::::::::::::::::::::::
    // Leyenda    
    var legend_2 = L.control({position: 'bottomright'});
    legend_2.onAdd = function (map) {
        var div = L.DomUtil.create('div', 'info legend'),
            grades = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
            labels = [];

        // loop through our density intervals and generate a label with a colored square for each interval
        for (var i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }

        return div;
    };
    legend_2.addTo(map2);

    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // ::: Mapa 3

    var map3 = L.map('map3').setView([4.683709901063048, -74.05116825770746], 4);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map3);

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

    function updateMap_3(dep_value, dim_value, ind_value) {
        // console.log("-- updateMap_1");
        layerGroup_3.clearLayers();
        $.getJSON(polyData, function (data) {
            var filtered_data_3 = data
            if (selection_departamento_3.value != 'todos') {
                filtered_data_3 = data['features'].filter(filtroDepartamental({selection: 3}));
            }
            else {
                filtered_data_3 = filtered_data_3.features;
            }
            filtered_data_3 = get_indicadores_data_municipal_map(filtered_data_3, dep_value, dim_value, ind_value);
            shape_data_3 = L.geoJson(filtered_data_3, { style: polystyle, onEachFeature: onEachFeature_3 });
            shape_data_3.addTo(layerGroup_3)
            map3.flyToBounds(shape_data_3.getBounds());
        });
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
        var ind3 = document.getElementById("selection_indicador_3");
        var ind3_value = ind3.value;
        var ind3_text = ind3.options[ind3.selectedIndex].text;

        this._div.innerHTML = '' +  (props ? '<b>' 
            + props.properties.MPIO_CNMBR + '</b><br>' 
            + ind3_text + '<br>'
            + props.valor_indicador + '' + '<br>'
            : 'Pase el cursor por el mapa');
    };
    info_3.addTo(map3);

    // ::::::::::::::::::::::::::::::::
    // Leyenda
    var legend_3 = L.control({position: 'bottomright'});
    legend_3.onAdd = function (map) {
        var div = L.DomUtil.create('div', 'info legend'),
            grades = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
            labels = [];

        // loop through our density intervals and generate a label with a colored square for each interval
        for (var i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }

        return div;
    };
    legend_3.addTo(map3);
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

