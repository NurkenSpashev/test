<template>
  <div class="container">
  </div>
</template>

<script>
  export default {
    name: 'Logout',
    mounted() {
      this.logout()
    },
    methods: {
      logout() {
        this.$store.commit('removeAccess');
        window.location.href = '/login';
      }
    }
  }
</script>
