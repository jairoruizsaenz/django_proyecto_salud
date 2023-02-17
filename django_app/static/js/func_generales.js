
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // <!-- Show_Hide_Sections -->
    function Show_Hide_Sections() {
        var section1 = document.getElementById("section1"); // Presentar - Mapa
        var section2 = document.getElementById("section2"); // Comparar  - Mapa
        var section3 = document.getElementById("section3"); // Comparar  - Radar

        var tipo_grafico = document.getElementById('selection_tipo_grafico');
        var tipo_grafico_value = tipo_grafico.options[tipo_grafico.selectedIndex].value;

        var selection_tipo_grafico_group = document.getElementById('selection_tipo_grafico_group');

        var compareCheck = document.getElementById('compareCheck');
        var compareCheck_value = compareCheck.checked;

        if (compareCheck_value) {
            selection_tipo_grafico_group.classList.add("visible");
            selection_tipo_grafico_group.classList.remove("hidden");
        } else {
            selection_tipo_grafico_group.classList.add("hidden");
            selection_tipo_grafico_group.classList.remove("visible");
        }

        section1.classList.remove("visible");
        section2.classList.remove("visible");
        section3.classList.remove("visible");

        section1.classList.add("hidden");
        section2.classList.add("hidden");
        section3.classList.add("hidden");

        if (compareCheck_value == false) {
            // console.log('Map - show')
            section1.classList.add("visible");
            section1.classList.remove("hidden");
        } else {

            if (tipo_grafico_value == 'map') {
                // console.log('Map - compare')
                section2.classList.add("visible");
                section2.classList.remove("hidden");
            } else if (tipo_grafico_value == 'radar') {
                // console.log('Radar - compare')
                section3.classList.add("visible");
                section3.classList.remove("hidden");
            }
        }
    };
    Show_Hide_Sections();

    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    // <!-- EventListener -->
    function updateGraphs(index) {
        // console.log('-- updateGraphs --------')

        if (index == 1) {
            var dep = document.getElementById("selection_departamento_1");
            var dep_value = dep.value;
            var dep_text = dep.options[dep.selectedIndex].text;

            var dim = document.getElementById("selection_dimension_1");
            var dim_value = dim.value;
            var dim_text = dim.options[dim.selectedIndex].text;

            var ind = document.getElementById("selection_indicador_1");
            var ind_value = ind.value;
            var ind_text = ind.options[ind.selectedIndex].text;
            
            var tipo_ind = document.getElementById( "selection_tipo_indicador_1");
            var tipo_ind_value = tipo_ind.value;
           
            if (tipo_ind_value == 'porcentual') {
                tipo_ind_value = true;
            } else if (tipo_ind_value == 'numerico') {
                tipo_ind_value = false;
            }

            // FIXME: Borrar
            updateMap_0(dep_value, dim_value, ind_value);

            updateMap_1(dep_value, dim_value, ind_value);
            get_dimensiones_data_departamental_radar_1(dep_value, dim_value, tipo_ind_value)

        } else if (index == 2) {
            var dep = document.getElementById("selection_departamento_2");
            var dep_value = dep.value;
            var dep_text = dep.options[dep.selectedIndex].text;

            var dim = document.getElementById("selection_dimension_2");
            var dim_value = dim.value;
            var dim_text = dim.options[dim.selectedIndex].text;

            var ind = document.getElementById("selection_indicador_2");
            var ind_value = ind.value;
            var ind_text = ind.options[ind.selectedIndex].text;

            updateMap_2(dep_value, dim_value, ind_value);
            // get_dimensiones_data_departamental_radar_1(dep_value, dim_value)

        } else if (index == 3) {
            var dep = document.getElementById("selection_departamento_3");
            var dep_value = dep.value;
            var dep_text = dep.options[dep.selectedIndex].text;

            var dim = document.getElementById("selection_dimension_3");
            var dim_value = dim.value;
            var dim_text = dim.options[dim.selectedIndex].text;

            var ind = document.getElementById("selection_indicador_3");
            var ind_value = ind.value;
            var ind_text = ind.options[ind.selectedIndex].text;

            updateMap_3(dep_value, dim_value, ind_value);
            // get_dimensiones_data_departamental_radar_1(dep_value, dim_value)

        } else if (index == 4) {            
            var dep_1 = document.getElementById("selection_departamento_4_1");
            var dep_1_value = dep_1.value;
            // var dep_1_text = dep_1.options[dep_1.selectedIndex].text;

            var dep_2 = document.getElementById("selection_departamento_4_2");
            var dep_2_value = dep_2.value;
            // var dep_2_text = dep_2.options[dep_2.selectedIndex].text;

            var dim = document.getElementById("selection_dimension_4");
            var dim_value = dim.value;
            // var dim_text = dim.options[dim.selectedIndex].text;

            // var ind = document.getElementById("selection_indicador_4");
            // var ind_value = ind.value;
            // var ind_text = ind.options[ind.selectedIndex].text;

            var tipo_ind = document.getElementById( "selection_tipo_indicador_4");
            var tipo_ind_value = tipo_ind.value;
           
            if (tipo_ind_value == 'porcentual') {
                tipo_ind_value = true;
            } else if (tipo_ind_value == 'numerico') {
                tipo_ind_value = false;
            }

            // updateMap_3(dep_value, dim_value, ind_value);
            get_dimensiones_data_departamental_radar_2(dep_1_value, dep_2_value, dim_value, tipo_ind_value)
        }
        // console.log('-------------------------------------------');
        // console.log(dep_text, ' - ', dim_text, ' - ', ind_text);
    }

    function departamento_change(index) {
        // console.log('-- dpto change --------');

        update_municipio_dropdownlist("#selection_departamento_1", "#selection_municipio_1");
        // if (index == 1) {
        //     update_municipio_dropdownlist("#selection_departamento_1", "#selection_municipio_1");
        // } else if (index == 2) {
        //     update_municipio_dropdownlist("#selection_departamento_2", "#selection_municipio_2");
        // } else if (index == 3) {
        //     update_municipio_dropdownlist("#selection_departamento_3", "#selection_municipio_3");
        // } else if (index == 4) {
        //     update_municipio_dropdownlist("#selection_departamento_4", "#selection_municipio_4");
        // }

        updateGraphs(index);
    }
    
    function dimension_change(index) {
        // console.log('-- dim change ---------');
        if (index == 1) {
            update_indicador_dropdownlist("#selection_dimension_1", "#selection_indicador_1");
        } else if (index == 2) {
            update_indicador_dropdownlist("#selection_dimension_2", "#selection_indicador_2");
        } else if (index == 3) {
            update_indicador_dropdownlist("#selection_dimension_3", "#selection_indicador_3");
        } else if (index == 4) {
            update_indicador_dropdownlist("#selection_dimension_4", "#selection_indicador_4");
        }
    }

    function indicador_change(index) {
        // console.log('-- indi change --------');
        updateGraphs(index);
    }

    document.getElementById('selection_departamento_1').addEventListener('change', function() { departamento_change(1); });
    document.getElementById('selection_dimension_1').addEventListener('change', function() { dimension_change(1); });

    document.getElementById('selection_departamento_2').addEventListener('change', function() { departamento_change(2); });
    document.getElementById('selection_dimension_2').addEventListener('change', function() { dimension_change(2); });

    document.getElementById('selection_departamento_3').addEventListener('change', function() { departamento_change(3); });
    document.getElementById('selection_dimension_3').addEventListener('change', function() { dimension_change(3); });

    document.getElementById('selection_departamento_4_1').addEventListener('change', function() { departamento_change(4); });
    document.getElementById('selection_departamento_4_2').addEventListener('change', function() { departamento_change(4); });
    document.getElementById('selection_dimension_4').addEventListener('change', function() { dimension_change(4); });

    update_indicador_dropdownlist("#selection_dimension_1", "#selection_indicador_1");
    update_indicador_dropdownlist("#selection_dimension_2", "#selection_indicador_2");
    update_indicador_dropdownlist("#selection_dimension_3", "#selection_indicador_3");
    update_indicador_dropdownlist("#selection_dimension_4", "#selection_indicador_4");
    
    update_municipio_dropdownlist("#selection_departamento_1", "#selection_municipio_1");