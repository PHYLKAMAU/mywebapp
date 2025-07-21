<template>
  <div class="home">
    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">
          Transforming Ideas Into Digital Reality
        </h1>
        <p class="hero-subtitle">Full-Stack Developer & IT Solutions Expert</p>
        <p class="hero-description">
          I help businesses leverage cutting-edge technology to drive growth, improve efficiency, 
          and stay ahead of the competition. From custom web applications to cloud infrastructure, 
          I deliver solutions that matter.
        </p>
        <div class="cta-buttons">
          <router-link to="/portfolio" class="btn btn-primary">View My Work</router-link>
          <router-link to="/contact" class="btn btn-secondary">Get In Touch</router-link>
        </div>
      </div>
    </section>

    <!-- Services Overview -->
    <section class="services-overview">
      <div class="container">
        <h2 class="section-title">What I Do</h2>
        <div class="services-grid" v-if="services.length">
          <div v-for="service in services.slice(0, 4)" :key="service.id" class="service-card">
            <div class="service-icon">{{ service.icon }}</div>
            <h3>{{ service.title }}</h3>
            <p>{{ service.description }}</p>
          </div>
        </div>
        <div v-else class="loading">
          <div class="spinner"></div>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="stats-section" v-if="stats">
      <div class="container">
        <div class="stats-grid">
          <div class="stat-item">
            <span class="stat-number">{{ stats.years_experience }}+</span>
            <span class="stat-label">Years Experience</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">{{ stats.projects_completed }}+</span>
            <span class="stat-label">Projects Completed</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">{{ stats.happy_clients }}+</span>
            <span class="stat-label">Happy Clients</span>
          </div>
          <div class="stat-item">
            <span class="stat-number">24/7</span>
            <span class="stat-label">Support Available</span>
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
  name: 'HomeView',
  setup() {
    const portfolioStore = usePortfolioStore()

    const services = computed(() => portfolioStore.services)
    const stats = computed(() => portfolioStore.stats)

    onMounted(async () => {
      await portfolioStore.initializeHomepage()
    })

    return {
      services,
      stats
    }
  }
}
</script>

<style lang="scss" scoped>
.hero {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  background: linear-gradient(135deg, var(--bg-dark) 0%, var(--bg-secondary) 100%);
  position: relative;
  overflow: hidden;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: radial-gradient(ellipse at center, rgba(205, 92, 42, 0.1) 0%, transparent 70%);
  }
}

.hero-content {
  max-width: 900px;
  padding: 0 2rem;
  position: relative;
  z-index: 2;

  @include mobile {
    padding: 0 1rem;
  }
}

.hero-title {
  font-size: clamp(2.5rem, 5vw, 4.5rem);
  margin-bottom: 1rem;
  background: linear-gradient(135deg, var(--text-primary) 0%, var(--primary-color) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
}

.hero-subtitle {
  font-size: 1.3rem;
  color: var(--primary-color);
  margin-bottom: 1rem;
  font-weight: 600;
}

.hero-description {
  font-size: 1.2rem;
  color: var(--text-secondary);
  margin-bottom: 2rem;
  line-height: 1.6;

  @include mobile {
    font-size: 1rem;
  }
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

.services-overview {
  padding: 6rem 0;
  background: var(--bg-secondary);
}

.services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.service-card {
  background: var(--bg-card);
  padding: 2rem;
  border-radius: 15px;
  border: 1px solid var(--border-color);
  text-align: center;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;

  &::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: var(--gradient-primary);
    transform: scaleX(0);
    transition: transform 0.3s ease;
  }

  &:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);

    &::before {
      transform: scaleX(1);
    }
  }
}

.service-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.service-card h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
  color: var(--text-primary);
}

.service-card p {
  color: var(--text-secondary);
  line-height: 1.6;
}

.stats-section {
  padding: 4rem 0;
  background: var(--bg-dark);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
}

.stat-item {
  text-align: center;
  padding: 1.5rem;
  background: var(--bg-card);
  border-radius: 10px;
  border: 1px solid var(--border-color);
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
  }
}

.stat-number {
  font-size: 2.5rem;
  font-weight: bold;
  color: var(--primary-color);
  display: block;
}

.stat-label {
  color: var(--text-secondary);
  font-size: 0.9rem;
  margin-top: 0.5rem;
}
</style>