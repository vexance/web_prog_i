<h3>Basic Pasta List, version 1.0</h3>
<hr/>
<table border="1">
<tr>
    <td><p>Id</p></td>
    <td><p>Noodle</p></td>
    <td><p>Sauce</p></td>
    <td><p>Rating</p></td>
    <td><p>Action</p></td>
</tr>
%for row in rows:
    <tr>
        <td>{{str(row[0])}}</td>
        <td>
            <a href="/update_item/{{row[0]}}">{{row[1]}}</a>
        </td>
        <td>
            <p>{{row[2]}}</p>
        </td>
        <td>
            <p>{{row[3]}}</p>
        </td>
        <td>
            <a href="/delete_item/{{row[0]}}">DELETE</a>
        </td>
    </tr>
%end
</table>
<hr/>
<a href="/new_item">New Item... :-)</a>