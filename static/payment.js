// Payment form logic for plan selection, order creation, and payment

document.addEventListener('DOMContentLoaded', () => {
    // Load plans into select
    async function loadPlansToSelect() {
        try {
            const res = await fetch('/api/products');
            const products = await res.json();
            const select = document.getElementById('plan');
            if (!select) return;
            select.innerHTML = '';
            products.forEach(product => {
                const option = document.createElement('option');
                option.value = product.id;
                option.textContent = `${product.name} - $${product.price}`;
                select.appendChild(option);
            });
        } catch (e) {
            console.error('Failed to load plans:', e);
        }
    }
    loadPlansToSelect();

    // Payment form handling
    const paymentForm = document.getElementById('payment-form');
    if (paymentForm) {
        paymentForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const plan = document.getElementById('plan').value;
            if (!email || !password) {
                alert('Please fill in all fields');
                return;
            }
            // Create order with status 'pending'
            try {
                const orderRes = await fetch('/api/orders', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        product_id: plan,
                        email: email,
                        password: password,
                        status: 'pending'
                    })
                });
                if (!orderRes.ok) {
                    const err = await orderRes.json();
                    alert('Order creation failed: ' + (err.detail || orderRes.statusText));
                    return;
                }
                // Proceed with payment
                const orderData = await orderRes.json();
                // Get payment token from backend
                const tokenRes = await fetch('/get_payment_token');
                if (!tokenRes.ok) {
                    alert('Failed to get payment token');
                    return;
                }
                const tokenData = await tokenRes.json();
                // Show payment widget
                const widget = new PayBox({
                    token: tokenData.token,
                    successCallback: function() {
                        alert('Payment successful!');
                        window.location.href = '/';
                    },
                    errorCallback: function(error) {
                        console.error('Payment failed:', error);
                        alert('Payment failed: ' + error);
                    }
                });
                widget.create();
            } catch (err) {
                alert('Unexpected error: ' + err);
            }
        });
    }
}); 