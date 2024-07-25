// Display 10 initial cards
document.addEventListener("DOMContentLoaded", function()
{
    
    let idk = document.getElementById("results");
    for(let i =0; i <10; i++)
    {   
        let description = "The Greatest book ever!";
        if (i == 3)
        {
            description = `This is a really long paragraphe  In recent years, many people have become increasingly aware of the need for physical fitness.* Almost everywhere people turn, whether it is to a newsstand, television or billboard,* advise for guarding and improving health bombards them. Although much of this advice is commercially motivated by those eager to sell vitamins, natural foods and reducing gimmicks,* some of it, especially those advocating a regular exercise program, merits serious attention. Such a program, if it consists of at least 30 minutes three times a week and if a person’s physician approves it,* provides numerous benefits. Regular exercise releases tension, improves appearance, and increases stamina.*
             In recent years, many people have become increasingly aware of the need for physical fitness.* Almost everywhere people turn, whether it is to a newsstand, television or billboard,* advise for guarding and improving health bombards them. Although much of this advice is commercially motivated by those eager to sell vitamins, natural foods and reducing gimmicks,* some of it, especially those advocating a regular exercise program, merits serious attention. Such a program, if it consists of at least 30 minutes three times a week and if a person’s physician approves it,* provides numerous benefits. Regular exercise releases tension, improves appearance, and increases stamina.*
             In recent years, many people have become increasingly aware of the need for physical fitness.* Almost everywhere people turn, whether it is to a newsstand, television or billboard,* advise for guarding and improving health bombards them. Although much of this advice is commercially motivated by those eager to sell vitamins, natural foods and reducing gimmicks,* some of it, especially those advocating a regular exercise program, merits serious attention. Such a program, if it consists of at least 30 minutes three times a week and if a person’s physician approves it,* provides numerous benefits. Regular exercise releases tension, improves appearance, and increases stamina.*
              In recent years, many people have become increasingly aware of the need for physical fitness.* Almost everywhere people turn, whether it is to a newsstand, television or billboard,* advise for guarding and improving health bombards them. Although much of this advice is commercially motivated by those eager to sell vitamins, natural foods and reducing gimmicks,* some of it, especially those advocating a regular exercise program, merits serious attention. Such a program, if it consists of at least 30 minutes three times a week and if a person’s physician approves it,* provides numerous benefits. Regular exercise releases tension, improves appearance, and increases stamina.*`;
        }
            
        let x  = new Book("Me", "Hello World", description);
        idk.append(x.element);
    }
});
