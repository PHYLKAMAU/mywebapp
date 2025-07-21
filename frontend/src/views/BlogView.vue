<template>
  <div class="blog-page">
    <div class="container">
      <h1 class="section-title">Blog</h1>
      <p class="text-center text-secondary">Coming soon...</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BlogView'
}
</script>

<style lang="scss" scoped>
.blog-page {
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