<html>
<head>
  <title>PastaRater OneDotOh</title>
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
  <link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet" />
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  <script>
  $(document).ready(function() {
    var cookies = document.cookie;
    var fav = cookies.substr(cookies.indexOf("fav_pasta=")+10, cookies.lastIndexOf(";"));
    $.getJSON("http://localhost/get_pastas_json", function(rows) {
        var tableContents = `<table border="1" class="w3-table-all w3-centered w3-hoverable w3-card-4"><tr><th class="w3-blue-grey"><p>Favorite</p></th><th class="w3-blue-grey"><p>Noodle</p></th><th class="w3-blue-grey"><p>Sauce</p></th><th class="w3-blue-grey"><p>Rating</p></th><th class="w3-blue-grey"><p>Action</p></th></tr>`;
        $.each(rows, function(i, row) {
            if (fav == row['id'].toString()) tableContents += `<tr><td><a href="/favorite/${row['id']}/" class="material-icons" style="text-decoration: none">star</a>`;
            else tableContents += `<tr><td><a href="/favorite/${row['id']}/" class="material-icons" style="text-decoration: none">star_outline</a>`;
            tableContents += `<td><p>${row['noodle']}</p></td><td><p>${row['sauce']}</p></td><td><p>${row['rating']}</p></td>`;
            tableContents += `<td><a href="/delete_item/${row['id']}" class="material-icons" style="text-decoration: none">delete</a>  `;
            tableContents += `  <a href="/update_item/${row['id']}" class="material-icons" style="text-decoration: none">edit</a></td></tr>`;
        });
        $("#content").append(tableContents);
    });
  })
  </script>
</head>
<body>
%include("header.tpl", session=session)
<div id="content" class="w3-container w3-padding-large"></div>
%include("footer.tpl", session=session)
</body>
</html>