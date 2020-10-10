<!DOCTYPE HTML>
<html>

<head>
    <title>PastaRater 1dot0</title>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
    <link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet" >
</head>

<body>
    <h3 class="w3-block w3-teal w3-center">Basic Pasta List, version 1.0</h3>
    
    <hr/>
    
    <div class="w3-container w3-padding-large">
    <table border="1" class="w3-table-all w3-centered w3-hoverable w3-card-4">
    <tr>
        <th class="w3-blue-grey"><p>Noodle</p></td>
        <th class="w3-blue-grey"><p>Sauce</p></td>
        <th class="w3-blue-grey"><p>Rating</p></td>
        <th class="w3-blue-grey"><p>Action</p></td>
    </tr>
    
    %for row in rows:
        <tr>
            <td><p>{{row[1]}}</p></td>
            <td><p>{{row[2]}}</p></td>
            <td><p>{{row[3]}}</p></td>
            <td>
                <a href="/delete_item/{{row[0]}}" class="material-icons" style="text-decoration: none">delete</a> {{str("   ")}} <a href="/update_item/{{row[0]}}" class="material-icons" style="text-decoration: none">edit</a>
            </td>
        </tr>
    %end
    
    </table>
    </div>
    
    <hr/>

    %if len(rows) == 0:
        <a href="/new_item" class="w3-button w3-block w3-teal"><Get Started</a>
    %else:
        <a href="/new_item" class="w3-button w3-block w3-teal">Add New Pasta Rating</a>
    %end
</body>