<!DOCTYPE HTML>
<html>

<head>
    <title>PastaRater 1dot0</title>
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet"/>
    <link href="https://www.w3schools.com/w3css/4/w3.css" rel="stylesheet" >
</head>

% include("header.tpl")

<body>    
    <hr/>
    
    <div class="w3-container w3-padding-large">
    <table border="1" class="w3-table-all w3-centered w3-hoverable w3-card-4">
    <tr>
        <th class="w3-blue-grey"><p>Favorite</p></th>
        <th class="w3-blue-grey"><p>Noodle</p></th>
        <th class="w3-blue-grey"><p>Sauce</p></th>
        <th class="w3-blue-grey"><p>Rating</p></th>
        <th class="w3-blue-grey"><p>Action</p></th>
    </tr>
    
    %for row in rows:
        <tr>
            <td>
            %if fav == str(row[0]):
                <a href="/favorite/{{row[0]}}/" class="material-icons" style="text-decoration: none">star</a>
            %else:
                <a href="/favorite/{{row[0]}}/" class="material-icons" style="text-decoration: none">star_outline</a>
            %end
            </td>

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

    <hr />

    %if len(rows) == 0:
        <div class="w3-center"><a href="/new_item" class="w3-button w3-round-xxlarge w3-blue-grey w3-border w3-border-teal" style="width: 20%">Get Started</a></div>
    %else:
        % include("footer.tpl")
    %end
</body>