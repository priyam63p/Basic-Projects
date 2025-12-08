const buttons = document.querySelector(".btn");
buttons.addEventListener("mouseover", (event) => {
  const x = event.pageX - buttons.offsetLeft;
  const y = event.pageY - buttons.offsetTop;

  buttons.style.setProperty("--xPos", x + "px");
  buttons.style.setProperty("--yPos", y + "px");
});
