
    // :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::    
    function updateRadar(graph, headers, values) {
        Plotly.restyle(graph, 'theta', [headers]);
        Plotly.restyle(graph, 'r', [values]);
    }
    
    // <!-- Plotly radar1 -->
    data = [{
        type: 'scatterpolar',
        r: [0], theta: [''], fill: 'toself'
    }]
    layout = {
        polar: {
            radialaxis: {
                visible: true,
                range: [0, 100]
            }
        },
        showlegend: false
    }
    Plotly.newPlot("radar1", data, layout)
    Plotly.newPlot("radar2", data, layout)

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
