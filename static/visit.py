#========== Example Cookie Operation - Visit Counter ==========#
@get("/visit")
def get_visit():
    session_id = request.cookies.get("session_id",str(uuid.uuid4()))
    result = db.search(query.session_id == session_id)
    if len(result) == 0:
        db.insert({'session_id':session_id, 'visit_count':1})
        visit_count = 1
    else:
        session = result[0]
        visit_count = session['visit_count'] + 1
        db.update({'visit_count':visit_count},query.session_id == session_id)
    response.set_cookie("session_id",session_id, path="/")
    return(f"Welcome, session_id #{session_id}. Visit# {visit_count}.")