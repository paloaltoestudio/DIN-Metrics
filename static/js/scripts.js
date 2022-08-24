window.onload = function() {
    // Material Design Input function
    var inputs = document.querySelectorAll('.form-control');

    for (var i = 0; i < inputs.length; i++) {

        if (inputs[i].value != ''){
            inputs[i].parentElement.classList.add('is-focused');
        }

        inputs[i].addEventListener('focus', function(e) {
        this.parentElement.classList.add('is-focused');
        }, false);

        inputs[i].onkeyup = function(e) {
        if (this.value != "") {
            this.parentElement.classList.add('is-filled');
        } else {
            this.parentElement.classList.remove('is-filled');
        }
        };

        inputs[i].addEventListener('focusout', function(e) {
        if (this.value != "") {
            this.parentElement.classList.add('is-filled');
        }
        this.parentElement.classList.remove('is-focused');
        }, false);
    }
}