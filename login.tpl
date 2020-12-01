<p>Login</p>
<form action="/login" method="POST">
    User Name: <input type="text" size="50" maxlength="50" name="username"/><br>
    Password:  <input type="text" size="50" maxlength="50" name="password"/><br>
    <hr>
    <input type="hidden" name="csrf_token" value="{{csrf_token}}"/><br>
    <input type="submit" name="login" value="Login"/>
</form>