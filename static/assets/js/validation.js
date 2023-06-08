function validateForm(){var e=document.getElementById("email"),a=e.value.trim();return!!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(a)||(alert("Please enter a valid email address."),e.focus(),!1)}
