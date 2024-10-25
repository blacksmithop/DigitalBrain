document.addEventListener('DOMContentLoaded', () => {
    let simplemde;

    const addButton = document.getElementById('add-button');
    const editorContainer = document.getElementById('editor-container');
    const titleInput = document.getElementById('title-input');

    // Initialize SimpleMDE editor when 'Add' is clicked
    addButton.addEventListener('click', () => {
        if (!simplemde) {
            simplemde = new SimpleMDE({ element: document.getElementById("markdown-editor") });
        }
        editorContainer.style.display = (editorContainer.style.display === 'none') ? 'block' : 'none';
    });

    // Saving the markdown content
    const saveButton = document.getElementById('save-button');
    saveButton.addEventListener('click', () => {
        const title = titleInput.value;
        const markdownContent = simplemde.value(); // Get markdown content from editor
        if (title && markdownContent) {
            console.log("Saved Markdown Content: ", { title, code: markdownContent });
            titleInput.value = ''; // Clear the input after saving
            simplemde.value(''); // Clear the editor after saving
            editorContainer.style.display = 'none';
        }
    });

    // Fetch knowledge base data
    function loadKnowledgeBase() {
        fetch('https://knowledge.abhinavkm.com/load_knowledge_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({})
        })
        .then(response => response.json())
        .then(data => displayKnowledgeBase(data.DevOpsTools)) // Adjust according to response structure
        .catch(error => console.error('Error loading knowledge base:', error));
    }

    // Generate the knowledge base structure
    function displayKnowledgeBase(data) {
        const baseContainer = document.getElementById('knowledge-base');
        const ul = document.createElement('ul');
        baseContainer.appendChild(ul);

        data.forEach(category => {
            const categoryLi = createExpandableItem(category.name, 'category', category.description);
            ul.appendChild(categoryLi);

            const examplesUl = document.createElement('ul');
            examplesUl.classList.add('collapsible');

            category.examples.forEach(example => {
                const exampleLi = createExpandableItem(example.title, 'example', example.code);
                examplesUl.appendChild(exampleLi);
            });

            categoryLi.appendChild(examplesUl);
            categoryLi.querySelector('.expander').addEventListener('click', () => {
                toggleVisibility(examplesUl);
                toggleDescription(categoryLi, category.description); 
            });
        });
    }

    // Create expandable item
    function createExpandableItem(name, type, content = null) {
        const li = document.createElement('li');
        const div = document.createElement('div');
        div.classList.add('expander');

        const icon = document.createElement('i');
        icon.classList.add(type === 'category' ? 'fas' : 'far', 'fa-folder');
        div.appendChild(icon);

        const span = document.createElement('span');
        span.textContent = name;
        div.appendChild(span);

        li.appendChild(div);

        if (type === 'category') {
            const descriptionDiv = document.createElement('div');
            descriptionDiv.classList.add('description');
            descriptionDiv.style.display = 'none';
            descriptionDiv.textContent = content;
            li.appendChild(descriptionDiv);
        } else if (type === 'example') {
            div.addEventListener('click', () => showModal(name, content));
        }

        return li;
    }

    // Show modal with markdown code and copy button
    function showModal(title, code) {
        const modal = document.createElement('div');
        modal.classList.add('modal');
        
        const modalContent = document.createElement('div');
        modalContent.classList.add('modal-content');

        const closeButton = document.createElement('span');
        closeButton.classList.add('close-button');
        closeButton.innerHTML = '&times;';
        closeButton.onclick = () => modal.remove();

        // Render markdown content using 'marked' and assign to a <pre> block
        const pre = document.createElement('pre');
        pre.innerHTML = marked(code); // Render markdown properly

        const copyIcon = document.createElement('span');
        copyIcon.innerHTML = '📋';
        copyIcon.classList.add('copy-icon');
        copyIcon.onclick = () => {
            copyToClipboard(pre.innerText);
        };

        modalContent.appendChild(closeButton);
        modalContent.appendChild(copyIcon);
        modalContent.appendChild(pre);
        modal.appendChild(modalContent);
        document.body.appendChild(modal);
    }

    function copyToClipboard(text) {
        const textarea = document.createElement('textarea');
        textarea.value = text;
        document.body.appendChild(textarea);
        textarea.select();
        document.execCommand('copy');
        document.body.removeChild(textarea);
    }

    // Toggle visibility of an element
    function toggleVisibility(element) {
        element.classList.toggle('visible');
    }

    // Toggle the description visibility
    function toggleDescription(li, description) {
        const descriptionDiv = li.querySelector('.description');
        descriptionDiv.style.display = descriptionDiv.style.display === 'none' ? 'block' : 'none';
    }

    // Load the knowledge base data when the page loads
    loadKnowledgeBase();
});
