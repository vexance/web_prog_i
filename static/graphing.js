const computeBarChart = (rawData, graph_id) => {
    google.charts.load('current', {'packages':['corechart']});
    google.charts.setOnLoadCallback(drawChart);

    var graphData = [["PastaName", "Rating"]];
    rawData.forEach(obj => {
        graphData.push([`${obj.noodle} ${obj.sauce}`, obj.rating]);
    });
    console.log(graphData);

    function drawChart() {
        var data = google.visualization.arrayToDataTable(graphData);
        var options = { title: 'Pasta Ratings', curveType: 'function', height: 400, legend: { position: 'bottom' } };
        var chart = new google.visualization.BarChart(document.getElementById(graph_id));
        chart.draw(data, options);
    }
}