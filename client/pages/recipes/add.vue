<template>
    <main class="container my-5">
        <div class="row">
            <div class="col-12 text-center my-3">
                <h2 class="mb-3 display-4 text-uppercase">{{ recipe.name }}</h2>
            </div>
            <div class="col-md-6 mb-4">
                <img v-if="preview" class="img-fluid"
                    style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);" :src="preview">
                <img v-else class="img-fluid"
                    style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"
                    src="/placeholder.png">
            </div>
            <div class="col-md-4">
                <form @submit.prevent="submitRecipe">
                    <div class="form-group">
                        <label>Recipe Name</label>
                        <input type="text" class="form-control" v-model="recipe.name">
                    </div>
                    <div class="form-group">
                        <label>Ingredients</label>
                        <input v-model="recipe.ingredients" type="text" class="form-control">
                    </div>
                    <div class="form-group">
                        <label>Food picture</label>
                        <input type="file" name="file" @change="onFileChange">
                    </div>
                    <div class="row">
                        <div class="col-md-6">
                            <div class="form-group">
                                <label>Difficulty</label>
                                <select v-model="recipe.difficulty" class="form-control">
                                    <option value="Easy">Easy</option>
                                    <option value="Medium">Medium</option>
                                    <option value="Hard">Hard</option>
                                </select>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="form-group">
                                <label>Prep time<small>(minutes)</small></label>
                                <input v-model="recipe.prep_time" type="number" class="form-control">
                            </div>
                        </div>
                    </div>
                    <div class="form-group mb-3">
                        <label>Preparation guide</label>
                        <textarea v-model="recipe.prep_guide" class="form-control" rows="8"></textarea>
                    </div>
                    <button type="submit" class="btn btn-primary">Submit</button>
                    <button type="submit" class="btn btn-sucess">voltar</button>
                </form>
            </div>
        </div>
    </main>
</template>
<script setup lang="ts">
import { reactive } from 'vue';
const baseUrl = 'http://localhost:8000/api/'
const recipe = reactive({
    name: "",
    picture: "",
    ingredients: "",
    difficulty: "",
    prep_time: "",
    prep_guide: ""
})

const preview = ref()
const submitRecipe = async () => {
    const formData = new FormData();
    formData.append("name", recipe[`name`])
    formData.append("picture", recipe[`picture`])
    formData.append("ingredients", recipe[`ingredients`])
    formData.append("difficulty", recipe[`difficulty`])
    formData.append("prep_time", recipe["prep_time"])
    formData.append("prep_guide", recipe[`prep_guide`])

    try {

        await useFetch(`${baseUrl}recipes/`,{
            method:'POST',
            body:formData
        })

        useRouter().push('/recipes')

    } catch (e) {
        console.log(e);

    }
}

const onFileChange = (e: any) => {
    let files = e.target.files || e.dataTransfer.files
    if (!files.length) { return }
    recipe.picture = files[0]
    createImage(files[0])
}

const createImage = (file: any) => {
    let reader = new FileReader()
    reader.onload = e => {
        if (e.target == null || !e.target) return
        return preview.value = e.target?.result
    }
    reader.readAsDataURL(file)
}

</script>
<style scoped></style>