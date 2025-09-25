<script setup>
import { ref } from 'vue';
import days from '../../parseddata/days.json';

</script>

<template>
	<div v-for="(day, idx) in days"
		 :key="day.date"
		 class="flex flex-col gap-1 p-2 mb-3 w-fit bg-slate-500 rounded">
		<div>
			<h3 class="font-semibold cursor-pointer">{{ day.displayDate }}</h3>
			<ul class="text-yellow-400">
				<li v-for="project in day.projects"
					:key="project.suuid"
					class="text-sm">
					<span class="font-semibold">{{ project.minutes }} mins</span> - {{ project.name }}
				</li>
			</ul>
		</div>
	</div>
</template>
