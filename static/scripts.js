function userData(){
    var tableBody = document.getElementById('tableBody');
    tableBody.innerHTML = '';

    var url = 'http://127.0.0.1:8000/api/datalist/';

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
        console.log(data)

        var table = data;
        for(var i in table){
            var displayTable = `
            <tr>
            <th scope="row">${parseInt(i) + 1}</th>
            <td>${data[i].date}</td>
            <td>${data[i].description}</td>
            <td>${data[i].amount}</td>
            <td>${data[i].category}</td>
            </tr>`;
        tableBody.innerHTML += displayTable;
        }
    })
    .catch(error => console.error('Error fetching data:', error));
}