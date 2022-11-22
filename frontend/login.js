$(function() {
    $("a").each((index, element) => {
        if ($(element).prop("href") == window.location.href) {
            $(element).addClass("active");
        }
    });

    $("form").submit((event) => {
        event.preventDefault();

        const formData = new FormData($("form")[0]);
        console.log(typeof(formData.get("username")))
        if (formData.get("username") === "") {
            alert("Put a username");
        }
        if (formData.get("password") === "") {
            alert("Put a password");
        }

        console.log(formData.get("username"))
        console.log(formData.get("password"))
        
        $.ajax({
            url:'http://127.0.0.1:8000/token',
            type: 'POST',
            data: formData,
            contentType: "application/x-www-form-urlencoded",
            success: function (response) {
                console.log("success")
            },
            error: function (error) {
                console.log(error)
            }
        })
    });
})