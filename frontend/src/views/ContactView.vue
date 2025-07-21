<template>
  <div class="contact-page">
    <!-- Hero Section -->
    <section class="contact-hero">
      <div class="container">
        <div class="hero-content">
          <h1>Let's Work Together</h1>
          <p>Ready to transform your ideas into reality? I'd love to hear about your project and discuss how we can create something amazing together.</p>
        </div>
      </div>
    </section>

    <!-- Contact Section -->
    <section class="contact-section">
      <div class="container">
        <div class="contact-content">
          <!-- Contact Information -->
          <div class="contact-info">
            <h2>Get In Touch</h2>
            <p>I'm always excited to work on new projects and help businesses grow through innovative technology solutions.</p>

            <div class="contact-methods">
              <div class="contact-item">
                <div class="contact-icon">📧</div>
                <div class="contact-details">
                  <h4>Email</h4>
                  <p>phylisofficial90@gmail.com</p>
                  <small>I'll respond within 24 hours</small>
                </div>
              </div>

              <div class="contact-item">
                <div class="contact-icon">
                  <img src="@/assets/phone.png" alt="Phone" class="contact-icon-img" />
                </div>
                <div class="contact-details">
                  <h4>Phone</h4>
                  <p>+254 110 872 854</p>
                  <small>Mon - Fri: 9:00 AM - 6:00 PM EAT</small>
                </div>
              </div>

              <div class="contact-item">
                <div class="contact-icon">
                  <img src="@/assets/whatsapp.jpg" alt="WhatsApp" class="contact-icon-img" />
                </div>
                <div class="contact-details">
                  <h4>WhatsApp</h4>
                  <p>+254 110 872 854</p>
                  <small>Quick responses via WhatsApp</small>
                </div>
              </div>

              <div class="contact-item">
                <div class="contact-icon">📍</div>
                <div class="contact-details">
                  <h4>Location</h4>
                  <p>Nairobi, Kenya 00100</p>
                  <small>Available for remote and local projects</small>
                </div>
              </div>
            </div>

            <div class="social-section">
              <h3>Connect With Me</h3>
              <div class="social-links">
                <a href="https://www.linkedin.com/in/phylis-kamau-98b58b232" target="_blank" class="social-link linkedin" title="LinkedIn">
                  <span class="social-icon">in</span> LinkedIn
                </a>
                <a href="https://github.com/PHYLKAMAU" target="_blank" class="social-link github" title="GitHub">
                  <img src="@/assets/git.png" alt="GitHub" class="social-icon-img" /> GitHub
                </a>
                <a href="https://x.com/just_phyl413" target="_blank" class="social-link twitter" title="X (Twitter)">
                  <img src="@/assets/x.png" alt="X" class="social-icon-img" /> X (Twitter)
                </a>
                <a href="mailto:phylisofficial90@gmail.com" class="social-link email" title="Email">
                  <span class="social-icon">@</span> Email
                </a>
                <a href="https://wa.me/254110872854" target="_blank" class="social-link whatsapp" title="WhatsApp">
                  <img src="@/assets/whatsapp.jpg" alt="WhatsApp" class="social-icon-img" /> WhatsApp
                </a>
              </div>
            </div>
          </div>

          <!-- Contact Form -->
          <div class="contact-form-section">
            <div class="form-container">
              <h3>Send Me a Message</h3>
              <p class="form-description">Fill out the form below and I'll get back to you as soon as possible.</p>

              <form @submit.prevent="submitForm" class="contact-form">
                <div class="form-row">
                  <div class="form-group">
                    <label for="name">Name *</label>
                    <input 
                      type="text" 
                      id="name" 
                      v-model="form.name" 
                      :class="{ 'error': errors.name }"
                      required 
                    />
                    <span v-if="errors.name" class="error-message">{{ errors.name }}</span>
                  </div>

                  <div class="form-group">
                    <label for="email">Email *</label>
                    <input 
                      type="email" 
                      id="email" 
                      v-model="form.email" 
                      :class="{ 'error': errors.email }"
                      required 
                    />
                    <span v-if="errors.email" class="error-message">{{ errors.email }}</span>
                  </div>
                </div>

                <div class="form-group">
                  <label for="subject">Subject *</label>
                  <select 
                    id="subject" 
                    v-model="form.subject" 
                    :class="{ 'error': errors.subject }"
                    required
                  >
                    <option value="">Select a subject</option>
                    <option value="web-development">Web Development Project</option>
                    <option value="mobile-app">Mobile App Development</option>
                    <option value="cloud-services">Cloud & DevOps Services</option>
                    <option value="consultation">Technical Consultation</option>
                    <option value="maintenance">Maintenance & Support</option>
                    <option value="other">Other</option>
                  </select>
                  <span v-if="errors.subject" class="error-message">{{ errors.subject }}</span>
                </div>

                <div class="form-group">
                  <label for="message">Message *</label>
                  <textarea 
                    id="message" 
                    v-model="form.message" 
                    rows="6" 
                    :class="{ 'error': errors.message }"
                    placeholder="Tell me about your project, timeline, requirements, and any specific questions you have..."
                    required
                  ></textarea>
                  <span v-if="errors.message" class="error-message">{{ errors.message }}</span>
                </div>

                <button 
                  type="submit" 
                  class="submit-btn" 
                  :disabled="isSubmitting"
                >
                  <span v-if="isSubmitting">Sending...</span>
                  <span v-else>Send Message</span>
                </button>
              </form>

              <!-- Success/Error Messages -->
              <div v-if="submitStatus === 'success'" class="success-message">
                <h4>✅ Message Sent Successfully!</h4>
                <p>Thank you for reaching out! I'll get back to you within 24 hours.</p>
              </div>

              <div v-if="submitStatus === 'error'" class="error-status">
                <h4>❌ Something went wrong</h4>
                <p>{{ submitError }}</p>
                <button @click="submitStatus = null" class="btn btn-secondary">Try Again</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQ Section -->
    <section class="faq-section">
      <div class="container">
        <h2 class="section-title">Frequently Asked Questions</h2>
        <div class="faq-grid">
          <div class="faq-item">
            <h4>How long does a typical project take?</h4>
            <p>Project timelines vary based on complexity, but most web applications take 2-8 weeks, while mobile apps typically require 4-12 weeks. I'll provide a detailed timeline during our initial consultation.</p>
          </div>

          <div class="faq-item">
            <h4>Do you work with international clients?</h4>
            <p>Absolutely! I work with clients globally and am experienced in remote collaboration. I'm flexible with time zones and use modern communication tools to ensure smooth project delivery.</p>
          </div>

          <div class="faq-item">
            <h4>What's included in your development services?</h4>
            <p>My services include planning, design, development, testing, deployment, and documentation. I also provide post-launch support and maintenance options to keep your application running smoothly.</p>
          </div>

          <div class="faq-item">
            <h4>Do you provide ongoing support?</h4>
            <p>Yes! I offer various support packages including bug fixes, feature updates, security patches, and performance optimization. Support can be arranged on a monthly basis or per-incident.</p>
          </div>

          <div class="faq-item">
            <h4>What information do you need to start?</h4>
            <p>I'll need details about your project goals, target audience, preferred timeline, budget range, and any specific features or integrations you require. The more information you provide, the better I can help you.</p>
          </div>

          <div class="faq-item">
            <h4>How do you handle project communication?</h4>
            <p>I believe in transparent communication with regular updates via email, video calls, and project management tools. You'll always know the current status and next steps of your project.</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, reactive } from 'vue'
import { usePortfolioStore } from '@/stores/portfolio'

export default {
  name: 'ContactView',
  setup() {
    const portfolioStore = usePortfolioStore()
    
    const form = reactive({
      name: '',
      email: '',
      subject: '',
      message: ''
    })

    const errors = ref({})
    const isSubmitting = ref(false)
    const submitStatus = ref(null) // null, 'success', 'error'
    const submitError = ref('')

    const validateForm = () => {
      const newErrors = {}

      if (!form.name.trim()) {
        newErrors.name = 'Name is required'
      } else if (form.name.trim().length < 2) {
        newErrors.name = 'Name must be at least 2 characters'
      }

      if (!form.email.trim()) {
        newErrors.email = 'Email is required'
      } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(form.email)) {
        newErrors.email = 'Please enter a valid email address'
      }

      if (!form.subject) {
        newErrors.subject = 'Please select a subject'
      }

      if (!form.message.trim()) {
        newErrors.message = 'Message is required'
      } else if (form.message.trim().length < 10) {
        newErrors.message = 'Message must be at least 10 characters'
      }

      errors.value = newErrors
      return Object.keys(newErrors).length === 0
    }

    const resetForm = () => {
      form.name = ''
      form.email = ''
      form.subject = ''
      form.message = ''
      errors.value = {}
    }

    const submitForm = async () => {
      if (!validateForm()) {
        return
      }

      isSubmitting.value = true
      submitStatus.value = null
      submitError.value = ''

      try {
        const response = await portfolioStore.submitContactMessage({
          name: form.name.trim(),
          email: form.email.trim(),
          subject: form.subject,
          message: form.message.trim()
        })

        submitStatus.value = 'success'
        resetForm()
        
        // Scroll to success message
        setTimeout(() => {
          document.querySelector('.success-message')?.scrollIntoView({ 
            behavior: 'smooth', 
            block: 'center' 
          })
        }, 100)

      } catch (error) {
        submitStatus.value = 'error'
        submitError.value = error.response?.data?.message || 'Failed to send message. Please try again.'
        console.error('Contact form error:', error)
      } finally {
        isSubmitting.value = false
      }
    }

    return {
      form,
      errors,
      isSubmitting,
      submitStatus,
      submitError,
      submitForm
    }
  }
}
</script>

<style lang="scss" scoped>
.contact-hero {
  padding: 6rem 0 4rem;
  background: linear-gradient(135deg, var(--bg-dark) 0%, var(--bg-secondary) 100%);
  text-align: center;

  h1 {
    font-size: 3rem;
    margin-bottom: 1rem;
    color: var(--text-primary);

    @include mobile {
      font-size: 2.5rem;
    }
  }

  p {
    font-size: 1.2rem;
    color: var(--text-secondary);
    max-width: 700px;
    margin: 0 auto;
    line-height: 1.6;

    @include mobile {
      font-size: 1rem;
    }
  }
}

.contact-section {
  padding: 6rem 0;
  background: var(--bg-secondary);
}

.contact-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;

  @include mobile {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
}

.contact-info h2 {
  font-size: 2rem;
  color: var(--text-primary);
  margin-bottom: 1rem;
}

.contact-info > p {
  color: var(--text-secondary);
  font-size: 1.1rem;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.contact-methods {
  margin-bottom: 3rem;
}

.contact-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin-bottom: 2rem;
}

.contact-icon {
  font-size: 1.5rem;
  width: 50px;
  height: 50px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;

  .contact-icon-img {
    width: 30px;
    height: 30px;
    object-fit: contain;
  }
}

.contact-details h4 {
  color: var(--text-primary);
  margin-bottom: 0.25rem;
  font-size: 1.1rem;
}

.contact-details p {
  color: var(--primary-color);
  font-weight: 600;
  margin-bottom: 0.25rem;
}

.contact-details small {
  color: var(--text-muted);
  font-size: 0.9rem;
}

.social-section {
  margin-top: 2rem;

  h3 {
    color: var(--primary-color);
    margin-bottom: 1rem;
    font-size: 1.2rem;
  }
}

.social-links {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.social-link {
  background: var(--bg-card);
  color: var(--text-primary);
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  text-decoration: none;
  border: 1px solid var(--border-color);
  transition: all 0.3s ease;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.5rem;

  &:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
  }

  .social-icon {
    font-size: 1.1rem;
    font-weight: bold;
    width: 20px;
    text-align: center;
  }

  .social-icon-img {
    width: 20px;
    height: 20px;
    object-fit: contain;
  }

  // Platform-specific styling
  &.linkedin {
    &:hover {
      background: #0077b5;
      color: white;
      border-color: #0077b5;
    }
  }

  &.github {
    &:hover {
      background: #333;
      color: white;
      border-color: #333;
    }
  }

  &.twitter {
    &:hover {
      background: #000;
      color: white;
      border-color: #000;
    }
  }

  &.email {
    &:hover {
      background: #ea4335;
      color: white;
      border-color: #ea4335;
    }
  }

  &.whatsapp {
    &:hover {
      background: #25d366;
      color: white;
      border-color: #25d366;
    }
  }
}

.form-container {
  background: var(--bg-card);
  padding: 2.5rem;
  border-radius: 20px;
  border: 1px solid var(--border-color);
}

.form-container h3 {
  color: var(--text-primary);
  margin-bottom: 0.5rem;
  font-size: 1.5rem;
}

.form-description {
  color: var(--text-secondary);
  margin-bottom: 2rem;
  line-height: 1.6;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;

  @include mobile {
    grid-template-columns: 1fr;
  }
}

.form-group {
  margin-bottom: 1.5rem;

  label {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
    font-weight: 500;
  }

  input,
  textarea,
  select {
    width: 100%;
    padding: 1rem;
    background: var(--bg-secondary);
    border: 2px solid var(--border-color);
    border-radius: 8px;
    color: var(--text-primary);
    font-size: 1rem;
    transition: all 0.3s ease;
    font-family: inherit;

    &:focus {
      outline: none;
      border-color: var(--primary-color);
      box-shadow: 0 0 0 3px rgba(205, 92, 42, 0.1);
    }

    &.error {
      border-color: #ff4757;
    }

    &::placeholder {
      color: var(--text-muted);
    }
  }

  select {
    cursor: pointer;
  }
}

.error-message {
  color: #ff4757;
  font-size: 0.8rem;
  margin-top: 0.25rem;
  display: block;
}

.submit-btn {
  background: var(--gradient-primary);
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  width: 100%;

  &:hover:not(:disabled) {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(205, 92, 42, 0.3);
  }

  &:disabled {
    opacity: 0.7;
    cursor: not-allowed;
  }
}

.success-message,
.error-status {
  margin-top: 2rem;
  padding: 1.5rem;
  border-radius: 8px;
  text-align: center;
}

.success-message {
  background: rgba(46, 204, 113, 0.1);
  border: 1px solid #2ecc71;

  h4 {
    color: #2ecc71;
    margin-bottom: 0.5rem;
  }

  p {
    color: var(--text-secondary);
  }
}

.error-status {
  background: rgba(255, 71, 87, 0.1);
  border: 1px solid #ff4757;

  h4 {
    color: #ff4757;
    margin-bottom: 0.5rem;
  }

  p {
    color: var(--text-secondary);
    margin-bottom: 1rem;
  }
}

.faq-section {
  padding: 6rem 0;
  background: var(--bg-dark);
}

.faq-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-top: 3rem;

  @include mobile {
    grid-template-columns: 1fr;
  }
}

.faq-item {
  background: var(--bg-card);
  padding: 2rem;
  border-radius: 15px;
  border: 1px solid var(--border-color);
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
  }

  h4 {
    color: var(--primary-color);
    margin-bottom: 1rem;
    font-size: 1.1rem;
  }

  p {
    color: var(--text-secondary);
    line-height: 1.6;
  }
}
</style>