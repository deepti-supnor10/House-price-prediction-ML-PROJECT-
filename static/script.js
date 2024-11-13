document.querySelectorAll('.option-button').forEach(button => {
    button.addEventListener('click', function() {
        const value = this.getAttribute('data-value');
        const inputId = this.closest('.option-group').querySelector('input[type="hidden"]').id;
        document.getElementById(inputId).value = value;

        // Highlight selected button
        this.parentNode.querySelectorAll('.option-button').forEach(btn => btn.classList.remove('selected'));
        this.classList.add('selected');
    });
});
