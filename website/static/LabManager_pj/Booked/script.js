// let seats = document.querySelector(".all-seats");
//  for (let i = 0; i < 19; i++) {
//      let randint = Math.floor(Math.random() * 2);
//      let booked = randint === 1 ? "booked" : "";

//     seats.insertAdjacentHTML(
//         "beforeend",
//         `<input type="checkbox" name="computers" id="c${i + 2}"/>
//         <label for="c${i + 2}" class="seat ${booked}"></label>`
//     )
// }

// let computers = seats.querySelectorAll("input");

// computers.forEach((com) => {
//     com.addEventListener("change", () => {
//         let count = document.querySelector(".count").innerHTML;

//         count = Number(count);

//         if (com.checked) {
//             count += 1;
//         } else {
//             count -= 1;
//         }

//         document.querySelector(".count").innerHTML = count;
//     });
// });

let seats = document.querySelector(".all-seats");

for (let i = 0; i < 21; i++) {  // ปรับจำนวนที่นั่งเป็น 21
    // ทุกที่นั่งจะเป็น "available" โดยไม่มีการจอง
    seats.insertAdjacentHTML(
        "beforeend",
        `<input type="checkbox" name="computers" id="c${i + 1}" />
        <label for="c${i + 1}" class="seat"></label>`
    );
}

// ฟังก์ชันในการจัดการการเลือกที่นั่ง
seats.addEventListener('change', (event) => {
    if (event.target.type === 'checkbox') {
        let seatLabel = event.target.nextElementSibling;

        // ถ้าเลือกที่นั่งแล้วให้เปลี่ยนสีให้เป็นสีเทา
        if (event.target.checked) {
            seatLabel.classList.add("booked");
        } else {
            seatLabel.classList.remove("booked");
        }
    }
});



