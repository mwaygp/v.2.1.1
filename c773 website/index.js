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