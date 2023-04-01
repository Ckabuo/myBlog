// FUNCTION FOR SEARCH
function search_blog() {
  let input = document.getElementById("search").value;
  input = input.toLowerCase();
  let x = document.getElementsByClassName("blog_post");

  for (i = 0; i < x.length; i++) {
    if (!x[i].innerHTML.toLowerCase().includes(input)) {
      x[i].style.display = "none";
    } else {
      x[i].style.display = "block";
    }
  }
}

// Get the contact form
const subscribeForm = document.getElementById("subscribe");

// Get the form inputs
let emailInput = document.getElementById("email");

// Add a submit event listener to the contact form
subscribeForm.addEventListener("submit", function(event) {
  event.preventDefault();

  // Get the input values
  let email = emailInput.value;

  // Validate the input values
  if (email === "") {
    alert("Please enter your email");
    return;
  }

  // Send the message
  alert("Thank you for Subscribing, We will be in touch with you soon.");

  // Clear the form inputs
  emailInput.value = "";
});

// FUNCTION FOR LIKES AND LIKES COUNT
let clicks = 0;

function myFunction(x) {
  // clicks++;
  // clicks = clicks === 0 ? 1 : 0;
  x.classList.toggle("fa-solid");
  x.classList.toggle("text-danger");
  let likesCount = x.nextSibling;
  if (likesCount.innerHTML == "1") {
    likesCount.innerHTML = --clicks;
  } else {
    likesCount.innerHTML = ++clicks;
  }
}

// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction();
};

function scrollFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  document.body.scrollTop = 0; // For Safari
  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
}

// VINcheck page
function vinCheckMethods(id) {
  let toggleButton = document.getElementById(id);
  toggleButton.classList.add("select");
  if (id === "toggle1") {
    let toggleButton2 = document.getElementById("toggle2");
    toggleButton2.classList.remove("select");
  } else {
    let toggleButton1 = document.getElementById("toggle1");
    toggleButton1.classList.remove("select");
  }
}

/*
//Blog post Automatic Upload

function uploadBlogPost() {
  // Get the automotive content from the OpenAI API
  fetch('https://api.openai.com/v1/chats/chat?prompt=category:automotive')
    .then(res => res.json())
    .then(({ data }) => {
      // Save the content to a file
      const file = new File([data[0].text], './post/automotive.txt', { type: 'text/plain' });

      // Read the file and upload the content to your blog platform
      const reader = new FileReader();
      reader.onload = function() {
        const content = reader.result;
        const title = 'Automotive';
        uploadToBlogPlatform(title, content);
      };
      reader.readAsText(file);
    });
}

function scheduleBlogPostUpload() {
  // Calculate the time until midnight
  const now = new Date();
  const midnight = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1, 0, 0, 0);
  const timeUntilMidnight = midnight - now;

  // Set a timeout to run the upload function at midnight
  setTimeout(uploadBlogPost, timeUntilMidnight);

  // Set an interval to run the upload function every midnight
  setInterval(uploadBlogPost, 86400000); // 86400000 is the number of milliseconds in one day
}

// Run the scheduling function when the page loads
window.addEventListener('load', scheduleBlogPostUpload);
*/