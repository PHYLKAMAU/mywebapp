<template>
  <div class="blog-post-page">
    <div class="container">
      <h1 class="section-title">Blog Post: {{ $route.params.slug }}</h1>
      <p class="text-center text-secondary">Coming soon...</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlogPostView'
}
</script>

<style lang="scss" scoped>
.blog-post-page {
  padding: 4rem 0;
  min-height: 60vh;
  display: flex;
  align-items: center;
}

.text-secondary {
  color: var(--text-secondary);
  font-size: 1.2rem;
}
</style>