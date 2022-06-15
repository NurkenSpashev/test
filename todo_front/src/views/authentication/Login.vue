<template>
  <div class="wrapper mt-5">
    <div id="formContent">
      <!-- Tabs Titles -->

      <!-- Login Form -->
      <form @submit.prevent="login" class="mt-5">
        <input type="text"
          id="login"
          class="signin-form-inupt"
          name="email"
          v-model="email"
          placeholder="Email"
          required
          >
        <span id="login-icon" class="signin-icon">
          <i class="bi bi-person"></i>
        </span>
        <input type="password" id="password" class="signin-form-inupt" name="password" v-model="password" placeholder="Password" required>
        <span class="signin-icon">
          <i class="bi bi-file-lock"></i>
        </span>
        <div v-if="error_message" class="alert alert-danger signin-form-inupt" role="alert">
          {{ error_message }}!
        </div>
        <input type="submit" class="fourth" value="Log In">
      </form>

      <!-- Remind Passowrd -->
      <div id="formFooter">
        <a class="underlineHover" href="#">Forgot Password?</a>
      </div>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
export default {
  name: 'Login',
  data() {
    return {
      email: null,
      password: null,
      error_message: false
    }
  },
  mounted() {
    console.log('Login')
  },
  methods: {
    login() {
        let formData = {
          email: this.email,
          password: this.password
        }
        let vue = this
        axios.post('http://localhost:8009/api/token/', formData)
          .then(function(response) {
            if (response.data.hasOwnProperty('access')) {
              console.log(response.data)
              let access = response.data.access
              let refresh = response.data.refresh

              vue.$store.commit('setAccess', access)

              axios.defaults.headers.common['Authorization'] = 'Bearer ' + access

              window.location.href = '/home';
            }
          })
          .catch(error => {
            if(error.response.status == 401) {
              this.error_message = error.response.data.detail;
              let password_error = document.getElementById('password')
              password_error.style.border = '2px solid red';
            } else if(error.response.status == 400) {
              if(error.response.data.hasOwnProperty('password')) {
                this.error_message = error.response.data.password[0];
                let password_error = document.getElementById('password')
                password_error.style.border = '2px solid red';
              } else {
                this.error_message = error.response.data.username[0];
                let username_error = document.getElementById('login')
                username_error.style.border = '2px solid red';
              }
            } else {
              this.error_message = 'Ошибка сервера, попробуйте позже.';
              console.error("SignIn error!", error);
            }
          });
      }
  }
}
</script>

<style scoped lang="scss">
  @import "./css/style.css"
</style>
