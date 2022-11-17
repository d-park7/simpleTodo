$(function() {
    $("a").each((index, element) => {
        if ($(element).prop("href") == window.location.href) {
            $(element).addClass("active");
        }
    });

    $("form").submit((event) => { 
        let val_one = event.currentTarget[0].value;
        if (val_one == "") {
            alert("Put a todo first");
        }
        
        let todo = $("<li></li>").text(val_one);
        $("#list").append(todo)
        event.preventDefault();
    });
});