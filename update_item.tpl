<p>Update Pasta</p>
<form action="/update_item" method="POST">
    <input type="text" size="40" maxlength="32" name="id" value="{{str(row[0])}}" hidden/>
    <input type="text" size="40" maxlength="32" name="noodle" value="{{str(row[1])}}"/>
    <input type="text" size="40" maxlength="32" name="sauce" value="{{str(row[2])}}"/>
    <input type="number" name="rating" value="{{str(row[3])}}"/>
    <hr/>
    <input type="submit" name="update_button" value="Update"/>
    <a href="/">Cancel</a>
</form>