const grey_btn = document.getElementById("grey");
const white_btn = document.getElementById("white");
const blue_btn = document.getElementById("blue");
const yellow_btn = document.getElementById("yellow");

grey_btn.addEventListener("click", function () {
  document.body.style.backgroundColor = "grey";
});

white_btn.addEventListener("click", function () {
  document.body.style.backgroundColor = "white";
});

blue_btn.addEventListener("click", function () {
  document.body.style.backgroundColor = "blue";
});

yellow_btn.addEventListener("click", function () {
  document.body.style.backgroundColor = "yellow";
});
