const timetable_ = document.querySelector('#timetable_');

myStorage = window.sessionStorage;

const getTimetable = () => {
    document.querySelector('#content').innerHTML = 'Here is timetable (in my imagination)';
    cookies_data = sessionStorage.getItem('cookies_data');
    csrfcookie_ = sessionStorage.getItem('csrfcookie');
    fetch(url = '../api/timetable', {
        method: 'POST',
        mode: 'cors',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfcookie_
        },
        body: cookies_data
    }).then(response => response.json()).then(data => {
        console.log(data)
    })
}

timetable_.addEventListener('click', getTimetable);