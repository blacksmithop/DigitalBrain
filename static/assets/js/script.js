// Dropdown Menu Toggle
const dropdownBtn = document.querySelector(".dropdown-btn");
const dropdownContent = document.querySelector(".dropdown-content");

dropdownBtn.addEventListener("click", () => {
    dropdownContent.classList.toggle("show");
});

// Search Button Click and Animation
const searchButton = document.getElementById("search-button");
const searchInput = document.getElementById("search-input");
const searchResults = document.getElementById("search-results");

searchButton.addEventListener("click", () => performSearch());
searchInput.addEventListener("keyup", (event) => {
    if (event.key === "Enter") performSearch();
});

// Elements for Modal
const addButton = document.getElementById("add-button");
const addModal = document.getElementById("add-modal");
const closeButton = document.querySelector(".close-button");

// Show modal when Add button is clicked
addButton.addEventListener("click", () => addModal.classList.add("show-modal"));

// Hide modal when close button or area outside modal content is clicked
closeButton.addEventListener("click", () => addModal.classList.remove("show-modal"));
addModal.addEventListener("click", (event) => {
    if (event.target === addModal) addModal.classList.remove("show-modal");
});

// Form submission for adding new category
document.getElementById("add-category-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const newCategory = {
        name: document.getElementById("name").value,
        description: document.getElementById("description").value,
        examples: [{ title: "Example", code: document.getElementById("example").value }],
        favicon: document.getElementById("favicon").value
    };
    console.log("New category added:", newCategory); // Mock adding

    // Close modal
    addModal.classList.remove("show-modal");
});

// Mock search function with dummy data for testing
async function performSearch() {
    const query = searchInput.value.trim();
    if (!query) {
        searchResults.innerHTML = "Please enter a search term.";
        searchResults.classList.add("show");
        return;
    }

    searchResults.innerHTML = `Searching for "${query}"...`;
    searchResults.classList.add("show");

    const mockData = [
        {
            name: "Docker",
            description: "Docker is a tool designed to make it easier to create, deploy, and run applications by using containers.",
            icon: "https://www.docker.com/favicon.ico",
            examples: [
                { title: "Introduction to Docker", code: "docker pull ubuntu" },
                { title: "Dockerfile Basics", code: "COPY package*.json ./" }
            ]
        }
    ];
    renderResults(mockData);
}

// Render search results with dropdown and collapsible examples
function renderResults(results) {
    searchResults.innerHTML = "";  
    searchResults.classList.add("show");

    results.forEach(result => {
        const resultItem = document.createElement("div");
        resultItem.className = "result-item";

        // Icon
        const icon = document.createElement("img");
        icon.className = "result-icon";
        icon.src = result.icon;
        icon.alt = `${result.name} icon`;

        // Content container
        const content = document.createElement("div");

        // Header
        const header = document.createElement("div");
        header.className = "result-header";
        header.textContent = result.name;

        // Description
        const description = document.createElement("div");
        description.className = "result-description";
        description.textContent = result.description;

        // Examples (collapsible)
        const examples = document.createElement("div");
        examples.className = "result-examples";
        result.examples.forEach(example => {
            const exampleTitle = document.createElement("p");
            exampleTitle.textContent = example.title;

            const exampleCode = document.createElement("pre");
            exampleCode.textContent = example.code;

            examples.appendChild(exampleTitle);
            examples.appendChild(exampleCode);
        });

        // Toggle button for examples
        const toggleButton = document.createElement("span");
        toggleButton.className = "example-toggle";
        toggleButton.textContent = "Show Examples";
        toggleButton.addEventListener("click", () => {
            examples.classList.toggle("show");
            toggleButton.textContent = examples.classList.contains("show") ? "Hide Examples" : "Show Examples";
        });

        // Dropdown for Edit/Delete options
        const dropdown = document.createElement("div");
        dropdown.className = "result-dropdown";
        dropdown.innerHTML = '⋮';
        
        const dropdownContent = document.createElement("div");
        dropdownContent.className = "result-dropdown-content";
        
        const editOption = document.createElement("a");
        editOption.href = "#";
        editOption.textContent = "Edit";
        
        const deleteOption = document.createElement("a");
        deleteOption.href = "#";
        deleteOption.textContent = "Delete";
        
        dropdownContent.appendChild(editOption);
        dropdownContent.appendChild(deleteOption);
        dropdown.appendChild(dropdownContent);

        // Append all parts to content container
        content.appendChild(header);
        content.appendChild(description);
        content.appendChild(toggleButton);
        content.appendChild(examples);

        // Append icon, content, and dropdown to result item
        resultItem.appendChild(icon);
        resultItem.appendChild(content);
        resultItem.appendChild(dropdown);

        // Append result item to search results container
        searchResults.appendChild(resultItem);
    });
}
