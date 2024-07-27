function sendQuery(searchBar)
{
    console.log(searchBar.value);
}
function setupSearchBar()
{
    let searchBar = document.getElementById("search-bar");
    let idk = document.querySelectorAll("filter-item");

    searchBar.addEventListener("keypress", function(e)
    {
        if (e.key == "Enter")
        {
            sendQuery(searchBar);
            console.log(idk);
        }
    });
}