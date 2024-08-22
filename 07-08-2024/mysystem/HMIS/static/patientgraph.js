const ctx = document.getElementById('patientdeatils').getContext('2d');

fetch('/api/day-counts/')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        console.log(data); // Log the data to ensure it's correct

        const labels = data.map(item => item.day_of_week);
        const values = data.map(item => item.count);

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'No of Patients',
                    data: values,
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    })
    .catch(error => console.error('Error fetching data:', error));


