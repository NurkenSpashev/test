<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/tasks">Tasks</router-link> |
    <router-link v-if="! if_authenticate" to="/login">Login</router-link>
    <router-link v-else to="/logout">Logout</router-link>
  </nav>
  <router-view/>
</template>
<script>
  import axios from 'axios'

  export default {
    name: 'App',
    data() {
       return {
           if_authenticate: false
       }
    },
    beforeCreate() {
      axios.defaults.BaseURL = "http://127.0.0.1:8000"

      this.$store.commit('initializeStore');
      const access = this.$store.state.access;

      if(access) {
        axios.defaults.headers.common['Authorization'] = 'Bearer ' + access
        this.if_authenticate = this.$store.state.isLoggedIn;
      } else {
        axios.defaults.headers.common['Authorization'] = null
        this.if_authenticate = false;
      }
    },
    mounted() {
      this.if_authenticate = this.$store.state.isLoggedIn;
    },
  }
</script>
<style lang="scss">
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  nav {
    padding: 30px;

    a {
      font-weight: bold;
      color: #2c3e50;

      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
</style>
