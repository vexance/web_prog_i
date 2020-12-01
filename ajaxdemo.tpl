<html>
<head>
  <title>Ajax Demo Page</title>
  <script>
  function onLoad() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            content = this.responseText;
            document.getElementById("my_text").innerHTML = content;
        } else if (this.status == 404) {
          document.getElementById("my_text").innerHTML = "Data file not found!";
        }
    }
    console.log("sending request");
    xhttp.open("GET", "http://localhost/static/data.txt", true);
    xhttp.send();
  };
  </script>
</head>
<body onload='onLoad();'>
Hello from the sandbox.
<hr/>
<div id="my_text"></div>
<hr/>
</body>
</html>