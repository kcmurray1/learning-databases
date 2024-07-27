class Category
{
    constructor(name, value)
    {
        this.name = name;
        this.value = value;

        this.element = document.createElement("li");
        this.element.className = "filter-item";

        // Checkbox
        let checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.name = this.name;
        checkbox.value = this.value;
        checkbox.id = this.name;

        // Label
        let checkboxLabel = document.createElement("label");
        checkboxLabel.htmlFor = checkbox.id;
        checkboxLabel.textContent = this.name;
        
        this.element.appendChild(checkbox);
        this.element.appendChild(checkboxLabel);
    }
}