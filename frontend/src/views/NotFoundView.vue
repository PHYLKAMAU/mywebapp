<template>
  <div class="not-found-page">
    <div class="container">
      <div class="not-found-content">
        <h1 class="error-code">404</h1>
        <h2>Page Not Found</h2>
        <p>The page you're looking for doesn't exist.</p>
        <router-link to="/" class="btn btn-primary">Go Home</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'NotFoundView'
}
</script>

<style lang="scss" scoped>
.not-found-page {
  padding: 4rem 0;
  min-height: 60vh;
  display: flex;
  align-items: center;
}

.not-found-content {
  text-align: center;
  max-width: 500px;
  margin: 0 auto;
}

.error-code {
  font-size: 6rem;
  font-weight: bold;
  color: var(--primary-color);
  margin-bottom: 1rem;
}

h2 {
  font-size: 2rem;
  color: var(--text-primary);
  margin-bottom: 1rem;
}

p {
  color: var(--text-secondary);
  font-size: 1.1rem;
  margin-bottom: 2rem;
}
</style>