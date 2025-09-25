<script setup>
import { ref } from 'vue';
import days from '../../parseddata/days.json';

</script>

<template>
	<div v-for="(day, idx) in days"
		 :key="day.date"
		 class="flex flex-col gap-1 p-2 mb-3 w-fit bg-slate-500 rounded">
		<div>
			<h3 class="font-semibold cursor-pointer">{{ day.date }}</h3>
			<p class="text-yellow-200">data</p>
		</div>
	</div>
</template>
