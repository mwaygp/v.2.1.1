function search() {
    var searchTerm = document.getElementById('searchInput').value.toLowerCase();
    var bodyContent = document.body.innerHTML;
    var content = document.body.innerText.toLowerCase();
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
    } else {
        alert('No matches found for "' + searchTerm + '".');
    }
}

// script to clear search  

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
    } else {
        alert('No matches found for "' + searchTerm + '".');
    }
}

function clearHighlights() {
    // Restore the original content
    document.body.innerHTML = originalContent;
    document.getElementById('searchInput').value = ''; // Clear the search input
}


</div>
<!-- second button clear option  -->
<!--         <div class="search-bar">
    <input type="text" id="searchInput" placeholder="Search...">
    <button type="button" onclick="search()">Search</button>
</div>
<div id="searchTermDisplay"></div>
<div class="clear-button-container">
    <button type="button" onclick="clearHighlights()">Clear</button>
</div> -->

</header>

<section id="home">
<img src="home.jpg" alt="Beautiful Beach">
<div class="text-box">
    <h2>What We Offer</h2>
    <p>Are you looking for a perfect vacation island to visit? Well, you are in luck! Taniti is the perfect destination spot! You are met with a picture-perfect beach to relax at numerous beautiful spots and resorts to have the time of your life! Come to Taniti and forget all of your worries!</p>
</div>
<!-- <img src="home.jpg" alt="Beautiful Beach"> -->





/* Footer styles */
footer {
    background-color: #4CAF50; /* Set footer background color */
    color: white; /* Set footer text color */
    padding: 5px 0; /* Reduce padding */
    margin-top: auto; /* Push footer to the bottom */
}

.footer-content {
    display: flex; /* Use flexbox for layout */
    align-items: center; /* Center items vertically */
    justify-content: space-between; /* Space items evenly */
    max-width: 1100px; /* Set maximum width */
    margin: 0 auto; /* Center the footer content horizontally */
    padding: 0px 0; /* Reduce padding */
    background-color: #4CAF50; /* Ensure the background color is applied to this container */
    border-radius: 8px; /* Add border radius for a smoother look */
}

.footer-content .social-media {
    display: flex; /* Use flexbox for layout */
    align-items: center; /* Center icons vertically */
}

.footer-content nav {
    flex: 1; /* Allow navigation to grow */
    display: flex; /* Use flexbox for layout */
    justify-content: center; /* Center navigation links */
    margin-left: 30px; /* Push the nav links more to the left */
}

.footer-content nav ul {
    list-style: none; /* Remove list bullets */
    padding: 0; /* Remove default padding */
    margin: 0; /* Remove default margin */
    display: flex; /* Use flexbox for layout */
    justify-content: center; /* Center navigation links */
    align-items: center; /* Center navigation vertically */
}

.footer-content nav ul li {
    margin: 0 5px; /* Reduce margin between navigation links */
}

.footer-content nav ul li a {
    color: white; /* Set navigation link color */
    text-decoration: none; /* Remove underline */
    font-weight: bold; /* Set navigation link font weight */
    font-size: 12px; /* Reduce font size */
}

.footer-content nav ul li a:hover {
    text-decoration: underline; /* Add underline on hover */
}

.footer-content .social-media a {
    color: white; /* Set icon color */
    text-decoration: none; /* Remove underline */
    margin: 0 5px; /* Reduce margin between icons */
    font-size: 12px; /* Reduce font size */
}

/* Align the copyright text to the right */
.footer-content .copyright {
    text-align: right; /* Align text to the right */
    margin-left: auto; /* Push the copyright text to the far right */
    white-space: nowrap; /* Prevent text from wrapping */
    font-size: 12px; /* Reduce font size */
}