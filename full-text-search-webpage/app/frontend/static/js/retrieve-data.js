function getBookData()
{
    fetch('/database')
        .then((response) => response.json())
        //Request SUCCESS
        .then((packet) => {
            console.log(packet["data"]);
           if (packet["data"] != "undefined")
           {
            let idk = document.getElementById("results");
            for(let entry of packet["data"])
            {
                let [price, title, category, month, year, description] = entry;
                idk.append(new Book("Author", title, description).element);
            
            }
           }
        })
        //Request FAILURE
        .catch((error) =>{
            console.error('Error:', error);
        });
}