<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section">
          <h4>Wambui Kamau</h4>
          <p>Full-Stack Developer & IT Solutions Expert</p>
          <p>Transforming businesses through innovative technology solutions.</p>
          <div class="social-links">
            <a href="https://www.linkedin.com/in/phylis-kamau-98b58b232" target="_blank" class="social-link" title="LinkedIn">
              💼
            </a>
            <a href="https://github.com/PHYLKAMAU" target="_blank" class="social-link" title="GitHub">
              🐱
            </a>
            <a href="https://x.com/just_phyl413" target="_blank" class="social-link" title="X (Twitter)">
              ✕
            </a>
            <a href="mailto:phylisofficial90@gmail.com" class="social-link" title="Email">
              📧
            </a>
          </div>
        </div>

        <div class="footer-section">
          <h4>Services</h4>
          <router-link to="/services">Web Development</router-link>
          <router-link to="/services">Mobile Apps</router-link>
          <router-link to="/services">Cloud Solutions</router-link>
          <router-link to="/services">Maintenance & Support</router-link>
        </div>

        <div class="footer-section">
          <h4>Quick Links</h4>
          <router-link to="/about">About</router-link>
          <router-link to="/portfolio">Portfolio</router-link>
          <router-link to="/blog">Blog</router-link>
          <router-link to="/contact">Contact</router-link>
        </div>

        <div class="footer-section">
          <h4>Contact Info</h4>
          <p>phylisofficial90@gmail.com</p>
          <p>+254 110872854</p>
          <p>Nairobi, Kenya</p>
          <p>Available Mon - Fri: 9:00 AM - 6:00 PM EAT</p>
        </div>
      </div>

      <div class="footer-bottom">
        <p>&copy; {{ currentYear }} Wambui Kamau. All rights reserved. | Crafting digital excellence since 2019.</p>
      </div>
    </div>
  </footer>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'FooterSection',
  setup() {
    const currentYear = computed(() => new Date().getFullYear())

    return {
      currentYear
    }
  }
}
</script>

<style lang="scss" scoped>
.footer {
  background: var(--bg-dark);
  padding: 3rem 0 1rem;
  border-top: 1px solid var(--border-color);
  margin-top: auto;
}

.footer-content {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;

  @include mobile {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }
}

.footer-section {
  h4 {
    color: var(--primary-color);
    margin-bottom: 1rem;
    font-size: 1.1rem;
  }

  p,
  a {
    color: var(--text-secondary);
    text-decoration: none;
    margin-bottom: 0.5rem;
    display: block;
    line-height: 1.6;
    transition: color 0.3s ease;

    &:hover {
      color: var(--primary-color);
    }
  }

  p {
    &:hover {
      color: var(--text-secondary);
    }
  }
}

.social-links {
  display: flex;
  gap: 1rem;
  margin-top: 1rem;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 45px;
  height: 45px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 50%;
  color: var(--primary-color);
  text-decoration: none;
  transition: all 0.3s ease;
  font-size: 1.2rem;
  font-weight: bold;

  &:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px var(--shadow-color);
  }

  // Platform-specific styling
  &.linkedin:hover {
    background: #0077b5;
    color: white;
    border-color: #0077b5;
  }

  &.github:hover {
    background: #333;
    color: white;
    border-color: #333;
  }

  &.twitter:hover {
    background: #000;
    color: white;
    border-color: #000;
  }

  &.email:hover {
    background: #ea4335;
    color: white;
    border-color: #ea4335;
  }

  .footer-icon-img {
    width: 20px;
    height: 20px;
    object-fit: contain;
  }
}

.footer-bottom {
  text-align: center;
  color: var(--text-muted);
  padding-top: 2rem;
  border-top: 1px solid var(--border-color);
  font-size: 0.9rem;

  @include mobile {
    font-size: 0.8rem;
  }
}
</style>