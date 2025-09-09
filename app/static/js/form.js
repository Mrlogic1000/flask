function setActionForm(action){

    let form = document.getElementById("auth_form")
    
    console.log(action)
    if (action === "login"){
        form.action = "/login"
        form.method = "post"
        form.submit();
    }else if(action === "register"){
        form.action = "/register"
        form.method = "post"
        form.submit();
    }
}