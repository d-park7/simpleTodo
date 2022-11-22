$(function() {
    $("a").each((index, element) => {
        if ($(element).prop("href") == window.location.href) {
            $(element).addClass("active");
        }
    });

    $("form").submit((event) => {
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
        
        // Adding ```id: 1``` bc schema require user id
        // but the db will automatically assign an id
        // when inserting the todo in
        // not really intended behavior but too lazy to fix rn
        new_user = JSON.stringify({id: 1, username: username, password: password});
        console.log(new_user)
        $.ajax({
            url:'http://127.0.0.1:8000/users/',
            type: 'POST',
            contentType: "application/json; charset=UTF-8",
            data: new_user,
            success: function (response) {
                console.log("response ", response)
                console.log("response.id ", response.id)
            },
            error: function (error) {
                console.log(error)
            }
        })
        event.preventDefault();
    });
})