function onSubmit() {
    let body = document.forms["todoForm"]["body"].value;
    if (body == "") {
        alert("Fill in the body");
        return false;
    }

    let list = document.getElementById('list');
    let listItem = document.createElement('li');
    listItem.appendChild(document.createTextNode(body));
    list.appendChild(listItem);
}