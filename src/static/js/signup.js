// Password Verification for signup.html

const verifySignup = (form) => {
  const match = form.password.value === form.password_verify.value;

  if (!match) {
    const fail_div = document.getElementById("password_fail");

    if (!fail_div.childElementCount) {
      const message = document.createElement("p"); // Add message to failed_div
      message.innerText = "Please make sure your passwords match";
      message.className = "message";

      fail_div.appendChild(message);
    }
  }

  return match;
};
