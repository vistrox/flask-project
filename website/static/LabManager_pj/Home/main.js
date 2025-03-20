const menuBtn = document.getElementById("menu-btn");
const navLinks = document.getElementById("nav-links");
const menuBtnIcon = menuBtn.querySelector("i");

menuBtn.addEventListener("click", () => {
  navLinks.classList.toggle("open");

  const isOpen = navLinks.classList.contains("open");
  menuBtnIcon.setAttribute("class", isOpen ? "ri-close-line" : "ri-menu-line");
});

// let seats = document.querySelector(".all-seats");
// for (let i = 0; i < 59; i++) {
//     let randint = Math.floor(Math.random() * 2);
//     let booked = randint === 1 ? "booked" : "";

//     seats.insertAdjacentHTML(
//         "beforeend",
//         `<input type="checkbox" name="computers" id="s${i + 2}"/>
//         <label for="s${i + 2}" class="seat ${booked}"></label>`
//     )
// }

