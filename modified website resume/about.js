document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('searchButton').addEventListener('click', function () {
        let searchText = document.getElementById('searchInput').value.trim().toLowerCase();
        highlightText(searchText);
    });

    document.getElementById('searchInput').addEventListener('input', function () {
        let searchText = this.value.trim().toLowerCase();
        highlightText(searchText);
    });
});

function highlightText(searchText) {
    let paragraphs = document.querySelectorAll('.info p');
    
    paragraphs.forEach(p => {
        let text = p.textContent.toLowerCase();
        if (text.includes(searchText) && searchText !== '') {
            let highlightedText = text.replace(
                new RegExp(searchText, 'gi'),
                match => `<span class="highlight">${match}</span>`
            );
            p.innerHTML = highlightedText;
        } else {
            p.innerHTML = text; // Reset original text
        }
    });
}







