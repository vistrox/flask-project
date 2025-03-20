
// สถานะการจองของอุปกรณ์
let devices = {
  1: { isBooked: false },
  2: { isBooked: false },
  3: { isBooked: false }
};

function bookDevice(deviceId) {
  const statusElement = document.getElementById(`status${deviceId}`);
  const deviceButton = document.querySelector(`#item${deviceId} .device`);

  if (!devices[deviceId].isBooked) {
    // หากอุปกรณ์ยังไม่ถูกจอง
    devices[deviceId].isBooked = true;
    statusElement.textContent = "ถูกจองแล้ว";
    statusElement.classList.remove("available");
    statusElement.classList.add("booked");
    deviceButton.disabled = true; // ปิดการใช้งานปุ่ม
  } else {
    // หากอุปกรณ์ถูกจองแล้ว
    alert("อุปกรณ์นี้ถูกจองแล้ว");
  }
}