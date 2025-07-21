<template>
  <header class="header" :class="{ 'scrolled': isScrolled }">
    <nav class="nav">
      <div class="nav-container">
        <router-link to="/" class="logo">
          Wambui Kamau
        </router-link>

        <ul class="nav-links" :class="{ 'show': mobileMenuOpen }">
          <li><router-link to="/" @click="closeMobileMenu">Home</router-link></li>
          <li><router-link to="/about" @click="closeMobileMenu">About</router-link></li>
          <li><router-link to="/services" @click="closeMobileMenu">Services</router-link></li>
          <li><router-link to="/portfolio" @click="closeMobileMenu">Portfolio</router-link></li>
          <li><router-link to="/pricing" @click="closeMobileMenu">Pricing</router-link></li>
          <li><router-link to="/blog" @click="closeMobileMenu">Blog</router-link></li>
          <li><router-link to="/contact" @click="closeMobileMenu">Contact</router-link></li>
        </ul>

        <div class="mobile-menu" @click="toggleMobileMenu" :class="{ 'open': mobileMenuOpen }">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { ref, onMounted, onUnmounted } from 'vue'

export default {
  name: 'HeaderNav',
  setup() {
    const isScrolled = ref(false)
    const mobileMenuOpen = ref(false)

    const handleScroll = () => {
      isScrolled.value = window.scrollY > 100
    }

    const toggleMobileMenu = () => {
      mobileMenuOpen.value = !mobileMenuOpen.value
    }

    const closeMobileMenu = () => {
      mobileMenuOpen.value = false
    }

    onMounted(() => {
      window.addEventListener('scroll', handleScroll)
    })

    onUnmounted(() => {
      window.removeEventListener('scroll', handleScroll)
    })

    return {
      isScrolled,
      mobileMenuOpen,
      toggleMobileMenu,
      closeMobileMenu
    }
  }
}
</script>

<style lang="scss" scoped>
.header {
  position: fixed;
  top: 0;
  width: 100%;
  background: rgba(10, 10, 10, 0.95);
  backdrop-filter: blur(10px);
  z-index: 1000;
  padding: 1rem 0;
  border-bottom: 1px solid var(--border-color);
  transition: all 0.3s ease;

  &.scrolled {
    background: rgba(10, 10, 10, 0.98);
    padding: 0.5rem 0;
  }
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 2rem;

  @include mobile {
    padding: 0 1rem;
  }
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--primary-color);
  text-decoration: none;
  transition: color 0.3s ease;

  &:hover {
    color: var(--primary-light);
  }
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 2rem;

  @include mobile {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    background: var(--bg-dark);
    flex-direction: column;
    padding: 1rem;
    border-bottom: 1px solid var(--border-color);
    gap: 0;

    &.show {
      display: flex;
    }

    li {
      padding: 0.5rem 0;
    }
  }

  a {
    color: var(--text-secondary);
    text-decoration: none;
    transition: color 0.3s ease;
    position: relative;
    font-weight: 500;

    &:hover,
    &.router-link-active {
      color: var(--primary-color);
    }

    &::after {
      content: '';
      position: absolute;
      width: 0;
      height: 2px;
      bottom: -5px;
      left: 0;
      background-color: var(--primary-color);
      transition: width 0.3s ease;

      @include mobile {
        display: none;
      }
    }

    &:hover::after,
    &.router-link-active::after {
      width: 100%;
    }
  }
}

.mobile-menu {
  display: none;
  flex-direction: column;
  cursor: pointer;
  padding: 0.5rem;

  @include mobile {
    display: flex;
  }

  span {
    width: 25px;
    height: 3px;
    background: var(--primary-color);
    margin: 3px 0;
    transition: 0.3s;
    transform-origin: center;
  }

  &.open {
    span:nth-child(1) {
      transform: rotate(45deg) translate(6px, 6px);
    }

    span:nth-child(2) {
      opacity: 0;
    }

    span:nth-child(3) {
      transform: rotate(-45deg) translate(6px, -6px);
    }
  }
}
</style>