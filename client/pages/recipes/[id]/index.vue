<template>
    <main class="container my-5">
        <div class="row">
            <div class="col-12 text-center my-3">
                <h2 class="mb-3 display-4 text-uppercase">{{ recipes.name }}</h2>
            </div>
            <div class="col-md-6 mb-4">
                <img class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem
    rgba(0,0,0,.7);" :src="recipes.picture">
            </div>
            <div class="col-md-6">
                <div class="recipe-details">
                    <h4>Ingredients</h4>
                    <p>{{ recipes.ingredients }}</p>
                    <h4>Preparation time ⏱</h4>
                    <p>{{ recipes.prep_time }} mins</p>
                    <h4>Difficulty</h4>
                    <p>{{ recipes.difficulty }}</p>
                    <h4>Preparation guide</h4>
                    <textarea class="form-control" rows="10" v-html="recipes.prep_guide" disabled />
                    <nuxt-link to="/recipes" class="btn mt-3 btn-warning">Voltar</nuxt-link>
                </div>
            </div>
        </div>
    </main>
</template>
<script setup lang="ts">
import { onMounted, reactive } from 'vue';
const getRecipes = async ():Promise<Recipes> => {
    return await $fetch(`http://localhost:8000/api/recipes/${useRoute().params.id}`)
}

onMounted(async () => {
    const res = await getRecipes()
    recipes.name = res.name
    recipes.picture = res.picture
    recipes.ingredients = res.ingredients
    recipes.difficulty = res.difficulty
    recipes.prep_time = res.prep_time
    recipes.prep_guide = res.prep_guide
})

interface Recipes{
    name: string,
    picture:string,
    ingredients:string,
    difficulty: string,
    prep_time: null,
    prep_guide: string;
}

const recipes = reactive({
    name: "",
    picture: "",
    ingredients: "",
    difficulty: "",
    prep_time: null,
    prep_guide: ""
})
</script>
<style scoped></style>