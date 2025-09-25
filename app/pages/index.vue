<script setup>
import { ref } from 'vue';
import days from '../../parseddata/days.json';

const revealed = ref(Array(days.length).fill(false));

function toggle(index) {
	revealed.value[index] = !revealed.value[index];
}
</script>

<template>
	<div v-for="(day, idx) in days"
		 :key="day.suuid"
		 class="flex flex-col gap-1 p-3 mb-3 w-fit bg-slate-500 rounded">
		<div>
			<h3 class="font-semibold cursor-pointer"
				@click="toggle(idx)">
				{{ day.date }}
			</h3>
			<p v-if="revealed[idx]"
			   class="text-yellow-200">data</p>
		</div>
	</div>
</template>
