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
        new_user = JSON.stringify({username: username, password: password});

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