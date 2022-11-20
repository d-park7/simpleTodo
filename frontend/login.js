$(function() {
    $("a").each((index, element) => {
        if ($(element).prop("href") == window.location.href) {
            $(element).addClass("active");
        }
    });

    $("form").submit(async (event) => {
        let username = event.currentTarget[0].value;
        let password = event.currentTarget[1].value;
        if (username == "") {
            alert("Put a username");
        }
        if (password == "") {
            alert("Put a password");
        }
        console.log(username);
        console.log(password);
        
        new_user = JSON.stringify({id: 1, username: username, password: password});
        console.log(new_user)
        $.ajax({
            url:'http://127.0.0.1:8000/users',
            type: 'POST',
            contentType: "application/json; charset=UTF-8",
            data: new_user,
            success: function (response) {
                console.log(response)
            },
            error: function (error) {
                console.log(error)
            }
        })
        event.preventDefault();
    });
})