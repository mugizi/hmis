document.querySelectorAll('.patient-name').forEach(item => {
    item.addEventListener('click', event => {
        event.preventDefault();
        var patientName = item.getAttribute('data-name');
        var patientId = item.getAttribute('data-id');
        
        document.getElementById('patientName').textContent = patientName;
        document.getElementById('patientId').value = patientId;

        // Fetch the form via AJAX
        fetch("{% url 'patients:load_provided_service_form' %}")
            .then(response => response.json())
            .then(data => {
                document.getElementById('formContainer').innerHTML = data.html;
                document.getElementById('serviceModal').classList.remove('hidden');
            });
    });
});

document.querySelector('.close-modal').addEventListener('click', () => {
    document.getElementById('serviceModal').classList.add('hidden');
});
