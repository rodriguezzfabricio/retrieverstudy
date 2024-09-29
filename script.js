document.addEventListener('DOMContentLoaded', function() {
    const subjectSelect = document.getElementById('subject');
    const courseSelect = document.getElementById('course');
    const queueUpBtn = document.getElementById('queue-up-btn');

    // Fetch subjects
    fetch('/api/subjects')
        .then(response => response.json())
        .then(data => {
            data.forEach(subject => {
                let option = document.createElement('option');
                option.value = subject.id;
                option.textContent = subject.name;
                subjectSelect.appendChild(option);
            });
        });

    // Fetch courses based on selected subject
    subjectSelect.addEventListener('change', function() {
        const subjectId = this.value;

        courseSelect.innerHTML = '<option value="">--Select a Course--</option>';
        if (subjectId) {
            fetch(`/api/courses/${subjectId}`)
                .then(response => response.json())
                .then(data => {
                    data.forEach(course => {
                        let option = document.createElement('option');
                        option.value = course.id;
                        option.textContent = course.name;
                        courseSelect.appendChild(option);
                    });
                });
        }

        validateForm();
    });

    courseSelect.addEventListener('change', validateForm);

    function validateForm() {
        if (subjectSelect.value && courseSelect.value) {
            queueUpBtn.disabled = false;
            queueUpBtn.classList.add('enabled');
        } else {
            queueUpBtn.disabled = true;
            queueUpBtn.classList.remove('enabled');
        }
    }
});