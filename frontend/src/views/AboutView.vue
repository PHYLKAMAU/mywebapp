<template>
  <div class="about-page">
    <!-- Hero Section -->
    <section class="about-hero">
      <div class="container">
        <div class="about-content">
          <div class="about-image">
            <div class="profile-photo">
              <img v-if="about?.profile_image_url" :src="about.profile_image_url" :alt="about.title" />
              <div v-else class="placeholder-avatar">WK</div>
            </div>
          </div>
          <div class="about-text">
            <h1>{{ about?.title || 'About Wambui Kamau' }}</h1>
            <h2>{{ about?.subtitle || 'Full-Stack Developer & IT Solutions Expert' }}</h2>
            <p>{{ about?.bio || 'Loading...' }}</p>
            <p><strong>My Mission:</strong> {{ about?.mission || 'Loading...' }}</p>
            
            <div class="about-stats" v-if="about">
              <div class="stat">
                <span class="stat-number">{{ about.years_experience }}+</span>
                <span class="stat-label">Years Experience</span>
              </div>
              <div class="stat">
                <span class="stat-number">{{ about.projects_completed }}+</span>
                <span class="stat-label">Projects Completed</span>
              </div>
              <div class="stat">
                <span class="stat-number">{{ about.happy_clients }}+</span>
                <span class="stat-label">Happy Clients</span>
              </div>
            </div>

            <div class="about-actions">
              <router-link to="/contact" class="btn btn-primary">Get In Touch</router-link>
              <a v-if="about?.cv_file_url" :href="about.cv_file_url" target="_blank" class="btn btn-secondary">
                Download CV
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Skills Section -->
    <section class="skills-section">
      <div class="container">
        <h2 class="section-title">Skills & Expertise</h2>
        <div class="skills-categories" v-if="skillsByCategory && Object.keys(skillsByCategory).length">
          <div v-for="(category, key) in skillsByCategory" :key="key" class="skill-category">
            <h3>{{ category.label }}</h3>
            <div class="skills-list">
              <div v-for="skill in category.skills" :key="skill.id" class="skill-item">
                <div class="skill-info">
                  <span class="skill-name">{{ skill.name }}</span>
                  <span class="skill-percentage">{{ skill.proficiency }}%</span>
                </div>
                <div class="skill-bar">
                  <div class="skill-progress" :style="{ width: skill.proficiency + '%' }"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-else class="loading">
          <div class="spinner"></div>
        </div>
      </div>
    </section>

    <!-- Experience Timeline (Static for now) -->
    <section class="experience-section">
      <div class="container">
        <h2 class="section-title">Professional Journey</h2>
        <div class="timeline">
          <div class="timeline-item">
            <div class="timeline-date">2019 - Present</div>
            <div class="timeline-content">
              <h3>Freelance Full-Stack Developer</h3>
              <p>Providing comprehensive web development and IT consulting services to businesses across various industries.</p>
            </div>
          </div>
          <div class="timeline-item">
            <div class="timeline-date">2017 - 2019</div>
            <div class="timeline-content">
              <h3>Senior Developer at TechCorp</h3>
              <p>Led development of enterprise applications using React, Node.js, and cloud technologies.</p>
            </div>
          </div>
          <div class="timeline-item">
            <div class="timeline-date">2015 - 2017</div>
            <div class="timeline-content">
              <h3>Software Developer at StartupHub</h3>
              <p>Developed scalable web applications and mobile solutions for startup clients.</p>
            </div>
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
  name: 'AboutView',
  setup() {
    const portfolioStore = usePortfolioStore()

    const about = computed(() => portfolioStore.about)
    const skillsByCategory = computed(() => portfolioStore.skillsByCategory)

    onMounted(async () => {
      await Promise.all([
        portfolioStore.fetchAbout(),
        portfolioStore.fetchSkillsByCategory().then(data => {
          portfolioStore.skillsByCategory = data
        })
      ])
    })

    return {
      about,
      skillsByCategory
    }
  }
}
</script>

<style lang="scss" scoped>
.about-hero {
  padding: 6rem 0;
  background: var(--bg-secondary);
}

.about-content {
  display: grid;
  grid-template-columns: 1fr 2fr;
  gap: 4rem;
  align-items: center;

  @include mobile {
    grid-template-columns: 1fr;
    gap: 2rem;
    text-align: center;
  }
}

.about-image {
  display: flex;
  justify-content: center;
}

.profile-photo {
  width: 300px;
  height: 300px;
  border-radius: 50%;
  overflow: hidden;
  border: 4px solid var(--primary-color);
  position: relative;

  @include mobile {
    width: 250px;
    height: 250px;
  }

  img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .placeholder-avatar {
    width: 100%;
    height: 100%;
    background: var(--gradient-primary);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4rem;
    color: white;
    font-weight: bold;
  }
}

.about-text h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
  color: var(--text-primary);

  @include mobile {
    font-size: 2rem;
  }
}

.about-text h2 {
  color: var(--primary-color);
  font-size: 1.3rem;
  margin-bottom: 2rem;
  font-weight: 600;
}

.about-text p {
  color: var(--text-secondary);
  margin-bottom: 1.5rem;
  line-height: 1.8;
  font-size: 1.1rem;
}

.about-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin: 2rem 0;

  @include mobile {
    grid-template-columns: 1fr;
  }
}

.stat {
  text-align: center;
  padding: 1rem;
  background: var(--bg-card);
  border-radius: 10px;
  border: 1px solid var(--border-color);

  .stat-number {
    display: block;
    font-size: 2rem;
    font-weight: bold;
    color: var(--primary-color);
  }

  .stat-label {
    color: var(--text-secondary);
    font-size: 0.9rem;
  }
}

.about-actions {
  display: flex;
  gap: 1rem;
  margin-top: 2rem;

  @include mobile {
    flex-direction: column;
    align-items: center;
  }
}

.skills-section {
  padding: 6rem 0;
  background: var(--bg-dark);
}

.skills-categories {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 3rem;
  margin-top: 3rem;
}

.skill-category h3 {
  color: var(--primary-color);
  margin-bottom: 1.5rem;
  font-size: 1.3rem;
}

.skill-item {
  margin-bottom: 1.5rem;
}

.skill-info {
  display: flex;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.skill-name {
  color: var(--text-primary);
  font-weight: 500;
}

.skill-percentage {
  color: var(--text-secondary);
  font-size: 0.9rem;
}

.skill-bar {
  height: 8px;
  background: var(--bg-card);
  border-radius: 4px;
  overflow: hidden;
}

.skill-progress {
  height: 100%;
  background: var(--gradient-primary);
  border-radius: 4px;
  transition: width 1s ease;
}

.experience-section {
  padding: 6rem 0;
  background: var(--bg-secondary);
}

.timeline {
  max-width: 800px;
  margin: 3rem auto 0;
  position: relative;

  &::before {
    content: '';
    position: absolute;
    left: 30px;
    top: 0;
    bottom: 0;
    width: 2px;
    background: var(--primary-color);

    @include mobile {
      left: 15px;
    }
  }
}

.timeline-item {
  position: relative;
  margin-bottom: 3rem;
  padding-left: 80px;

  @include mobile {
    padding-left: 50px;
  }

  &::before {
    content: '';
    position: absolute;
    left: 22px;
    top: 8px;
    width: 16px;
    height: 16px;
    background: var(--primary-color);
    border-radius: 50%;
    border: 3px solid var(--bg-secondary);

    @include mobile {
      left: 7px;
    }
  }
}

.timeline-date {
  color: var(--primary-color);
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.timeline-content h3 {
  color: var(--text-primary);
  margin-bottom: 0.5rem;
  font-size: 1.2rem;
}

.timeline-content p {
  color: var(--text-secondary);
  line-height: 1.6;
}
</style>