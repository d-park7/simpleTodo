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
        event.preventDefault();
    });
})