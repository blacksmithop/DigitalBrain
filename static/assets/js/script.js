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
document.getElementById("add-category-form").addEventListener("submit", async (e) => {
    e.preventDefault();
    console.log("Form submission started");

    // Build the payload
    const payload = {
        _id: Date.now().toString(), // Temporary unique ID for example
        name: document.getElementById("name").value,
        description: document.getElementById("description").value,
        favicon: document.getElementById("favicon").value,
        examples: [
            {
                title: "Example",
                code: document.getElementById("example").value
            }
        ]
    };

    console.log("Payload to be sent:", payload);

    try {
        // Send data to the server
        const response = await fetch("http://localhost:8080/load_knowledge_data", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        if (response.ok) {
            console.log("Data successfully sent to /load_knowledge_data");
            alert("Category added successfully!");
            addModal.classList.remove("show-modal");
            document.getElementById("add-category-form").reset();
        } else {
            console.error("Failed to add category. Status:", response.status);
        }
    } catch (error) {
        console.error("Error adding category:", error);
    }
});

// Perform search by fetching data from the API using POST request
async function performSearch() {
    const query = searchInput.value.trim();
    if (!query) {
        searchResults.innerHTML = "Please enter a search term.";
        searchResults.classList.add("show");
        return;
    }

    console.log("Performing search with query:", query);

    try {
        // POST request to load knowledge data
        const response = await fetch("http://localhost:8080/load_knowledge_data", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ query }) // Sending the search query as part of the body
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Data fetched from API:", data);
            renderResults(data);
        } else {
            console.error("Failed to fetch data. Status:", response.status);
            searchResults.innerHTML = "Failed to load data.";
        }
    } catch (error) {
        console.error("Error fetching data:", error);
        searchResults.innerHTML = "Error loading data.";
    }
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
        icon.src = result.favicon || "default-icon-path"; // Use a default icon if none provided
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
