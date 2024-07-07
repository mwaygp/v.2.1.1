function openModal() {
    document.getElementById("consultationModal").style.display = "block";
}

function closeModal() {
    document.getElementById("consultationModal").style.display = "none";
}

// Close the modal when the user clicks outside of it
window.onclick = function(event) {
    var modal = document.getElementById("consultationModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function searchFAQs() {
    var input, filter, faqContent, faqItems, question, i, txtValue;
    input = document.getElementById('faq-search');
    filter = input.value.toUpperCase();
    faqContent = document.getElementsByClassName('faq-content')[0];
    faqItems = faqContent.getElementsByClassName('faq-item');

    clearHighlights(); // Clear previous highlights

    for (i = 0; i < faqItems.length; i++) {
        question = faqItems[i].getElementsByTagName('h4')[0];
        txtValue = question.textContent || question.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
            faqItems[i].style.display = "";
            highlightText(question, input.value); // Highlight the search term
        } else {
            faqItems[i].style.display = "none";
        }
    }
}

function highlightText(element, text) {
    var innerHTML = element.innerHTML;
    var index = innerHTML.toUpperCase().indexOf(text.toUpperCase());
    if (index >= 0) {
        innerHTML = innerHTML.substring(0, index) + "<span class='highlight'>" + innerHTML.substring(index, index + text.length) + "</span>" + innerHTML.substring(index + text.length);
        element.innerHTML = innerHTML;
    }
}

function clearHighlights() {
    var highlightedElements = document.querySelectorAll('.highlight');
    highlightedElements.forEach(function(element) {
        element.classList.remove('highlight');
        element.outerHTML = element.innerHTML; // Remove span but keep the text
    });
}

function clearSearch() {
    var input = document.getElementById('faq-search');
    input.value = '';
    searchFAQs(); // Re-run the search function to reset the display
}

document.getElementById('clear-search').addEventListener('click', clearSearch);

