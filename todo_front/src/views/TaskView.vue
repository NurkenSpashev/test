<template>
  <div class="container" v-if="if_authenticate">
    <button class="btn btn-info" @click="createTask" style="margin-left:90%">Add</button>
      <div class="row" v-if="task">
        <div class="col-md-4" v-for="task in tasks" :key="task.id">
           <div class="card m-3">
              <div class="card-body">
                <h5 class="card-title">{{ task.title }}</h5>
                <h6 class="card-subtitle mb-2 text-muted">{{ task.author }}</h6>
                <p class="card-text">{{ task.description }}</p>
                <button  @click="toggleTask(task)" :class="{'btn btn-success m-1': task.status, 'btn btn-warning m-1': !task.status}">{{ task.status ? 'Undo' : 'Done' }}</button>
                <button @click="editTask(task)" class="btn btn-primary m-1">Edit</button>
                <button @click="deleteTask(task)" class="btn btn-danger m-1">Delete</button>
              </div>
          </div>
        </div>
      </div>
      <div class="row" v-else-if="edit">
        <div class="card col-md-5">
           <form @submit.prevent="updateTask(taskForm.id)" class="m-3">
            <div class="form-group m-1">
              <input type="text" class="form-control" id="title" name="title" v-model="taskForm.title" aria-describedby="title">
            </div>
             <div class="form-group m-2">
               <textarea class="form-control" id="description" name="description" v-model="taskForm.description" aria-describedby="description"></textarea>
             </div>
            <div class="form-group mt-2">
              <input type="checkbox" class="form-check-input" id="exampleCheck1" name="status" v-model="taskForm.status">
              <span for="exampleCheck1">Status</span>
            </div>
            <input type="submit" class="btn btn-primary" value="Save">
          </form>
       </div>
      </div>
  </div>
  <div class="container" v-else>
    <div class="row">
      <div class="col-md-12">
        <div class="card">
           <div class="card-body">
             <h5 class="card-title">Need authenticate!</h5>
           </div>
       </div>
     </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TaskView',
  data() {
     return {
         tasks: [''],
         if_authenticate: false,
         task: false,
         create: false,
         edit: false,
         taskForm: {
           title: '',
           description: '',
           status: false
         }
     }
 },
 mounted() {
    this.if_authenticate = this.$store.state.isLoggedIn ? true : false;
    this.getData();
 },
 methods: {
  async getData() {
    if(this.$store.state.isLoggedIn) {
      try {
          const response = await axios.get('http://localhost:8009/api/tasks/');
          this.tasks = response.data;
          this.task = true;
          this.create = false;
          this.edit = false;
      } catch (error) {
          console.log(error);
      }
    }
  },
  async toggleTask(task) {
    let formData = {
      id: task.id,
      status: task.status ? false : true,
    }
    if(this.$store.state.isLoggedIn) {
      const response = await axios.patch('http://localhost:8009/api/tasks/' + task.id + '/', formData);
      this.getData();
    }
  },
  async editTask(task) {
    if(this.$store.state.isLoggedIn) {
      this.edit = true;
      this.create = false;
      this.task = false;
      const response = await axios.get('http://localhost:8009/api/tasks/' + task.id + '/');
      this.taskForm = response.data;
    }
  },
  async deleteTask(task) {
    if(this.$store.state.isLoggedIn) {
      const response = await axios.delete('http://localhost:8009/api/tasks/' + task.id + '/');
      this.getData();
    }
  },
  async updateTask(id) {
    if(this.$store.state.isLoggedIn) {
      const response = await axios.put('http://localhost:8009/api/tasks/' + id + '/', this.taskForm);
      this.getData();
    }
  },
  async createTask() {
    this.$router.push({ name: 'create' })
  },
  async saveTask() {
    if(this.$store.state.isLoggedIn) {
      this.create = true;
    }
  }
}
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
