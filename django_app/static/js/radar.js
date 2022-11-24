
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    
    // <!-- Plotly radar1 -->
    function updateRadar(graph, headers, values) {
        Plotly.restyle(graph, 'theta', [headers]);
        Plotly.restyle(graph, 'r', [values]);
    }

    data_1 = [{
        type: 'scatterpolar',
        r: [0], theta: [''], fill: 'toself'
    }]
    layout_1 = {
        margin: { l: 40, r: 40, b: 40, t: 40 },
        polar: {
            radialaxis: {
                visible: true,
                // range: [0, 100]
            }
        },
        showlegend: false
    }
    Plotly.newPlot("radar1", data_1, layout_1)
    
    // <!-- Plotly radar2 -->
    function updateRadar2(graph, headers_1, values_1, name_1, headers_2, values_2, name_2) {
        update_1 = { theta: [headers_1], r:[values_1], name:name_1 }
        update_2 = { theta: [headers_2], r:[values_2], name:name_2 }

        Plotly.restyle(graph, update_1, 0);
        Plotly.restyle(graph, update_2, 1);
    }

    data_2 = [
        {
            type: 'scatterpolar',
            r: [0], theta: [''], fill: 'toself', name: 'Group A'
        },
        {
            type: 'scatterpolar',
            r: [0], theta: [''], fill: 'toself', name: 'Group B'
        }
    ]
    layout_2 = {
        margin: { l: 40, r: 40, b: 40, t: 40 },
        polar: {
            radialaxis: {
                visible: true,
                // range: [0, 100]
            }
        },
        showlegend: true
    }
    Plotly.newPlot("radar2", data_2, layout_2)

    // <!-- Plotly radar2 -->
    // data = [
    //     {
    //         type: 'scatterpolar',
    //         r: [39, 28, 8, 7, 28, 39],
    //         theta: ['A','B','C', 'D', 'E', 'A'],
    //         fill: 'toself',
    //         name: 'Group A'
    //     },
    //     {
    //         type: 'scatterpolar',
    //         r: [1.5, 10, 39, 31, 15, 1.5],
    //         theta: ['A','B','C', 'D', 'E', 'A'],
    //         fill: 'toself',
    //         name: 'Group B'
    //     }
    // ]
        
    // layout = {
    //     polar: {
    //         radialaxis: {
    //             visible: true,
    //             range: [0, 50]
    //         }
    //     }
    // }
        
    // Plotly.newPlot("radar2", data, layout)
