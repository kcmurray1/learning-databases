class InputTextField
{
    constructor(label, id)
    {
        this.label = label;

        this.element = document.createElement("form")
        this.element.className = "inputTextField"
        
        this.labelElement = document.createElement("label")
        this.labelElement.textContent = this.label
        this.element.appendChild(this.labelElement)
        this.element.innerHTML += "<br>"


        this.element.appendChild(document.createElement("input"))

    }
}