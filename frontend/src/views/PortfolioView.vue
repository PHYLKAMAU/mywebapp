<template>
  <div class="portfolio-page">
    <!-- Hero Section -->
    <section class="portfolio-hero">
      <div class="container">
        <div class="hero-content">
          <h1>Portfolio</h1>
          <p>Showcasing innovative solutions that drive business growth. Each project represents a unique challenge solved with cutting-edge technology and strategic thinking.</p>
        </div>
      </div>
    </section>

    <!-- Filter Section -->
    <section class="filter-section">
      <div class="container">
        <div class="filter-controls">
          <button 
            @click="setFilter('all')" 
            :class="{ active: activeFilter === 'all' }"
            class="filter-btn"
          >
            All Projects
          </button>
          <button 
            @click="setFilter('featured')" 
            :class="{ active: activeFilter === 'featured' }"
            class="filter-btn"
          >
            Featured
          </button>
          <button 
            @click="setFilter('web')" 
            :class="{ active: activeFilter === 'web' }"
            class="filter-btn"
          >
            Web Apps
          </button>
          <button 
            @click="setFilter('mobile')" 
            :class="{ active: activeFilter === 'mobile' }"
            class="filter-btn"
          >
            Mobile Apps
          </button>
        </div>
      </div>
    </section>

    <!-- Projects Grid -->
    <section class="projects-section">
      <div class="container">
        <div v-if="loading" class="loading">
          <div class="spinner"></div>
          <p>Loading projects...</p>
        </div>

        <div v-else-if="error" class="error-state">
          <p>Error loading projects: {{ error }}</p>
          <button @click="$router.go(0)" class="btn btn-secondary">Retry</button>
        </div>

        <div v-else-if="filteredProjects.length" class="projects-grid">
          <div 
            v-for="project in filteredProjects" 
            :key="project.id" 
            class="project-card"
            :class="{ 'featured': project.is_featured }"
          >
            <div class="project-image">
              <img :src="project.image_url" :alt="project.title" />
              <div class="project-overlay">
                <div class="project-actions">
                  <a v-if="project.demo_url" :href="project.demo_url" target="_blank" class="action-btn">
                    🔗 Live Demo
                  </a>
                  <a v-if="project.github_url" :href="project.github_url" target="_blank" class="action-btn">
                    🐙 GitHub
                  </a>
                  <a v-if="project.case_study_url" :href="project.case_study_url" target="_blank" class="action-btn">
                    📖 Case Study
                  </a>
                </div>
              </div>
            </div>

            <div class="project-content">
              <div class="project-header">
                <h3>{{ project.title }}</h3>
                <span v-if="project.is_featured" class="featured-badge">Featured</span>
              </div>
              
              <p class="project-description">{{ project.description }}</p>
              
              <div class="tech-stack">
                <span v-for="tech in project.tech_stack" :key="tech" class="tech-tag">
                  {{ tech }}
                </span>
              </div>

              <div class="project-footer">
                <span class="project-date">{{ formatDate(project.completed_date) }}</span>
                <div class="project-links">
                  <a v-if="project.demo_url" :href="project.demo_url" target="_blank" class="project-link">
                    Demo
                  </a>
                  <a v-if="project.github_url" :href="project.github_url" target="_blank" class="project-link">
                    Code
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div v-else class="no-projects">
          <p>No projects found for the selected filter.</p>
        </div>
      </div>
    </section>

    <!-- Stats Section -->
    <section class="portfolio-stats" v-if="stats">
      <div class="container">
        <h2 class="section-title">Project Impact</h2>
        <div class="stats-grid">
          <div class="stat-card">
            <div class="stat-icon">📊</div>
            <h3>{{ stats.total_projects }}</h3>
            <p>Total Projects</p>
          </div>
          <div class="stat-card">
            <div class="stat-icon">⭐</div>
            <h3>{{ featuredCount }}</h3>
            <p>Featured Projects</p>
          </div>
          <div class="stat-card">
            <div class="stat-icon">🚀</div>
            <h3>{{ stats.happy_clients }}+</h3>
            <p>Happy Clients</p>
          </div>
          <div class="stat-card">
            <div class="stat-icon">💼</div>
            <h3>{{ stats.years_experience }}+</h3>
            <p>Years Experience</p>
          </div>
        </div>
      </div>
    </section>

    <!-- CTA Section -->
    <section class="portfolio-cta">
      <div class="container">
        <div class="cta-content">
          <h2>Ready to Start Your Project?</h2>
          <p>Let's discuss how I can help bring your vision to life with custom technology solutions.</p>
          <div class="cta-buttons">
            <router-link to="/contact" class="btn btn-primary">Start a Project</router-link>
            <router-link to="/services" class="btn btn-secondary">View Services</router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { usePortfolioStore } from '@/stores/portfolio'

export default {
  name: 'PortfolioView',
  setup() {
    const portfolioStore = usePortfolioStore()
    const activeFilter = ref('all')

    const projects = computed(() => {
      // Handle case where store contains the full API response
      if (portfolioStore.projects?.results && Array.isArray(portfolioStore.projects.results)) {
        return portfolioStore.projects.results
      }
      // Handle case where store contains just the array
      if (Array.isArray(portfolioStore.projects)) {
        return portfolioStore.projects
      }
      // Fallback to empty array
      return []
    })
    const stats = computed(() => portfolioStore.stats)
    const loading = computed(() => portfolioStore.loading)
    const error = computed(() => portfolioStore.error)

    const featuredCount = computed(() => 
      Array.isArray(projects.value) ? projects.value.filter(project => project.is_featured).length : 0
    )

    const filteredProjects = computed(() => {
      if (!Array.isArray(projects.value)) {
        return []
      }
      
      if (activeFilter.value === 'all') {
        return projects.value
      } else if (activeFilter.value === 'featured') {
        return projects.value.filter(project => project.is_featured)
      } else if (activeFilter.value === 'web') {
        return projects.value.filter(project => 
          Array.isArray(project.tech_stack) && project.tech_stack.some(tech => 
            ['React', 'Vue.js', 'Angular', 'Node.js', 'Django', 'Express.js'].includes(tech)
          )
        )
      } else if (activeFilter.value === 'mobile') {
        return projects.value.filter(project => 
          Array.isArray(project.tech_stack) && project.tech_stack.some(tech => 
            ['React Native', 'Flutter', 'iOS', 'Android', 'Expo'].includes(tech)
          )
        )
      }
      return projects.value
    })

    const setFilter = (filter) => {
      activeFilter.value = filter
    }

    const formatDate = (dateString) => {
      const date = new Date(dateString)
      return date.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'long'
      })
    }

    onMounted(async () => {
      console.log('Portfolio page mounted, fetching projects...')
      try {
        await Promise.all([
          portfolioStore.fetchProjects(),
          portfolioStore.fetchStats()
        ])
        console.log('Projects loaded:', portfolioStore.projects)
        console.log('Stats loaded:', portfolioStore.stats)
      } catch (err) {
        console.error('Error in portfolio page:', err)
      }
    })

    const checkStore = () => {
      console.log('=== STORE CHECK ===')
      console.log('Store projects:', portfolioStore.projects)
      console.log('Store loading:', portfolioStore.loading)
      console.log('Store error:', portfolioStore.error)
      console.log('Computed projects:', projects.value)
      console.log('Filtered projects:', filteredProjects.value)
      console.log('=================')
    }

    // Check store state after a delay
    setTimeout(checkStore, 2000)

    return {
      projects,
      stats,
      loading,
      error,
      activeFilter,
      filteredProjects,
      featuredCount,
      setFilter,
      formatDate,
      // Debug info
      rawProjects: computed(() => portfolioStore.projects),
      storeState: computed(() => ({
        projectsLength: Array.isArray(portfolioStore.projects) ? portfolioStore.projects.length : 'NOT_ARRAY',
        projectsType: typeof portfolioStore.projects,
        loading: portfolioStore.loading,
        error: portfolioStore.error,
        hasResults: portfolioStore.projects?.results ? 'YES' : 'NO'
      })),
      checkStore
    }
  }
}
</script>

<style lang="scss" scoped>
.portfolio-hero {
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

.filter-section {
  padding: 3rem 0;
  background: var(--bg-secondary);
  border-bottom: 1px solid var(--border-color);
}

.filter-controls {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.filter-btn {
  padding: 0.75rem 1.5rem;
  background: transparent;
  border: 2px solid var(--border-color);
  color: var(--text-secondary);
  border-radius: 25px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-weight: 500;

  &:hover,
  &.active {
    background: var(--primary-color);
    border-color: var(--primary-color);
    color: white;
  }
}

.projects-section {
  padding: 6rem 0;
  background: var(--bg-dark);
}

.projects-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 2.5rem;
  margin-top: 2rem;

  @include mobile {
    grid-template-columns: 1fr;
  }
}

.project-card {
  background: var(--bg-card);
  border-radius: 20px;
  border: 1px solid var(--border-color);
  overflow: hidden;
  transition: all 0.3s ease;
  position: relative;

  &.featured::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: var(--gradient-primary);
    z-index: 2;
  }

  &:hover {
    transform: translateY(-10px);
    box-shadow: 0 25px 50px rgba(0, 0, 0, 0.3);
  }
}

.project-image {
  position: relative;
  height: 250px;
  overflow: hidden;

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.3s ease;
  }

  &:hover img {
    transform: scale(1.05);
  }
}

.project-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s ease;
}

.project-card:hover .project-overlay {
  opacity: 1;
}

.project-actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
  justify-content: center;
}

.action-btn {
  background: var(--gradient-primary);
  color: white;
  padding: 0.75rem 1.5rem;
  border-radius: 25px;
  text-decoration: none;
  font-weight: 600;
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-2px);
  }
}

.project-content {
  padding: 2rem;
}

.project-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1rem;

  h3 {
    color: var(--text-primary);
    font-size: 1.3rem;
    flex: 1;
  }
}

.featured-badge {
  background: var(--gradient-primary);
  color: white;
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
  font-weight: 600;
  margin-left: 1rem;
}

.project-description {
  color: var(--text-secondary);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.tech-stack {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.tech-tag {
  background: var(--bg-secondary);
  color: var(--primary-color);
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
  border: 1px solid var(--border-color);
}

.project-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1rem;
  border-top: 1px solid var(--border-color);
}

.project-date {
  color: var(--text-muted);
  font-size: 0.9rem;
}

.project-links {
  display: flex;
  gap: 1rem;
}

.project-link {
  color: var(--primary-color);
  text-decoration: none;
  font-weight: 600;
  font-size: 0.9rem;
  transition: color 0.3s ease;

  &:hover {
    color: var(--primary-light);
  }
}

.portfolio-stats {
  padding: 6rem 0;
  background: var(--bg-secondary);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.stat-card {
  background: var(--bg-card);
  padding: 2rem;
  border-radius: 15px;
  border: 1px solid var(--border-color);
  text-align: center;
  transition: transform 0.3s ease;

  &:hover {
    transform: translateY(-5px);
  }
}

.stat-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

.stat-card h3 {
  font-size: 2rem;
  color: var(--primary-color);
  margin-bottom: 0.5rem;
}

.stat-card p {
  color: var(--text-secondary);
}

.portfolio-cta {
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

.error-state,
.no-projects {
  text-align: center;
  padding: 4rem 2rem;
  color: var(--text-secondary);
}
</style>