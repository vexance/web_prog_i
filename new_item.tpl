<!DOCTYPE HTML>
<html>

<head>
    <title>PastaRater 1dot0</title>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
    <link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet" >
</head>

<body>
    <p class="w3-block w3-teal w3-center">New Pasta Rating</p>
    <form class="w3-center" action="/new_item" method="POST">
        <input type="text" size="40" maxlength="32" name="noodle" placeholder="Noodle Type" required /> 
        <input type="text" size="40" maxlength="32" name="sauce" placeholder="Sauce" required />
        <input type="number" size="3" name="rating" placeholder="5" required /> 
        <input type="submit" name="save" value="Add Rating"/>
    </form>

    <hr />

    <div class="w3-center"><a href="/" class="w3-button w3-round-xxlarge w3-blue-grey w3-border w3-border-teal" style="width: 20%">Cancel</a></div>
</body>

</html>