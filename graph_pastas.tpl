%include("header.tpl", session=session)

<link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
<link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet" />
<script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
<script type="text/javascript" src="/static/graphing.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<!-- Begin Chart Section -->
<div class="w3-container w3-padding-large">
    <div class="w3-row">
        <div class="w3-card-4">
            <div class="w3-container w3-blue-grey w3-padding-small w3-center"><h2>Pasta Ratings Visualized</h2></div>
                <div class="w3-container" id="pasta_graph">
                    <script>
                        $.getJSON("http://localhost/get_pastas_json", function(rows) {
                            computeBarChart(rows, "chart_pasta");
                        });
                    </script>
                <div id="chart_pasta" ></div>
            </div>
        </div>
    </div>
</div>

%include("footer.tpl", session=session)