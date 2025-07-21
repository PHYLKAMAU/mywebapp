<template>
  <div class="services-page">
    <!-- Hero Section -->
    <section class="services-hero">
      <div class="container">
        <div class="hero-content">
          <h1>Services</h1>
          <p>Comprehensive IT solutions tailored to your business needs. From concept to deployment, I deliver technology that drives growth and innovation.</p>
        </div>
      </div>
    </section>

    <!-- Services Grid -->
    <section class="services-section">
      <div class="container">
        <h2 class="section-title">What I Offer</h2>
        
        <div v-if="services.length" class="services-grid">
          <div 
            v-for="service in services" 
            :key="service.id" 
            class="service-card"
            :class="{ 'featured': service.is_featured }"
          >
            <div class="service-header">
              <div class="service-icon">{{ service.icon }}</div>
              <h3>{{ service.title }}</h3>
              <p class="service-description">{{ service.description }}</p>
            </div>

            <div class="service-features">
              <h4>What's Included:</h4>
              <ul class="features-list">
                <li v-for="feature in service.features" :key="feature" class="feature-item">
                  <span class="check-icon">✓</span>
                  {{ feature }}
                </li>
              </ul>
            </div>

            <div class="service-footer">
              <div class="price-range" v-if="service.price_range">
                <span class="price-label">Starting from</span>
                <span class="price">{{ service.price_range }}</span>
              </div>
              <router-link to="/contact" class="btn btn-primary">Get Quote</router-link>
            </div>
          </div>
        </div>

        <div v-else class="loading">
          <div class="spinner"></div>
        </div>
      </div>
    </section>

    <!-- Process Section -->
    <section class="process-section">
      <div class="container">
        <h2 class="section-title">My Development Process</h2>
        <div class="process-steps">
          <div class="process-step">
            <div class="step-number">01</div>
            <h3>Discovery & Planning</h3>
            <p>Understanding your business requirements, goals, and technical needs to create a comprehensive project roadmap.</p>
          </div>
          <div class="process-step">
            <div class="step-number">02</div>
            <h3>Design & Architecture</h3>
            <p>Creating user-centric designs and robust technical architecture that scales with your business growth.</p>
          </div>
          <div class="process-step">
            <div class="step-number">03</div>
            <h3>Development & Testing</h3>
            <p>Building your solution using best practices, with continuous testing to ensure quality and performance.</p>
          </div>
          <div class="process-step">
            <div class="step-number">04</div>
            <h3>Deployment & Support</h3>
            <p>Launching your project with ongoing support and maintenance to keep everything running smoothly.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Technologies Section -->
    <section class="technologies-section">
      <div class="container">
        <h2 class="section-title">Technologies I Use</h2>
        <div class="tech-categories">
          <div class="tech-category">
            <h3>Frontend</h3>
            <div class="tech-tags">
              <span class="tech-tag">React</span>
              <span class="tech-tag">Vue.js</span>
              <span class="tech-tag">Angular</span>
              <span class="tech-tag">TypeScript</span>
              <span class="tech-tag">Next.js</span>
              <span class="tech-tag">Nuxt.js</span>
            </div>
          </div>
          <div class="tech-category">
            <h3>Backend</h3>
            <div class="tech-tags">
              <span class="tech-tag">Node.js</span>
              <span class="tech-tag">Python</span>
              <span class="tech-tag">Django</span>
              <span class="tech-tag">Express.js</span>
              <span class="tech-tag">FastAPI</span>
              <span class="tech-tag">REST APIs</span>
            </div>
          </div>
          <div class="tech-category">
            <h3>Database</h3>
            <div class="tech-tags">
              <span class="tech-tag">PostgreSQL</span>
              <span class="tech-tag">MongoDB</span>
              <span class="tech-tag">MySQL</span>
              <span class="tech-tag">Redis</span>
              <span class="tech-tag">Supabase</span>
              <span class="tech-tag">Firebase</span>
            </div>
          </div>
          <div class="tech-category">
            <h3>Cloud & DevOps</h3>
            <div class="tech-tags">
              <span class="tech-tag">AWS</span>
              <span class="tech-tag">Docker</span>
              <span class="tech-tag">Kubernetes</span>
              <span class="tech-tag">CI/CD</span>
              <span class="tech-tag">Vercel</span>
              <span class="tech-tag">Netlify</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="cta-section">
      <div class="container">
        <div class="cta-content">
          <h2>Ready to Start Your Project?</h2>
          <p>Let's discuss your requirements and create a solution that drives your business forward.</p>
          <div class="cta-buttons">
            <router-link to="/contact" class="btn btn-primary">Get Started</router-link>
            <router-link to="/portfolio" class="btn btn-secondary">View Portfolio</router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { onMounted, computed } from 'vue'
import { usePortfolioStore } from '@/stores/portfolio'

export default {
  name: 'ServicesView',
  setup() {
    const portfolioStore = usePortfolioStore()

    const services = computed(() => portfolioStore.services)

    onMounted(async () => {
      await portfolioStore.fetchServices()
    })

    return {
      services
    }
  }
}
</script>

<style lang="scss" scoped>
.services-hero {
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
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.6;

    @include mobile {
      font-size: 1rem;
    }
  }
}

.services-section {
  padding: 6rem 0;
  background: var(--bg-secondary);
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
  gap: 2rem;
  margin-top: 3rem;

  @include mobile {
    grid-template-columns: 1fr;
  }
}

.service-card {
  background: var(--bg-card);
  border-radius: 20px;
  border: 1px solid var(--border-color);
  padding: 2.5rem;
  display: flex;
  flex-direction: column;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;

  &.featured::before {
    content: 'Popular';
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: var(--gradient-primary);
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
  }

  &::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--gradient-primary);
    transform: scaleX(0);
    transition: transform 0.3s ease;
  }

  &:hover {
    transform: translateY(-10px);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);

    &::after {
      transform: scaleX(1);
    }
  }
}

.service-header {
  text-align: center;
  margin-bottom: 2rem;
}

.service-icon {
  font-size: 3.5rem;
  margin-bottom: 1rem;
}

.service-card h3 {
  font-size: 1.5rem;
  color: var(--text-primary);
  margin-bottom: 1rem;
}

.service-description {
  color: var(--text-secondary);
  line-height: 1.6;
}

.service-features {
  flex: 1;
  margin-bottom: 2rem;

  h4 {
    color: var(--primary-color);
    margin-bottom: 1rem;
    font-size: 1rem;
  }
}

.features-list {
  list-style: none;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0;
  color: var(--text-secondary);
  border-bottom: 1px solid var(--border-color);

  &:last-child {
    border-bottom: none;
  }
}

.check-icon {
  color: var(--primary-color);
  font-weight: bold;
  font-size: 1.1rem;
}

.service-footer {
  text-align: center;
}

.price-range {
  margin-bottom: 1.5rem;
}

.price-label {
  display: block;
  color: var(--text-muted);
  font-size: 0.9rem;
  margin-bottom: 0.25rem;
}

.price {
  color: var(--primary-color);
  font-size: 1.3rem;
  font-weight: bold;
}

.process-section {
  padding: 6rem 0;
  background: var(--bg-dark);
}

.process-steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 3rem;

  @include mobile {
    grid-template-columns: 1fr;
  }
}

.process-step {
  text-align: center;
  padding: 2rem;
}

.step-number {
  width: 60px;
  height: 60px;
  background: var(--gradient-primary);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0 auto 1rem;
}

.process-step h3 {
  color: var(--text-primary);
  margin-bottom: 1rem;
  font-size: 1.3rem;
}

.process-step p {
  color: var(--text-secondary);
  line-height: 1.6;
}

.technologies-section {
  padding: 6rem 0;
  background: var(--bg-secondary);
}

.tech-categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.tech-category h3 {
  color: var(--primary-color);
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.tech-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.tech-tag {
  background: var(--bg-card);
  color: var(--text-primary);
  padding: 0.5rem 1rem;
  border-radius: 25px;
  border: 1px solid var(--border-color);
  font-size: 0.9rem;
  transition: all 0.3s ease;

  &:hover {
    background: var(--primary-color);
    color: white;
    transform: translateY(-2px);
  }
}

.cta-section {
  padding: 6rem 0;
  background: var(--bg-dark);
  text-align: center;
}

.cta-content h2 {
  font-size: 2.5rem;
  color: var(--text-primary);
  margin-bottom: 1rem;

  @include mobile {
    font-size: 2rem;
  }
}

.cta-content p {
  font-size: 1.2rem;
  color: var(--text-secondary);
  margin-bottom: 2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;

  @include mobile {
    flex-direction: column;
    align-items: center;
  }
}
</style>