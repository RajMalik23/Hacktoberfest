document.querySelector('form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form submission
  
    var username = document.querySelector('input[name="usr"]').value;
  
    if (username.trim() === "") {
      alert("Please enter a username.");
    } else {
      // Perform your login logic here
      alert("Login successful!");
      // Redirect to another page or perform other actions
    }
  });
  