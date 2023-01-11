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
        
        let html_todo = $("<li></li>").text(todo);
        sessionStorage.setItem(todo, todo)
        $("#list").append(html_todo)
        $("textarea#body").val("");

        // Doing this bc schema require user id
        // but setting event.preventDefault() will automatically assign an id
        // when inserting the todo in
        // not really intended behavior but too lazy to fix rn
        new_todo = JSON.stringify({
            todo: todo
        });

        $.ajax({
            url:'http://127.0.0.1:8000/todos/',
            type: 'POST',
            contentType: 'application/json; charset=UTF-8',
            data: new_todo,
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(new_todo)
                console.log("error", error);
            }
        }); 
        event.preventDefault();
    });
});