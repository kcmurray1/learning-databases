class Book 
{
    constructor (author, title, description) 
    {
        this.author = author;
        this.title = title;
        this.description = description

        //Create list item element
        this.element = document.createElement('li');
        this.element.className = 'book';

        //Create inner html
        const card = document.createElement('div')
        card.className = "card book-content";

        // Create the <div> element with the class 'card-img-top' and style
        const cardImgTop = document.createElement('div');
        cardImgTop.className = 'card-img-top';
        cardImgTop.style.textAlign = 'center';

        // Create the <p> element for the title inside 'card-img-top'
        const titleElement = document.createElement('p');
        titleElement.textContent = `${this.title} by ${this.author}`;

        // Append the title <p> to the 'card-img-top' <div>
        cardImgTop.appendChild(titleElement);

        // Create the <div> element with the class 'card-body'
        const cardBody = document.createElement('div');
        cardBody.className = 'card-body';

        // Create the <p> element for the content inside 'card-body'
        const content = document.createElement('p');
        content.className = 'card-text';
        content.textContent = this.description;

        // Append the content <p> to the 'card-body' <div>
        cardBody.appendChild(content);

        // Append 'card-img-top' and 'card-body' to the main 'card' <div>
        card.appendChild(cardImgTop);
        card.appendChild(cardBody);

        // Append the 'card' <div> to the <li> element
        this.element.appendChild(card);
    }
}