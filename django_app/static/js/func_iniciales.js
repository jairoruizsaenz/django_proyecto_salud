    // <!-- filtroDepartamental -->
    function filtroDepartamental({selection}) {
        return function filter(item) {
            if (selection == 1) {
                return item['properties'].DPTO_CCDGO == selection_departamento_1.value;
            } else if (selection == 2) {
                return item['properties'].DPTO_CCDGO == selection_departamento_2.value;
            } else if (selection == 3) {
                return item['properties'].DPTO_CCDGO == selection_departamento_3.value;
            } else {
                console.log('Error - filtroDepartamental')
            }
        };
    }
