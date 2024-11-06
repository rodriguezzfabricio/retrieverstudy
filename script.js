document.addEventListener('DOMContentLoaded', function() {
    const subjectSelect = document.getElementById('subject');
    const courseSelect = document.getElementById('course');
    const queueUpBtn = document.getElementById('queue-up-btn');

    // Event listener for the subject dropdown change
    subjectSelect.addEventListener('change', function() {
        const selectedSubject = this.value;

        // Clear current course options
        courseSelect.innerHTML = '<option value="">--Select a Course--</option>';

        // Populate course options based on selected subject
        if (selectedSubject) {
            // Select all course options that are already rendered
            const allCourses = document.querySelectorAll('#course option[data-subject]');
            allCourses.forEach(courseOption => {
                // If the course's subject matches the selected subject, add it to the course dropdown
                if (courseOption.getAttribute('data-subject') === selectedSubject) {
                    courseSelect.appendChild(courseOption.cloneNode(true));
                }
            });
        }

        // Validate the form to check if a subject and course are selected
        validateForm();
    });

    // Event listener for the course dropdown change
    courseSelect.addEventListener('change', validateForm);

    // Function to validate the form
    function validateForm() {
        if (subjectSelect.value && courseSelect.value) {
            // Enable the "Queue Up" button if both subject and course are selected
            queueUpBtn.disabled = false;
            queueUpBtn.classList.add('enabled');
        } else {
            // Disable the "Queue Up" button if either subject or course is not selected
            queueUpBtn.disabled = true;
            queueUpBtn.classList.remove('enabled');
        }
    }
});
