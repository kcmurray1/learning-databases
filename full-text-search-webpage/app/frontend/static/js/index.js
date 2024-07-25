function foo ()
{
    fetch('/database')
        .then((response) => response.json())
        //Request SUCCESS
        .then((packet) => {
           console.log(packet);
            // for(let data of packet){
            //     console.log(data);
            // }
            
        })
        //Request FAILURE
        .catch((error) =>{
            console.error('Error:', error);
        });
}
console.log("Hello World");
// setInterval(()=> {foo()}, 5000);