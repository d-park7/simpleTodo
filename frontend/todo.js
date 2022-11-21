$(function() {
    $("a").each((index, element) => {
        if ($(element).prop("href") == window.location.href) {
            $(element).addClass("active");
        }
    });

    $("form").submit((event) => { 
        let todo = event.currentTarget[0].value;
        if (todo == "") {
            alert("Put a todo first");
        }
        
        let html_todo = $("<li></li>").text(val_one);
        $("#list").append(html_todo)
        $("textarea#body").val("");
        new_todo = JSON.stringify({ id: })
        $.ajax({
            url:'http://127.0.0.1:8000/todos/',
            type: 'POST',
            contentType: 'application/json; charset=UTF-8',
            data: JSON.stringify(todo),
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        })
        event.preventDefault();
    });
});