<template>
    <main class="container mt-5 ">
        <div class="row">
            <div class="col-12 text-right mb-4">
                <div class="d-flex justify-content-between">
                    <h3>La Recipes</h3>
                    <nuxt-link to="/recipes/add" class="btn btn-info">Add
                        Recipe</nuxt-link>
                </div>
            </div>
            <template v-for="recipe in recipes">
                <div v-if="recipes.length > 0" :key="recipe.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
                    <recipe-card :onDelete="deleteRecipe" :recipe="recipe"></recipe-card>
                </div>
            </template>
        </div>
    </main>
</template>
<script setup lang="ts">
import { ref } from 'vue';
interface Recipes {
    id: number, difficulty: string, ingredients: string, name: string, picture: string, prep_guide: string, prep_time: number
}
const baseUrl = 'http://localhost:8000/api/'
const recipes = ref<Recipes[]>([])

const getRecipes = async (): Promise<Recipes[]> => {
    return await $fetch(baseUrl+'recipes/')
}

const deleteRecipe = async(recipe_id:number) => {
    await $fetch(`${baseUrl}recipes/${recipe_id}/`,{method:'delete'})
    recipes.value = await getRecipes()
}

onMounted(async () => {
    recipes.value = await getRecipes()
})


</script>
<style scoped></style>