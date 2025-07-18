// Dynamic Reviews Loading
async function loadReviews() {
    const container = document.getElementById('reviews-container');
    if (!container) return;
    try {
        const res = await fetch('/api/review');
        const reviews = await res.json();
        container.innerHTML = '';
        reviews.forEach(r => {
            const stars = Array(Math.floor(r.rating)).fill('<i class="fas fa-star"></i>').join('') + (r.rating % 1 ? '<i class="fas fa-star-half-alt"></i>' : '');
            container.innerHTML += `
                <div class="bg-white p-6 rounded-lg shadow">
                    <div class="flex items-center mb-4">
                        <div class="w-12 h-12 rounded-full bg-gray-300 flex items-center justify-center mr-4">
                            <i class="fas fa-user text-gray-500 text-xl"></i>
                        </div>
                        <div>
                            <h4 class="font-semibold">${r.name}</h4>
                            <div class="flex text-yellow-400">${stars}</div>
                        </div>
                    </div>
                    <p class="text-gray-600">"${r.text}"</p>
                </div>
            `;
        });
    } catch (e) {
        container.innerHTML = '<p class="text-red-500">Failed to load reviews.</p>';
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadReviews();

    // Payment form handling
    document.getElementById('payment-form')?.addEventListener('submit', function(e) {
        e.preventDefault();
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        const plan = document.getElementById('plan').value;
        if (!email || !password) {
            alert('Please fill in all fields');
            return;
        }
        document.getElementById('payment-page').style.display = 'none';
        document.getElementById('processing-page').style.display = 'block';
        setTimeout(() => {
            alert('Payment successful! Your account details have been sent to your email.');
            window.location.href = '/';
        }, 3000);
    });

    // Handle plan selection from main page
    document.querySelectorAll('.plan-card button').forEach(button => {
        button.addEventListener('click', function() {
            document.getElementById('payment-page').style.display = 'block';
            document.getElementById('payment-page').scrollIntoView({behavior: 'smooth'});
        });
    });

    // FAQ accordion
    document.querySelectorAll('#faq button').forEach(button => {
        button.addEventListener('click', () => {
            const content = button.nextElementSibling;
            const icon = button.querySelector('i');
            if (content.style.display === 'block' || !content.style.display) {
                content.style.display = 'none';
                icon.classList.remove('fa-chevron-up');
                icon.classList.add('fa-chevron-down');
            } else {
                content.style.display = 'block';
                icon.classList.remove('fa-chevron-down');
                icon.classList.add('fa-chevron-up');
            }
        });
    });
}); 