function getBookData()
{
    fetch('/database')
        .then((response) => response.json())
        //Request SUCCESS
        .then((packet) => {
           console.log(packet["data"]);
           if (packet["data"].length != 0)
           {
            let idk = document.getElementById("results");
            for(let entry of packet["data"])
            {
                let [authors, price, title, month, year, description] = entry;
                idk.append(new Book(authors, title, description).element);
            
            }
           }
        })
        //Request FAILURE
        .catch((error) =>{
            console.error('Error:', error);
        });
}

function getFilterData()
{
    fetch('/database/filters')
        .then((response) => response.json())
        .then((packet) => {
            if (packet["data"].length != 0)
            {
                let categories = document.getElementsByClassName("filter-list");
                console.log(categories);
                for(let category of packet["data"])
                {
                    let [category_id, category_name] = category
                    categories[0].append(new Category(category_name, category_id).element);
                }
            }
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}