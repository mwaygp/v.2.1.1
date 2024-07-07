// search for word, highlight the word yellow and show clear box in the screen to clear the word
var originalContent = document.body.innerHTML; // Save the original content of the body

function search() {
    var searchTerm = document.getElementById('searchInput').value.toLowerCase();
    var bodyContent = originalContent; // Use the original content for searching
    var content = bodyContent.toLowerCase();
    var matches = content.match(new RegExp(searchTerm, 'g'));

    // Remove previous highlights
    document.body.innerHTML = bodyContent.replace(/<span class="highlight">(.*?)<\/span>/g, '$1');

    if (matches) {
        alert('Found ' + matches.length + ' occurrences of "' + searchTerm + '".');

        // Highlight the searched term
        var highlightedContent = document.body.innerHTML.replace(new RegExp(searchTerm, 'gi'), function(match) {
            return '<span class="highlight">' + match + '</span>';
        });
        document.body.innerHTML = highlightedContent;

        // Show the clear modal
        document.getElementById('clearModal').style.display = 'block';
    } else {
        alert('No matches found for "' + searchTerm + '".');
    }
}

function clearHighlights() {
    // Restore the original content
    document.body.innerHTML = originalContent;
    document.getElementById('searchInput').value = ''; // Clear the search input

    // Hide the clear modal
    document.getElementById('clearModal').style.display = 'none';
}

function closeModal() {
    // Hide the clear modal
    document.getElementById('clearModal').style.display = 'none';
}

function redirectToPage() {
    window.location.href = "login.html";
}

function redirectToSignup() {
    window.location.href = "signup.html"; // Replace with your target signup page
}



