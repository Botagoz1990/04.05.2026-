document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.hamburger');
    const navMenu = document.querySelector('.nav-menu');
    const dropdowns = document.querySelectorAll('.dropdown');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
            document.body.classList.toggle('no-scroll');
        });

        // Close menu when clicking a link
        document.querySelectorAll('.nav-menu a').forEach(link => {
            link.addEventListener('click', (e) => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
                document.body.classList.remove('no-scroll');
            });
        });
    }

    // --- Lead Integration Logic (Bitrix24) ---
    
    // PLACEHOLDER: Paste your Bitrix24 Webhook URL here
    // Example: 'https://company.bitrix24.kz/rest/1/webhook_key/crm.lead.add.json'
    const BITRIX24_WEBHOOK_URL = ''; 

    async function submitToBitrix24(data, leadTitle = 'Новая заявка с сайта') {
        if (!BITRIX24_WEBHOOK_URL) {
            console.warn('Bitrix24 Webhook URL not configured. Data:', data);
            return true; // Simulate success for UI testing
        }

        const payload = {
            fields: {
                TITLE: leadTitle,
                NAME: data.name || '',
                PHONE: [{ VALUE: data.phone || '', VALUE_TYPE: 'WORK' }],
                EMAIL: [{ VALUE: data.email || '', VALUE_TYPE: 'WORK' }],
                COMPANY_TITLE: data.company || '',
                COMMENTS: data.message || '',
                SOURCE_ID: 'WEB',
            }
        };

        try {
            const response = await fetch(BITRIX24_WEBHOOK_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            });
            return response.ok;
        } catch (error) {
            console.error('Bitrix24 Integration Error:', error);
            return false;
        }
    }

    // Main Contact Form Handler
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const submitBtn = contactForm.querySelector('button');
            const originalBtnText = submitBtn.textContent;
            
            submitBtn.disabled = true;
            submitBtn.textContent = 'Отправка...';

            const formData = {
                name: contactForm.querySelector('input[placeholder="Имя"]').value,
                company: contactForm.querySelector('input[placeholder="Компания"]').value,
                phone: contactForm.querySelector('input[placeholder="Телефон"]').value,
                email: contactForm.querySelector('input[placeholder="Email"]').value,
                message: contactForm.querySelector('input[placeholder*="задача"]').value
            };

            const success = await submitToBitrix24(formData, 'Заявка: Обсудить проект');

            if (success) {
                contactForm.innerHTML = `
                    <div style="text-align: center; padding: 40px 20px;">
                        <i class="ph ph-check-circle" style="font-size: 64px; color: var(--primary); margin-bottom: 20px;"></i>
                        <h3>Заявка отправлена!</h3>
                        <p>Мы свяжемся с вами в ближайшее рабочее время.</p>
                    </div>
                `;
            } else {
                alert('Произошла ошибка при отправке. Пожалуйста, попробуйте позже или свяжитесь с нами напрямую.');
                submitBtn.disabled = false;
                submitBtn.textContent = originalBtnText;
            }
        });
    }

    // Modal Lead Form Logic
    const modal = document.getElementById('magnetModal');
    const modalForm = document.getElementById('magnetForm');
    const closeBtn = document.querySelector('.modal-close');
    const magnetButtons = document.querySelectorAll('.btn-magnet');

    if (modal && magnetButtons.length > 0) {
        let activeMagnetTitle = '';

        magnetButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                activeMagnetTitle = btn.parentElement.querySelector('h3').textContent;
                modal.style.display = 'block';
                document.body.style.overflow = 'hidden'; 
            });
        });

        const closeModal = () => {
            modal.style.display = 'none';
            document.body.style.overflow = ''; 
        };

        if (closeBtn) closeBtn.addEventListener('click', closeModal);
        window.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });
        window.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeModal(); });

        if (modalForm) {
            modalForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                const submitBtn = modalForm.querySelector('button');
                submitBtn.disabled = true;

                const formData = {
                    name: document.getElementById('modalName').value,
                    phone: document.getElementById('modalPhone').value,
                    email: document.getElementById('modalEmail').value
                };

                const success = await submitToBitrix24(formData, `Лид-магнит: ${activeMagnetTitle}`);

                if (success) {
                    const content = modal.querySelector('.modal-content');
                    content.innerHTML = `
                        <div style="text-align: center; padding: 20px 0;">
                            <i class="ph ph-check-circle" style="font-size: 64px; color: var(--primary); margin-bottom: 20px;"></i>
                            <h3>Готово!</h3>
                            <p>Материал «${activeMagnetTitle}» отправлен на вашу почту.</p>
                            <button class="btn btn-primary" onclick="location.reload()" style="margin-top: 20px;">Закрыть</button>
                        </div>
                    `;
                } else {
                    alert('Ошибка отправки. Попробуйте еще раз.');
                    submitBtn.disabled = false;
                }
            });
        }
    }

    // --- Quiz Logic ---
    const quizSteps = document.querySelectorAll('.quiz-step');
    const quizNextBtn = document.getElementById('quiz-next-btn');
    const quizProgressFill = document.getElementById('quiz-progress-fill');
    const quizOptions = document.querySelectorAll('.quiz-option');
    const quizForm = document.getElementById('quiz-form');
    const quizFooter = document.getElementById('quiz-footer');
    
    let currentStep = 0;
    const quizData = {};

    if (quizSteps.length > 0) {
        const updateQuiz = () => {
            console.log("Updating quiz to step:", currentStep);
            quizSteps.forEach((step, index) => {
                step.classList.toggle('active', index === currentStep);
            });

            // Update progress
            const progress = (currentStep / (quizSteps.length - 2)) * 100;
            if (quizProgressFill) quizProgressFill.style.width = `${Math.min(progress, 100)}%`;

            // Hide footer on success step
            if (quizSteps[currentStep].dataset.step === 'success') {
                if (quizFooter) quizFooter.style.display = 'none';
            } else if (quizSteps[currentStep].dataset.step === 'final') {
                if (quizNextBtn) quizNextBtn.style.display = 'none';
            } else {
                if (quizNextBtn) {
                    quizNextBtn.style.display = 'block';
                    const hasAnswer = !!quizData[`step${currentStep + 1}`];
                    quizNextBtn.disabled = !hasAnswer;
                    console.log("Step answer status:", hasAnswer);
                }
            }
        };

        // Initial update
        updateQuiz();

        quizOptions.forEach(option => {
            option.addEventListener('click', () => {
                const step = option.closest('.quiz-step').dataset.step;
                const value = option.dataset.value;
                console.log(`Option clicked: step ${step}, value ${value}`);
                
                // Toggle selection
                option.closest('.quiz-options').querySelectorAll('.quiz-option').forEach(opt => opt.classList.remove('selected'));
                option.classList.add('selected');
                
                quizData[`step${step}`] = value;
                if (quizNextBtn) {
                    quizNextBtn.disabled = false;
                    console.log("Next button enabled");
                }
            });
        });

        if (quizNextBtn) {
            quizNextBtn.addEventListener('click', () => {
                console.log("Next button clicked");
                if (currentStep < quizSteps.length - 1) {
                    currentStep++;
                    updateQuiz();
                }
            });
        }

        if (quizForm) {
            quizForm.addEventListener('submit', async (e) => {
                e.preventDefault();
                const submitBtn = quizForm.querySelector('button');
                submitBtn.disabled = true;

                const formData = {
                    name: quizForm.querySelector('input[placeholder="Имя"]').value,
                    phone: quizForm.querySelector('input[placeholder="Телефон"]').value,
                    email: quizForm.querySelector('input[placeholder="Email"]').value,
                    message: `Квиз пройден. Ответы: ${JSON.stringify(quizData)}`
                };

                const success = await submitToBitrix24(formData, 'Квиз: Расчет эффективности');

                if (success) {
                    currentStep++; // Move to success step
                    updateQuiz();
                } else {
                    alert('Ошибка при отправке. Попробуйте снова.');
                    submitBtn.disabled = false;
                }
            });
        }
    }
});
