function userchangeinf(name) {
    console.log(name)
    value = document.getElementById(`${name}`).value
    url = '/'
    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({
            'name': name,
            'value': value
        })
    })
        .then((response) => {
            response.json().then((data) => {
                console.log(data)

            })
        })

}