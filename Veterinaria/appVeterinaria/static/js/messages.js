document.addEventListener("DOMContentLoaded", function() {
    const djangoMessages = JSON.parse(document.getElementById("django-messages").textContent);
    djangoMessages.forEach(message => {
        alert(message.text);  // O usa un modal, toast, etc., en lugar de alert.
    });
});
