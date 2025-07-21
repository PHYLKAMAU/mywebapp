import { defineStore } from 'pinia'
import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api'

// Configure axios defaults
axios.defaults.baseURL = API_BASE_URL

export const usePortfolioStore = defineStore('portfolio', {
  state: () => ({
    about: null,
    services: [],
    projects: [],
    featuredProjects: [],
    skills: [],
    skillsByCategory: {},
    testimonials: [],
    blogPosts: [],
    featuredBlogPosts: [],
    categories: [],
    stats: null,
    loading: false,
    error: null
  }),

  actions: {
    async fetchAbout() {
      try {
        this.loading = true
        const response = await axios.get('/portfolio/about/')
        this.about = response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching about data:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchServices() {
      try {
        this.loading = true
        const response = await axios.get('/portfolio/services/')
        // Handle paginated response
        this.services = response.data.results || response.data
        console.log('Services loaded:', this.services)
      } catch (error) {
        this.error = error.message
        console.error('Error fetching services:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchProjects() {
      try {
        this.loading = true
        const response = await axios.get('/portfolio/projects/')
        this.projects = response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching projects:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchFeaturedProjects() {
      try {
        this.loading = true
        const response = await axios.get('/portfolio/projects/featured/')
        this.featuredProjects = response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching featured projects:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchSkills() {
      try {
        this.loading = true
        const response = await axios.get('/portfolio/skills/')
        this.skills = response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching skills:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchSkillsByCategory() {
      try {
        this.loading = true
        const response = await axios.get('/portfolio/skills/by-category/')
        return response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching skills by category:', error)
        return {}
      } finally {
        this.loading = false
      }
    },

    async fetchTestimonials() {
      try {
        this.loading = true
        const response = await axios.get('/portfolio/testimonials/')
        this.testimonials = response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching testimonials:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchStats() {
      try {
        this.loading = true
        const response = await axios.get('/portfolio/stats/')
        this.stats = response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching stats:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchBlogPosts() {
      try {
        this.loading = true
        const response = await axios.get('/blog/posts/')
        this.blogPosts = response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching blog posts:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchFeaturedBlogPosts() {
      try {
        this.loading = true
        const response = await axios.get('/blog/posts/featured/')
        this.featuredBlogPosts = response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching featured blog posts:', error)
      } finally {
        this.loading = false
      }
    },

    async fetchBlogPost(slug) {
      try {
        this.loading = true
        const response = await axios.get(`/blog/posts/${slug}/`)
        return response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching blog post:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async fetchCategories() {
      try {
        this.loading = true
        const response = await axios.get('/blog/categories/')
        this.categories = response.data
      } catch (error) {
        this.error = error.message
        console.error('Error fetching categories:', error)
      } finally {
        this.loading = false
      }
    },

    async submitContactMessage(data) {
      try {
        this.loading = true
        const response = await axios.post('/contact/message/', data)
        return response.data
      } catch (error) {
        this.error = error.response?.data?.message || error.message
        console.error('Error submitting contact message:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    async submitQuoteRequest(data) {
      try {
        this.loading = true
        const response = await axios.post('/contact/quote/', data)
        return response.data
      } catch (error) {
        this.error = error.response?.data?.message || error.message
        console.error('Error submitting quote request:', error)
        throw error
      } finally {
        this.loading = false
      }
    },

    // Utility actions
    clearError() {
      this.error = null
    },

    async initializeHomepage() {
      // Fetch all data needed for homepage
      await Promise.all([
        this.fetchAbout(),
        this.fetchServices(),
        this.fetchFeaturedProjects(),
        this.fetchTestimonials(),
        this.fetchFeaturedBlogPosts(),
        this.fetchStats()
      ])
    }
  }
})