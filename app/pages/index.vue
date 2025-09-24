<script setup>
import { ref } from 'vue';
import flashcards from '../../parseddata/flashcards.json';

const revealed = ref(Array(flashcards.length).fill(false));

function toggle(index) {
	revealed.value[index] = !revealed.value[index];
}
</script>

<template>
	<p class="mb-4">Welcome to this site.</p>
	<p class="text-xl mb-3">
		There are {{ flashcards.length }} flashcards:
	</p>
	<div v-for="(card, idx) in flashcards"
		 :key="card.suuid"
		 class="flex flex-col gap-1 p-3 mb-3 w-fit bg-slate-500 rounded">
		<div>
			<h3 class="font-semibold cursor-pointer"
				@click="toggle(idx)">
				{{ card.front }}
			</h3>
			<p v-if="revealed[idx]"
			   class="text-yellow-200">{{ card.back }}</p>
		</div>
	</div>
</template>
